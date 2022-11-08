"""
Helper methods for parsing results from NVD API
"""

from datetime import datetime
import json
import logging
from stix2 import Software

from cpe2stix.error_handling import error_logger

logger = logging.getLogger(__name__)


def parse_cpe_api_response(cpe_content):
    parsed_response = []
    for cpe_item in cpe_content["result"]["cpes"]:

        software_dict = {
            "name": cpe_item["titles"][0]["title"],
            "cpe": cpe_item["cpe23Uri"],
            "version": cpe_item["cpe23Uri"].split(":")[5],
            "vendor": cpe_item["cpe23Uri"].split(":")[3],
            "languages": cpe_item["titles"][0]["lang"],
            # "revoked": cpe_item["deprecated"],
            "extensions": {
                "extension-definition--6c453e0f-9895-498f-a273-2e2dda473377": {
                    "extension_type": "property-extension",
                    "nvd_cpe": cpe_item,
                }
            },
        }

        software = Software(**software_dict)
        parsed_response.append(software)

    return parsed_response
