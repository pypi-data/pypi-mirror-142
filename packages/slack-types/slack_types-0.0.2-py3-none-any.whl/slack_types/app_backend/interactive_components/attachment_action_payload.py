# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = attachment_action_payload_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class Action:
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        text = from_union([from_str, from_none], obj.get("text"))
        return Action(name, type, value, text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        result["text"] = from_union([from_str, from_none], self.text)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Channel(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Field:
    title: Optional[str] = None
    value: Optional[str] = None
    short: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Field':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        value = from_union([from_str, from_none], obj.get("value"))
        short = from_union([from_bool, from_none], obj.get("short"))
        return Field(title, value, short)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["value"] = from_union([from_str, from_none], self.value)
        result["short"] = from_union([from_bool, from_none], self.short)
        return result


@dataclass
class Attachment:
    id: Optional[int] = None
    callback_id: Optional[str] = None
    title: Optional[str] = None
    text: Optional[str] = None
    fallback: Optional[str] = None
    color: Optional[str] = None
    attachment_type: Optional[str] = None
    actions: Optional[List[Action]] = None
    fields: Optional[List[Field]] = None
    author_name: Optional[str] = None
    author_icon: Optional[str] = None
    image_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attachment':
        assert isinstance(obj, dict)
        id = from_union([from_int, from_none], obj.get("id"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        title = from_union([from_str, from_none], obj.get("title"))
        text = from_union([from_str, from_none], obj.get("text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        color = from_union([from_str, from_none], obj.get("color"))
        attachment_type = from_union([from_str, from_none], obj.get("attachment_type"))
        actions = from_union([lambda x: from_list(Action.from_dict, x), from_none], obj.get("actions"))
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        author_icon = from_union([from_str, from_none], obj.get("author_icon"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        return Attachment(id, callback_id, title, text, fallback, color, attachment_type, actions, fields, author_name, author_icon, image_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_int, from_none], self.id)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["title"] = from_union([from_str, from_none], self.title)
        result["text"] = from_union([from_str, from_none], self.text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["color"] = from_union([from_str, from_none], self.color)
        result["attachment_type"] = from_union([from_str, from_none], self.attachment_type)
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(Action, x), x), from_none], self.actions)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["author_name"] = from_union([from_str, from_none], self.author_name)
        result["author_icon"] = from_union([from_str, from_none], self.author_icon)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        return result


@dataclass
class OriginalMessage:
    bot_id: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    user: Optional[str] = None
    username: Optional[str] = None
    ts: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    subtype: Optional[str] = None
    thread_ts: Optional[str] = None
    parent_user_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OriginalMessage':
        assert isinstance(obj, dict)
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        username = from_union([from_str, from_none], obj.get("username"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        attachments = from_union([lambda x: from_list(Attachment.from_dict, x), from_none], obj.get("attachments"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        return OriginalMessage(bot_id, type, text, user, username, ts, attachments, subtype, thread_ts, parent_user_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["username"] = from_union([from_str, from_none], self.username)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["attachments"] = from_union([lambda x: from_list(lambda x: to_class(Attachment, x), x), from_none], self.attachments)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        return result


@dataclass
class Team:
    id: Optional[str] = None
    domain: Optional[str] = None
    enterprise_id: Optional[str] = None
    enterprise_name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        enterprise_name = from_union([from_str, from_none], obj.get("enterprise_name"))
        return Team(id, domain, enterprise_id, enterprise_name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["domain"] = from_union([from_str, from_none], self.domain)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["enterprise_name"] = from_union([from_str, from_none], self.enterprise_name)
        return result


@dataclass
class User:
    id: Optional[str] = None
    name: Optional[str] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return User(id, name, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class AttachmentActionPayload:
    type: Optional[str] = None
    actions: Optional[List[Action]] = None
    callback_id: Optional[str] = None
    enterprise: Optional[Channel] = None
    team: Optional[Team] = None
    channel: Optional[Channel] = None
    user: Optional[User] = None
    action_ts: Optional[str] = None
    message_ts: Optional[str] = None
    attachment_id: Optional[str] = None
    token: Optional[str] = None
    is_app_unfurl: Optional[bool] = None
    original_message: Optional[OriginalMessage] = None
    response_url: Optional[str] = None
    trigger_id: Optional[str] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AttachmentActionPayload':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        actions = from_union([lambda x: from_list(Action.from_dict, x), from_none], obj.get("actions"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        enterprise = from_union([Channel.from_dict, from_none], obj.get("enterprise"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        action_ts = from_union([from_str, from_none], obj.get("action_ts"))
        message_ts = from_union([from_str, from_none], obj.get("message_ts"))
        attachment_id = from_union([from_str, from_none], obj.get("attachment_id"))
        token = from_union([from_str, from_none], obj.get("token"))
        is_app_unfurl = from_union([from_bool, from_none], obj.get("is_app_unfurl"))
        original_message = from_union([OriginalMessage.from_dict, from_none], obj.get("original_message"))
        response_url = from_union([from_str, from_none], obj.get("response_url"))
        trigger_id = from_union([from_str, from_none], obj.get("trigger_id"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return AttachmentActionPayload(type, actions, callback_id, enterprise, team, channel, user, action_ts, message_ts, attachment_id, token, is_app_unfurl, original_message, response_url, trigger_id, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(Action, x), x), from_none], self.actions)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["enterprise"] = from_union([lambda x: to_class(Channel, x), from_none], self.enterprise)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["action_ts"] = from_union([from_str, from_none], self.action_ts)
        result["message_ts"] = from_union([from_str, from_none], self.message_ts)
        result["attachment_id"] = from_union([from_str, from_none], self.attachment_id)
        result["token"] = from_union([from_str, from_none], self.token)
        result["is_app_unfurl"] = from_union([from_bool, from_none], self.is_app_unfurl)
        result["original_message"] = from_union([lambda x: to_class(OriginalMessage, x), from_none], self.original_message)
        result["response_url"] = from_union([from_str, from_none], self.response_url)
        result["trigger_id"] = from_union([from_str, from_none], self.trigger_id)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


def attachment_action_payload_from_dict(s: Any) -> AttachmentActionPayload:
    return AttachmentActionPayload.from_dict(s)


def attachment_action_payload_to_dict(x: AttachmentActionPayload) -> Any:
    return to_class(AttachmentActionPayload, x)
