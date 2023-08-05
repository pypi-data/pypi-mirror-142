# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = search_files_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, Dict, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class Public:
    reply_users: Optional[List[str]] = None
    reply_users_count: Optional[int] = None
    reply_count: Optional[int] = None
    ts: Optional[str] = None
    channel_name: Optional[str] = None
    team_id: Optional[str] = None
    share_user_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Public':
        assert isinstance(obj, dict)
        reply_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        share_user_id = from_union([from_str, from_none], obj.get("share_user_id"))
        return Public(reply_users, reply_users_count, reply_count, ts, channel_name, team_id, share_user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["reply_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["share_user_id"] = from_union([from_str, from_none], self.share_user_id)
        return result


@dataclass
class Shares:
    public: Optional[Dict[str, List[Public]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Shares':
        assert isinstance(obj, dict)
        public = from_union([lambda x: from_dict(lambda x: from_list(Public.from_dict, x), x), from_none], obj.get("public"))
        return Shares(public)

    def to_dict(self) -> dict:
        result: dict = {}
        result["public"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Public, x), x), x), from_none], self.public)
        return result


@dataclass
class Match:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    mimetype: Optional[str] = None
    filetype: Optional[str] = None
    pretty_type: Optional[str] = None
    user: Optional[str] = None
    editable: Optional[bool] = None
    size: Optional[int] = None
    mode: Optional[str] = None
    is_external: Optional[bool] = None
    external_type: Optional[str] = None
    is_public: Optional[bool] = None
    public_url_shared: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    username: Optional[str] = None
    url_private: Optional[str] = None
    thumb_64: Optional[str] = None
    thumb_80: Optional[str] = None
    thumb_360: Optional[str] = None
    thumb_360__w: Optional[int] = None
    thumb_360__h: Optional[int] = None
    thumb_480: Optional[str] = None
    thumb_480__w: Optional[int] = None
    thumb_480__h: Optional[int] = None
    thumb_160: Optional[str] = None
    thumb_720: Optional[str] = None
    thumb_720__w: Optional[int] = None
    thumb_720__h: Optional[int] = None
    thumb_800: Optional[str] = None
    thumb_800__w: Optional[int] = None
    thumb_800__h: Optional[int] = None
    thumb_960: Optional[str] = None
    thumb_960__w: Optional[int] = None
    thumb_960__h: Optional[int] = None
    thumb_1024: Optional[str] = None
    thumb_1024__w: Optional[int] = None
    thumb_1024__h: Optional[int] = None
    original_w: Optional[int] = None
    original_h: Optional[int] = None
    thumb_tiny: Optional[str] = None
    permalink: Optional[str] = None
    is_starred: Optional[bool] = None
    shares: Optional[Shares] = None
    channels: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    ims: Optional[List[str]] = None
    external_id: Optional[str] = None
    external_url: Optional[str] = None
    has_rich_preview: Optional[bool] = None
    url_private_download: Optional[str] = None
    permalink_public: Optional[str] = None
    edit_link: Optional[str] = None
    preview: Optional[str] = None
    preview_highlight: Optional[str] = None
    lines: Optional[int] = None
    lines_more: Optional[int] = None
    preview_is_truncated: Optional[bool] = None
    image_exif_rotation: Optional[int] = None
    last_editor: Optional[str] = None
    non_owner_editable: Optional[bool] = None
    updated: Optional[int] = None
    thumb_video: Optional[str] = None
    media_display_type: Optional[str] = None
    comments_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Match':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        user = from_union([from_str, from_none], obj.get("user"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        size = from_union([from_int, from_none], obj.get("size"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
        is_public = from_union([from_bool, from_none], obj.get("is_public"))
        public_url_shared = from_union([from_bool, from_none], obj.get("public_url_shared"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        username = from_union([from_str, from_none], obj.get("username"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        thumb_64 = from_union([from_str, from_none], obj.get("thumb_64"))
        thumb_80 = from_union([from_str, from_none], obj.get("thumb_80"))
        thumb_360 = from_union([from_str, from_none], obj.get("thumb_360"))
        thumb_360__w = from_union([from_int, from_none], obj.get("thumb_360_w"))
        thumb_360__h = from_union([from_int, from_none], obj.get("thumb_360_h"))
        thumb_480 = from_union([from_str, from_none], obj.get("thumb_480"))
        thumb_480__w = from_union([from_int, from_none], obj.get("thumb_480_w"))
        thumb_480__h = from_union([from_int, from_none], obj.get("thumb_480_h"))
        thumb_160 = from_union([from_str, from_none], obj.get("thumb_160"))
        thumb_720 = from_union([from_str, from_none], obj.get("thumb_720"))
        thumb_720__w = from_union([from_int, from_none], obj.get("thumb_720_w"))
        thumb_720__h = from_union([from_int, from_none], obj.get("thumb_720_h"))
        thumb_800 = from_union([from_str, from_none], obj.get("thumb_800"))
        thumb_800__w = from_union([from_int, from_none], obj.get("thumb_800_w"))
        thumb_800__h = from_union([from_int, from_none], obj.get("thumb_800_h"))
        thumb_960 = from_union([from_str, from_none], obj.get("thumb_960"))
        thumb_960__w = from_union([from_int, from_none], obj.get("thumb_960_w"))
        thumb_960__h = from_union([from_int, from_none], obj.get("thumb_960_h"))
        thumb_1024 = from_union([from_str, from_none], obj.get("thumb_1024"))
        thumb_1024__w = from_union([from_int, from_none], obj.get("thumb_1024_w"))
        thumb_1024__h = from_union([from_int, from_none], obj.get("thumb_1024_h"))
        original_w = from_union([from_int, from_none], obj.get("original_w"))
        original_h = from_union([from_int, from_none], obj.get("original_h"))
        thumb_tiny = from_union([from_str, from_none], obj.get("thumb_tiny"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        shares = from_union([Shares.from_dict, from_none], obj.get("shares"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        ims = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ims"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        external_url = from_union([from_str, from_none], obj.get("external_url"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        url_private_download = from_union([from_str, from_none], obj.get("url_private_download"))
        permalink_public = from_union([from_str, from_none], obj.get("permalink_public"))
        edit_link = from_union([from_str, from_none], obj.get("edit_link"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        preview_highlight = from_union([from_str, from_none], obj.get("preview_highlight"))
        lines = from_union([from_int, from_none], obj.get("lines"))
        lines_more = from_union([from_int, from_none], obj.get("lines_more"))
        preview_is_truncated = from_union([from_bool, from_none], obj.get("preview_is_truncated"))
        image_exif_rotation = from_union([from_int, from_none], obj.get("image_exif_rotation"))
        last_editor = from_union([from_str, from_none], obj.get("last_editor"))
        non_owner_editable = from_union([from_bool, from_none], obj.get("non_owner_editable"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        thumb_video = from_union([from_str, from_none], obj.get("thumb_video"))
        media_display_type = from_union([from_str, from_none], obj.get("media_display_type"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        return Match(id, created, timestamp, name, title, mimetype, filetype, pretty_type, user, editable, size, mode, is_external, external_type, is_public, public_url_shared, display_as_bot, username, url_private, thumb_64, thumb_80, thumb_360, thumb_360__w, thumb_360__h, thumb_480, thumb_480__w, thumb_480__h, thumb_160, thumb_720, thumb_720__w, thumb_720__h, thumb_800, thumb_800__w, thumb_800__h, thumb_960, thumb_960__w, thumb_960__h, thumb_1024, thumb_1024__w, thumb_1024__h, original_w, original_h, thumb_tiny, permalink, is_starred, shares, channels, groups, ims, external_id, external_url, has_rich_preview, url_private_download, permalink_public, edit_link, preview, preview_highlight, lines, lines_more, preview_is_truncated, image_exif_rotation, last_editor, non_owner_editable, updated, thumb_video, media_display_type, comments_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
        result["is_public"] = from_union([from_bool, from_none], self.is_public)
        result["public_url_shared"] = from_union([from_bool, from_none], self.public_url_shared)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["username"] = from_union([from_str, from_none], self.username)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["thumb_64"] = from_union([from_str, from_none], self.thumb_64)
        result["thumb_80"] = from_union([from_str, from_none], self.thumb_80)
        result["thumb_360"] = from_union([from_str, from_none], self.thumb_360)
        result["thumb_360_w"] = from_union([from_int, from_none], self.thumb_360__w)
        result["thumb_360_h"] = from_union([from_int, from_none], self.thumb_360__h)
        result["thumb_480"] = from_union([from_str, from_none], self.thumb_480)
        result["thumb_480_w"] = from_union([from_int, from_none], self.thumb_480__w)
        result["thumb_480_h"] = from_union([from_int, from_none], self.thumb_480__h)
        result["thumb_160"] = from_union([from_str, from_none], self.thumb_160)
        result["thumb_720"] = from_union([from_str, from_none], self.thumb_720)
        result["thumb_720_w"] = from_union([from_int, from_none], self.thumb_720__w)
        result["thumb_720_h"] = from_union([from_int, from_none], self.thumb_720__h)
        result["thumb_800"] = from_union([from_str, from_none], self.thumb_800)
        result["thumb_800_w"] = from_union([from_int, from_none], self.thumb_800__w)
        result["thumb_800_h"] = from_union([from_int, from_none], self.thumb_800__h)
        result["thumb_960"] = from_union([from_str, from_none], self.thumb_960)
        result["thumb_960_w"] = from_union([from_int, from_none], self.thumb_960__w)
        result["thumb_960_h"] = from_union([from_int, from_none], self.thumb_960__h)
        result["thumb_1024"] = from_union([from_str, from_none], self.thumb_1024)
        result["thumb_1024_w"] = from_union([from_int, from_none], self.thumb_1024__w)
        result["thumb_1024_h"] = from_union([from_int, from_none], self.thumb_1024__h)
        result["original_w"] = from_union([from_int, from_none], self.original_w)
        result["original_h"] = from_union([from_int, from_none], self.original_h)
        result["thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["shares"] = from_union([lambda x: to_class(Shares, x), from_none], self.shares)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        result["ims"] = from_union([lambda x: from_list(from_str, x), from_none], self.ims)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["external_url"] = from_union([from_str, from_none], self.external_url)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["url_private_download"] = from_union([from_str, from_none], self.url_private_download)
        result["permalink_public"] = from_union([from_str, from_none], self.permalink_public)
        result["edit_link"] = from_union([from_str, from_none], self.edit_link)
        result["preview"] = from_union([from_str, from_none], self.preview)
        result["preview_highlight"] = from_union([from_str, from_none], self.preview_highlight)
        result["lines"] = from_union([from_int, from_none], self.lines)
        result["lines_more"] = from_union([from_int, from_none], self.lines_more)
        result["preview_is_truncated"] = from_union([from_bool, from_none], self.preview_is_truncated)
        result["image_exif_rotation"] = from_union([from_int, from_none], self.image_exif_rotation)
        result["last_editor"] = from_union([from_str, from_none], self.last_editor)
        result["non_owner_editable"] = from_union([from_bool, from_none], self.non_owner_editable)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["thumb_video"] = from_union([from_str, from_none], self.thumb_video)
        result["media_display_type"] = from_union([from_str, from_none], self.media_display_type)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        return result


@dataclass
class Pagination:
    total_count: Optional[int] = None
    page: Optional[int] = None
    per_page: Optional[int] = None
    page_count: Optional[int] = None
    first: Optional[int] = None
    last: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Pagination':
        assert isinstance(obj, dict)
        total_count = from_union([from_int, from_none], obj.get("total_count"))
        page = from_union([from_int, from_none], obj.get("page"))
        per_page = from_union([from_int, from_none], obj.get("per_page"))
        page_count = from_union([from_int, from_none], obj.get("page_count"))
        first = from_union([from_int, from_none], obj.get("first"))
        last = from_union([from_int, from_none], obj.get("last"))
        return Pagination(total_count, page, per_page, page_count, first, last)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total_count"] = from_union([from_int, from_none], self.total_count)
        result["page"] = from_union([from_int, from_none], self.page)
        result["per_page"] = from_union([from_int, from_none], self.per_page)
        result["page_count"] = from_union([from_int, from_none], self.page_count)
        result["first"] = from_union([from_int, from_none], self.first)
        result["last"] = from_union([from_int, from_none], self.last)
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
class Files:
    total: Optional[int] = None
    pagination: Optional[Pagination] = None
    paging: Optional[Paging] = None
    matches: Optional[List[Match]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Files':
        assert isinstance(obj, dict)
        total = from_union([from_int, from_none], obj.get("total"))
        pagination = from_union([Pagination.from_dict, from_none], obj.get("pagination"))
        paging = from_union([Paging.from_dict, from_none], obj.get("paging"))
        matches = from_union([lambda x: from_list(Match.from_dict, x), from_none], obj.get("matches"))
        return Files(total, pagination, paging, matches)

    def to_dict(self) -> dict:
        result: dict = {}
        result["total"] = from_union([from_int, from_none], self.total)
        result["pagination"] = from_union([lambda x: to_class(Pagination, x), from_none], self.pagination)
        result["paging"] = from_union([lambda x: to_class(Paging, x), from_none], self.paging)
        result["matches"] = from_union([lambda x: from_list(lambda x: to_class(Match, x), x), from_none], self.matches)
        return result


@dataclass
class SearchFilesResponse:
    ok: Optional[bool] = None
    query: Optional[str] = None
    files: Optional[Files] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SearchFilesResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        query = from_union([from_str, from_none], obj.get("query"))
        files = from_union([Files.from_dict, from_none], obj.get("files"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return SearchFilesResponse(ok, query, files, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["query"] = from_union([from_str, from_none], self.query)
        result["files"] = from_union([lambda x: to_class(Files, x), from_none], self.files)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def search_files_response_from_dict(s: Any) -> SearchFilesResponse:
    return SearchFilesResponse.from_dict(s)


def search_files_response_to_dict(x: SearchFilesResponse) -> Any:
    return to_class(SearchFilesResponse, x)
