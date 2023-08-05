# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = app_rate_limited_event_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AppRateLimitedEvent:
    type: Optional[str] = None
    token: Optional[str] = None
    team_id: Optional[str] = None
    minute_rate_limited: Optional[int] = None
    api_app_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppRateLimitedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        token = from_union([from_str, from_none], obj.get("token"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        minute_rate_limited = from_union([from_int, from_none], obj.get("minute_rate_limited"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        return AppRateLimitedEvent(type, token, team_id, minute_rate_limited, api_app_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["token"] = from_union([from_str, from_none], self.token)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["minute_rate_limited"] = from_union([from_int, from_none], self.minute_rate_limited)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        return result


def app_rate_limited_event_from_dict(s: Any) -> AppRateLimitedEvent:
    return AppRateLimitedEvent.from_dict(s)


def app_rate_limited_event_to_dict(x: AppRateLimitedEvent) -> Any:
    return to_class(AppRateLimitedEvent, x)
