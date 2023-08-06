from http import HTTPStatus
from typing import List, Union

from pydantic.main import BaseModel

from . import core
from .core import Error, Paginated

endpoint = "/v2/voices"


class Style(BaseModel):
    name: str
    intensity: str


class ProsodyAbilities(BaseModel):
    rate: bool
    pitch: bool
    volume: bool


class Abilities(BaseModel):
    style: Style
    prosody: ProsodyAbilities


class Voice(BaseModel):
    name: str
    gender: str
    nationality: str
    abilities: List[Abilities]


def retrieve(name: str) -> Union[Voice, Error]:
    """Retrieve a Voice object by name.

    Args:
        name (str): The name of the Voice to retrieve.

    Returns:
        Union[Voice, Error]: A Voice object or Error if the request failed.
    """
    r = core.get(f"{endpoint}/{name}")

    j = r.json()

    if r.status_code != HTTPStatus.OK:
        return Error(**j)

    return Voice(**j)


def list(page: int = 1, per_page: int = 50) -> Union[Paginated[Voice], Error]:
    """List Voice objects.

    Args:
        page (int, optional): The page. Defaults to 1.
        per_page (int, optional): The page size. Defaults to 50.

    Returns:
        Union[Paginated[Voice], Error]: A Paginated object containing Voice items or Error if the request failed.
    """
    r = core.get(endpoint, params={"page": page, "per_page": per_page})

    j = r.json()

    if r.status_code != HTTPStatus.OK:
        return Error(**j)

    return Paginated[Voice](**j)
