# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = external_org_migration_started_event_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Team:
    id: Optional[str] = None
    is_migrating: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        is_migrating = from_union([from_bool, from_none], obj.get("is_migrating"))
        return Team(id, is_migrating)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["is_migrating"] = from_union([from_bool, from_none], self.is_migrating)
        return result


@dataclass
class ExternalOrgMigrationStartedEvent:
    type: Optional[str] = None
    team: Optional[Team] = None
    date_started: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ExternalOrgMigrationStartedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        date_started = from_union([from_int, from_none], obj.get("date_started"))
        return ExternalOrgMigrationStartedEvent(type, team, date_started)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["date_started"] = from_union([from_int, from_none], self.date_started)
        return result


def external_org_migration_started_event_from_dict(s: Any) -> ExternalOrgMigrationStartedEvent:
    return ExternalOrgMigrationStartedEvent.from_dict(s)


def external_org_migration_started_event_to_dict(x: ExternalOrgMigrationStartedEvent) -> Any:
    return to_class(ExternalOrgMigrationStartedEvent, x)
