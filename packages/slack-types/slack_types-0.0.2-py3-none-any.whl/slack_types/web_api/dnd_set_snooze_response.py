# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dnd_set_snooze_response_from_dict(json.loads(json_string))

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
class DNDSetSnoozeResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    snooze_enabled: Optional[bool] = None
    snooze_endtime: Optional[int] = None
    snooze_remaining: Optional[int] = None
    snooze_is_indefinite: Optional[bool] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DNDSetSnoozeResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        snooze_enabled = from_union([from_bool, from_none], obj.get("snooze_enabled"))
        snooze_endtime = from_union([from_int, from_none], obj.get("snooze_endtime"))
        snooze_remaining = from_union([from_int, from_none], obj.get("snooze_remaining"))
        snooze_is_indefinite = from_union([from_bool, from_none], obj.get("snooze_is_indefinite"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return DNDSetSnoozeResponse(ok, error, snooze_enabled, snooze_endtime, snooze_remaining, snooze_is_indefinite, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["snooze_enabled"] = from_union([from_bool, from_none], self.snooze_enabled)
        result["snooze_endtime"] = from_union([from_int, from_none], self.snooze_endtime)
        result["snooze_remaining"] = from_union([from_int, from_none], self.snooze_remaining)
        result["snooze_is_indefinite"] = from_union([from_bool, from_none], self.snooze_is_indefinite)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def dnd_set_snooze_response_from_dict(s: Any) -> DNDSetSnoozeResponse:
    return DNDSetSnoozeResponse.from_dict(s)


def dnd_set_snooze_response_to_dict(x: DNDSetSnoozeResponse) -> Any:
    return to_class(DNDSetSnoozeResponse, x)
