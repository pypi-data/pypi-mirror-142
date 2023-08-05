# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = usergroups_create_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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
class Prefs:
    channels: Optional[List[str]] = None
    groups: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Prefs':
        assert isinstance(obj, dict)
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        return Prefs(channels, groups)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        return result


@dataclass
class Usergroup:
    id: Optional[str] = None
    team_id: Optional[str] = None
    is_usergroup: Optional[bool] = None
    is_subteam: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    handle: Optional[str] = None
    is_external: Optional[bool] = None
    date_create: Optional[int] = None
    date_update: Optional[int] = None
    date_delete: Optional[int] = None
    auto_provision: Optional[bool] = None
    enterprise_subteam_id: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    prefs: Optional[Prefs] = None
    channel_count: Optional[int] = None
    users: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Usergroup':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        is_usergroup = from_union([from_bool, from_none], obj.get("is_usergroup"))
        is_subteam = from_union([from_bool, from_none], obj.get("is_subteam"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        handle = from_union([from_str, from_none], obj.get("handle"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        date_create = from_union([from_int, from_none], obj.get("date_create"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        date_delete = from_union([from_int, from_none], obj.get("date_delete"))
        auto_provision = from_union([from_bool, from_none], obj.get("auto_provision"))
        enterprise_subteam_id = from_union([from_str, from_none], obj.get("enterprise_subteam_id"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        updated_by = from_union([from_str, from_none], obj.get("updated_by"))
        prefs = from_union([Prefs.from_dict, from_none], obj.get("prefs"))
        channel_count = from_union([from_int, from_none], obj.get("channel_count"))
        users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("users"))
        return Usergroup(id, team_id, is_usergroup, is_subteam, name, description, handle, is_external, date_create, date_update, date_delete, auto_provision, enterprise_subteam_id, created_by, updated_by, prefs, channel_count, users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["is_usergroup"] = from_union([from_bool, from_none], self.is_usergroup)
        result["is_subteam"] = from_union([from_bool, from_none], self.is_subteam)
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["handle"] = from_union([from_str, from_none], self.handle)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["date_create"] = from_union([from_int, from_none], self.date_create)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["date_delete"] = from_union([from_int, from_none], self.date_delete)
        result["auto_provision"] = from_union([from_bool, from_none], self.auto_provision)
        result["enterprise_subteam_id"] = from_union([from_str, from_none], self.enterprise_subteam_id)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["updated_by"] = from_union([from_str, from_none], self.updated_by)
        result["prefs"] = from_union([lambda x: to_class(Prefs, x), from_none], self.prefs)
        result["channel_count"] = from_union([from_int, from_none], self.channel_count)
        result["users"] = from_union([lambda x: from_list(from_str, x), from_none], self.users)
        return result


@dataclass
class UsergroupsCreateResponse:
    ok: Optional[bool] = None
    usergroup: Optional[Usergroup] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UsergroupsCreateResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        usergroup = from_union([Usergroup.from_dict, from_none], obj.get("usergroup"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return UsergroupsCreateResponse(ok, usergroup, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["usergroup"] = from_union([lambda x: to_class(Usergroup, x), from_none], self.usergroup)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def usergroups_create_response_from_dict(s: Any) -> UsergroupsCreateResponse:
    return UsergroupsCreateResponse.from_dict(s)


def usergroups_create_response_to_dict(x: UsergroupsCreateResponse) -> Any:
    return to_class(UsergroupsCreateResponse, x)
