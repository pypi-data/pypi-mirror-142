# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = files_comments_edit_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Comment:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    user: Optional[str] = None
    is_intro: Optional[bool] = None
    comment: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        user = from_union([from_str, from_none], obj.get("user"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        return Comment(id, created, timestamp, user, is_intro, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["user"] = from_union([from_str, from_none], self.user)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        result["comment"] = from_union([from_str, from_none], self.comment)
        return result


@dataclass
class FilesCommentsEditResponse:
    ok: Optional[bool] = None
    comment: Optional[Comment] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FilesCommentsEditResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        comment = from_union([Comment.from_dict, from_none], obj.get("comment"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return FilesCommentsEditResponse(ok, comment, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["comment"] = from_union([lambda x: to_class(Comment, x), from_none], self.comment)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def files_comments_edit_response_from_dict(s: Any) -> FilesCommentsEditResponse:
    return FilesCommentsEditResponse.from_dict(s)


def files_comments_edit_response_to_dict(x: FilesCommentsEditResponse) -> Any:
    return to_class(FilesCommentsEditResponse, x)
