# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = calls_info_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class User:
    external_id: Optional[str] = None
    avatar_url: Optional[str] = None
    display_name: Optional[str] = None
    slack_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        avatar_url = from_union([from_str, from_none], obj.get("avatar_url"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        slack_id = from_union([from_str, from_none], obj.get("slack_id"))
        return User(external_id, avatar_url, display_name, slack_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["avatar_url"] = from_union([from_str, from_none], self.avatar_url)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["slack_id"] = from_union([from_str, from_none], self.slack_id)
        return result


@dataclass
class Call:
    id: Optional[str] = None
    date_start: Optional[int] = None
    external_unique_id: Optional[str] = None
    join_url: Optional[str] = None
    channels: Optional[List[str]] = None
    external_display_id: Optional[str] = None
    title: Optional[str] = None
    desktop_app_join_url: Optional[str] = None
    users: Optional[List[User]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Call':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        date_start = from_union([from_int, from_none], obj.get("date_start"))
        external_unique_id = from_union([from_str, from_none], obj.get("external_unique_id"))
        join_url = from_union([from_str, from_none], obj.get("join_url"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        external_display_id = from_union([from_str, from_none], obj.get("external_display_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        desktop_app_join_url = from_union([from_str, from_none], obj.get("desktop_app_join_url"))
        users = from_union([lambda x: from_list(User.from_dict, x), from_none], obj.get("users"))
        return Call(id, date_start, external_unique_id, join_url, channels, external_display_id, title, desktop_app_join_url, users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["date_start"] = from_union([from_int, from_none], self.date_start)
        result["external_unique_id"] = from_union([from_str, from_none], self.external_unique_id)
        result["join_url"] = from_union([from_str, from_none], self.join_url)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["external_display_id"] = from_union([from_str, from_none], self.external_display_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["desktop_app_join_url"] = from_union([from_str, from_none], self.desktop_app_join_url)
        result["users"] = from_union([lambda x: from_list(lambda x: to_class(User, x), x), from_none], self.users)
        return result


@dataclass
class CallsInfoResponse:
    ok: Optional[bool] = None
    call: Optional[Call] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CallsInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        call = from_union([Call.from_dict, from_none], obj.get("call"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return CallsInfoResponse(ok, call, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["call"] = from_union([lambda x: to_class(Call, x), from_none], self.call)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def calls_info_response_from_dict(s: Any) -> CallsInfoResponse:
    return CallsInfoResponse.from_dict(s)


def calls_info_response_to_dict(x: CallsInfoResponse) -> Any:
    return to_class(CallsInfoResponse, x)
