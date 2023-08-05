# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_conversations_search_response_from_dict(json.loads(json_string))

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
class Conversation:
    id: Optional[str] = None
    name: Optional[str] = None
    purpose: Optional[str] = None
    member_count: Optional[int] = None
    created: Optional[int] = None
    creator_id: Optional[str] = None
    is_private: Optional[bool] = None
    is_archived: Optional[bool] = None
    is_general: Optional[bool] = None
    last_activity_ts: Optional[int] = None
    is_ext_shared: Optional[bool] = None
    is_global_shared: Optional[bool] = None
    is_org_default: Optional[bool] = None
    is_org_mandatory: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    is_frozen: Optional[bool] = None
    internal_team_ids_count: Optional[int] = None
    internal_team_ids_sample_team: Optional[str] = None
    pending_connected_team_ids: Optional[List[str]] = None
    is_pending_ext_shared: Optional[bool] = None
    connected_team_ids: Optional[List[str]] = None
    conversation_host_id: Optional[str] = None
    channel_email_addresses: Optional[List[str]] = None
    connected_limited_team_ids: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Conversation':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        purpose = from_union([from_str, from_none], obj.get("purpose"))
        member_count = from_union([from_int, from_none], obj.get("member_count"))
        created = from_union([from_int, from_none], obj.get("created"))
        creator_id = from_union([from_str, from_none], obj.get("creator_id"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_general = from_union([from_bool, from_none], obj.get("is_general"))
        last_activity_ts = from_union([from_int, from_none], obj.get("last_activity_ts"))
        is_ext_shared = from_union([from_bool, from_none], obj.get("is_ext_shared"))
        is_global_shared = from_union([from_bool, from_none], obj.get("is_global_shared"))
        is_org_default = from_union([from_bool, from_none], obj.get("is_org_default"))
        is_org_mandatory = from_union([from_bool, from_none], obj.get("is_org_mandatory"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        is_frozen = from_union([from_bool, from_none], obj.get("is_frozen"))
        internal_team_ids_count = from_union([from_int, from_none], obj.get("internal_team_ids_count"))
        internal_team_ids_sample_team = from_union([from_str, from_none], obj.get("internal_team_ids_sample_team"))
        pending_connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_connected_team_ids"))
        is_pending_ext_shared = from_union([from_bool, from_none], obj.get("is_pending_ext_shared"))
        connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_team_ids"))
        conversation_host_id = from_union([from_str, from_none], obj.get("conversation_host_id"))
        channel_email_addresses = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel_email_addresses"))
        connected_limited_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_limited_team_ids"))
        return Conversation(id, name, purpose, member_count, created, creator_id, is_private, is_archived, is_general, last_activity_ts, is_ext_shared, is_global_shared, is_org_default, is_org_mandatory, is_org_shared, is_frozen, internal_team_ids_count, internal_team_ids_sample_team, pending_connected_team_ids, is_pending_ext_shared, connected_team_ids, conversation_host_id, channel_email_addresses, connected_limited_team_ids)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["purpose"] = from_union([from_str, from_none], self.purpose)
        result["member_count"] = from_union([from_int, from_none], self.member_count)
        result["created"] = from_union([from_int, from_none], self.created)
        result["creator_id"] = from_union([from_str, from_none], self.creator_id)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_general"] = from_union([from_bool, from_none], self.is_general)
        result["last_activity_ts"] = from_union([from_int, from_none], self.last_activity_ts)
        result["is_ext_shared"] = from_union([from_bool, from_none], self.is_ext_shared)
        result["is_global_shared"] = from_union([from_bool, from_none], self.is_global_shared)
        result["is_org_default"] = from_union([from_bool, from_none], self.is_org_default)
        result["is_org_mandatory"] = from_union([from_bool, from_none], self.is_org_mandatory)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["is_frozen"] = from_union([from_bool, from_none], self.is_frozen)
        result["internal_team_ids_count"] = from_union([from_int, from_none], self.internal_team_ids_count)
        result["internal_team_ids_sample_team"] = from_union([from_str, from_none], self.internal_team_ids_sample_team)
        result["pending_connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_connected_team_ids)
        result["is_pending_ext_shared"] = from_union([from_bool, from_none], self.is_pending_ext_shared)
        result["connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_team_ids)
        result["conversation_host_id"] = from_union([from_str, from_none], self.conversation_host_id)
        result["channel_email_addresses"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel_email_addresses)
        result["connected_limited_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_limited_team_ids)
        return result


@dataclass
class AdminConversationsSearchResponse:
    ok: Optional[bool] = None
    conversations: Optional[List[Conversation]] = None
    next_cursor: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminConversationsSearchResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        conversations = from_union([lambda x: from_list(Conversation.from_dict, x), from_none], obj.get("conversations"))
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminConversationsSearchResponse(ok, conversations, next_cursor, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["conversations"] = from_union([lambda x: from_list(lambda x: to_class(Conversation, x), x), from_none], self.conversations)
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_conversations_search_response_from_dict(s: Any) -> AdminConversationsSearchResponse:
    return AdminConversationsSearchResponse.from_dict(s)


def admin_conversations_search_response_to_dict(x: AdminConversationsSearchResponse) -> Any:
    return to_class(AdminConversationsSearchResponse, x)
