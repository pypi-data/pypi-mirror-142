# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = group_rename_event_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    name_normalized: Optional[str] = None
    is_channel: Optional[bool] = None
    is_group: Optional[bool] = None
    is_mpim: Optional[bool] = None
    created: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_channel = from_union([from_bool, from_none], obj.get("is_channel"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        created = from_union([from_int, from_none], obj.get("created"))
        return Channel(id, name, name_normalized, is_channel, is_group, is_mpim, created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_channel"] = from_union([from_bool, from_none], self.is_channel)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["created"] = from_union([from_int, from_none], self.created)
        return result


@dataclass
class GroupRenameEvent:
    type: Optional[str] = None
    channel: Optional[Channel] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupRenameEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return GroupRenameEvent(type, channel, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def group_rename_event_from_dict(s: Any) -> GroupRenameEvent:
    return GroupRenameEvent.from_dict(s)


def group_rename_event_to_dict(x: GroupRenameEvent) -> Any:
    return to_class(GroupRenameEvent, x)
