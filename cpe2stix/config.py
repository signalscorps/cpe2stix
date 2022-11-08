"""
Stores the config of cve2stix tool
"""

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
import os

CVESTIX_FOLDER = Path(os.path.abspath(__file__)).parent
REPO_FOLDER = CVESTIX_FOLDER.parent
CREDENTIALS_FILE_PATH = REPO_FOLDER / "credentials.yml"

STIX2_OBJECTS_FOLDER = os.path.abspath("stix2_objects")
STIX2_BUNDLES_FOLDER = os.path.abspath("stix2_bundles")


@dataclass
class Config:
    cpe_start_date: datetime = None
    cpe_end_date: datetime = None
    stix2_objects_folder: str = STIX2_OBJECTS_FOLDER
    stix2_bundles_folder: str = STIX2_BUNDLES_FOLDER
    run_mode: str = "download" # or "update"
    api_key: str = None

    # Constant configs, SHOULD NOT be changed
    nvd_cpe_api_endpoint: str = "https://services.nvd.nist.gov/rest/json/cpes/1.0/"
    results_per_page: int = 500
