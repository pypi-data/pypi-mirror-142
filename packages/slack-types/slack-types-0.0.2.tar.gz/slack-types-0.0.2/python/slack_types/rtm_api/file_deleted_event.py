# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = file_deleted_event_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class FileDeletedEvent:
    type: Optional[str] = None
    file_id: Optional[str] = None
    channel_ids: Optional[List[Any]] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FileDeletedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        file_id = from_union([from_str, from_none], obj.get("file_id"))
        channel_ids = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("channel_ids"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return FileDeletedEvent(type, file_id, channel_ids, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["file_id"] = from_union([from_str, from_none], self.file_id)
        result["channel_ids"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.channel_ids)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def file_deleted_event_from_dict(s: Any) -> FileDeletedEvent:
    return FileDeletedEvent.from_dict(s)


def file_deleted_event_to_dict(x: FileDeletedEvent) -> Any:
    return to_class(FileDeletedEvent, x)
