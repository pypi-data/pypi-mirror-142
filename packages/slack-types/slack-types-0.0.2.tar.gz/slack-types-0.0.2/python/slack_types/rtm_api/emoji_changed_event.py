# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = emoji_changed_event_from_dict(json.loads(json_string))

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
class EmojiChangedEvent:
    type: Optional[str] = None
    subtype: Optional[str] = None
    names: Optional[List[str]] = None
    name: Optional[str] = None
    value: Optional[str] = None
    old_name: Optional[str] = None
    new_name: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EmojiChangedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("names"))
        name = from_union([from_str, from_none], obj.get("name"))
        value = from_union([from_str, from_none], obj.get("value"))
        old_name = from_union([from_str, from_none], obj.get("old_name"))
        new_name = from_union([from_str, from_none], obj.get("new_name"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return EmojiChangedEvent(type, subtype, names, name, value, old_name, new_name, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["names"] = from_union([lambda x: from_list(from_str, x), from_none], self.names)
        result["name"] = from_union([from_str, from_none], self.name)
        result["value"] = from_union([from_str, from_none], self.value)
        result["old_name"] = from_union([from_str, from_none], self.old_name)
        result["new_name"] = from_union([from_str, from_none], self.new_name)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def emoji_changed_event_from_dict(s: Any) -> EmojiChangedEvent:
    return EmojiChangedEvent.from_dict(s)


def emoji_changed_event_to_dict(x: EmojiChangedEvent) -> Any:
    return to_class(EmojiChangedEvent, x)
