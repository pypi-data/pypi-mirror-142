# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = reminders_info_response_from_dict(json.loads(json_string))

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
class Reminder:
    id: Optional[str] = None
    creator: Optional[str] = None
    text: Optional[str] = None
    user: Optional[str] = None
    recurring: Optional[bool] = None
    time: Optional[int] = None
    complete_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reminder':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        recurring = from_union([from_bool, from_none], obj.get("recurring"))
        time = from_union([from_int, from_none], obj.get("time"))
        complete_ts = from_union([from_int, from_none], obj.get("complete_ts"))
        return Reminder(id, creator, text, user, recurring, time, complete_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["recurring"] = from_union([from_bool, from_none], self.recurring)
        result["time"] = from_union([from_int, from_none], self.time)
        result["complete_ts"] = from_union([from_int, from_none], self.complete_ts)
        return result


@dataclass
class RemindersInfoResponse:
    ok: Optional[bool] = None
    reminder: Optional[Reminder] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemindersInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        reminder = from_union([Reminder.from_dict, from_none], obj.get("reminder"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return RemindersInfoResponse(ok, reminder, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["reminder"] = from_union([lambda x: to_class(Reminder, x), from_none], self.reminder)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def reminders_info_response_from_dict(s: Any) -> RemindersInfoResponse:
    return RemindersInfoResponse.from_dict(s)


def reminders_info_response_to_dict(x: RemindersInfoResponse) -> Any:
    return to_class(RemindersInfoResponse, x)
