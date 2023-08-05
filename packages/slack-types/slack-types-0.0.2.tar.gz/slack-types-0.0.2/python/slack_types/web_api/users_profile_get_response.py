# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = users_profile_get_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, Dict, List, TypeVar, Callable, Type, cast


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


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
class Field:
    value: Optional[str] = None
    alt: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        alt = from_union([from_str, from_none], obj.get("alt"))
        return Field(value, alt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["alt"] = from_union([from_str, from_none], self.alt)
        return result


@dataclass
class StatusEmojiDisplayInfo:
    emoji_name: Optional[str] = None
    display_alias: Optional[str] = None
    display_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'StatusEmojiDisplayInfo':
        assert isinstance(obj, dict)
        emoji_name = from_union([from_str, from_none], obj.get("emoji_name"))
        display_alias = from_union([from_str, from_none], obj.get("display_alias"))
        display_url = from_union([from_str, from_none], obj.get("display_url"))
        return StatusEmojiDisplayInfo(emoji_name, display_alias, display_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emoji_name"] = from_union([from_str, from_none], self.emoji_name)
        result["display_alias"] = from_union([from_str, from_none], self.display_alias)
        result["display_url"] = from_union([from_str, from_none], self.display_url)
        return result


@dataclass
class Profile:
    title: Optional[str] = None
    phone: Optional[str] = None
    skype: Optional[str] = None
    real_name: Optional[str] = None
    real_name_normalized: Optional[str] = None
    display_name: Optional[str] = None
    display_name_normalized: Optional[str] = None
    fields: Optional[Dict[str, Field]] = None
    status_text: Optional[str] = None
    status_emoji: Optional[str] = None
    status_expiration: Optional[int] = None
    avatar_hash: Optional[str] = None
    image_original: Optional[str] = None
    is_custom_image: Optional[bool] = None
    email: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    image_24: Optional[str] = None
    image_32: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None
    image_1024: Optional[str] = None
    status_text_canonical: Optional[str] = None
    status_emoji_url: Optional[str] = None
    pronouns: Optional[str] = None
    status_emoji_display_info: Optional[List[StatusEmojiDisplayInfo]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        skype = from_union([from_str, from_none], obj.get("skype"))
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        real_name_normalized = from_union([from_str, from_none], obj.get("real_name_normalized"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        display_name_normalized = from_union([from_str, from_none], obj.get("display_name_normalized"))
        fields = from_union([lambda x: from_dict(Field.from_dict, x), from_none], obj.get("fields"))
        status_text = from_union([from_str, from_none], obj.get("status_text"))
        status_emoji = from_union([from_str, from_none], obj.get("status_emoji"))
        status_expiration = from_union([from_int, from_none], obj.get("status_expiration"))
        avatar_hash = from_union([from_str, from_none], obj.get("avatar_hash"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        is_custom_image = from_union([from_bool, from_none], obj.get("is_custom_image"))
        email = from_union([from_str, from_none], obj.get("email"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        last_name = from_union([from_str, from_none], obj.get("last_name"))
        image_24 = from_union([from_str, from_none], obj.get("image_24"))
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        image_1024 = from_union([from_str, from_none], obj.get("image_1024"))
        status_text_canonical = from_union([from_str, from_none], obj.get("status_text_canonical"))
        status_emoji_url = from_union([from_str, from_none], obj.get("status_emoji_url"))
        pronouns = from_union([from_str, from_none], obj.get("pronouns"))
        status_emoji_display_info = from_union([lambda x: from_list(StatusEmojiDisplayInfo.from_dict, x), from_none], obj.get("status_emoji_display_info"))
        return Profile(title, phone, skype, real_name, real_name_normalized, display_name, display_name_normalized, fields, status_text, status_emoji, status_expiration, avatar_hash, image_original, is_custom_image, email, first_name, last_name, image_24, image_32, image_48, image_72, image_192, image_512, image_1024, status_text_canonical, status_emoji_url, pronouns, status_emoji_display_info)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["phone"] = from_union([from_str, from_none], self.phone)
        result["skype"] = from_union([from_str, from_none], self.skype)
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["real_name_normalized"] = from_union([from_str, from_none], self.real_name_normalized)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["display_name_normalized"] = from_union([from_str, from_none], self.display_name_normalized)
        result["fields"] = from_union([lambda x: from_dict(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["status_text"] = from_union([from_str, from_none], self.status_text)
        result["status_emoji"] = from_union([from_str, from_none], self.status_emoji)
        result["status_expiration"] = from_union([from_int, from_none], self.status_expiration)
        result["avatar_hash"] = from_union([from_str, from_none], self.avatar_hash)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        result["is_custom_image"] = from_union([from_bool, from_none], self.is_custom_image)
        result["email"] = from_union([from_str, from_none], self.email)
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["last_name"] = from_union([from_str, from_none], self.last_name)
        result["image_24"] = from_union([from_str, from_none], self.image_24)
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        result["image_1024"] = from_union([from_str, from_none], self.image_1024)
        result["status_text_canonical"] = from_union([from_str, from_none], self.status_text_canonical)
        result["status_emoji_url"] = from_union([from_str, from_none], self.status_emoji_url)
        result["pronouns"] = from_union([from_str, from_none], self.pronouns)
        result["status_emoji_display_info"] = from_union([lambda x: from_list(lambda x: to_class(StatusEmojiDisplayInfo, x), x), from_none], self.status_emoji_display_info)
        return result


@dataclass
class UsersProfileGetResponse:
    ok: Optional[bool] = None
    profile: Optional[Profile] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UsersProfileGetResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        profile = from_union([Profile.from_dict, from_none], obj.get("profile"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return UsersProfileGetResponse(ok, profile, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.profile)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def users_profile_get_response_from_dict(s: Any) -> UsersProfileGetResponse:
    return UsersProfileGetResponse.from_dict(s)


def users_profile_get_response_to_dict(x: UsersProfileGetResponse) -> Any:
    return to_class(UsersProfileGetResponse, x)
