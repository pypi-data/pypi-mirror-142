from dataclasses import asdict, is_dataclass
from json import JSONEncoder


class Serialiser(JSONEncoder):
    def default(self, o):
        if is_dataclass(o):
            return asdict(o)
        else:
            return super().default(o)
