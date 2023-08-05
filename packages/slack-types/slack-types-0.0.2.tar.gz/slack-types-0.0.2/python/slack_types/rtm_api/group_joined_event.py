# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = group_joined_event_from_dict(json.loads(json_string))

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
class GroupJoinedEvent:
    type: Optional[str] = None
    channel: Optional[Channel] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupJoinedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        return GroupJoinedEvent(type, channel)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        return result


def group_joined_event_from_dict(s: Any) -> GroupJoinedEvent:
    return GroupJoinedEvent.from_dict(s)


def group_joined_event_to_dict(x: GroupJoinedEvent) -> Any:
    return to_class(GroupJoinedEvent, x)
