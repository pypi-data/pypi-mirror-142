# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_emoji_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Callable, Type, cast


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Emoji:
    url: Optional[str] = None
    date_created: Optional[int] = None
    uploaded_by: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Emoji':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        uploaded_by = from_union([from_str, from_none], obj.get("uploaded_by"))
        return Emoji(url, date_created, uploaded_by)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_union([from_str, from_none], self.url)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["uploaded_by"] = from_union([from_str, from_none], self.uploaded_by)
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
class AdminEmojiListResponse:
    ok: Optional[bool] = None
    emoji: Optional[Dict[str, Emoji]] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminEmojiListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        emoji = from_union([lambda x: from_dict(Emoji.from_dict, x), from_none], obj.get("emoji"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminEmojiListResponse(ok, emoji, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["emoji"] = from_union([lambda x: from_dict(lambda x: to_class(Emoji, x), x), from_none], self.emoji)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_emoji_list_response_from_dict(s: Any) -> AdminEmojiListResponse:
    return AdminEmojiListResponse.from_dict(s)


def admin_emoji_list_response_to_dict(x: AdminEmojiListResponse) -> Any:
    return to_class(AdminEmojiListResponse, x)
