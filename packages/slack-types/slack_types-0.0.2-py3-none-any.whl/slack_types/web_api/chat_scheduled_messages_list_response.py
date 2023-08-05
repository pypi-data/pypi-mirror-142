# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = chat_scheduled_messages_list_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


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
class ScheduledMessage:
    id: Optional[str] = None
    channel_id: Optional[str] = None
    post_at: Optional[int] = None
    date_created: Optional[int] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ScheduledMessage':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        post_at = from_union([from_int, from_none], obj.get("post_at"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        text = from_union([from_str, from_none], obj.get("text"))
        return ScheduledMessage(id, channel_id, post_at, date_created, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["post_at"] = from_union([from_int, from_none], self.post_at)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["text"] = from_union([from_str, from_none], self.text)
        return result


@dataclass
class ChatScheduledMessagesListResponse:
    ok: Optional[bool] = None
    scheduled_messages: Optional[List[ScheduledMessage]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChatScheduledMessagesListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        scheduled_messages = from_union([lambda x: from_list(ScheduledMessage.from_dict, x), from_none], obj.get("scheduled_messages"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ChatScheduledMessagesListResponse(ok, scheduled_messages, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["scheduled_messages"] = from_union([lambda x: from_list(lambda x: to_class(ScheduledMessage, x), x), from_none], self.scheduled_messages)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def chat_scheduled_messages_list_response_from_dict(s: Any) -> ChatScheduledMessagesListResponse:
    return ChatScheduledMessagesListResponse.from_dict(s)


def chat_scheduled_messages_list_response_to_dict(x: ChatScheduledMessagesListResponse) -> Any:
    return to_class(ChatScheduledMessagesListResponse, x)
