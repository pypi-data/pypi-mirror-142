# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_conversations_invite_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class FailedUserIDS:
    u00000000: Optional[str] = None
    u00000001: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'FailedUserIDS':
        assert isinstance(obj, dict)
        u00000000 = from_union([from_str, from_none], obj.get("U00000000"))
        u00000001 = from_union([from_str, from_none], obj.get("U00000001"))
        return FailedUserIDS(u00000000, u00000001)

    def to_dict(self) -> dict:
        result: dict = {}
        result["U00000000"] = from_union([from_str, from_none], self.u00000000)
        result["U00000001"] = from_union([from_str, from_none], self.u00000001)
        return result


@dataclass
class AdminConversationsInviteResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    failed_user_ids: Optional[FailedUserIDS] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminConversationsInviteResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        failed_user_ids = from_union([FailedUserIDS.from_dict, from_none], obj.get("failed_user_ids"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminConversationsInviteResponse(ok, error, failed_user_ids, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["failed_user_ids"] = from_union([lambda x: to_class(FailedUserIDS, x), from_none], self.failed_user_ids)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_conversations_invite_response_from_dict(s: Any) -> AdminConversationsInviteResponse:
    return AdminConversationsInviteResponse.from_dict(s)


def admin_conversations_invite_response_to_dict(x: AdminConversationsInviteResponse) -> Any:
    return to_class(AdminConversationsInviteResponse, x)
