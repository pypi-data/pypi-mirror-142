# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dnd_team_info_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Callable, Type, cast


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class User:
    dnd_enabled: Optional[bool] = None
    next_dnd_start_ts: Optional[int] = None
    next_dnd_end_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        dnd_enabled = from_union([from_bool, from_none], obj.get("dnd_enabled"))
        next_dnd_start_ts = from_union([from_int, from_none], obj.get("next_dnd_start_ts"))
        next_dnd_end_ts = from_union([from_int, from_none], obj.get("next_dnd_end_ts"))
        return User(dnd_enabled, next_dnd_start_ts, next_dnd_end_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dnd_enabled"] = from_union([from_bool, from_none], self.dnd_enabled)
        result["next_dnd_start_ts"] = from_union([from_int, from_none], self.next_dnd_start_ts)
        result["next_dnd_end_ts"] = from_union([from_int, from_none], self.next_dnd_end_ts)
        return result


@dataclass
class DNDTeamInfoResponse:
    ok: Optional[bool] = None
    users: Optional[Dict[str, User]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DNDTeamInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        users = from_union([lambda x: from_dict(User.from_dict, x), from_none], obj.get("users"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return DNDTeamInfoResponse(ok, users, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["users"] = from_union([lambda x: from_dict(lambda x: to_class(User, x), x), from_none], self.users)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def dnd_team_info_response_from_dict(s: Any) -> DNDTeamInfoResponse:
    return DNDTeamInfoResponse.from_dict(s)


def dnd_team_info_response_to_dict(x: DNDTeamInfoResponse) -> Any:
    return to_class(DNDTeamInfoResponse, x)
