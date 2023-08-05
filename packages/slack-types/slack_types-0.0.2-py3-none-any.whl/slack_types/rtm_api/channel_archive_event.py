# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = channel_archive_event_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ChannelArchiveEvent:
    type: Optional[str] = None
    channel: Optional[str] = None
    user: Optional[str] = None
    is_moved: Optional[int] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChannelArchiveEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        user = from_union([from_str, from_none], obj.get("user"))
        is_moved = from_union([from_int, from_none], obj.get("is_moved"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return ChannelArchiveEvent(type, channel, user, is_moved, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["user"] = from_union([from_str, from_none], self.user)
        result["is_moved"] = from_union([from_int, from_none], self.is_moved)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def channel_archive_event_from_dict(s: Any) -> ChannelArchiveEvent:
    return ChannelArchiveEvent.from_dict(s)


def channel_archive_event_to_dict(x: ChannelArchiveEvent) -> Any:
    return to_class(ChannelArchiveEvent, x)
