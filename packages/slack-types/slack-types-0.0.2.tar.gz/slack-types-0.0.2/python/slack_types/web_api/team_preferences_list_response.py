# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_preferences_list_response_from_dict(json.loads(json_string))

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
class TeamPreferencesListResponse:
    ok: Optional[bool] = None
    msg_edit_window_mins: Optional[int] = None
    allow_message_deletion: Optional[bool] = None
    display_real_names: Optional[bool] = None
    disable_file_uploads: Optional[str] = None
    who_can_post_general: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamPreferencesListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        msg_edit_window_mins = from_union([from_int, from_none], obj.get("msg_edit_window_mins"))
        allow_message_deletion = from_union([from_bool, from_none], obj.get("allow_message_deletion"))
        display_real_names = from_union([from_bool, from_none], obj.get("display_real_names"))
        disable_file_uploads = from_union([from_str, from_none], obj.get("disable_file_uploads"))
        who_can_post_general = from_union([from_str, from_none], obj.get("who_can_post_general"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return TeamPreferencesListResponse(ok, msg_edit_window_mins, allow_message_deletion, display_real_names, disable_file_uploads, who_can_post_general, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["msg_edit_window_mins"] = from_union([from_int, from_none], self.msg_edit_window_mins)
        result["allow_message_deletion"] = from_union([from_bool, from_none], self.allow_message_deletion)
        result["display_real_names"] = from_union([from_bool, from_none], self.display_real_names)
        result["disable_file_uploads"] = from_union([from_str, from_none], self.disable_file_uploads)
        result["who_can_post_general"] = from_union([from_str, from_none], self.who_can_post_general)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def team_preferences_list_response_from_dict(s: Any) -> TeamPreferencesListResponse:
    return TeamPreferencesListResponse.from_dict(s)


def team_preferences_list_response_to_dict(x: TeamPreferencesListResponse) -> Any:
    return to_class(TeamPreferencesListResponse, x)
