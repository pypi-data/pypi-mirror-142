# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_auth_policy_get_entities_response_from_dict(json.loads(json_string))

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
class Entity:
    entity_id: Optional[str] = None
    entity_type: Optional[str] = None
    date_added: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entity':
        assert isinstance(obj, dict)
        entity_id = from_union([from_str, from_none], obj.get("entity_id"))
        entity_type = from_union([from_str, from_none], obj.get("entity_type"))
        date_added = from_union([from_int, from_none], obj.get("date_added"))
        return Entity(entity_id, entity_type, date_added)

    def to_dict(self) -> dict:
        result: dict = {}
        result["entity_id"] = from_union([from_str, from_none], self.entity_id)
        result["entity_type"] = from_union([from_str, from_none], self.entity_type)
        result["date_added"] = from_union([from_int, from_none], self.date_added)
        return result


@dataclass
class AdminAuthPolicyGetEntitiesResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    entities: Optional[List[Entity]] = None
    entity_total_count: Optional[int] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminAuthPolicyGetEntitiesResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        entities = from_union([lambda x: from_list(Entity.from_dict, x), from_none], obj.get("entities"))
        entity_total_count = from_union([from_int, from_none], obj.get("entity_total_count"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminAuthPolicyGetEntitiesResponse(ok, error, entities, entity_total_count, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["entities"] = from_union([lambda x: from_list(lambda x: to_class(Entity, x), x), from_none], self.entities)
        result["entity_total_count"] = from_union([from_int, from_none], self.entity_total_count)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_auth_policy_get_entities_response_from_dict(s: Any) -> AdminAuthPolicyGetEntitiesResponse:
    return AdminAuthPolicyGetEntitiesResponse.from_dict(s)


def admin_auth_policy_get_entities_response_to_dict(x: AdminAuthPolicyGetEntitiesResponse) -> Any:
    return to_class(AdminAuthPolicyGetEntitiesResponse, x)
