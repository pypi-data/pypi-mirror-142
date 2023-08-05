# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = group_open_event_from_dict(json.loads(json_string))

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
class GroupOpenEvent:
    type: Optional[str] = None
    channel: Optional[str] = None
    user: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupOpenEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        user = from_union([from_str, from_none], obj.get("user"))
        return GroupOpenEvent(type, channel, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["user"] = from_union([from_str, from_none], self.user)
        return result


def group_open_event_from_dict(s: Any) -> GroupOpenEvent:
    return GroupOpenEvent.from_dict(s)


def group_open_event_to_dict(x: GroupOpenEvent) -> Any:
    return to_class(GroupOpenEvent, x)
