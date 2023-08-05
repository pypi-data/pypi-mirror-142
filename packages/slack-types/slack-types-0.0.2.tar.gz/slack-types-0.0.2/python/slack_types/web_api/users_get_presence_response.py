# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = users_get_presence_response_from_dict(json.loads(json_string))

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
class UsersGetPresenceResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    presence: Optional[str] = None
    online: Optional[bool] = None
    auto_away: Optional[bool] = None
    manual_away: Optional[bool] = None
    connection_count: Optional[int] = None
    last_activity: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UsersGetPresenceResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        presence = from_union([from_str, from_none], obj.get("presence"))
        online = from_union([from_bool, from_none], obj.get("online"))
        auto_away = from_union([from_bool, from_none], obj.get("auto_away"))
        manual_away = from_union([from_bool, from_none], obj.get("manual_away"))
        connection_count = from_union([from_int, from_none], obj.get("connection_count"))
        last_activity = from_union([from_int, from_none], obj.get("last_activity"))
        return UsersGetPresenceResponse(ok, warning, error, needed, provided, presence, online, auto_away, manual_away, connection_count, last_activity)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["presence"] = from_union([from_str, from_none], self.presence)
        result["online"] = from_union([from_bool, from_none], self.online)
        result["auto_away"] = from_union([from_bool, from_none], self.auto_away)
        result["manual_away"] = from_union([from_bool, from_none], self.manual_away)
        result["connection_count"] = from_union([from_int, from_none], self.connection_count)
        result["last_activity"] = from_union([from_int, from_none], self.last_activity)
        return result


def users_get_presence_response_from_dict(s: Any) -> UsersGetPresenceResponse:
    return UsersGetPresenceResponse.from_dict(s)


def users_get_presence_response_to_dict(x: UsersGetPresenceResponse) -> Any:
    return to_class(UsersGetPresenceResponse, x)
