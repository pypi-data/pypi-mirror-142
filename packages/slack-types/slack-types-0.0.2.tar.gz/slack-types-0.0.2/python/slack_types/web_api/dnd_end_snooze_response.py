# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dnd_end_snooze_response_from_dict(json.loads(json_string))

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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class DNDEndSnoozeResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    dnd_enabled: Optional[bool] = None
    next_dnd_start_ts: Optional[int] = None
    next_dnd_end_ts: Optional[int] = None
    snooze_enabled: Optional[bool] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DNDEndSnoozeResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        dnd_enabled = from_union([from_bool, from_none], obj.get("dnd_enabled"))
        next_dnd_start_ts = from_union([from_int, from_none], obj.get("next_dnd_start_ts"))
        next_dnd_end_ts = from_union([from_int, from_none], obj.get("next_dnd_end_ts"))
        snooze_enabled = from_union([from_bool, from_none], obj.get("snooze_enabled"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return DNDEndSnoozeResponse(ok, error, dnd_enabled, next_dnd_start_ts, next_dnd_end_ts, snooze_enabled, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["dnd_enabled"] = from_union([from_bool, from_none], self.dnd_enabled)
        result["next_dnd_start_ts"] = from_union([from_int, from_none], self.next_dnd_start_ts)
        result["next_dnd_end_ts"] = from_union([from_int, from_none], self.next_dnd_end_ts)
        result["snooze_enabled"] = from_union([from_bool, from_none], self.snooze_enabled)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def dnd_end_snooze_response_from_dict(s: Any) -> DNDEndSnoozeResponse:
    return DNDEndSnoozeResponse.from_dict(s)


def dnd_end_snooze_response_to_dict(x: DNDEndSnoozeResponse) -> Any:
    return to_class(DNDEndSnoozeResponse, x)
