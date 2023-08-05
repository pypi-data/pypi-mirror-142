# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = bookmarks_add_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Bookmark:
    id: Optional[str] = None
    channel_id: Optional[str] = None
    title: Optional[str] = None
    link: Optional[str] = None
    emoji: Optional[str] = None
    icon_url: Optional[str] = None
    entity_id: Optional[str] = None
    type: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    rank: Optional[str] = None
    last_updated_by_user_id: Optional[str] = None
    last_updated_by_team_id: Optional[str] = None
    shortcut_id: Optional[str] = None
    app_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Bookmark':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        link = from_union([from_str, from_none], obj.get("link"))
        emoji = from_union([from_str, from_none], obj.get("emoji"))
        icon_url = from_union([from_str, from_none], obj.get("icon_url"))
        entity_id = from_union([from_str, from_none], obj.get("entity_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        date_updated = from_union([from_int, from_none], obj.get("date_updated"))
        rank = from_union([from_str, from_none], obj.get("rank"))
        last_updated_by_user_id = from_union([from_str, from_none], obj.get("last_updated_by_user_id"))
        last_updated_by_team_id = from_union([from_str, from_none], obj.get("last_updated_by_team_id"))
        shortcut_id = from_union([from_str, from_none], obj.get("shortcut_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        return Bookmark(id, channel_id, title, link, emoji, icon_url, entity_id, type, date_created, date_updated, rank, last_updated_by_user_id, last_updated_by_team_id, shortcut_id, app_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["link"] = from_union([from_str, from_none], self.link)
        result["emoji"] = from_union([from_str, from_none], self.emoji)
        result["icon_url"] = from_union([from_str, from_none], self.icon_url)
        result["entity_id"] = from_union([from_str, from_none], self.entity_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["date_updated"] = from_union([from_int, from_none], self.date_updated)
        result["rank"] = from_union([from_str, from_none], self.rank)
        result["last_updated_by_user_id"] = from_union([from_str, from_none], self.last_updated_by_user_id)
        result["last_updated_by_team_id"] = from_union([from_str, from_none], self.last_updated_by_team_id)
        result["shortcut_id"] = from_union([from_str, from_none], self.shortcut_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class BookmarksAddResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    bookmark: Optional[Bookmark] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BookmarksAddResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        bookmark = from_union([Bookmark.from_dict, from_none], obj.get("bookmark"))
        return BookmarksAddResponse(ok, error, response_metadata, needed, provided, bookmark)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["bookmark"] = from_union([lambda x: to_class(Bookmark, x), from_none], self.bookmark)
        return result


def bookmarks_add_response_from_dict(s: Any) -> BookmarksAddResponse:
    return BookmarksAddResponse.from_dict(s)


def bookmarks_add_response_to_dict(x: BookmarksAddResponse) -> Any:
    return to_class(BookmarksAddResponse, x)
