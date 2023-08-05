# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = groups_rename_response_from_dict(json.loads(json_string))

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
class Purpose:
    value: Optional[str] = None
    creator: Optional[str] = None
    last_set: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Purpose':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        last_set = from_union([from_int, from_none], obj.get("last_set"))
        return Purpose(value, creator, last_set)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["last_set"] = from_union([from_int, from_none], self.last_set)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    is_group: Optional[bool] = None
    created: Optional[int] = None
    creator: Optional[str] = None
    is_archived: Optional[bool] = None
    name_normalized: Optional[str] = None
    is_mpim: Optional[bool] = None
    members: Optional[List[str]] = None
    topic: Optional[Purpose] = None
    purpose: Optional[Purpose] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        created = from_union([from_int, from_none], obj.get("created"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        members = from_union([lambda x: from_list(from_str, x), from_none], obj.get("members"))
        topic = from_union([Purpose.from_dict, from_none], obj.get("topic"))
        purpose = from_union([Purpose.from_dict, from_none], obj.get("purpose"))
        return Channel(id, name, is_group, created, creator, is_archived, name_normalized, is_mpim, members, topic, purpose)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["created"] = from_union([from_int, from_none], self.created)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["members"] = from_union([lambda x: from_list(from_str, x), from_none], self.members)
        result["topic"] = from_union([lambda x: to_class(Purpose, x), from_none], self.topic)
        result["purpose"] = from_union([lambda x: to_class(Purpose, x), from_none], self.purpose)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None
    warnings: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(from_str, x), from_none], obj.get("warnings"))
        return ResponseMetadata(messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(from_str, x), from_none], self.warnings)
        return result


@dataclass
class GroupsRenameResponse:
    channel: Optional[Channel] = None
    ok: Optional[bool] = None
    warning: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupsRenameResponse':
        assert isinstance(obj, dict)
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return GroupsRenameResponse(channel, ok, warning, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def groups_rename_response_from_dict(s: Any) -> GroupsRenameResponse:
    return GroupsRenameResponse.from_dict(s)


def groups_rename_response_to_dict(x: GroupsRenameResponse) -> Any:
    return to_class(GroupsRenameResponse, x)
