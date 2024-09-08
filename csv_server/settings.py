import os
from pathlib import Path
from typing import Literal


def get_root_folder() -> Path:
    root_folder = os.environ.get("ROOT_FOLDER")
    if not root_folder:
        raise ValueError("ROOT_FOLDER environment variable not set.")
    return Path(root_folder)


def get_env() -> Literal["DEV", "PROD", "TEST"]:
    env = os.environ.get("ENV")
    if env not in ["DEV", "PROD", "TEST"]:
        raise ValueError("Invalid value for ENV environment variable.")
    return env  # type: ignore[return-value]


def get_storage() -> Literal["CSV", "MEMORY"]:
    storage = os.environ.get("STORAGE", "CSV")
    if storage not in ["CSV", "MEMORY"]:
        raise ValueError("Invalid value for STORAGE environment variable.")
    return storage  # type: ignore[return-value]


ENV: Literal["DEV", "PROD", "TEST"] = get_env()
ROOT_FOLDER = get_root_folder()
data_folder = "data" if ENV != "TEST" else "test_data"
ROOT_CSV_FOLDER = ROOT_FOLDER / Path(data_folder)
STORAGE: Literal["CSV", "MEMORY"] = get_storage()

__all__ = ["ROOT_FOLDER", "ROOT_CSV_FOLDER"]
