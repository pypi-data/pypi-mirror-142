# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = reminders_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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
class Recurrence:
    frequency: Optional[str] = None
    weekdays: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Recurrence':
        assert isinstance(obj, dict)
        frequency = from_union([from_str, from_none], obj.get("frequency"))
        weekdays = from_union([lambda x: from_list(from_str, x), from_none], obj.get("weekdays"))
        return Recurrence(frequency, weekdays)

    def to_dict(self) -> dict:
        result: dict = {}
        result["frequency"] = from_union([from_str, from_none], self.frequency)
        result["weekdays"] = from_union([lambda x: from_list(from_str, x), from_none], self.weekdays)
        return result


@dataclass
class Reminder:
    id: Optional[str] = None
    creator: Optional[str] = None
    text: Optional[str] = None
    user: Optional[str] = None
    recurring: Optional[bool] = None
    time: Optional[int] = None
    complete_ts: Optional[int] = None
    channel: Optional[str] = None
    recurrence: Optional[Recurrence] = None

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
        channel = from_union([from_str, from_none], obj.get("channel"))
        recurrence = from_union([Recurrence.from_dict, from_none], obj.get("recurrence"))
        return Reminder(id, creator, text, user, recurring, time, complete_ts, channel, recurrence)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["recurring"] = from_union([from_bool, from_none], self.recurring)
        result["time"] = from_union([from_int, from_none], self.time)
        result["complete_ts"] = from_union([from_int, from_none], self.complete_ts)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["recurrence"] = from_union([lambda x: to_class(Recurrence, x), from_none], self.recurrence)
        return result


@dataclass
class RemindersListResponse:
    ok: Optional[bool] = None
    reminders: Optional[List[Reminder]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RemindersListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        reminders = from_union([lambda x: from_list(Reminder.from_dict, x), from_none], obj.get("reminders"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return RemindersListResponse(ok, reminders, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["reminders"] = from_union([lambda x: from_list(lambda x: to_class(Reminder, x), x), from_none], self.reminders)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def reminders_list_response_from_dict(s: Any) -> RemindersListResponse:
    return RemindersListResponse.from_dict(s)


def reminders_list_response_to_dict(x: RemindersListResponse) -> Any:
    return to_class(RemindersListResponse, x)
