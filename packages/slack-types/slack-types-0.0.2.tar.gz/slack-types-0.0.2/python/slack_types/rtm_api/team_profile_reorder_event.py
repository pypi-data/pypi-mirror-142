# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_profile_reorder_event_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Field:
    id: Optional[str] = None
    ordering: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        ordering = from_union([from_int, from_none], obj.get("ordering"))
        return Field(id, ordering)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["ordering"] = from_union([from_int, from_none], self.ordering)
        return result


@dataclass
class Profile:
    fields: Optional[List[Field]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        return Profile(fields)

    def to_dict(self) -> dict:
        result: dict = {}
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        return result


@dataclass
class TeamProfileReorderEvent:
    type: Optional[str] = None
    profile: Optional[Profile] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamProfileReorderEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        profile = from_union([Profile.from_dict, from_none], obj.get("profile"))
        return TeamProfileReorderEvent(type, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.profile)
        return result


def team_profile_reorder_event_from_dict(s: Any) -> TeamProfileReorderEvent:
    return TeamProfileReorderEvent.from_dict(s)


def team_profile_reorder_event_to_dict(x: TeamProfileReorderEvent) -> Any:
    return to_class(TeamProfileReorderEvent, x)
