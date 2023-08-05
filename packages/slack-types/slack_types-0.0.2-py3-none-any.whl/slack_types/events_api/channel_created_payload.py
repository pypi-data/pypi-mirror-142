# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = channel_created_payload_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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
class Channel:
    id: Optional[str] = None
    is_channel: Optional[bool] = None
    name: Optional[str] = None
    name_normalized: Optional[str] = None
    created: Optional[int] = None
    creator: Optional[str] = None
    is_shared: Optional[bool] = None
    is_org_shared: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        is_channel = from_union([from_bool, from_none], obj.get("is_channel"))
        name = from_union([from_str, from_none], obj.get("name"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        created = from_union([from_int, from_none], obj.get("created"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_shared = from_union([from_bool, from_none], obj.get("is_shared"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        return Channel(id, is_channel, name, name_normalized, created, creator, is_shared, is_org_shared)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["is_channel"] = from_union([from_bool, from_none], self.is_channel)
        result["name"] = from_union([from_str, from_none], self.name)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["created"] = from_union([from_int, from_none], self.created)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_shared"] = from_union([from_bool, from_none], self.is_shared)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    channel: Optional[Channel] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return Event(type, channel, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


@dataclass
class ChannelCreatedPayload:
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
    def from_dict(obj: Any) -> 'ChannelCreatedPayload':
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
        return ChannelCreatedPayload(token, team_id, enterprise_id, api_app_id, event, type, event_id, event_time, authorizations, is_ext_shared_channel, event_context)

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


def channel_created_payload_from_dict(s: Any) -> ChannelCreatedPayload:
    return ChannelCreatedPayload.from_dict(s)


def channel_created_payload_to_dict(x: ChannelCreatedPayload) -> Any:
    return to_class(ChannelCreatedPayload, x)
