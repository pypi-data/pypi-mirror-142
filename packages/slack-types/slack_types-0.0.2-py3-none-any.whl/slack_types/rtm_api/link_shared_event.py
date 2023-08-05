# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = link_shared_event_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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
class LinkSharedEvent:
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
    def from_dict(obj: Any) -> 'LinkSharedEvent':
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
        return LinkSharedEvent(type, channel, user, message_ts, thread_ts, links, is_bot_user_member, unfurl_id, source, event_ts)

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


def link_shared_event_from_dict(s: Any) -> LinkSharedEvent:
    return LinkSharedEvent.from_dict(s)


def link_shared_event_to_dict(x: LinkSharedEvent) -> Any:
    return to_class(LinkSharedEvent, x)
