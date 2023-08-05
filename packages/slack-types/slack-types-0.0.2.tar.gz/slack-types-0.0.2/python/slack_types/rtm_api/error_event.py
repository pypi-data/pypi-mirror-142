# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = error_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
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
class Error:
    code: Optional[int] = None
    msg: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Error':
        assert isinstance(obj, dict)
        code = from_union([from_int, from_none], obj.get("code"))
        msg = from_union([from_str, from_none], obj.get("msg"))
        return Error(code, msg)

    def to_dict(self) -> dict:
        result: dict = {}
        result["code"] = from_union([from_int, from_none], self.code)
        result["msg"] = from_union([from_str, from_none], self.msg)
        return result


@dataclass
class ErrorEvent:
    type: Optional[str] = None
    error: Optional[Error] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ErrorEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        error = from_union([Error.from_dict, from_none], obj.get("error"))
        return ErrorEvent(type, error)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["error"] = from_union([lambda x: to_class(Error, x), from_none], self.error)
        return result


def error_event_from_dict(s: Any) -> ErrorEvent:
    return ErrorEvent.from_dict(s)


def error_event_to_dict(x: ErrorEvent) -> Any:
    return to_class(ErrorEvent, x)
