# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = user_resource_removed_event_from_dict(json.loads(json_string))

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
class UserResourceRemovedEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    trigger_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserResourceRemovedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        trigger_id = from_union([from_str, from_none], obj.get("trigger_id"))
        return UserResourceRemovedEvent(type, user, trigger_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["trigger_id"] = from_union([from_str, from_none], self.trigger_id)
        return result


def user_resource_removed_event_from_dict(s: Any) -> UserResourceRemovedEvent:
    return UserResourceRemovedEvent.from_dict(s)


def user_resource_removed_event_to_dict(x: UserResourceRemovedEvent) -> Any:
    return to_class(UserResourceRemovedEvent, x)
