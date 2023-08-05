# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dnd_updated_user_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class DNDStatus:
    dnd_enabled: Optional[bool] = None
    next_dnd_start_ts: Optional[int] = None
    next_dnd_end_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DNDStatus':
        assert isinstance(obj, dict)
        dnd_enabled = from_union([from_bool, from_none], obj.get("dnd_enabled"))
        next_dnd_start_ts = from_union([from_int, from_none], obj.get("next_dnd_start_ts"))
        next_dnd_end_ts = from_union([from_int, from_none], obj.get("next_dnd_end_ts"))
        return DNDStatus(dnd_enabled, next_dnd_start_ts, next_dnd_end_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dnd_enabled"] = from_union([from_bool, from_none], self.dnd_enabled)
        result["next_dnd_start_ts"] = from_union([from_int, from_none], self.next_dnd_start_ts)
        result["next_dnd_end_ts"] = from_union([from_int, from_none], self.next_dnd_end_ts)
        return result


@dataclass
class DNDUpdatedUserEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    dnd_status: Optional[DNDStatus] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DNDUpdatedUserEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        dnd_status = from_union([DNDStatus.from_dict, from_none], obj.get("dnd_status"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return DNDUpdatedUserEvent(type, user, dnd_status, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["dnd_status"] = from_union([lambda x: to_class(DNDStatus, x), from_none], self.dnd_status)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def dnd_updated_user_event_from_dict(s: Any) -> DNDUpdatedUserEvent:
    return DNDUpdatedUserEvent.from_dict(s)


def dnd_updated_user_event_to_dict(x: DNDUpdatedUserEvent) -> Any:
    return to_class(DNDUpdatedUserEvent, x)
