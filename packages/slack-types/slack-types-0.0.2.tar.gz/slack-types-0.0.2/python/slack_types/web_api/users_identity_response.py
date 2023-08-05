# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = users_identity_response_from_dict(json.loads(json_string))

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
class Team:
    name: Optional[str] = None
    id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        return Team(name, id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["id"] = from_union([from_str, from_none], self.id)
        return result


@dataclass
class User:
    name: Optional[str] = None
    id: Optional[str] = None
    email: Optional[str] = None
    image_24: Optional[str] = None
    image_32: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        id = from_union([from_str, from_none], obj.get("id"))
        email = from_union([from_str, from_none], obj.get("email"))
        image_24 = from_union([from_str, from_none], obj.get("image_24"))
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        return User(name, id, email, image_24, image_32, image_48, image_72, image_192, image_512)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["id"] = from_union([from_str, from_none], self.id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["image_24"] = from_union([from_str, from_none], self.image_24)
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        return result


@dataclass
class UsersIdentityResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    user: Optional[User] = None
    team: Optional[Team] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UsersIdentityResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        return UsersIdentityResponse(ok, warning, error, needed, provided, user, team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        return result


def users_identity_response_from_dict(s: Any) -> UsersIdentityResponse:
    return UsersIdentityResponse.from_dict(s)


def users_identity_response_to_dict(x: UsersIdentityResponse) -> Any:
    return to_class(UsersIdentityResponse, x)
