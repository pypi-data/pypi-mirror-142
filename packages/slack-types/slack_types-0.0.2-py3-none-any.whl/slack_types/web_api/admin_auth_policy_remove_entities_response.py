# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_auth_policy_remove_entities_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AdminAuthPolicyRemoveEntitiesResponse:
    ok: Optional[bool] = None
    entity_total_count: Optional[int] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminAuthPolicyRemoveEntitiesResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        entity_total_count = from_union([from_int, from_none], obj.get("entity_total_count"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminAuthPolicyRemoveEntitiesResponse(ok, entity_total_count, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["entity_total_count"] = from_union([from_int, from_none], self.entity_total_count)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_auth_policy_remove_entities_response_from_dict(s: Any) -> AdminAuthPolicyRemoveEntitiesResponse:
    return AdminAuthPolicyRemoveEntitiesResponse.from_dict(s)


def admin_auth_policy_remove_entities_response_to_dict(x: AdminAuthPolicyRemoveEntitiesResponse) -> Any:
    return to_class(AdminAuthPolicyRemoveEntitiesResponse, x)
