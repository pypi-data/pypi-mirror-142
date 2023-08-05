# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_teams_settings_info_response_from_dict(json.loads(json_string))

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


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Icon:
    image_34: Optional[str] = None
    image_44: Optional[str] = None
    image_68: Optional[str] = None
    image_88: Optional[str] = None
    image_102: Optional[str] = None
    image_132: Optional[str] = None
    image_230: Optional[str] = None
    image_original: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icon':
        assert isinstance(obj, dict)
        image_34 = from_union([from_str, from_none], obj.get("image_34"))
        image_44 = from_union([from_str, from_none], obj.get("image_44"))
        image_68 = from_union([from_str, from_none], obj.get("image_68"))
        image_88 = from_union([from_str, from_none], obj.get("image_88"))
        image_102 = from_union([from_str, from_none], obj.get("image_102"))
        image_132 = from_union([from_str, from_none], obj.get("image_132"))
        image_230 = from_union([from_str, from_none], obj.get("image_230"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        return Icon(image_34, image_44, image_68, image_88, image_102, image_132, image_230, image_original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_34"] = from_union([from_str, from_none], self.image_34)
        result["image_44"] = from_union([from_str, from_none], self.image_44)
        result["image_68"] = from_union([from_str, from_none], self.image_68)
        result["image_88"] = from_union([from_str, from_none], self.image_88)
        result["image_102"] = from_union([from_str, from_none], self.image_102)
        result["image_132"] = from_union([from_str, from_none], self.image_132)
        result["image_230"] = from_union([from_str, from_none], self.image_230)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        return result


@dataclass
class Team:
    id: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None
    email_domain: Optional[str] = None
    icon: Optional[Icon] = None
    enterprise_id: Optional[str] = None
    enterprise_name: Optional[str] = None
    default_channels: Optional[List[str]] = None
    is_verified: Optional[bool] = None
    enterprise_domain: Optional[str] = None
    url: Optional[str] = None
    avatar_base_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        email_domain = from_union([from_str, from_none], obj.get("email_domain"))
        icon = from_union([Icon.from_dict, from_none], obj.get("icon"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        enterprise_name = from_union([from_str, from_none], obj.get("enterprise_name"))
        default_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("default_channels"))
        is_verified = from_union([from_bool, from_none], obj.get("is_verified"))
        enterprise_domain = from_union([from_str, from_none], obj.get("enterprise_domain"))
        url = from_union([from_str, from_none], obj.get("url"))
        avatar_base_url = from_union([from_str, from_none], obj.get("avatar_base_url"))
        return Team(id, name, domain, email_domain, icon, enterprise_id, enterprise_name, default_channels, is_verified, enterprise_domain, url, avatar_base_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["domain"] = from_union([from_str, from_none], self.domain)
        result["email_domain"] = from_union([from_str, from_none], self.email_domain)
        result["icon"] = from_union([lambda x: to_class(Icon, x), from_none], self.icon)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["enterprise_name"] = from_union([from_str, from_none], self.enterprise_name)
        result["default_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.default_channels)
        result["is_verified"] = from_union([from_bool, from_none], self.is_verified)
        result["enterprise_domain"] = from_union([from_str, from_none], self.enterprise_domain)
        result["url"] = from_union([from_str, from_none], self.url)
        result["avatar_base_url"] = from_union([from_str, from_none], self.avatar_base_url)
        return result


@dataclass
class AdminTeamsSettingsInfoResponse:
    ok: Optional[bool] = None
    team: Optional[Team] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminTeamsSettingsInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return AdminTeamsSettingsInfoResponse(ok, team, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def admin_teams_settings_info_response_from_dict(s: Any) -> AdminTeamsSettingsInfoResponse:
    return AdminTeamsSettingsInfoResponse.from_dict(s)


def admin_teams_settings_info_response_to_dict(x: AdminTeamsSettingsInfoResponse) -> Any:
    return to_class(AdminTeamsSettingsInfoResponse, x)
