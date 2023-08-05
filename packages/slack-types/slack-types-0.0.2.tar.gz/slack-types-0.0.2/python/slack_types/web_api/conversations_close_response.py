# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conversations_close_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ConversationsCloseResponse:
    ok: Optional[bool] = None
    already_closed: Optional[bool] = None
    no_op: Optional[bool] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationsCloseResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        already_closed = from_union([from_bool, from_none], obj.get("already_closed"))
        no_op = from_union([from_bool, from_none], obj.get("no_op"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ConversationsCloseResponse(ok, already_closed, no_op, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["already_closed"] = from_union([from_bool, from_none], self.already_closed)
        result["no_op"] = from_union([from_bool, from_none], self.no_op)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def conversations_close_response_from_dict(s: Any) -> ConversationsCloseResponse:
    return ConversationsCloseResponse.from_dict(s)


def conversations_close_response_to_dict(x: ConversationsCloseResponse) -> Any:
    return to_class(ConversationsCloseResponse, x)
