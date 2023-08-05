# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_billable_info_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, Dict, TypeVar, Callable, Type, cast


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
class BillableInfo:
    billing_active: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BillableInfo':
        assert isinstance(obj, dict)
        billing_active = from_union([from_bool, from_none], obj.get("billing_active"))
        return BillableInfo(billing_active)

    def to_dict(self) -> dict:
        result: dict = {}
        result["billing_active"] = from_union([from_bool, from_none], self.billing_active)
        return result


@dataclass
class TeamBillableInfoResponse:
    ok: Optional[bool] = None
    billable_info: Optional[Dict[str, BillableInfo]] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamBillableInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        billable_info = from_union([lambda x: from_dict(BillableInfo.from_dict, x), from_none], obj.get("billable_info"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return TeamBillableInfoResponse(ok, billable_info, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["billable_info"] = from_union([lambda x: from_dict(lambda x: to_class(BillableInfo, x), x), from_none], self.billable_info)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def team_billable_info_response_from_dict(s: Any) -> TeamBillableInfoResponse:
    return TeamBillableInfoResponse.from_dict(s)


def team_billable_info_response_to_dict(x: TeamBillableInfoResponse) -> Any:
    return to_class(TeamBillableInfoResponse, x)
