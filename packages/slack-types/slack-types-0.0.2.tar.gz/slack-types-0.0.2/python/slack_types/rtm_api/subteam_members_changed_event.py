# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = subteam_members_changed_event_from_dict(json.loads(json_string))

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
class SubteamMembersChangedEvent:
    type: Optional[str] = None
    subteam_id: Optional[str] = None
    team_id: Optional[str] = None
    date_previous_update: Optional[int] = None
    date_update: Optional[int] = None
    added_users: Optional[List[str]] = None
    added_users_count: Optional[int] = None
    removed_users: Optional[List[str]] = None
    removed_users_count: Optional[int] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SubteamMembersChangedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subteam_id = from_union([from_str, from_none], obj.get("subteam_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        date_previous_update = from_union([from_int, from_none], obj.get("date_previous_update"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        added_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("added_users"))
        added_users_count = from_union([from_int, from_none], obj.get("added_users_count"))
        removed_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("removed_users"))
        removed_users_count = from_union([from_int, from_none], obj.get("removed_users_count"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return SubteamMembersChangedEvent(type, subteam_id, team_id, date_previous_update, date_update, added_users, added_users_count, removed_users, removed_users_count, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subteam_id"] = from_union([from_str, from_none], self.subteam_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["date_previous_update"] = from_union([from_int, from_none], self.date_previous_update)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["added_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.added_users)
        result["added_users_count"] = from_union([from_int, from_none], self.added_users_count)
        result["removed_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.removed_users)
        result["removed_users_count"] = from_union([from_int, from_none], self.removed_users_count)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def subteam_members_changed_event_from_dict(s: Any) -> SubteamMembersChangedEvent:
    return SubteamMembersChangedEvent.from_dict(s)


def subteam_members_changed_event_to_dict(x: SubteamMembersChangedEvent) -> Any:
    return to_class(SubteamMembersChangedEvent, x)
