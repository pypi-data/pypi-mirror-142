# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = openid_connect_token_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class OpenidConnectTokenResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    access_token: Optional[str] = None
    token_type: Optional[str] = None
    id_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OpenidConnectTokenResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        token_type = from_union([from_str, from_none], obj.get("token_type"))
        id_token = from_union([from_str, from_none], obj.get("id_token"))
        refresh_token = from_union([from_str, from_none], obj.get("refresh_token"))
        expires_in = from_union([from_int, from_none], obj.get("expires_in"))
        return OpenidConnectTokenResponse(ok, warning, error, needed, provided, access_token, token_type, id_token, refresh_token, expires_in)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["access_token"] = from_union([from_str, from_none], self.access_token)
        result["token_type"] = from_union([from_str, from_none], self.token_type)
        result["id_token"] = from_union([from_str, from_none], self.id_token)
        result["refresh_token"] = from_union([from_str, from_none], self.refresh_token)
        result["expires_in"] = from_union([from_int, from_none], self.expires_in)
        return result


def openid_connect_token_response_from_dict(s: Any) -> OpenidConnectTokenResponse:
    return OpenidConnectTokenResponse.from_dict(s)


def openid_connect_token_response_to_dict(x: OpenidConnectTokenResponse) -> Any:
    return to_class(OpenidConnectTokenResponse, x)
