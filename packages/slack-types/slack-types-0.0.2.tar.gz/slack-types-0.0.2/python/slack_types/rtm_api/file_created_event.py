# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = file_created_event_from_dict(json.loads(json_string))

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
class FileCreatedEvent:
    type: Optional[str] = None
    file_id: Optional[str] = None
    file: Optional[File] = None
    user_id: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileCreatedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return FileCreatedEvent(type, file_id, file, user_id, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def file_created_event_from_dict(s: Any) -> FileCreatedEvent:
    return FileCreatedEvent.from_dict(s)


def file_created_event_to_dict(x: FileCreatedEvent) -> Any:
    return to_class(FileCreatedEvent, x)
