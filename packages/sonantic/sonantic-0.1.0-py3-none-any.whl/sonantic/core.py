import logging
import time
from typing import Generic, List, Optional, TypeVar

import requests
from pydantic import BaseModel
from pydantic.generics import GenericModel

import sonantic

from .version import __version__

logger = logging.getLogger(__name__)


class SonanticError(Exception):
    def __init__(self, message: Optional[str] = None) -> None:
        super().__init__(message)


NO_API_KEY_MESSAGE = """No API key provided. (Please set your API key using "sonantic.api_key = <API-KEY>"). You can generate API keys in your Sonantic dashboard."""


def check_api_key():
    if sonantic.api_key is None:
        raise SonanticError(message=NO_API_KEY_MESSAGE)


HTTP_HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": f"sonantic/python/{__version__}",
}


session = requests.Session()
session.headers.update(HTTP_HEADERS)


def post(endpoint: str, **kwargs):
    check_api_key()

    start_time = time.perf_counter()
    url = f"{sonantic.api_base}{endpoint}"
    HTTP_HEADERS["Authorization"] = f"Bearer {sonantic.api_key}"
    r = session.post(url, headers=HTTP_HEADERS, **kwargs)
    end_time = time.perf_counter()
    logger.debug("POST %s %d (%.3fs)", url, r.status_code, end_time - start_time)
    return r


def patch(endpoint: str, **kwargs):
    check_api_key()

    start_time = time.perf_counter()
    url = f"{sonantic.api_base}{endpoint}"
    HTTP_HEADERS["Authorization"] = f"Bearer {sonantic.api_key}"
    r = session.patch(url, headers=HTTP_HEADERS, **kwargs)
    end_time = time.perf_counter()
    logger.debug("PATCH %s %d (%.3fs)", url, r.status_code, end_time - start_time)
    return r


def get(endpoint: str, **kwargs):
    check_api_key()

    start_time = time.perf_counter()
    url = f"{sonantic.api_base}{endpoint}"
    HTTP_HEADERS["Authorization"] = f"Bearer {sonantic.api_key}"
    r = session.get(url, headers=HTTP_HEADERS, **kwargs)
    end_time = time.perf_counter()
    logger.debug("GET %s %d (%.3fs)", url, r.status_code, end_time - start_time)
    return r


class Error(BaseModel):
    error: str
    message: str


T = TypeVar("T")


class Paginated(GenericModel, Generic[T]):
    page: int
    per_page: int
    total: int
    items: List[T]

    @property
    def has_more(self):
        return self.total > self.page * self.per_page
