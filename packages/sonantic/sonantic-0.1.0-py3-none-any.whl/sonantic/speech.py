import base64
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

from pydantic import BaseModel

from . import core
from .core import Error, Paginated

endpoint = "/v2/speech"

SpeechId = Union[str, int]


class Style(BaseModel):
    name: str
    intensity: str


class Prosody(BaseModel):
    rate: Union[str, float]


class Text(BaseModel):
    content: str
    style: Optional[Style]
    prosody: Optional[Prosody]


class PhonemeInput(BaseModel):
    phoneme: str
    pitch: float
    rate: float = 1.0


class Phonemes(BaseModel):
    id: SpeechId
    content: List[PhonemeInput]


class AudioParams(BaseModel):
    encoding: str = "linear16"
    sample_rate: int = 22050
    timecode: Optional[str] = None
    peak: Optional[float] = None
    rms: Optional[float] = None
    lufs: Optional[float] = None
    start_silence: Optional[float] = None
    end_silence: Optional[float] = None


class Audio(AudioParams):
    content: Optional[Union[bytes, str]]


class Phoneme(BaseModel):
    phoneme: str
    pitch: float
    start: float
    end: float


class Speech(BaseModel):
    id: str
    voice: str
    text: Optional[Text]
    ssml: Optional[str]
    metadata: Optional[Dict[Any, Any]]
    audio: Audio
    style: Style
    prosody: Optional[Prosody]
    phonemes: Optional[List[Phoneme]]
    words: Optional[List[str]]


class CreateSpeech(BaseModel):
    voice: Optional[str]
    text: Optional[Text]
    ssml: Optional[str]
    phonemes: Optional[Phonemes]
    metadata: Optional[Dict[Any, Any]]


def create(
    *,
    voice: Optional[str] = None,
    text: Optional[Union[str, Text]] = None,
    ssml: Optional[str] = None,
    phonemes: Optional[Phonemes] = None,
    audio: Optional[AudioParams] = None,
    metadata: Optional[Dict[Any, Any]] = None,
    decode_audio: bool = True,
) -> Union[Speech, Error]:
    """Create a Speech object.

    Args:
        voice (Optional[str], optional): The voice to generate speech with if using text or ssml.
        text (Optional[Union[str, Text]], optional): A text string or Text object. Defaults to None.
        ssml (Optional[str], optional): SSML. Defaults to None.
        phonemes (Optional[Phonemes], optional): Phonetic input to control previously generated speech. Defaults to None.
        phonemes (Optional[AudioParams], optional): Audio paramst to apply. Defaults to None.
        metadata (Optional[Dict[Any, Any]], optional): Key-value metadata to attach to the speech. Defaults to None.
        decode_audio (bool, optional): Automatically decode the base-64 encoded audio string into bytes. Defaults to True.

    Returns:
        Union[Speech, Error]: A Speech object or Error if the request failed.
    """
    if text is None and ssml is None and phonemes is None:
        raise ValueError("One of `text`, `ssml` or `phonemes` must be specified.")

    if text is not None:
        if isinstance(text, str):
            text = Text(content=text)

    create_speech = CreateSpeech(
        voice=voice,
        text=text,
        ssml=ssml,
        phonemes=phonemes,
        audio=audio,
        metadata=metadata,
    )

    r = core.post(endpoint, json=create_speech.dict())
    j = r.json()

    if r.status_code != HTTPStatus.OK:
        return Error(**j)

    if decode_audio:
        j["audio"]["content"] = base64.b64decode(j["audio"]["content"])

    return Speech(**j)


def retrieve(
    speech_id: SpeechId,
    decode_audio: bool = True,
) -> Union[Speech, Error]:
    """Retrieve a Speech object.

    Args:
        id (SpeechId): The id of the Speech object to retrieve.
        decode_audio (bool, optional): Automatically decode the base-64 encoded audio string into bytes. Defaults to True.

    Returns:
        Union[Speech, Error]: A Speech object or Error if the request failed.
    """
    query = {}

    r = core.get(f"{endpoint}/{speech_id}", params=query)
    j = r.json()

    if r.status_code != HTTPStatus.OK:
        return Error(**j)

    if decode_audio:
        j["audio"]["content"] = base64.b64decode(j["audio"]["content"])

    return Speech(**j)


def list(page: int = 1, per_page: int = 10, **query) -> Union[Paginated[Speech], Error]:
    """List and query Speech objects.

    Args:
        page (int, optional): The page. Defaults to 1.
        per_page (int, optional): The page size. Defaults to 10.

    Returns:
        Union[Paginated[Speech], Error]: A Paginated object containing Speech items or Error if the request failed.
    """
    query["page"] = page
    query["per_page"] = per_page
    r = core.get(f"{endpoint}", params=query)

    j = r.json()

    if r.status_code != HTTPStatus.OK:
        return Error(**j)

    return Paginated[Speech](**j)


def update(speech_id: SpeechId, **metadata) -> Union[Speech, Error]:
    """Update a Speech object.

    Args:
        id (SpeechId): The id of the Speech object to update.

    Returns:
        Union[Speech, Error]: A Speech object or Error if the request failed.
    """
    r = core.patch(f"{endpoint}/{speech_id}", json={"metadata": metadata})
    j = r.json()

    if r.status_code != HTTPStatus.OK:
        return Error(**j)

    return Speech(**j)


def retrieve_audio(speech_id: SpeechId, **query) -> Union[bytes, Error]:
    """Retrieve the audio bytes of a Speech object.

    Args:
        id (SpeechId): The id of the Speech object to retrieve audio for.

    Returns:
        Union[bytes, Error]: Speech audio bytes.
    """
    r = core.get(f"{endpoint}/{speech_id}/audio", params=query)

    if r.status_code != HTTPStatus.OK:
        j = r.json()

        return Error(**j)

    return r.content
