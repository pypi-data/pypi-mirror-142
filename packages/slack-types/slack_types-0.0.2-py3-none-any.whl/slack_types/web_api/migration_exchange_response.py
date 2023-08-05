# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = migration_exchange_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, List, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class UserIDMap:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'UserIDMap':
        assert isinstance(obj, dict)
        return UserIDMap()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class MigrationExchangeResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    team_id: Optional[str] = None
    enterprise_id: Optional[str] = None
    invalid_user_ids: Optional[List[str]] = None
    user_id_map: Optional[UserIDMap] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MigrationExchangeResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        invalid_user_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("invalid_user_ids"))
        user_id_map = from_union([UserIDMap.from_dict, from_none], obj.get("user_id_map"))
        return MigrationExchangeResponse(ok, warning, error, needed, provided, team_id, enterprise_id, invalid_user_ids, user_id_map)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["invalid_user_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.invalid_user_ids)
        result["user_id_map"] = from_union([lambda x: to_class(UserIDMap, x), from_none], self.user_id_map)
        return result


def migration_exchange_response_from_dict(s: Any) -> MigrationExchangeResponse:
    return MigrationExchangeResponse.from_dict(s)


def migration_exchange_response_to_dict(x: MigrationExchangeResponse) -> Any:
    return to_class(MigrationExchangeResponse, x)
