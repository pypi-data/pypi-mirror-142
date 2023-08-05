# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = emoji_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Dict, Any, TypeVar, Callable, Type, cast


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class EmojiListResponse:
    ok: Optional[bool] = None
    emoji: Optional[Dict[str, str]] = None
    cache_ts: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EmojiListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        emoji = from_union([lambda x: from_dict(from_str, x), from_none], obj.get("emoji"))
        cache_ts = from_union([from_str, from_none], obj.get("cache_ts"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return EmojiListResponse(ok, emoji, cache_ts, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["emoji"] = from_union([lambda x: from_dict(from_str, x), from_none], self.emoji)
        result["cache_ts"] = from_union([from_str, from_none], self.cache_ts)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def emoji_list_response_from_dict(s: Any) -> EmojiListResponse:
    return EmojiListResponse.from_dict(s)


def emoji_list_response_to_dict(x: EmojiListResponse) -> Any:
    return to_class(EmojiListResponse, x)
