# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = scope_denied_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ScopeDeniedEvent:
    type: Optional[str] = None
    scopes: Optional[List[str]] = None
    trigger_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ScopeDeniedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        trigger_id = from_union([from_str, from_none], obj.get("trigger_id"))
        return ScopeDeniedEvent(type, scopes, trigger_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        result["trigger_id"] = from_union([from_str, from_none], self.trigger_id)
        return result


def scope_denied_event_from_dict(s: Any) -> ScopeDeniedEvent:
    return ScopeDeniedEvent.from_dict(s)


def scope_denied_event_to_dict(x: ScopeDeniedEvent) -> Any:
    return to_class(ScopeDeniedEvent, x)
