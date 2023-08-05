# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = file_comment_added_event_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Any, Optional, TypeVar, Type, cast


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
class Comment:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        return Comment()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


@dataclass
class File:
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        return File(id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class FileCommentAddedEvent:
    type: Optional[str] = None
    comment: Optional[Comment] = None
    file_id: Optional[str] = None
    file: Optional[File] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileCommentAddedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        comment = from_union([Comment.from_dict, from_none], obj.get("comment"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        return FileCommentAddedEvent(type, comment, file_id, file)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["comment"] = from_union([lambda x: to_class(Comment, x), from_none], self.comment)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        return result


def file_comment_added_event_from_dict(s: Any) -> FileCommentAddedEvent:
    return FileCommentAddedEvent.from_dict(s)


def file_comment_added_event_to_dict(x: FileCommentAddedEvent) -> Any:
    return to_class(FileCommentAddedEvent, x)
