# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_migration_started_event_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class TeamMigrationStartedEvent:
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamMigrationStartedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        return TeamMigrationStartedEvent(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        return result


def team_migration_started_event_from_dict(s: Any) -> TeamMigrationStartedEvent:
    return TeamMigrationStartedEvent.from_dict(s)


def team_migration_started_event_to_dict(x: TeamMigrationStartedEvent) -> Any:
    return to_class(TeamMigrationStartedEvent, x)
