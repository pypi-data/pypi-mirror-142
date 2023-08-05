# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_integration_logs_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, Callable, cast


T = TypeVar("T")


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_str(x: Any) -> str:
    assert isinstance(x, str)
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


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Log:
    date: Optional[int] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    change_type: Optional[str] = None
    app_type: Optional[str] = None
    app_id: Optional[str] = None
    scope: Optional[str] = None
    rss_feed: Optional[bool] = None
    rss_feed_change_type: Optional[str] = None
    rss_feed_title: Optional[str] = None
    rss_feed_url: Optional[str] = None
    service_id: Optional[int] = None
    service_type: Optional[str] = None
    channel: Optional[str] = None
    reason: Optional[str] = None
    resolution: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Log':
        assert isinstance(obj, dict)
        date = from_union([from_none, lambda x: int(from_str(x))], obj.get("date"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        user_name = from_union([from_str, from_none], obj.get("user_name"))
        change_type = from_union([from_str, from_none], obj.get("change_type"))
        app_type = from_union([from_str, from_none], obj.get("app_type"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        scope = from_union([from_str, from_none], obj.get("scope"))
        rss_feed = from_union([from_bool, from_none], obj.get("rss_feed"))
        rss_feed_change_type = from_union([from_str, from_none], obj.get("rss_feed_change_type"))
        rss_feed_title = from_union([from_str, from_none], obj.get("rss_feed_title"))
        rss_feed_url = from_union([from_str, from_none], obj.get("rss_feed_url"))
        service_id = from_union([from_int, from_none], obj.get("service_id"))
        service_type = from_union([from_str, from_none], obj.get("service_type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        reason = from_union([from_str, from_none], obj.get("reason"))
        resolution = from_union([from_str, from_none], obj.get("resolution"))
        return Log(date, user_id, user_name, change_type, app_type, app_id, scope, rss_feed, rss_feed_change_type, rss_feed_title, rss_feed_url, service_id, service_type, channel, reason, resolution)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.date)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["user_name"] = from_union([from_str, from_none], self.user_name)
        result["change_type"] = from_union([from_str, from_none], self.change_type)
        result["app_type"] = from_union([from_str, from_none], self.app_type)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["scope"] = from_union([from_str, from_none], self.scope)
        result["rss_feed"] = from_union([from_bool, from_none], self.rss_feed)
        result["rss_feed_change_type"] = from_union([from_str, from_none], self.rss_feed_change_type)
        result["rss_feed_title"] = from_union([from_str, from_none], self.rss_feed_title)
        result["rss_feed_url"] = from_union([from_str, from_none], self.rss_feed_url)
        result["service_id"] = from_union([from_int, from_none], self.service_id)
        result["service_type"] = from_union([from_str, from_none], self.service_type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["reason"] = from_union([from_str, from_none], self.reason)
        result["resolution"] = from_union([from_str, from_none], self.resolution)
        return result


@dataclass
class Paging:
    count: Optional[int] = None
    total: Optional[int] = None
    page: Optional[int] = None
    pages: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Paging':
        assert isinstance(obj, dict)
        count = from_union([from_int, from_none], obj.get("count"))
        total = from_union([from_int, from_none], obj.get("total"))
        page = from_union([from_int, from_none], obj.get("page"))
        pages = from_union([from_int, from_none], obj.get("pages"))
        return Paging(count, total, page, pages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["count"] = from_union([from_int, from_none], self.count)
        result["total"] = from_union([from_int, from_none], self.total)
        result["page"] = from_union([from_int, from_none], self.page)
        result["pages"] = from_union([from_int, from_none], self.pages)
        return result


@dataclass
class TeamIntegrationLogsResponse:
    ok: Optional[bool] = None
    logs: Optional[List[Log]] = None
    paging: Optional[Paging] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamIntegrationLogsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        logs = from_union([lambda x: from_list(Log.from_dict, x), from_none], obj.get("logs"))
        paging = from_union([Paging.from_dict, from_none], obj.get("paging"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return TeamIntegrationLogsResponse(ok, logs, paging, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["logs"] = from_union([lambda x: from_list(lambda x: to_class(Log, x), x), from_none], self.logs)
        result["paging"] = from_union([lambda x: to_class(Paging, x), from_none], self.paging)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def team_integration_logs_response_from_dict(s: Any) -> TeamIntegrationLogsResponse:
    return TeamIntegrationLogsResponse.from_dict(s)


def team_integration_logs_response_to_dict(x: TeamIntegrationLogsResponse) -> Any:
    return to_class(TeamIntegrationLogsResponse, x)
