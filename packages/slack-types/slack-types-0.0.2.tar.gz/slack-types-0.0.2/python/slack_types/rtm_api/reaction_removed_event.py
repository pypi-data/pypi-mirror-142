# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = reaction_removed_event_from_dict(json.loads(json_string))

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
class Item:
    type: Optional[str] = None
    channel: Optional[str] = None
    ts: Optional[str] = None
    file: Optional[str] = None
    file_comment: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Item':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        file = from_union([from_str, from_none], obj.get("file"))
        file_comment = from_union([from_str, from_none], obj.get("file_comment"))
        return Item(type, channel, ts, file, file_comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["file"] = from_union([from_str, from_none], self.file)
        result["file_comment"] = from_union([from_str, from_none], self.file_comment)
        return result


@dataclass
class ReactionRemovedEvent:
    type: Optional[str] = None
    user: Optional[str] = None
    reaction: Optional[str] = None
    item_user: Optional[str] = None
    item: Optional[Item] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ReactionRemovedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        reaction = from_union([from_str, from_none], obj.get("reaction"))
        item_user = from_union([from_str, from_none], obj.get("item_user"))
        item = from_union([Item.from_dict, from_none], obj.get("item"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return ReactionRemovedEvent(type, user, reaction, item_user, item, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["reaction"] = from_union([from_str, from_none], self.reaction)
        result["item_user"] = from_union([from_str, from_none], self.item_user)
        result["item"] = from_union([lambda x: to_class(Item, x), from_none], self.item)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def reaction_removed_event_from_dict(s: Any) -> ReactionRemovedEvent:
    return ReactionRemovedEvent.from_dict(s)


def reaction_removed_event_to_dict(x: ReactionRemovedEvent) -> Any:
    return to_class(ReactionRemovedEvent, x)
