# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = im_created_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, TypeVar, Type, cast


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
class Channel:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        return Channel()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class IMCreatedEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    channel: Optional[Channel] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IMCreatedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        return IMCreatedEvent(type, user, channel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        return result


def im_created_event_from_dict(s: Any) -> IMCreatedEvent:
    return IMCreatedEvent.from_dict(s)


def im_created_event_to_dict(x: IMCreatedEvent) -> Any:
    return to_class(IMCreatedEvent, x)
