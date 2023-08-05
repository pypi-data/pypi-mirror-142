# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = subteam_created_payload_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Authorization:
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    is_bot: Optional[bool] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Authorization':
        assert isinstance(obj, dict)
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return Authorization(enterprise_id, team_id, user_id, is_bot, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


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
class Subteam:
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
    users: Optional[List[str]] = None
    user_count: Optional[int] = None
    channel_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Subteam':
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
        users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("users"))
        user_count = from_union([from_int, from_none], obj.get("user_count"))
        channel_count = from_union([from_int, from_none], obj.get("channel_count"))
        return Subteam(id, team_id, is_usergroup, is_subteam, name, description, handle, is_external, date_create, date_update, date_delete, auto_provision, enterprise_subteam_id, created_by, updated_by, prefs, users, user_count, channel_count)

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
        result["users"] = from_union([lambda x: from_list(from_str, x), from_none], self.users)
        result["user_count"] = from_union([from_int, from_none], self.user_count)
        result["channel_count"] = from_union([from_int, from_none], self.channel_count)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    subteam: Optional[Subteam] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subteam = from_union([Subteam.from_dict, from_none], obj.get("subteam"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return Event(type, subteam, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subteam"] = from_union([lambda x: to_class(Subteam, x), from_none], self.subteam)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


@dataclass
class SubteamCreatedPayload:
    token: Optional[str] = None
    team_id: Optional[str] = None
    enterprise_id: Optional[str] = None
    api_app_id: Optional[str] = None
    event: Optional[Event] = None
    type: Optional[str] = None
    event_id: Optional[str] = None
    event_time: Optional[int] = None
    authorizations: Optional[List[Authorization]] = None
    is_ext_shared_channel: Optional[bool] = None
    event_context: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubteamCreatedPayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        event = from_union([Event.from_dict, from_none], obj.get("event"))
        type = from_union([from_str, from_none], obj.get("type"))
        event_id = from_union([from_str, from_none], obj.get("event_id"))
        event_time = from_union([from_int, from_none], obj.get("event_time"))
        authorizations = from_union([lambda x: from_list(Authorization.from_dict, x), from_none], obj.get("authorizations"))
        is_ext_shared_channel = from_union([from_bool, from_none], obj.get("is_ext_shared_channel"))
        event_context = from_union([from_str, from_none], obj.get("event_context"))
        return SubteamCreatedPayload(token, team_id, enterprise_id, api_app_id, event, type, event_id, event_time, authorizations, is_ext_shared_channel, event_context)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["event"] = from_union([lambda x: to_class(Event, x), from_none], self.event)
        result["type"] = from_union([from_str, from_none], self.type)
        result["event_id"] = from_union([from_str, from_none], self.event_id)
        result["event_time"] = from_union([from_int, from_none], self.event_time)
        result["authorizations"] = from_union([lambda x: from_list(lambda x: to_class(Authorization, x), x), from_none], self.authorizations)
        result["is_ext_shared_channel"] = from_union([from_bool, from_none], self.is_ext_shared_channel)
        result["event_context"] = from_union([from_str, from_none], self.event_context)
        return result


def subteam_created_payload_from_dict(s: Any) -> SubteamCreatedPayload:
    return SubteamCreatedPayload.from_dict(s)


def subteam_created_payload_to_dict(x: SubteamCreatedPayload) -> Any:
    return to_class(SubteamCreatedPayload, x)
