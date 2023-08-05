# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = user_change_payload_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, TypeVar, Type, cast, Callable


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


@dataclass
class Authorization:
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    is_bot: Optional[bool] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Authorization':
        assert isinstance(obj, dict)
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return Authorization(enterprise_id, team_id, user_id, is_bot, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


@dataclass
class EnterpriseUser:
    id: Optional[str] = None
    enterprise_id: Optional[str] = None
    enterprise_name: Optional[str] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EnterpriseUser':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        enterprise_name = from_union([from_str, from_none], obj.get("enterprise_name"))
        is_admin = from_union([from_bool, from_none], obj.get("is_admin"))
        is_owner = from_union([from_bool, from_none], obj.get("is_owner"))
        return EnterpriseUser(id, enterprise_id, enterprise_name, is_admin, is_owner)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["enterprise_name"] = from_union([from_str, from_none], self.enterprise_name)
        result["is_admin"] = from_union([from_bool, from_none], self.is_admin)
        result["is_owner"] = from_union([from_bool, from_none], self.is_owner)
        return result


@dataclass
class Profile:
    guest_channels: Optional[str] = None
    guest_invited_by: Optional[str] = None
    guest_expiration_ts: Optional[int] = None
    avatar_hash: Optional[str] = None
    status_text: Optional[str] = None
    status_text_canonical: Optional[str] = None
    status_emoji: Optional[str] = None
    status_emoji_url: Optional[str] = None
    status_expiration: Optional[int] = None
    display_name: Optional[str] = None
    display_name_normalized: Optional[str] = None
    real_name: Optional[str] = None
    real_name_normalized: Optional[str] = None
    bot_id: Optional[str] = None
    title: Optional[str] = None
    email: Optional[str] = None
    skype: Optional[str] = None
    phone: Optional[str] = None
    team: Optional[str] = None
    api_app_id: Optional[str] = None
    always_active: Optional[bool] = None
    image_original: Optional[str] = None
    image_24: Optional[str] = None
    image_32: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None
    image_1024: Optional[str] = None
    is_custom_image: Optional[bool] = None
    pronouns: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        guest_channels = from_union([from_str, from_none], obj.get("guest_channels"))
        guest_invited_by = from_union([from_str, from_none], obj.get("guest_invited_by"))
        guest_expiration_ts = from_union([from_int, from_none], obj.get("guest_expiration_ts"))
        avatar_hash = from_union([from_str, from_none], obj.get("avatar_hash"))
        status_text = from_union([from_str, from_none], obj.get("status_text"))
        status_text_canonical = from_union([from_str, from_none], obj.get("status_text_canonical"))
        status_emoji = from_union([from_str, from_none], obj.get("status_emoji"))
        status_emoji_url = from_union([from_str, from_none], obj.get("status_emoji_url"))
        status_expiration = from_union([from_int, from_none], obj.get("status_expiration"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        display_name_normalized = from_union([from_str, from_none], obj.get("display_name_normalized"))
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        real_name_normalized = from_union([from_str, from_none], obj.get("real_name_normalized"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        email = from_union([from_str, from_none], obj.get("email"))
        skype = from_union([from_str, from_none], obj.get("skype"))
        phone = from_union([from_str, from_none], obj.get("phone"))
        team = from_union([from_str, from_none], obj.get("team"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        always_active = from_union([from_bool, from_none], obj.get("always_active"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        image_24 = from_union([from_str, from_none], obj.get("image_24"))
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        image_1024 = from_union([from_str, from_none], obj.get("image_1024"))
        is_custom_image = from_union([from_bool, from_none], obj.get("is_custom_image"))
        pronouns = from_union([from_str, from_none], obj.get("pronouns"))
        first_name = from_union([from_str, from_none], obj.get("first_name"))
        last_name = from_union([from_str, from_none], obj.get("last_name"))
        return Profile(guest_channels, guest_invited_by, guest_expiration_ts, avatar_hash, status_text, status_text_canonical, status_emoji, status_emoji_url, status_expiration, display_name, display_name_normalized, real_name, real_name_normalized, bot_id, title, email, skype, phone, team, api_app_id, always_active, image_original, image_24, image_32, image_48, image_72, image_192, image_512, image_1024, is_custom_image, pronouns, first_name, last_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["guest_channels"] = from_union([from_str, from_none], self.guest_channels)
        result["guest_invited_by"] = from_union([from_str, from_none], self.guest_invited_by)
        result["guest_expiration_ts"] = from_union([from_int, from_none], self.guest_expiration_ts)
        result["avatar_hash"] = from_union([from_str, from_none], self.avatar_hash)
        result["status_text"] = from_union([from_str, from_none], self.status_text)
        result["status_text_canonical"] = from_union([from_str, from_none], self.status_text_canonical)
        result["status_emoji"] = from_union([from_str, from_none], self.status_emoji)
        result["status_emoji_url"] = from_union([from_str, from_none], self.status_emoji_url)
        result["status_expiration"] = from_union([from_int, from_none], self.status_expiration)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["display_name_normalized"] = from_union([from_str, from_none], self.display_name_normalized)
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["real_name_normalized"] = from_union([from_str, from_none], self.real_name_normalized)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["email"] = from_union([from_str, from_none], self.email)
        result["skype"] = from_union([from_str, from_none], self.skype)
        result["phone"] = from_union([from_str, from_none], self.phone)
        result["team"] = from_union([from_str, from_none], self.team)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["always_active"] = from_union([from_bool, from_none], self.always_active)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        result["image_24"] = from_union([from_str, from_none], self.image_24)
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        result["image_1024"] = from_union([from_str, from_none], self.image_1024)
        result["is_custom_image"] = from_union([from_bool, from_none], self.is_custom_image)
        result["pronouns"] = from_union([from_str, from_none], self.pronouns)
        result["first_name"] = from_union([from_str, from_none], self.first_name)
        result["last_name"] = from_union([from_str, from_none], self.last_name)
        return result


@dataclass
class User:
    id: Optional[str] = None
    team_id: Optional[str] = None
    name: Optional[str] = None
    deleted: Optional[bool] = None
    color: Optional[str] = None
    real_name: Optional[str] = None
    tz: Optional[str] = None
    tz_label: Optional[str] = None
    tz_offset: Optional[int] = None
    profile: Optional[Profile] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_primary_owner: Optional[bool] = None
    is_invited_user: Optional[bool] = None
    is_restricted: Optional[bool] = None
    is_ultra_restricted: Optional[bool] = None
    is_bot: Optional[bool] = None
    is_stranger: Optional[bool] = None
    is_app_user: Optional[bool] = None
    updated: Optional[int] = None
    has_2_fa: Optional[bool] = None
    is_email_confirmed: Optional[bool] = None
    presence: Optional[str] = None
    enterprise_user: Optional[EnterpriseUser] = None
    two_factor_type: Optional[str] = None
    has_files: Optional[bool] = None
    locale: Optional[str] = None
    is_workflow_bot: Optional[bool] = None
    who_can_share_contact_card: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        color = from_union([from_str, from_none], obj.get("color"))
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        tz = from_union([from_str, from_none], obj.get("tz"))
        tz_label = from_union([from_str, from_none], obj.get("tz_label"))
        tz_offset = from_union([from_int, from_none], obj.get("tz_offset"))
        profile = from_union([Profile.from_dict, from_none], obj.get("profile"))
        is_admin = from_union([from_bool, from_none], obj.get("is_admin"))
        is_owner = from_union([from_bool, from_none], obj.get("is_owner"))
        is_primary_owner = from_union([from_bool, from_none], obj.get("is_primary_owner"))
        is_invited_user = from_union([from_bool, from_none], obj.get("is_invited_user"))
        is_restricted = from_union([from_bool, from_none], obj.get("is_restricted"))
        is_ultra_restricted = from_union([from_bool, from_none], obj.get("is_ultra_restricted"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        is_stranger = from_union([from_bool, from_none], obj.get("is_stranger"))
        is_app_user = from_union([from_bool, from_none], obj.get("is_app_user"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        has_2_fa = from_union([from_bool, from_none], obj.get("has_2fa"))
        is_email_confirmed = from_union([from_bool, from_none], obj.get("is_email_confirmed"))
        presence = from_union([from_str, from_none], obj.get("presence"))
        enterprise_user = from_union([EnterpriseUser.from_dict, from_none], obj.get("enterprise_user"))
        two_factor_type = from_union([from_str, from_none], obj.get("two_factor_type"))
        has_files = from_union([from_bool, from_none], obj.get("has_files"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        is_workflow_bot = from_union([from_bool, from_none], obj.get("is_workflow_bot"))
        who_can_share_contact_card = from_union([from_bool, from_none], obj.get("who_can_share_contact_card"))
        return User(id, team_id, name, deleted, color, real_name, tz, tz_label, tz_offset, profile, is_admin, is_owner, is_primary_owner, is_invited_user, is_restricted, is_ultra_restricted, is_bot, is_stranger, is_app_user, updated, has_2_fa, is_email_confirmed, presence, enterprise_user, two_factor_type, has_files, locale, is_workflow_bot, who_can_share_contact_card)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["color"] = from_union([from_str, from_none], self.color)
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["tz"] = from_union([from_str, from_none], self.tz)
        result["tz_label"] = from_union([from_str, from_none], self.tz_label)
        result["tz_offset"] = from_union([from_int, from_none], self.tz_offset)
        result["profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.profile)
        result["is_admin"] = from_union([from_bool, from_none], self.is_admin)
        result["is_owner"] = from_union([from_bool, from_none], self.is_owner)
        result["is_primary_owner"] = from_union([from_bool, from_none], self.is_primary_owner)
        result["is_invited_user"] = from_union([from_bool, from_none], self.is_invited_user)
        result["is_restricted"] = from_union([from_bool, from_none], self.is_restricted)
        result["is_ultra_restricted"] = from_union([from_bool, from_none], self.is_ultra_restricted)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["is_stranger"] = from_union([from_bool, from_none], self.is_stranger)
        result["is_app_user"] = from_union([from_bool, from_none], self.is_app_user)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["has_2fa"] = from_union([from_bool, from_none], self.has_2_fa)
        result["is_email_confirmed"] = from_union([from_bool, from_none], self.is_email_confirmed)
        result["presence"] = from_union([from_str, from_none], self.presence)
        result["enterprise_user"] = from_union([lambda x: to_class(EnterpriseUser, x), from_none], self.enterprise_user)
        result["two_factor_type"] = from_union([from_str, from_none], self.two_factor_type)
        result["has_files"] = from_union([from_bool, from_none], self.has_files)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["is_workflow_bot"] = from_union([from_bool, from_none], self.is_workflow_bot)
        result["who_can_share_contact_card"] = from_union([from_bool, from_none], self.who_can_share_contact_card)
        return result


@dataclass
class Event:
    type: Optional[str] = None
    user: Optional[User] = None
    cache_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        cache_ts = from_union([from_int, from_none], obj.get("cache_ts"))
        return Event(type, user, cache_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["cache_ts"] = from_union([from_int, from_none], self.cache_ts)
        return result


@dataclass
class UserChangePayload:
    token: Optional[str] = None
    enterprise_id: Optional[str] = None
    team_id: Optional[str] = None
    api_app_id: Optional[str] = None
    type: Optional[str] = None
    authed_users: Optional[List[str]] = None
    authed_teams: Optional[List[str]] = None
    authorizations: Optional[List[Authorization]] = None
    is_ext_shared_channel: Optional[bool] = None
    event_id: Optional[str] = None
    event_time: Optional[int] = None
    event_context: Optional[str] = None
    event: Optional[Event] = None

    @staticmethod
    def from_dict(obj: Any) -> 'UserChangePayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        authed_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_users"))
        authed_teams = from_union([lambda x: from_list(from_str, x), from_none], obj.get("authed_teams"))
        authorizations = from_union([lambda x: from_list(Authorization.from_dict, x), from_none], obj.get("authorizations"))
        is_ext_shared_channel = from_union([from_bool, from_none], obj.get("is_ext_shared_channel"))
        event_id = from_union([from_str, from_none], obj.get("event_id"))
        event_time = from_union([from_int, from_none], obj.get("event_time"))
        event_context = from_union([from_str, from_none], obj.get("event_context"))
        event = from_union([Event.from_dict, from_none], obj.get("event"))
        return UserChangePayload(token, enterprise_id, team_id, api_app_id, type, authed_users, authed_teams, authorizations, is_ext_shared_channel, event_id, event_time, event_context, event)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["authed_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_users)
        result["authed_teams"] = from_union([lambda x: from_list(from_str, x), from_none], self.authed_teams)
        result["authorizations"] = from_union([lambda x: from_list(lambda x: to_class(Authorization, x), x), from_none], self.authorizations)
        result["is_ext_shared_channel"] = from_union([from_bool, from_none], self.is_ext_shared_channel)
        result["event_id"] = from_union([from_str, from_none], self.event_id)
        result["event_time"] = from_union([from_int, from_none], self.event_time)
        result["event_context"] = from_union([from_str, from_none], self.event_context)
        result["event"] = from_union([lambda x: to_class(Event, x), from_none], self.event)
        return result


def user_change_payload_from_dict(s: Any) -> UserChangePayload:
    return UserChangePayload.from_dict(s)


def user_change_payload_to_dict(x: UserChangePayload) -> Any:
    return to_class(UserChangePayload, x)
