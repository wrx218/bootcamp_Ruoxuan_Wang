"""Configuration helpers for Homework 02."""

import os
from pathlib import Path

from dotenv import load_dotenv


def load_env(env_path=None):
    """Load variables from a .env file and return whether one was found."""
    path = Path(env_path) if env_path else Path(__file__).resolve().parents[1] / ".env"
    return load_dotenv(dotenv_path=path)


def get_key(key, default=None):
    """Return an environment variable after loading the project .env file."""
    load_env()
    return os.getenv(key, default)
