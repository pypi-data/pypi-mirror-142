# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = team_access_logs_response_from_dict(json.loads(json_string))

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
class Login:
    user_id: Optional[str] = None
    username: Optional[str] = None
    date_first: Optional[int] = None
    date_last: Optional[int] = None
    count: Optional[int] = None
    ip: Optional[str] = None
    user_agent: Optional[str] = None
    isp: Optional[str] = None
    country: Optional[str] = None
    region: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Login':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        username = from_union([from_str, from_none], obj.get("username"))
        date_first = from_union([from_int, from_none], obj.get("date_first"))
        date_last = from_union([from_int, from_none], obj.get("date_last"))
        count = from_union([from_int, from_none], obj.get("count"))
        ip = from_union([from_str, from_none], obj.get("ip"))
        user_agent = from_union([from_str, from_none], obj.get("user_agent"))
        isp = from_union([from_str, from_none], obj.get("isp"))
        country = from_union([from_str, from_none], obj.get("country"))
        region = from_union([from_str, from_none], obj.get("region"))
        return Login(user_id, username, date_first, date_last, count, ip, user_agent, isp, country, region)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["username"] = from_union([from_str, from_none], self.username)
        result["date_first"] = from_union([from_int, from_none], self.date_first)
        result["date_last"] = from_union([from_int, from_none], self.date_last)
        result["count"] = from_union([from_int, from_none], self.count)
        result["ip"] = from_union([from_str, from_none], self.ip)
        result["user_agent"] = from_union([from_str, from_none], self.user_agent)
        result["isp"] = from_union([from_str, from_none], self.isp)
        result["country"] = from_union([from_str, from_none], self.country)
        result["region"] = from_union([from_str, from_none], self.region)
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
class TeamAccessLogsResponse:
    ok: Optional[bool] = None
    logins: Optional[List[Login]] = None
    paging: Optional[Paging] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamAccessLogsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        logins = from_union([lambda x: from_list(Login.from_dict, x), from_none], obj.get("logins"))
        paging = from_union([Paging.from_dict, from_none], obj.get("paging"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return TeamAccessLogsResponse(ok, logins, paging, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["logins"] = from_union([lambda x: from_list(lambda x: to_class(Login, x), x), from_none], self.logins)
        result["paging"] = from_union([lambda x: to_class(Paging, x), from_none], self.paging)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def team_access_logs_response_from_dict(s: Any) -> TeamAccessLogsResponse:
    return TeamAccessLogsResponse.from_dict(s)


def team_access_logs_response_to_dict(x: TeamAccessLogsResponse) -> Any:
    return to_class(TeamAccessLogsResponse, x)
