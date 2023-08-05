# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = api_test_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Args:
    error: Optional[str] = None
    foo: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Args':
        assert isinstance(obj, dict)
        error = from_union([from_str, from_none], obj.get("error"))
        foo = from_union([from_str, from_none], obj.get("foo"))
        return Args(error, foo)

    def to_dict(self) -> dict:
        result: dict = {}
        result["error"] = from_union([from_str, from_none], self.error)
        result["foo"] = from_union([from_str, from_none], self.foo)
        return result


@dataclass
class APITestResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    args: Optional[Args] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'APITestResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        args = from_union([Args.from_dict, from_none], obj.get("args"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return APITestResponse(ok, error, args, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["args"] = from_union([lambda x: to_class(Args, x), from_none], self.args)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def api_test_response_from_dict(s: Any) -> APITestResponse:
    return APITestResponse.from_dict(s)


def api_test_response_to_dict(x: APITestResponse) -> Any:
    return to_class(APITestResponse, x)
