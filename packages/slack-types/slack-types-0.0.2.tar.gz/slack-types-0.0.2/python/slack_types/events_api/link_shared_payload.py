# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = link_shared_payload_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


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
class Link:
    domain: Optional[str] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Link':
        assert isinstance(obj, dict)
        domain = from_union([from_str, from_none], obj.get("domain"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Link(domain, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["domain"] = from_union([from_str, from_none], self.domain)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    channel: Optional[str] = None
    user: Optional[str] = None
    message_ts: Optional[str] = None
    thread_ts: Optional[str] = None
    links: Optional[List[Link]] = None
    is_bot_user_member: Optional[bool] = None
    unfurl_id: Optional[str] = None
    source: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        user = from_union([from_str, from_none], obj.get("user"))
        message_ts = from_union([from_str, from_none], obj.get("message_ts"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        links = from_union([lambda x: from_list(Link.from_dict, x), from_none], obj.get("links"))
        is_bot_user_member = from_union([from_bool, from_none], obj.get("is_bot_user_member"))
        unfurl_id = from_union([from_str, from_none], obj.get("unfurl_id"))
        source = from_union([from_str, from_none], obj.get("source"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return Event(type, channel, user, message_ts, thread_ts, links, is_bot_user_member, unfurl_id, source, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["user"] = from_union([from_str, from_none], self.user)
        result["message_ts"] = from_union([from_str, from_none], self.message_ts)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["links"] = from_union([lambda x: from_list(lambda x: to_class(Link, x), x), from_none], self.links)
        result["is_bot_user_member"] = from_union([from_bool, from_none], self.is_bot_user_member)
        result["unfurl_id"] = from_union([from_str, from_none], self.unfurl_id)
        result["source"] = from_union([from_str, from_none], self.source)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


@dataclass
class LinkSharedPayload:
    token: Optional[str] = None
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    api_app_id: Optional[str] = None
    type: Optional[str] = None
    authed_users: Optional[List[str]] = None
    authed_teams: Optional[List[str]] = None
    authorizations: Optional[List[Authorization]] = None
    is_ext_shared_channel: Optional[bool] = None
    event_id: Optional[str] = None
    event_time: Optional[int] = None
    event_context: Optional[str] = None
    event: Optional[Event] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LinkSharedPayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        authed_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_users"))
        authed_teams = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_teams"))
        authorizations = from_union([lambda x: from_list(Authorization.from_dict, x), from_none], obj.get("authorizations"))
        is_ext_shared_channel = from_union([from_bool, from_none], obj.get("is_ext_shared_channel"))
        event_id = from_union([from_str, from_none], obj.get("event_id"))
        event_time = from_union([from_int, from_none], obj.get("event_time"))
        event_context = from_union([from_str, from_none], obj.get("event_context"))
        event = from_union([Event.from_dict, from_none], obj.get("event"))
        return LinkSharedPayload(token, enterprise_id, team_id, api_app_id, type, authed_users, authed_teams, authorizations, is_ext_shared_channel, event_id, event_time, event_context, event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["authed_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_users)
        result["authed_teams"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_teams)
        result["authorizations"] = from_union([lambda x: from_list(lambda x: to_class(Authorization, x), x), from_none], self.authorizations)
        result["is_ext_shared_channel"] = from_union([from_bool, from_none], self.is_ext_shared_channel)
        result["event_id"] = from_union([from_str, from_none], self.event_id)
        result["event_time"] = from_union([from_int, from_none], self.event_time)
        result["event_context"] = from_union([from_str, from_none], self.event_context)
        result["event"] = from_union([lambda x: to_class(Event, x), from_none], self.event)
        return result


def link_shared_payload_from_dict(s: Any) -> LinkSharedPayload:
    return LinkSharedPayload.from_dict(s)


def link_shared_payload_to_dict(x: LinkSharedPayload) -> Any:
    return to_class(LinkSharedPayload, x)
