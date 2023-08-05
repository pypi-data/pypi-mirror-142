# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_users_session_get_settings_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class SessionSetting:
    user_id: Optional[str] = None
    desktop_app_browser_quit: Optional[bool] = None
    duration: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SessionSetting':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        desktop_app_browser_quit = from_union([from_bool, from_none], obj.get("desktop_app_browser_quit"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        return SessionSetting(user_id, desktop_app_browser_quit, duration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["desktop_app_browser_quit"] = from_union([from_bool, from_none], self.desktop_app_browser_quit)
        result["duration"] = from_union([from_int, from_none], self.duration)
        return result


@dataclass
class AdminUsersSessionGetSettingsResponse:
    ok: Optional[bool] = None
    session_settings: Optional[List[SessionSetting]] = None
    no_settings_applied: Optional[List[str]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminUsersSessionGetSettingsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        session_settings = from_union([lambda x: from_list(SessionSetting.from_dict, x), from_none], obj.get("session_settings"))
        no_settings_applied = from_union([lambda x: from_list(from_str, x), from_none], obj.get("no_settings_applied"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminUsersSessionGetSettingsResponse(ok, session_settings, no_settings_applied, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["session_settings"] = from_union([lambda x: from_list(lambda x: to_class(SessionSetting, x), x), from_none], self.session_settings)
        result["no_settings_applied"] = from_union([lambda x: from_list(from_str, x), from_none], self.no_settings_applied)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_users_session_get_settings_response_from_dict(s: Any) -> AdminUsersSessionGetSettingsResponse:
    return AdminUsersSessionGetSettingsResponse.from_dict(s)


def admin_users_session_get_settings_response_to_dict(x: AdminUsersSessionGetSettingsResponse) -> Any:
    return to_class(AdminUsersSessionGetSettingsResponse, x)
