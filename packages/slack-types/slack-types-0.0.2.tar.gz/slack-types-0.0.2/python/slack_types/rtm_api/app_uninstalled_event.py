# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = app_uninstalled_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AppUninstalledEvent:
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppUninstalledEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        return AppUninstalledEvent(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        return result


def app_uninstalled_event_from_dict(s: Any) -> AppUninstalledEvent:
    return AppUninstalledEvent.from_dict(s)


def app_uninstalled_event_to_dict(x: AppUninstalledEvent) -> Any:
    return to_class(AppUninstalledEvent, x)
