# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_plan_change_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class TeamPlanChangeEvent:
    type: Optional[str] = None
    plan: Optional[str] = None
    can_add_ura: Optional[bool] = None
    paid_features: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamPlanChangeEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        plan = from_union([from_str, from_none], obj.get("plan"))
        can_add_ura = from_union([from_bool, from_none], obj.get("can_add_ura"))
        paid_features = from_union([lambda x: from_list(from_str, x), from_none], obj.get("paid_features"))
        return TeamPlanChangeEvent(type, plan, can_add_ura, paid_features)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["plan"] = from_union([from_str, from_none], self.plan)
        result["can_add_ura"] = from_union([from_bool, from_none], self.can_add_ura)
        result["paid_features"] = from_union([lambda x: from_list(from_str, x), from_none], self.paid_features)
        return result


def team_plan_change_event_from_dict(s: Any) -> TeamPlanChangeEvent:
    return TeamPlanChangeEvent.from_dict(s)


def team_plan_change_event_to_dict(x: TeamPlanChangeEvent) -> Any:
    return to_class(TeamPlanChangeEvent, x)
