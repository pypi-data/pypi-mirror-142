# Sonantic Python Library

[![CI](https://github.com/sonantic/sonantic-python/actions/workflows/ci.yaml/badge.svg)](https://github.com/sonantic/sonantic-python/actions/workflows/ci.yaml)

Interact with the Sonantic API from Python.

## Installation

You can install `sonantic` from PyPI

```sh
pip install sonantic
```

## Example

You will need to set your API key which can be found in your [Sonantic Dashboard](https://app.sonantic.io/developers)

```python
import sonantic
from sonantic.core import Error

# make sure to set the API key before you call any methods
sonantic.api_key = "live_c..."

# list available voices
voices = sonantic.voices.list()


print("Available voices")
for voice in voices.items:
    print(f"\t{voice.name}")

print()
print("Creating speech...")

speech = sonantic.speech.create(
    voice="taylor", text="The quick brown fox jumps over the lazy dog."
)

# check the request was successful and handle the error otherwise
if isinstance(speech, Speech):
    path = f"./{speech.id}.wav"
    print(f"Saving audio to file {path}")
    # store generated speech - the audio is decoded by default
    with open(path, "bx") as f:
        f.write(speech.audio.content)
else:
    # handle the error
    print(speech.error)
    print(speech.message)
```
