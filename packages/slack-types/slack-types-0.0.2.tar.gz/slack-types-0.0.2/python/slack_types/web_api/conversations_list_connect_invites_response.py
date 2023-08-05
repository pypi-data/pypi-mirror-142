# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = conversations_list_connect_invites_response_from_dict(json.loads(json_string))

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
class Icon:
    image_102: Optional[str] = None
    image_132: Optional[str] = None
    image_230: Optional[str] = None
    image_34: Optional[str] = None
    image_44: Optional[str] = None
    image_68: Optional[str] = None
    image_88: Optional[str] = None
    image_original: Optional[str] = None
    image_default: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icon':
        assert isinstance(obj, dict)
        image_102 = from_union([from_str, from_none], obj.get("image_102"))
        image_132 = from_union([from_str, from_none], obj.get("image_132"))
        image_230 = from_union([from_str, from_none], obj.get("image_230"))
        image_34 = from_union([from_str, from_none], obj.get("image_34"))
        image_44 = from_union([from_str, from_none], obj.get("image_44"))
        image_68 = from_union([from_str, from_none], obj.get("image_68"))
        image_88 = from_union([from_str, from_none], obj.get("image_88"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        image_default = from_union([from_bool, from_none], obj.get("image_default"))
        return Icon(image_102, image_132, image_230, image_34, image_44, image_68, image_88, image_original, image_default)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_102"] = from_union([from_str, from_none], self.image_102)
        result["image_132"] = from_union([from_str, from_none], self.image_132)
        result["image_230"] = from_union([from_str, from_none], self.image_230)
        result["image_34"] = from_union([from_str, from_none], self.image_34)
        result["image_44"] = from_union([from_str, from_none], self.image_44)
        result["image_68"] = from_union([from_str, from_none], self.image_68)
        result["image_88"] = from_union([from_str, from_none], self.image_88)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        result["image_default"] = from_union([from_bool, from_none], self.image_default)
        return result


@dataclass
class IngTeam:
    id: Optional[str] = None
    name: Optional[str] = None
    icon: Optional[Icon] = None
    is_verified: Optional[bool] = None
    domain: Optional[str] = None
    date_created: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IngTeam':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        icon = from_union([Icon.from_dict, from_none], obj.get("icon"))
        is_verified = from_union([from_bool, from_none], obj.get("is_verified"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        return IngTeam(id, name, icon, is_verified, domain, date_created)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["icon"] = from_union([lambda x: to_class(Icon, x), from_none], self.icon)
        result["is_verified"] = from_union([from_bool, from_none], self.is_verified)
        result["domain"] = from_union([from_str, from_none], self.domain)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        return result


@dataclass
class Profile:
    real_name: Optional[str] = None
    display_name: Optional[str] = None
    real_name_normalized: Optional[str] = None
    display_name_normalized: Optional[str] = None
    team: Optional[str] = None
    avatar_hash: Optional[str] = None
    email: Optional[str] = None
    image_24: Optional[str] = None
    image_32: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None
    image_1024: Optional[str] = None
    image_original: Optional[str] = None
    is_custom_image: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        real_name_normalized = from_union([from_str, from_none], obj.get("real_name_normalized"))
        display_name_normalized = from_union([from_str, from_none], obj.get("display_name_normalized"))
        team = from_union([from_str, from_none], obj.get("team"))
        avatar_hash = from_union([from_str, from_none], obj.get("avatar_hash"))
        email = from_union([from_str, from_none], obj.get("email"))
        image_24 = from_union([from_str, from_none], obj.get("image_24"))
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        image_1024 = from_union([from_str, from_none], obj.get("image_1024"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        is_custom_image = from_union([from_bool, from_none], obj.get("is_custom_image"))
        return Profile(real_name, display_name, real_name_normalized, display_name_normalized, team, avatar_hash, email, image_24, image_32, image_48, image_72, image_192, image_512, image_1024, image_original, is_custom_image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["real_name_normalized"] = from_union([from_str, from_none], self.real_name_normalized)
        result["display_name_normalized"] = from_union([from_str, from_none], self.display_name_normalized)
        result["team"] = from_union([from_str, from_none], self.team)
        result["avatar_hash"] = from_union([from_str, from_none], self.avatar_hash)
        result["email"] = from_union([from_str, from_none], self.email)
        result["image_24"] = from_union([from_str, from_none], self.image_24)
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        result["image_1024"] = from_union([from_str, from_none], self.image_1024)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        result["is_custom_image"] = from_union([from_bool, from_none], self.is_custom_image)
        return result


@dataclass
class TingUser:
    id: Optional[str] = None
    team_id: Optional[str] = None
    name: Optional[str] = None
    updated: Optional[int] = None
    profile: Optional[Profile] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TingUser':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        profile = from_union([Profile.from_dict, from_none], obj.get("profile"))
        return TingUser(id, team_id, name, updated, profile)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["profile"] = from_union([lambda x: to_class(Profile, x), from_none], self.profile)
        return result


@dataclass
class Review:
    type: Optional[str] = None
    date_review: Optional[int] = None
    reviewing_team: Optional[IngTeam] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Review':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        date_review = from_union([from_int, from_none], obj.get("date_review"))
        reviewing_team = from_union([IngTeam.from_dict, from_none], obj.get("reviewing_team"))
        return Review(type, date_review, reviewing_team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["date_review"] = from_union([from_int, from_none], self.date_review)
        result["reviewing_team"] = from_union([lambda x: to_class(IngTeam, x), from_none], self.reviewing_team)
        return result


@dataclass
class Acceptance:
    approval_status: Optional[str] = None
    date_accepted: Optional[int] = None
    date_invalid: Optional[int] = None
    date_last_updated: Optional[int] = None
    accepting_team: Optional[IngTeam] = None
    accepting_user: Optional[TingUser] = None
    reviews: Optional[List[Review]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Acceptance':
        assert isinstance(obj, dict)
        approval_status = from_union([from_str, from_none], obj.get("approval_status"))
        date_accepted = from_union([from_int, from_none], obj.get("date_accepted"))
        date_invalid = from_union([from_int, from_none], obj.get("date_invalid"))
        date_last_updated = from_union([from_int, from_none], obj.get("date_last_updated"))
        accepting_team = from_union([IngTeam.from_dict, from_none], obj.get("accepting_team"))
        accepting_user = from_union([TingUser.from_dict, from_none], obj.get("accepting_user"))
        reviews = from_union([lambda x: from_list(Review.from_dict, x), from_none], obj.get("reviews"))
        return Acceptance(approval_status, date_accepted, date_invalid, date_last_updated, accepting_team, accepting_user, reviews)

    def to_dict(self) -> dict:
        result: dict = {}
        result["approval_status"] = from_union([from_str, from_none], self.approval_status)
        result["date_accepted"] = from_union([from_int, from_none], self.date_accepted)
        result["date_invalid"] = from_union([from_int, from_none], self.date_invalid)
        result["date_last_updated"] = from_union([from_int, from_none], self.date_last_updated)
        result["accepting_team"] = from_union([lambda x: to_class(IngTeam, x), from_none], self.accepting_team)
        result["accepting_user"] = from_union([lambda x: to_class(TingUser, x), from_none], self.accepting_user)
        result["reviews"] = from_union([lambda x: from_list(lambda x: to_class(Review, x), x), from_none], self.reviews)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    is_im: Optional[bool] = None
    is_private: Optional[bool] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        is_im = from_union([from_bool, from_none], obj.get("is_im"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Channel(id, is_im, is_private, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["is_im"] = from_union([from_bool, from_none], self.is_im)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class InviteInvite:
    id: Optional[str] = None
    date_created: Optional[int] = None
    date_invalid: Optional[int] = None
    inviting_team: Optional[IngTeam] = None
    inviting_user: Optional[TingUser] = None
    link: Optional[str] = None
    recipient_user_id: Optional[str] = None
    recipient_email: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InviteInvite':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        date_created = from_union([from_int, from_none], obj.get("date_created"))
        date_invalid = from_union([from_int, from_none], obj.get("date_invalid"))
        inviting_team = from_union([IngTeam.from_dict, from_none], obj.get("inviting_team"))
        inviting_user = from_union([TingUser.from_dict, from_none], obj.get("inviting_user"))
        link = from_union([from_str, from_none], obj.get("link"))
        recipient_user_id = from_union([from_str, from_none], obj.get("recipient_user_id"))
        recipient_email = from_union([from_str, from_none], obj.get("recipient_email"))
        return InviteInvite(id, date_created, date_invalid, inviting_team, inviting_user, link, recipient_user_id, recipient_email)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["date_created"] = from_union([from_int, from_none], self.date_created)
        result["date_invalid"] = from_union([from_int, from_none], self.date_invalid)
        result["inviting_team"] = from_union([lambda x: to_class(IngTeam, x), from_none], self.inviting_team)
        result["inviting_user"] = from_union([lambda x: to_class(TingUser, x), from_none], self.inviting_user)
        result["link"] = from_union([from_str, from_none], self.link)
        result["recipient_user_id"] = from_union([from_str, from_none], self.recipient_user_id)
        result["recipient_email"] = from_union([from_str, from_none], self.recipient_email)
        return result


@dataclass
class InviteElement:
    direction: Optional[str] = None
    status: Optional[str] = None
    date_last_updated: Optional[int] = None
    invite_type: Optional[str] = None
    invite: Optional[InviteInvite] = None
    channel: Optional[Channel] = None
    acceptances: Optional[List[Acceptance]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InviteElement':
        assert isinstance(obj, dict)
        direction = from_union([from_str, from_none], obj.get("direction"))
        status = from_union([from_str, from_none], obj.get("status"))
        date_last_updated = from_union([from_int, from_none], obj.get("date_last_updated"))
        invite_type = from_union([from_str, from_none], obj.get("invite_type"))
        invite = from_union([InviteInvite.from_dict, from_none], obj.get("invite"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        acceptances = from_union([lambda x: from_list(Acceptance.from_dict, x), from_none], obj.get("acceptances"))
        return InviteElement(direction, status, date_last_updated, invite_type, invite, channel, acceptances)

    def to_dict(self) -> dict:
        result: dict = {}
        result["direction"] = from_union([from_str, from_none], self.direction)
        result["status"] = from_union([from_str, from_none], self.status)
        result["date_last_updated"] = from_union([from_int, from_none], self.date_last_updated)
        result["invite_type"] = from_union([from_str, from_none], self.invite_type)
        result["invite"] = from_union([lambda x: to_class(InviteInvite, x), from_none], self.invite)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["acceptances"] = from_union([lambda x: from_list(lambda x: to_class(Acceptance, x), x), from_none], self.acceptances)
        return result


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(next_cursor, messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class ConversationsListConnectInvitesResponse:
    ok: Optional[bool] = None
    error: Optional[str] = None
    arg: Optional[str] = None
    invites: Optional[List[InviteElement]] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ConversationsListConnectInvitesResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        arg = from_union([from_str, from_none], obj.get("arg"))
        invites = from_union([lambda x: from_list(InviteElement.from_dict, x), from_none], obj.get("invites"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ConversationsListConnectInvitesResponse(ok, error, arg, invites, response_metadata, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["arg"] = from_union([from_str, from_none], self.arg)
        result["invites"] = from_union([lambda x: from_list(lambda x: to_class(InviteElement, x), x), from_none], self.invites)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def conversations_list_connect_invites_response_from_dict(s: Any) -> ConversationsListConnectInvitesResponse:
    return ConversationsListConnectInvitesResponse.from_dict(s)


def conversations_list_connect_invites_response_to_dict(x: ConversationsListConnectInvitesResponse) -> Any:
    return to_class(ConversationsListConnectInvitesResponse, x)
