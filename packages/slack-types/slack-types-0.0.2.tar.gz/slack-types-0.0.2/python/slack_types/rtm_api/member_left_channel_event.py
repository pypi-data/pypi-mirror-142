# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = member_left_channel_event_from_dict(json.loads(json_string))

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
class MemberLeftChannelEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    channel: Optional[str] = None
    channel_type: Optional[str] = None
    team: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MemberLeftChannelEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        channel_type = from_union([from_str, from_none], obj.get("channel_type"))
        team = from_union([from_str, from_none], obj.get("team"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return MemberLeftChannelEvent(type, user, channel, channel_type, team, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["channel_type"] = from_union([from_str, from_none], self.channel_type)
        result["team"] = from_union([from_str, from_none], self.team)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def member_left_channel_event_from_dict(s: Any) -> MemberLeftChannelEvent:
    return MemberLeftChannelEvent.from_dict(s)


def member_left_channel_event_to_dict(x: MemberLeftChannelEvent) -> Any:
    return to_class(MemberLeftChannelEvent, x)
