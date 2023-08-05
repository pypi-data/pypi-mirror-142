# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conversations_accept_shared_invite_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ConversationsAcceptSharedInviteResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    implicit_approval: Optional[bool] = None
    channel_id: Optional[str] = None
    invite_id: Optional[str] = None
    can_open_scdm: Optional[bool] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationsAcceptSharedInviteResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        implicit_approval = from_union([from_bool, from_none], obj.get("implicit_approval"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        invite_id = from_union([from_str, from_none], obj.get("invite_id"))
        can_open_scdm = from_union([from_bool, from_none], obj.get("can_open_scdm"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ConversationsAcceptSharedInviteResponse(ok, error, implicit_approval, channel_id, invite_id, can_open_scdm, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["implicit_approval"] = from_union([from_bool, from_none], self.implicit_approval)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["invite_id"] = from_union([from_str, from_none], self.invite_id)
        result["can_open_scdm"] = from_union([from_bool, from_none], self.can_open_scdm)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def conversations_accept_shared_invite_response_from_dict(s: Any) -> ConversationsAcceptSharedInviteResponse:
    return ConversationsAcceptSharedInviteResponse.from_dict(s)


def conversations_accept_shared_invite_response_to_dict(x: ConversationsAcceptSharedInviteResponse) -> Any:
    return to_class(ConversationsAcceptSharedInviteResponse, x)
