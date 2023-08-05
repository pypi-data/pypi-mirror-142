# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = auth_test_response_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AuthTestResponse:
    ok: Optional[bool] = None
    url: Optional[str] = None
    team: Optional[str] = None
    user: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    bot_id: Optional[str] = None
    is_enterprise_install: Optional[bool] = None
    app_name: Optional[str] = None
    app_id: Optional[str] = None
    enterprise_id: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthTestResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        url = from_union([from_str, from_none], obj.get("url"))
        team = from_union([from_str, from_none], obj.get("team"))
        user = from_union([from_str, from_none], obj.get("user"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        app_name = from_union([from_str, from_none], obj.get("app_name"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AuthTestResponse(ok, url, team, user, team_id, user_id, bot_id, is_enterprise_install, app_name, app_id, enterprise_id, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["url"] = from_union([from_str, from_none], self.url)
        result["team"] = from_union([from_str, from_none], self.team)
        result["user"] = from_union([from_str, from_none], self.user)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        result["app_name"] = from_union([from_str, from_none], self.app_name)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def auth_test_response_from_dict(s: Any) -> AuthTestResponse:
    return AuthTestResponse.from_dict(s)


def auth_test_response_to_dict(x: AuthTestResponse) -> Any:
    return to_class(AuthTestResponse, x)
