# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_users_session_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Created:
    device_hardware: Optional[str] = None
    os: Optional[str] = None
    os_version: Optional[str] = None
    slack_client_version: Optional[str] = None
    ip: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Created':
        assert isinstance(obj, dict)
        device_hardware = from_union([from_str, from_none], obj.get("device_hardware"))
        os = from_union([from_str, from_none], obj.get("os"))
        os_version = from_union([from_str, from_none], obj.get("os_version"))
        slack_client_version = from_union([from_str, from_none], obj.get("slack_client_version"))
        ip = from_union([from_str, from_none], obj.get("ip"))
        return Created(device_hardware, os, os_version, slack_client_version, ip)

    def to_dict(self) -> dict:
        result: dict = {}
        result["device_hardware"] = from_union([from_str, from_none], self.device_hardware)
        result["os"] = from_union([from_str, from_none], self.os)
        result["os_version"] = from_union([from_str, from_none], self.os_version)
        result["slack_client_version"] = from_union([from_str, from_none], self.slack_client_version)
        result["ip"] = from_union([from_str, from_none], self.ip)
        return result


@dataclass
class ActiveSession:
    user_id: Optional[str] = None
    session_id: Optional[int] = None
    team_id: Optional[str] = None
    created: Optional[Created] = None
    recent: Optional[Created] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActiveSession':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        session_id = from_union([from_int, from_none], obj.get("session_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        created = from_union([Created.from_dict, from_none], obj.get("created"))
        recent = from_union([Created.from_dict, from_none], obj.get("recent"))
        return ActiveSession(user_id, session_id, team_id, created, recent)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["session_id"] = from_union([from_int, from_none], self.session_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["created"] = from_union([lambda x: to_class(Created, x), from_none], self.created)
        result["recent"] = from_union([lambda x: to_class(Created, x), from_none], self.recent)
        return result


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        return ResponseMetadata(next_cursor)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        return result


@dataclass
class AdminUsersSessionListResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    active_sessions: Optional[List[ActiveSession]] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminUsersSessionListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        active_sessions = from_union([lambda x: from_list(ActiveSession.from_dict, x), from_none], obj.get("active_sessions"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminUsersSessionListResponse(ok, error, active_sessions, response_metadata, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["active_sessions"] = from_union([lambda x: from_list(lambda x: to_class(ActiveSession, x), x), from_none], self.active_sessions)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_users_session_list_response_from_dict(s: Any) -> AdminUsersSessionListResponse:
    return AdminUsersSessionListResponse.from_dict(s)


def admin_users_session_list_response_to_dict(x: AdminUsersSessionListResponse) -> Any:
    return to_class(AdminUsersSessionListResponse, x)
