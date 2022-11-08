"""
Main driver logic for cve2stix
"""

import json
import logging
import math
import requests
import time
from stix2 import new_version
from stix2.exceptions import InvalidValueError

from cpe2stix.config import Config
from cpe2stix.error_handling import store_error_logs_in_file
from cpe2stix.helper import get_date_string_nvd_format
from cpe2stix.parse_api_response import parse_cpe_api_response
from cpe2stix.stix_store import StixStore

logger = logging.getLogger(__name__)


def store_new_cpe(stix_store, software):
    stix_objects = [software]

    status = stix_store.store_cpe_in_bundle(software["cpe"], stix_objects, update=True)
    if status == False:
        return False

    stix_store.store_objects_in_filestore(stix_objects)
    return True


def main(config: Config):

    start_date = config.cpe_start_date
    end_date = config.cpe_end_date
    total_results = math.inf
    start_index = -1
    backoff_time = 10

    logger.info(
        "Downloading CPEs from %s to %s",
        start_date.strftime("%Y-%m-%d"),
        end_date.strftime("%Y-%m-%d"),
    )

    while config.results_per_page * (start_index + 1) < total_results:

        start_index += 1

        logger.debug("Calling NVD CPE API with startIndex: %d", start_index)

        # Create CVE query and send request to NVD API
        query = {
            "apiKey": config.api_key,
            "modStartDate": get_date_string_nvd_format(start_date),
            "modEndDate": get_date_string_nvd_format(end_date),
            "addOns": "cves",
            "resultsPerPage": config.results_per_page,
            "sortOrder": "publishedDate",
            "startIndex": start_index * config.results_per_page,
        }

        try:

            response = requests.get(config.nvd_cpe_api_endpoint, query)

            if response.status_code != 200:
                logger.warning("Got response status code %d.", response.status_code)
                raise requests.ConnectionError

        except requests.ConnectionError as ex:
            logger.warning(
                "Got ConnectionError. Backing off for %d seconds.", backoff_time
            )
            start_index -= 1
            time.sleep(backoff_time)
            backoff_time *= 2
            continue

        content = response.json()
        logger.debug(
            "Got response from NVD API with status code: %d", response.status_code
        )

        parsed_responses = parse_cpe_api_response(content)
        logger.debug(
            "Parsed %s CVEs into vulnerability stix objects", len(parsed_responses)
        )

        total_results = content["totalResults"]

        # Store CPEs in database and stix store
        stix_store = StixStore(config.stix2_objects_folder, config.stix2_bundles_folder)
        total_store_count = 0

        for software in parsed_responses:
            # CVE not present, so we download it
            status = store_new_cpe(stix_store, software)
            if status == True:
                total_store_count += 1

        logger.info(
            "Downloaded %d cpes",
            total_store_count,
        )

        if config.results_per_page * (start_index + 1) < total_results:
            time.sleep(5)

        backoff_time = 10

    store_error_logs_in_file()
