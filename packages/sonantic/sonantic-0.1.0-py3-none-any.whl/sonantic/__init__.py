import os

api_key = None
api_base = os.environ.get("SONANTIC_API_BASE", "https://api.sonantic.io")
api_version = os.environ.get("SONANTIC_API_VERSION")

__version__ = "0.1.0"


from . import speech, voices
