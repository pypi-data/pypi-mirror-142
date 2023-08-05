# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = groups_history_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Message:
    type: Optional[str] = None
    subtype: Optional[str] = None
    ts: Optional[str] = None
    user: Optional[str] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        user = from_union([from_str, from_none], obj.get("user"))
        text = from_union([from_str, from_none], obj.get("text"))
        return Message(type, subtype, ts, user, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["user"] = from_union([from_str, from_none], self.user)
        result["text"] = from_union([from_str, from_none], self.text)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None
    warnings: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(from_str, x), from_none], obj.get("warnings"))
        return ResponseMetadata(messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(from_str, x), from_none], self.warnings)
        return result


@dataclass
class GroupsHistoryResponse:
    ok: Optional[bool] = None
    messages: Optional[List[Message]] = None
    has_more: Optional[bool] = None
    channel_actions_count: Optional[int] = None
    warning: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupsHistoryResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        messages = from_union([lambda x: from_list(Message.from_dict, x), from_none], obj.get("messages"))
        has_more = from_union([from_bool, from_none], obj.get("has_more"))
        channel_actions_count = from_union([from_int, from_none], obj.get("channel_actions_count"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return GroupsHistoryResponse(ok, messages, has_more, channel_actions_count, warning, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["messages"] = from_union([lambda x: from_list(lambda x: to_class(Message, x), x), from_none], self.messages)
        result["has_more"] = from_union([from_bool, from_none], self.has_more)
        result["channel_actions_count"] = from_union([from_int, from_none], self.channel_actions_count)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def groups_history_response_from_dict(s: Any) -> GroupsHistoryResponse:
    return GroupsHistoryResponse.from_dict(s)


def groups_history_response_to_dict(x: GroupsHistoryResponse) -> Any:
    return to_class(GroupsHistoryResponse, x)
