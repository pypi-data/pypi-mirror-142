# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = block_action_payload_from_dict(json.loads(json_string))

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Type, cast, Callable


T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


class TypeEnum(Enum):
    EMPTY = ""
    MRKDWN = "mrkdwn"
    PLAIN_TEXT = "plain_text"


@dataclass
class Close:
    type: Optional[TypeEnum] = None
    text: Optional[str] = None
    emoji: Optional[bool] = None
    verbatim: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Close':
        assert isinstance(obj, dict)
        type = from_union([TypeEnum, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        emoji = from_union([from_bool, from_none], obj.get("emoji"))
        verbatim = from_union([from_bool, from_none], obj.get("verbatim"))
        return Close(type, text, emoji, verbatim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: to_enum(TypeEnum, x), from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["emoji"] = from_union([from_bool, from_none], self.emoji)
        result["verbatim"] = from_union([from_bool, from_none], self.verbatim)
        return result


@dataclass
class ElementConfirm:
    title: Optional[Close] = None
    text: Optional[Close] = None
    confirm: Optional[Close] = None
    deny: Optional[Close] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ElementConfirm':
        assert isinstance(obj, dict)
        title = from_union([Close.from_dict, from_none], obj.get("title"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        confirm = from_union([Close.from_dict, from_none], obj.get("confirm"))
        deny = from_union([Close.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return ElementConfirm(title, text, confirm, deny, style)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(Close, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["confirm"] = from_union([lambda x: to_class(Close, x), from_none], self.confirm)
        result["deny"] = from_union([lambda x: to_class(Close, x), from_none], self.deny)
        result["style"] = from_union([from_str, from_none], self.style)
        return result


@dataclass
class InitialOption:
    text: Optional[Close] = None
    value: Optional[str] = None
    description: Optional[Close] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialOption':
        assert isinstance(obj, dict)
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([Close.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return InitialOption(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(Close, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class SelectedOption:
    text: Optional[Close] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SelectedOption':
        assert isinstance(obj, dict)
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        return SelectedOption(text, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class BlockActionPayloadAction:
    action_id: Optional[str] = None
    block_id: Optional[str] = None
    text: Optional[Close] = None
    value: Optional[str] = None
    type: Optional[str] = None
    action_ts: Optional[str] = None
    placeholder: Optional[Close] = None
    confirm: Optional[ElementConfirm] = None
    url: Optional[str] = None
    initial_option: Optional[InitialOption] = None
    selected_option: Optional[SelectedOption] = None
    selected_user: Optional[str] = None
    initial_user: Optional[str] = None
    selected_conversation: Optional[str] = None
    initial_conversation: Optional[str] = None
    selected_channel: Optional[str] = None
    initial_channel: Optional[str] = None
    min_query_length: Optional[int] = None
    selected_date: Optional[str] = None
    initial_date: Optional[str] = None
    selected_time: Optional[str] = None
    initial_time: Optional[str] = None
    selected_options: Optional[List[SelectedOption]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BlockActionPayloadAction':
        assert isinstance(obj, dict)
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        type = from_union([from_str, from_none], obj.get("type"))
        action_ts = from_union([from_str, from_none], obj.get("action_ts"))
        placeholder = from_union([Close.from_dict, from_none], obj.get("placeholder"))
        confirm = from_union([ElementConfirm.from_dict, from_none], obj.get("confirm"))
        url = from_union([from_str, from_none], obj.get("url"))
        initial_option = from_union([InitialOption.from_dict, from_none], obj.get("initial_option"))
        selected_option = from_union([SelectedOption.from_dict, from_none], obj.get("selected_option"))
        selected_user = from_union([from_str, from_none], obj.get("selected_user"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        selected_conversation = from_union([from_str, from_none], obj.get("selected_conversation"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        selected_channel = from_union([from_str, from_none], obj.get("selected_channel"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        selected_date = from_union([from_str, from_none], obj.get("selected_date"))
        initial_date = from_union([from_str, from_none], obj.get("initial_date"))
        selected_time = from_union([from_str, from_none], obj.get("selected_time"))
        initial_time = from_union([from_str, from_none], obj.get("initial_time"))
        selected_options = from_union([lambda x: from_list(SelectedOption.from_dict, x), from_none], obj.get("selected_options"))
        return BlockActionPayloadAction(action_id, block_id, text, value, type, action_ts, placeholder, confirm, url, initial_option, selected_option, selected_user, initial_user, selected_conversation, initial_conversation, selected_channel, initial_channel, min_query_length, selected_date, initial_date, selected_time, initial_time, selected_options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["type"] = from_union([from_str, from_none], self.type)
        result["action_ts"] = from_union([from_str, from_none], self.action_ts)
        result["placeholder"] = from_union([lambda x: to_class(Close, x), from_none], self.placeholder)
        result["confirm"] = from_union([lambda x: to_class(ElementConfirm, x), from_none], self.confirm)
        result["url"] = from_union([from_str, from_none], self.url)
        result["initial_option"] = from_union([lambda x: to_class(InitialOption, x), from_none], self.initial_option)
        result["selected_option"] = from_union([lambda x: to_class(SelectedOption, x), from_none], self.selected_option)
        result["selected_user"] = from_union([from_str, from_none], self.selected_user)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        result["selected_conversation"] = from_union([from_str, from_none], self.selected_conversation)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["selected_channel"] = from_union([from_str, from_none], self.selected_channel)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["selected_date"] = from_union([from_str, from_none], self.selected_date)
        result["initial_date"] = from_union([from_str, from_none], self.initial_date)
        result["selected_time"] = from_union([from_str, from_none], self.selected_time)
        result["initial_time"] = from_union([from_str, from_none], self.initial_time)
        result["selected_options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOption, x), x), from_none], self.selected_options)
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
class Container:
    type: Optional[str] = None
    message_ts: Optional[str] = None
    attachment_id: Optional[int] = None
    channel_id: Optional[str] = None
    text: Optional[str] = None
    is_ephemeral: Optional[bool] = None
    is_app_unfurl: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Container':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        message_ts = from_union([from_str, from_none], obj.get("message_ts"))
        attachment_id = from_union([from_int, from_none], obj.get("attachment_id"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        text = from_union([from_str, from_none], obj.get("text"))
        is_ephemeral = from_union([from_bool, from_none], obj.get("is_ephemeral"))
        is_app_unfurl = from_union([from_bool, from_none], obj.get("is_app_unfurl"))
        return Container(type, message_ts, attachment_id, channel_id, text, is_ephemeral, is_app_unfurl)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["message_ts"] = from_union([from_str, from_none], self.message_ts)
        result["attachment_id"] = from_union([from_int, from_none], self.attachment_id)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["text"] = from_union([from_str, from_none], self.text)
        result["is_ephemeral"] = from_union([from_bool, from_none], self.is_ephemeral)
        result["is_app_unfurl"] = from_union([from_bool, from_none], self.is_app_unfurl)
        return result


@dataclass
class PurpleConfirm:
    title: Optional[str] = None
    text: Optional[str] = None
    ok_text: Optional[str] = None
    dismiss_text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'PurpleConfirm':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        text = from_union([from_str, from_none], obj.get("text"))
        ok_text = from_union([from_str, from_none], obj.get("ok_text"))
        dismiss_text = from_union([from_str, from_none], obj.get("dismiss_text"))
        return PurpleConfirm(title, text, ok_text, dismiss_text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["text"] = from_union([from_str, from_none], self.text)
        result["ok_text"] = from_union([from_str, from_none], self.ok_text)
        result["dismiss_text"] = from_union([from_str, from_none], self.dismiss_text)
        return result


@dataclass
class AttachmentAction:
    id: Optional[str] = None
    name: Optional[str] = None
    text: Optional[str] = None
    style: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    confirm: Optional[PurpleConfirm] = None
    options: Optional[List[Any]] = None
    selected_options: Optional[List[Any]] = None
    data_source: Optional[str] = None
    min_query_length: Optional[int] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AttachmentAction':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        text = from_union([from_str, from_none], obj.get("text"))
        style = from_union([from_str, from_none], obj.get("style"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        confirm = from_union([PurpleConfirm.from_dict, from_none], obj.get("confirm"))
        options = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("options"))
        selected_options = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("selected_options"))
        data_source = from_union([from_str, from_none], obj.get("data_source"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        url = from_union([from_str, from_none], obj.get("url"))
        return AttachmentAction(id, name, text, style, type, value, confirm, options, selected_options, data_source, min_query_length, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["text"] = from_union([from_str, from_none], self.text)
        result["style"] = from_union([from_str, from_none], self.style)
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        result["confirm"] = from_union([lambda x: to_class(PurpleConfirm, x), from_none], self.confirm)
        result["options"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.options)
        result["selected_options"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.selected_options)
        result["data_source"] = from_union([from_str, from_none], self.data_source)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["url"] = from_union([from_str, from_none], self.url)
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
class Metadata:
    thumb_64: Optional[bool] = None
    thumb_80: Optional[bool] = None
    thumb_160: Optional[bool] = None
    original_w: Optional[int] = None
    original_h: Optional[int] = None
    thumb_360__w: Optional[int] = None
    thumb_360__h: Optional[int] = None
    format: Optional[str] = None
    extension: Optional[str] = None
    rotation: Optional[int] = None
    thumb_tiny: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Metadata':
        assert isinstance(obj, dict)
        thumb_64 = from_union([from_bool, from_none], obj.get("thumb_64"))
        thumb_80 = from_union([from_bool, from_none], obj.get("thumb_80"))
        thumb_160 = from_union([from_bool, from_none], obj.get("thumb_160"))
        original_w = from_union([from_int, from_none], obj.get("original_w"))
        original_h = from_union([from_int, from_none], obj.get("original_h"))
        thumb_360__w = from_union([from_int, from_none], obj.get("thumb_360_w"))
        thumb_360__h = from_union([from_int, from_none], obj.get("thumb_360_h"))
        format = from_union([from_str, from_none], obj.get("format"))
        extension = from_union([from_str, from_none], obj.get("extension"))
        rotation = from_union([from_int, from_none], obj.get("rotation"))
        thumb_tiny = from_union([from_str, from_none], obj.get("thumb_tiny"))
        return Metadata(thumb_64, thumb_80, thumb_160, original_w, original_h, thumb_360__w, thumb_360__h, format, extension, rotation, thumb_tiny)

    def to_dict(self) -> dict:
        result: dict = {}
        result["thumb_64"] = from_union([from_bool, from_none], self.thumb_64)
        result["thumb_80"] = from_union([from_bool, from_none], self.thumb_80)
        result["thumb_160"] = from_union([from_bool, from_none], self.thumb_160)
        result["original_w"] = from_union([from_int, from_none], self.original_w)
        result["original_h"] = from_union([from_int, from_none], self.original_h)
        result["thumb_360_w"] = from_union([from_int, from_none], self.thumb_360__w)
        result["thumb_360_h"] = from_union([from_int, from_none], self.thumb_360__h)
        result["format"] = from_union([from_str, from_none], self.format)
        result["extension"] = from_union([from_str, from_none], self.extension)
        result["rotation"] = from_union([from_int, from_none], self.rotation)
        result["thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        return result


@dataclass
class Attachment:
    msg_subtype: Optional[str] = None
    fallback: Optional[str] = None
    callback_id: Optional[str] = None
    color: Optional[str] = None
    pretext: Optional[str] = None
    service_url: Optional[str] = None
    service_name: Optional[str] = None
    service_icon: Optional[str] = None
    author_id: Optional[str] = None
    author_name: Optional[str] = None
    author_link: Optional[str] = None
    author_icon: Optional[str] = None
    from_url: Optional[str] = None
    original_url: Optional[str] = None
    author_subname: Optional[str] = None
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    id: Optional[int] = None
    bot_id: Optional[str] = None
    indent: Optional[bool] = None
    is_msg_unfurl: Optional[bool] = None
    is_reply_unfurl: Optional[bool] = None
    is_thread_root_unfurl: Optional[bool] = None
    is_app_unfurl: Optional[bool] = None
    app_unfurl_url: Optional[str] = None
    title: Optional[str] = None
    title_link: Optional[str] = None
    text: Optional[str] = None
    fields: Optional[List[Field]] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    thumb_url: Optional[str] = None
    thumb_width: Optional[int] = None
    thumb_height: Optional[int] = None
    video_url: Optional[str] = None
    video_html: Optional[str] = None
    video_html_width: Optional[int] = None
    video_html_height: Optional[int] = None
    footer: Optional[str] = None
    footer_icon: Optional[str] = None
    ts: Optional[str] = None
    mrkdwn_in: Optional[List[str]] = None
    actions: Optional[List[AttachmentAction]] = None
    filename: Optional[str] = None
    size: Optional[int] = None
    mimetype: Optional[str] = None
    url: Optional[str] = None
    metadata: Optional[Metadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Attachment':
        assert isinstance(obj, dict)
        msg_subtype = from_union([from_str, from_none], obj.get("msg_subtype"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        color = from_union([from_str, from_none], obj.get("color"))
        pretext = from_union([from_str, from_none], obj.get("pretext"))
        service_url = from_union([from_str, from_none], obj.get("service_url"))
        service_name = from_union([from_str, from_none], obj.get("service_name"))
        service_icon = from_union([from_str, from_none], obj.get("service_icon"))
        author_id = from_union([from_str, from_none], obj.get("author_id"))
        author_name = from_union([from_str, from_none], obj.get("author_name"))
        author_link = from_union([from_str, from_none], obj.get("author_link"))
        author_icon = from_union([from_str, from_none], obj.get("author_icon"))
        from_url = from_union([from_str, from_none], obj.get("from_url"))
        original_url = from_union([from_str, from_none], obj.get("original_url"))
        author_subname = from_union([from_str, from_none], obj.get("author_subname"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        id = from_union([from_int, from_none], obj.get("id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        indent = from_union([from_bool, from_none], obj.get("indent"))
        is_msg_unfurl = from_union([from_bool, from_none], obj.get("is_msg_unfurl"))
        is_reply_unfurl = from_union([from_bool, from_none], obj.get("is_reply_unfurl"))
        is_thread_root_unfurl = from_union([from_bool, from_none], obj.get("is_thread_root_unfurl"))
        is_app_unfurl = from_union([from_bool, from_none], obj.get("is_app_unfurl"))
        app_unfurl_url = from_union([from_str, from_none], obj.get("app_unfurl_url"))
        title = from_union([from_str, from_none], obj.get("title"))
        title_link = from_union([from_str, from_none], obj.get("title_link"))
        text = from_union([from_str, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(Field.from_dict, x), from_none], obj.get("fields"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        thumb_url = from_union([from_str, from_none], obj.get("thumb_url"))
        thumb_width = from_union([from_int, from_none], obj.get("thumb_width"))
        thumb_height = from_union([from_int, from_none], obj.get("thumb_height"))
        video_url = from_union([from_str, from_none], obj.get("video_url"))
        video_html = from_union([from_str, from_none], obj.get("video_html"))
        video_html_width = from_union([from_int, from_none], obj.get("video_html_width"))
        video_html_height = from_union([from_int, from_none], obj.get("video_html_height"))
        footer = from_union([from_str, from_none], obj.get("footer"))
        footer_icon = from_union([from_str, from_none], obj.get("footer_icon"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        mrkdwn_in = from_union([lambda x: from_list(from_str, x), from_none], obj.get("mrkdwn_in"))
        actions = from_union([lambda x: from_list(AttachmentAction.from_dict, x), from_none], obj.get("actions"))
        filename = from_union([from_str, from_none], obj.get("filename"))
        size = from_union([from_int, from_none], obj.get("size"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        url = from_union([from_str, from_none], obj.get("url"))
        metadata = from_union([Metadata.from_dict, from_none], obj.get("metadata"))
        return Attachment(msg_subtype, fallback, callback_id, color, pretext, service_url, service_name, service_icon, author_id, author_name, author_link, author_icon, from_url, original_url, author_subname, channel_id, channel_name, id, bot_id, indent, is_msg_unfurl, is_reply_unfurl, is_thread_root_unfurl, is_app_unfurl, app_unfurl_url, title, title_link, text, fields, image_url, image_width, image_height, image_bytes, thumb_url, thumb_width, thumb_height, video_url, video_html, video_html_width, video_html_height, footer, footer_icon, ts, mrkdwn_in, actions, filename, size, mimetype, url, metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["msg_subtype"] = from_union([from_str, from_none], self.msg_subtype)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["color"] = from_union([from_str, from_none], self.color)
        result["pretext"] = from_union([from_str, from_none], self.pretext)
        result["service_url"] = from_union([from_str, from_none], self.service_url)
        result["service_name"] = from_union([from_str, from_none], self.service_name)
        result["service_icon"] = from_union([from_str, from_none], self.service_icon)
        result["author_id"] = from_union([from_str, from_none], self.author_id)
        result["author_name"] = from_union([from_str, from_none], self.author_name)
        result["author_link"] = from_union([from_str, from_none], self.author_link)
        result["author_icon"] = from_union([from_str, from_none], self.author_icon)
        result["from_url"] = from_union([from_str, from_none], self.from_url)
        result["original_url"] = from_union([from_str, from_none], self.original_url)
        result["author_subname"] = from_union([from_str, from_none], self.author_subname)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["id"] = from_union([from_int, from_none], self.id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["indent"] = from_union([from_bool, from_none], self.indent)
        result["is_msg_unfurl"] = from_union([from_bool, from_none], self.is_msg_unfurl)
        result["is_reply_unfurl"] = from_union([from_bool, from_none], self.is_reply_unfurl)
        result["is_thread_root_unfurl"] = from_union([from_bool, from_none], self.is_thread_root_unfurl)
        result["is_app_unfurl"] = from_union([from_bool, from_none], self.is_app_unfurl)
        result["app_unfurl_url"] = from_union([from_str, from_none], self.app_unfurl_url)
        result["title"] = from_union([from_str, from_none], self.title)
        result["title_link"] = from_union([from_str, from_none], self.title_link)
        result["text"] = from_union([from_str, from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Field, x), x), from_none], self.fields)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["thumb_url"] = from_union([from_str, from_none], self.thumb_url)
        result["thumb_width"] = from_union([from_int, from_none], self.thumb_width)
        result["thumb_height"] = from_union([from_int, from_none], self.thumb_height)
        result["video_url"] = from_union([from_str, from_none], self.video_url)
        result["video_html"] = from_union([from_str, from_none], self.video_html)
        result["video_html_width"] = from_union([from_int, from_none], self.video_html_width)
        result["video_html_height"] = from_union([from_int, from_none], self.video_html_height)
        result["footer"] = from_union([from_str, from_none], self.footer)
        result["footer_icon"] = from_union([from_str, from_none], self.footer_icon)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["mrkdwn_in"] = from_union([lambda x: from_list(from_str, x), from_none], self.mrkdwn_in)
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(AttachmentAction, x), x), from_none], self.actions)
        result["filename"] = from_union([from_str, from_none], self.filename)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["url"] = from_union([from_str, from_none], self.url)
        result["metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
        return result


@dataclass
class Accessory:
    type: Optional[str] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Accessory':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        return Accessory(type, image_url, alt_text, fallback, image_width, image_height, image_bytes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        return result


@dataclass
class Filter:
    include: Optional[List[str]] = None
    exclude_external_shared_channels: Optional[bool] = None
    exclude_bot_users: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Filter':
        assert isinstance(obj, dict)
        include = from_union([lambda x: from_list(from_str, x), from_none], obj.get("include"))
        exclude_external_shared_channels = from_union([from_bool, from_none], obj.get("exclude_external_shared_channels"))
        exclude_bot_users = from_union([from_bool, from_none], obj.get("exclude_bot_users"))
        return Filter(include, exclude_external_shared_channels, exclude_bot_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["include"] = from_union([lambda x: from_list(from_str, x), from_none], self.include)
        result["exclude_external_shared_channels"] = from_union([from_bool, from_none], self.exclude_external_shared_channels)
        result["exclude_bot_users"] = from_union([from_bool, from_none], self.exclude_bot_users)
        return result


@dataclass
class Element:
    type: Optional[str] = None
    text: Optional[Close] = None
    action_id: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[ElementConfirm] = None
    accessibility_label: Optional[str] = None
    placeholder: Optional[Close] = None
    initial_channel: Optional[str] = None
    response_url_enabled: Optional[bool] = None
    focus_on_load: Optional[bool] = None
    max_selected_items: Optional[int] = None
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    filter: Optional[Filter] = None
    initial_date: Optional[str] = None
    initial_option: Optional[InitialOption] = None
    min_query_length: Optional[int] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    initial_user: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Element':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_str, from_none], obj.get("value"))
        style = from_union([from_str, from_none], obj.get("style"))
        confirm = from_union([ElementConfirm.from_dict, from_none], obj.get("confirm"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        placeholder = from_union([Close.from_dict, from_none], obj.get("placeholder"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        response_url_enabled = from_union([from_bool, from_none], obj.get("response_url_enabled"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        max_selected_items = from_union([from_int, from_none], obj.get("max_selected_items"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        default_to_current_conversation = from_union([from_bool, from_none], obj.get("default_to_current_conversation"))
        filter = from_union([Filter.from_dict, from_none], obj.get("filter"))
        initial_date = from_union([from_str, from_none], obj.get("initial_date"))
        initial_option = from_union([InitialOption.from_dict, from_none], obj.get("initial_option"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        return Element(type, text, action_id, url, value, style, confirm, accessibility_label, placeholder, initial_channel, response_url_enabled, focus_on_load, max_selected_items, initial_conversation, default_to_current_conversation, filter, initial_date, initial_option, min_query_length, image_url, alt_text, fallback, image_width, image_height, image_bytes, initial_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["value"] = from_union([from_str, from_none], self.value)
        result["style"] = from_union([from_str, from_none], self.style)
        result["confirm"] = from_union([lambda x: to_class(ElementConfirm, x), from_none], self.confirm)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["placeholder"] = from_union([lambda x: to_class(Close, x), from_none], self.placeholder)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["response_url_enabled"] = from_union([from_bool, from_none], self.response_url_enabled)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["max_selected_items"] = from_union([from_int, from_none], self.max_selected_items)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["default_to_current_conversation"] = from_union([from_bool, from_none], self.default_to_current_conversation)
        result["filter"] = from_union([lambda x: to_class(Filter, x), from_none], self.filter)
        result["initial_date"] = from_union([from_str, from_none], self.initial_date)
        result["initial_option"] = from_union([lambda x: to_class(InitialOption, x), from_none], self.initial_option)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        return result


@dataclass
class Block:
    type: Optional[str] = None
    elements: Optional[List[Element]] = None
    block_id: Optional[str] = None
    fallback: Optional[str] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    alt_text: Optional[str] = None
    title: Optional[Close] = None
    text: Optional[Close] = None
    fields: Optional[List[Close]] = None
    accessory: Optional[Accessory] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Block':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(Element.from_dict, x), from_none], obj.get("elements"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        title = from_union([Close.from_dict, from_none], obj.get("title"))
        text = from_union([Close.from_dict, from_none], obj.get("text"))
        fields = from_union([lambda x: from_list(Close.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
        return Block(type, elements, block_id, fallback, image_url, image_width, image_height, image_bytes, alt_text, title, text, fields, accessory)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(Element, x), x), from_none], self.elements)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["title"] = from_union([lambda x: to_class(Close, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(Close, x), from_none], self.text)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Close, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
        return result


@dataclass
class BotProfileIcons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfileIcons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return BotProfileIcons(image_36, image_48, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class BotProfile:
    id: Optional[str] = None
    deleted: Optional[bool] = None
    name: Optional[str] = None
    updated: Optional[int] = None
    app_id: Optional[str] = None
    icons: Optional[BotProfileIcons] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfile':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        icons = from_union([BotProfileIcons.from_dict, from_none], obj.get("icons"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return BotProfile(id, deleted, name, updated, app_id, icons, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["icons"] = from_union([lambda x: to_class(BotProfileIcons, x), from_none], self.icons)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class Comment:
    id: Optional[str] = None
    name: Optional[str] = None
    title: Optional[str] = None
    created: Optional[str] = None
    timestamp: Optional[str] = None
    user: Optional[str] = None
    username: Optional[str] = None
    is_intro: Optional[bool] = None
    is_public: Optional[bool] = None
    is_starred: Optional[bool] = None
    public_url_shared: Optional[bool] = None
    url_private: Optional[str] = None
    url_private_download: Optional[bool] = None
    permalink: Optional[str] = None
    permalink_public: Optional[bool] = None
    edit_link: Optional[str] = None
    preview: Optional[str] = None
    preview_highlight: Optional[str] = None
    lines: Optional[int] = None
    lines_more: Optional[int] = None
    preview_is_truncated: Optional[bool] = None
    has_rich_preview: Optional[bool] = None
    media_display_type: Optional[str] = None
    mimetype: Optional[str] = None
    filetype: Optional[str] = None
    pretty_type: Optional[str] = None
    is_external: Optional[bool] = None
    external_type: Optional[str] = None
    editable: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    size: Optional[int] = None
    mode: Optional[str] = None
    comment: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Comment':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        created = from_union([from_str, from_none], obj.get("created"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        user = from_union([from_str, from_none], obj.get("user"))
        username = from_union([from_str, from_none], obj.get("username"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        is_public = from_union([from_bool, from_none], obj.get("is_public"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        public_url_shared = from_union([from_bool, from_none], obj.get("public_url_shared"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        url_private_download = from_union([from_bool, from_none], obj.get("url_private_download"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        permalink_public = from_union([from_bool, from_none], obj.get("permalink_public"))
        edit_link = from_union([from_str, from_none], obj.get("edit_link"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        preview_highlight = from_union([from_str, from_none], obj.get("preview_highlight"))
        lines = from_union([from_int, from_none], obj.get("lines"))
        lines_more = from_union([from_int, from_none], obj.get("lines_more"))
        preview_is_truncated = from_union([from_bool, from_none], obj.get("preview_is_truncated"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        media_display_type = from_union([from_str, from_none], obj.get("media_display_type"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        size = from_union([from_int, from_none], obj.get("size"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        return Comment(id, name, title, created, timestamp, user, username, is_intro, is_public, is_starred, public_url_shared, url_private, url_private_download, permalink, permalink_public, edit_link, preview, preview_highlight, lines, lines_more, preview_is_truncated, has_rich_preview, media_display_type, mimetype, filetype, pretty_type, is_external, external_type, editable, display_as_bot, size, mode, comment)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["created"] = from_union([from_str, from_none], self.created)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        result["user"] = from_union([from_str, from_none], self.user)
        result["username"] = from_union([from_str, from_none], self.username)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        result["is_public"] = from_union([from_bool, from_none], self.is_public)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["public_url_shared"] = from_union([from_bool, from_none], self.public_url_shared)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["url_private_download"] = from_union([from_bool, from_none], self.url_private_download)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["permalink_public"] = from_union([from_bool, from_none], self.permalink_public)
        result["edit_link"] = from_union([from_str, from_none], self.edit_link)
        result["preview"] = from_union([from_str, from_none], self.preview)
        result["preview_highlight"] = from_union([from_str, from_none], self.preview_highlight)
        result["lines"] = from_union([from_int, from_none], self.lines)
        result["lines_more"] = from_union([from_int, from_none], self.lines_more)
        result["preview_is_truncated"] = from_union([from_bool, from_none], self.preview_is_truncated)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["media_display_type"] = from_union([from_str, from_none], self.media_display_type)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["comment"] = from_union([from_str, from_none], self.comment)
        return result


@dataclass
class Edited:
    user: Optional[str] = None
    ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Edited':
        assert isinstance(obj, dict)
        user = from_union([from_str, from_none], obj.get("user"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        return Edited(user, ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = from_union([from_str, from_none], self.user)
        result["ts"] = from_union([from_str, from_none], self.ts)
        return result


@dataclass
class Headers:
    date: Optional[str] = None
    in_reply_to: Optional[str] = None
    reply_to: Optional[str] = None
    message_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Headers':
        assert isinstance(obj, dict)
        date = from_union([from_str, from_none], obj.get("date"))
        in_reply_to = from_union([from_str, from_none], obj.get("in_reply_to"))
        reply_to = from_union([from_str, from_none], obj.get("reply_to"))
        message_id = from_union([from_str, from_none], obj.get("message_id"))
        return Headers(date, in_reply_to, reply_to, message_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["date"] = from_union([from_str, from_none], self.date)
        result["in_reply_to"] = from_union([from_str, from_none], self.in_reply_to)
        result["reply_to"] = from_union([from_str, from_none], self.reply_to)
        result["message_id"] = from_union([from_str, from_none], self.message_id)
        return result


@dataclass
class InitialComment:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    user: Optional[str] = None
    comment: Optional[str] = None
    channel: Optional[str] = None
    is_intro: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialComment':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        user = from_union([from_str, from_none], obj.get("user"))
        comment = from_union([from_str, from_none], obj.get("comment"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        return InitialComment(id, created, timestamp, user, comment, channel, is_intro)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["user"] = from_union([from_str, from_none], self.user)
        result["comment"] = from_union([from_str, from_none], self.comment)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        return result


@dataclass
class Private:
    share_user_id: Optional[str] = None
    reply_users: Optional[List[str]] = None
    reply_users_count: Optional[int] = None
    reply_count: Optional[int] = None
    ts: Optional[str] = None
    thread_ts: Optional[str] = None
    latest_reply: Optional[str] = None
    channel_name: Optional[str] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Private':
        assert isinstance(obj, dict)
        share_user_id = from_union([from_str, from_none], obj.get("share_user_id"))
        reply_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return Private(share_user_id, reply_users, reply_users_count, reply_count, ts, thread_ts, latest_reply, channel_name, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["share_user_id"] = from_union([from_str, from_none], self.share_user_id)
        result["reply_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class Shares:
    public: Optional[Dict[str, List[Private]]] = None
    private: Optional[Dict[str, List[Private]]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Shares':
        assert isinstance(obj, dict)
        public = from_union([lambda x: from_dict(lambda x: from_list(Private.from_dict, x), x), from_none], obj.get("public"))
        private = from_union([lambda x: from_dict(lambda x: from_list(Private.from_dict, x), x), from_none], obj.get("private"))
        return Shares(public, private)

    def to_dict(self) -> dict:
        result: dict = {}
        result["public"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Private, x), x), x), from_none], self.public)
        result["private"] = from_union([lambda x: from_dict(lambda x: from_list(lambda x: to_class(Private, x), x), x), from_none], self.private)
        return result


@dataclass
class File:
    id: Optional[str] = None
    created: Optional[int] = None
    timestamp: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    subject: Optional[str] = None
    mimetype: Optional[str] = None
    filetype: Optional[str] = None
    pretty_type: Optional[str] = None
    user: Optional[str] = None
    mode: Optional[str] = None
    editable: Optional[bool] = None
    non_owner_editable: Optional[bool] = None
    editor: Optional[str] = None
    last_editor: Optional[str] = None
    updated: Optional[int] = None
    original_attachment_count: Optional[int] = None
    is_external: Optional[bool] = None
    external_type: Optional[str] = None
    external_id: Optional[str] = None
    external_url: Optional[str] = None
    username: Optional[str] = None
    size: Optional[int] = None
    url_private: Optional[str] = None
    url_private_download: Optional[str] = None
    app_id: Optional[str] = None
    app_name: Optional[str] = None
    thumb_64: Optional[str] = None
    thumb_64__gif: Optional[str] = None
    thumb_64__w: Optional[str] = None
    thumb_64__h: Optional[str] = None
    thumb_80: Optional[str] = None
    thumb_80__gif: Optional[str] = None
    thumb_80__w: Optional[str] = None
    thumb_80__h: Optional[str] = None
    thumb_160: Optional[str] = None
    thumb_160__gif: Optional[str] = None
    thumb_160__w: Optional[str] = None
    thumb_160__h: Optional[str] = None
    thumb_360: Optional[str] = None
    thumb_360__gif: Optional[str] = None
    thumb_360__w: Optional[str] = None
    thumb_360__h: Optional[str] = None
    thumb_480: Optional[str] = None
    thumb_480__gif: Optional[str] = None
    thumb_480__w: Optional[str] = None
    thumb_480__h: Optional[str] = None
    thumb_720: Optional[str] = None
    thumb_720__gif: Optional[str] = None
    thumb_720__w: Optional[str] = None
    thumb_720__h: Optional[str] = None
    thumb_800: Optional[str] = None
    thumb_800__gif: Optional[str] = None
    thumb_800__w: Optional[str] = None
    thumb_800__h: Optional[str] = None
    thumb_960: Optional[str] = None
    thumb_960__gif: Optional[str] = None
    thumb_960__w: Optional[str] = None
    thumb_960__h: Optional[str] = None
    thumb_1024: Optional[str] = None
    thumb_1024__gif: Optional[str] = None
    thumb_1024__w: Optional[str] = None
    thumb_1024__h: Optional[str] = None
    thumb_video: Optional[str] = None
    thumb_gif: Optional[str] = None
    thumb_pdf: Optional[str] = None
    thumb_pdf_w: Optional[str] = None
    thumb_pdf_h: Optional[str] = None
    thumb_tiny: Optional[str] = None
    converted_pdf: Optional[str] = None
    image_exif_rotation: Optional[int] = None
    original_w: Optional[str] = None
    original_h: Optional[str] = None
    deanimate: Optional[str] = None
    deanimate_gif: Optional[str] = None
    pjpeg: Optional[str] = None
    permalink: Optional[str] = None
    permalink_public: Optional[str] = None
    edit_link: Optional[str] = None
    has_rich_preview: Optional[bool] = None
    media_display_type: Optional[str] = None
    preview_is_truncated: Optional[bool] = None
    preview: Optional[str] = None
    preview_highlight: Optional[str] = None
    plain_text: Optional[str] = None
    preview_plain_text: Optional[str] = None
    has_more: Optional[bool] = None
    sent_to_self: Optional[bool] = None
    lines: Optional[int] = None
    lines_more: Optional[int] = None
    is_public: Optional[bool] = None
    public_url_shared: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    shares: Optional[Shares] = None
    channel_actions_ts: Optional[str] = None
    channel_actions_count: Optional[int] = None
    headers: Optional[Headers] = None
    simplified_html: Optional[str] = None
    bot_id: Optional[str] = None
    initial_comment: Optional[InitialComment] = None
    num_stars: Optional[int] = None
    is_starred: Optional[bool] = None
    comments_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        timestamp = from_union([from_int, from_none], obj.get("timestamp"))
        name = from_union([from_str, from_none], obj.get("name"))
        title = from_union([from_str, from_none], obj.get("title"))
        subject = from_union([from_str, from_none], obj.get("subject"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        pretty_type = from_union([from_str, from_none], obj.get("pretty_type"))
        user = from_union([from_str, from_none], obj.get("user"))
        mode = from_union([from_str, from_none], obj.get("mode"))
        editable = from_union([from_bool, from_none], obj.get("editable"))
        non_owner_editable = from_union([from_bool, from_none], obj.get("non_owner_editable"))
        editor = from_union([from_str, from_none], obj.get("editor"))
        last_editor = from_union([from_str, from_none], obj.get("last_editor"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        original_attachment_count = from_union([from_int, from_none], obj.get("original_attachment_count"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        external_type = from_union([from_str, from_none], obj.get("external_type"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        external_url = from_union([from_str, from_none], obj.get("external_url"))
        username = from_union([from_str, from_none], obj.get("username"))
        size = from_union([from_int, from_none], obj.get("size"))
        url_private = from_union([from_str, from_none], obj.get("url_private"))
        url_private_download = from_union([from_str, from_none], obj.get("url_private_download"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        app_name = from_union([from_str, from_none], obj.get("app_name"))
        thumb_64 = from_union([from_str, from_none], obj.get("thumb_64"))
        thumb_64__gif = from_union([from_str, from_none], obj.get("thumb_64_gif"))
        thumb_64__w = from_union([from_str, from_none], obj.get("thumb_64_w"))
        thumb_64__h = from_union([from_str, from_none], obj.get("thumb_64_h"))
        thumb_80 = from_union([from_str, from_none], obj.get("thumb_80"))
        thumb_80__gif = from_union([from_str, from_none], obj.get("thumb_80_gif"))
        thumb_80__w = from_union([from_str, from_none], obj.get("thumb_80_w"))
        thumb_80__h = from_union([from_str, from_none], obj.get("thumb_80_h"))
        thumb_160 = from_union([from_str, from_none], obj.get("thumb_160"))
        thumb_160__gif = from_union([from_str, from_none], obj.get("thumb_160_gif"))
        thumb_160__w = from_union([from_str, from_none], obj.get("thumb_160_w"))
        thumb_160__h = from_union([from_str, from_none], obj.get("thumb_160_h"))
        thumb_360 = from_union([from_str, from_none], obj.get("thumb_360"))
        thumb_360__gif = from_union([from_str, from_none], obj.get("thumb_360_gif"))
        thumb_360__w = from_union([from_str, from_none], obj.get("thumb_360_w"))
        thumb_360__h = from_union([from_str, from_none], obj.get("thumb_360_h"))
        thumb_480 = from_union([from_str, from_none], obj.get("thumb_480"))
        thumb_480__gif = from_union([from_str, from_none], obj.get("thumb_480_gif"))
        thumb_480__w = from_union([from_str, from_none], obj.get("thumb_480_w"))
        thumb_480__h = from_union([from_str, from_none], obj.get("thumb_480_h"))
        thumb_720 = from_union([from_str, from_none], obj.get("thumb_720"))
        thumb_720__gif = from_union([from_str, from_none], obj.get("thumb_720_gif"))
        thumb_720__w = from_union([from_str, from_none], obj.get("thumb_720_w"))
        thumb_720__h = from_union([from_str, from_none], obj.get("thumb_720_h"))
        thumb_800 = from_union([from_str, from_none], obj.get("thumb_800"))
        thumb_800__gif = from_union([from_str, from_none], obj.get("thumb_800_gif"))
        thumb_800__w = from_union([from_str, from_none], obj.get("thumb_800_w"))
        thumb_800__h = from_union([from_str, from_none], obj.get("thumb_800_h"))
        thumb_960 = from_union([from_str, from_none], obj.get("thumb_960"))
        thumb_960__gif = from_union([from_str, from_none], obj.get("thumb_960_gif"))
        thumb_960__w = from_union([from_str, from_none], obj.get("thumb_960_w"))
        thumb_960__h = from_union([from_str, from_none], obj.get("thumb_960_h"))
        thumb_1024 = from_union([from_str, from_none], obj.get("thumb_1024"))
        thumb_1024__gif = from_union([from_str, from_none], obj.get("thumb_1024_gif"))
        thumb_1024__w = from_union([from_str, from_none], obj.get("thumb_1024_w"))
        thumb_1024__h = from_union([from_str, from_none], obj.get("thumb_1024_h"))
        thumb_video = from_union([from_str, from_none], obj.get("thumb_video"))
        thumb_gif = from_union([from_str, from_none], obj.get("thumb_gif"))
        thumb_pdf = from_union([from_str, from_none], obj.get("thumb_pdf"))
        thumb_pdf_w = from_union([from_str, from_none], obj.get("thumb_pdf_w"))
        thumb_pdf_h = from_union([from_str, from_none], obj.get("thumb_pdf_h"))
        thumb_tiny = from_union([from_str, from_none], obj.get("thumb_tiny"))
        converted_pdf = from_union([from_str, from_none], obj.get("converted_pdf"))
        image_exif_rotation = from_union([from_int, from_none], obj.get("image_exif_rotation"))
        original_w = from_union([from_str, from_none], obj.get("original_w"))
        original_h = from_union([from_str, from_none], obj.get("original_h"))
        deanimate = from_union([from_str, from_none], obj.get("deanimate"))
        deanimate_gif = from_union([from_str, from_none], obj.get("deanimate_gif"))
        pjpeg = from_union([from_str, from_none], obj.get("pjpeg"))
        permalink = from_union([from_str, from_none], obj.get("permalink"))
        permalink_public = from_union([from_str, from_none], obj.get("permalink_public"))
        edit_link = from_union([from_str, from_none], obj.get("edit_link"))
        has_rich_preview = from_union([from_bool, from_none], obj.get("has_rich_preview"))
        media_display_type = from_union([from_str, from_none], obj.get("media_display_type"))
        preview_is_truncated = from_union([from_bool, from_none], obj.get("preview_is_truncated"))
        preview = from_union([from_str, from_none], obj.get("preview"))
        preview_highlight = from_union([from_str, from_none], obj.get("preview_highlight"))
        plain_text = from_union([from_str, from_none], obj.get("plain_text"))
        preview_plain_text = from_union([from_str, from_none], obj.get("preview_plain_text"))
        has_more = from_union([from_bool, from_none], obj.get("has_more"))
        sent_to_self = from_union([from_bool, from_none], obj.get("sent_to_self"))
        lines = from_union([from_int, from_none], obj.get("lines"))
        lines_more = from_union([from_int, from_none], obj.get("lines_more"))
        is_public = from_union([from_bool, from_none], obj.get("is_public"))
        public_url_shared = from_union([from_bool, from_none], obj.get("public_url_shared"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        shares = from_union([Shares.from_dict, from_none], obj.get("shares"))
        channel_actions_ts = from_union([from_str, from_none], obj.get("channel_actions_ts"))
        channel_actions_count = from_union([from_int, from_none], obj.get("channel_actions_count"))
        headers = from_union([Headers.from_dict, from_none], obj.get("headers"))
        simplified_html = from_union([from_str, from_none], obj.get("simplified_html"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        initial_comment = from_union([InitialComment.from_dict, from_none], obj.get("initial_comment"))
        num_stars = from_union([from_int, from_none], obj.get("num_stars"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        return File(id, created, timestamp, name, title, subject, mimetype, filetype, pretty_type, user, mode, editable, non_owner_editable, editor, last_editor, updated, original_attachment_count, is_external, external_type, external_id, external_url, username, size, url_private, url_private_download, app_id, app_name, thumb_64, thumb_64__gif, thumb_64__w, thumb_64__h, thumb_80, thumb_80__gif, thumb_80__w, thumb_80__h, thumb_160, thumb_160__gif, thumb_160__w, thumb_160__h, thumb_360, thumb_360__gif, thumb_360__w, thumb_360__h, thumb_480, thumb_480__gif, thumb_480__w, thumb_480__h, thumb_720, thumb_720__gif, thumb_720__w, thumb_720__h, thumb_800, thumb_800__gif, thumb_800__w, thumb_800__h, thumb_960, thumb_960__gif, thumb_960__w, thumb_960__h, thumb_1024, thumb_1024__gif, thumb_1024__w, thumb_1024__h, thumb_video, thumb_gif, thumb_pdf, thumb_pdf_w, thumb_pdf_h, thumb_tiny, converted_pdf, image_exif_rotation, original_w, original_h, deanimate, deanimate_gif, pjpeg, permalink, permalink_public, edit_link, has_rich_preview, media_display_type, preview_is_truncated, preview, preview_highlight, plain_text, preview_plain_text, has_more, sent_to_self, lines, lines_more, is_public, public_url_shared, display_as_bot, shares, channel_actions_ts, channel_actions_count, headers, simplified_html, bot_id, initial_comment, num_stars, is_starred, comments_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["timestamp"] = from_union([from_int, from_none], self.timestamp)
        result["name"] = from_union([from_str, from_none], self.name)
        result["title"] = from_union([from_str, from_none], self.title)
        result["subject"] = from_union([from_str, from_none], self.subject)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["pretty_type"] = from_union([from_str, from_none], self.pretty_type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["mode"] = from_union([from_str, from_none], self.mode)
        result["editable"] = from_union([from_bool, from_none], self.editable)
        result["non_owner_editable"] = from_union([from_bool, from_none], self.non_owner_editable)
        result["editor"] = from_union([from_str, from_none], self.editor)
        result["last_editor"] = from_union([from_str, from_none], self.last_editor)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["original_attachment_count"] = from_union([from_int, from_none], self.original_attachment_count)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["external_type"] = from_union([from_str, from_none], self.external_type)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["external_url"] = from_union([from_str, from_none], self.external_url)
        result["username"] = from_union([from_str, from_none], self.username)
        result["size"] = from_union([from_int, from_none], self.size)
        result["url_private"] = from_union([from_str, from_none], self.url_private)
        result["url_private_download"] = from_union([from_str, from_none], self.url_private_download)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["app_name"] = from_union([from_str, from_none], self.app_name)
        result["thumb_64"] = from_union([from_str, from_none], self.thumb_64)
        result["thumb_64_gif"] = from_union([from_str, from_none], self.thumb_64__gif)
        result["thumb_64_w"] = from_union([from_str, from_none], self.thumb_64__w)
        result["thumb_64_h"] = from_union([from_str, from_none], self.thumb_64__h)
        result["thumb_80"] = from_union([from_str, from_none], self.thumb_80)
        result["thumb_80_gif"] = from_union([from_str, from_none], self.thumb_80__gif)
        result["thumb_80_w"] = from_union([from_str, from_none], self.thumb_80__w)
        result["thumb_80_h"] = from_union([from_str, from_none], self.thumb_80__h)
        result["thumb_160"] = from_union([from_str, from_none], self.thumb_160)
        result["thumb_160_gif"] = from_union([from_str, from_none], self.thumb_160__gif)
        result["thumb_160_w"] = from_union([from_str, from_none], self.thumb_160__w)
        result["thumb_160_h"] = from_union([from_str, from_none], self.thumb_160__h)
        result["thumb_360"] = from_union([from_str, from_none], self.thumb_360)
        result["thumb_360_gif"] = from_union([from_str, from_none], self.thumb_360__gif)
        result["thumb_360_w"] = from_union([from_str, from_none], self.thumb_360__w)
        result["thumb_360_h"] = from_union([from_str, from_none], self.thumb_360__h)
        result["thumb_480"] = from_union([from_str, from_none], self.thumb_480)
        result["thumb_480_gif"] = from_union([from_str, from_none], self.thumb_480__gif)
        result["thumb_480_w"] = from_union([from_str, from_none], self.thumb_480__w)
        result["thumb_480_h"] = from_union([from_str, from_none], self.thumb_480__h)
        result["thumb_720"] = from_union([from_str, from_none], self.thumb_720)
        result["thumb_720_gif"] = from_union([from_str, from_none], self.thumb_720__gif)
        result["thumb_720_w"] = from_union([from_str, from_none], self.thumb_720__w)
        result["thumb_720_h"] = from_union([from_str, from_none], self.thumb_720__h)
        result["thumb_800"] = from_union([from_str, from_none], self.thumb_800)
        result["thumb_800_gif"] = from_union([from_str, from_none], self.thumb_800__gif)
        result["thumb_800_w"] = from_union([from_str, from_none], self.thumb_800__w)
        result["thumb_800_h"] = from_union([from_str, from_none], self.thumb_800__h)
        result["thumb_960"] = from_union([from_str, from_none], self.thumb_960)
        result["thumb_960_gif"] = from_union([from_str, from_none], self.thumb_960__gif)
        result["thumb_960_w"] = from_union([from_str, from_none], self.thumb_960__w)
        result["thumb_960_h"] = from_union([from_str, from_none], self.thumb_960__h)
        result["thumb_1024"] = from_union([from_str, from_none], self.thumb_1024)
        result["thumb_1024_gif"] = from_union([from_str, from_none], self.thumb_1024__gif)
        result["thumb_1024_w"] = from_union([from_str, from_none], self.thumb_1024__w)
        result["thumb_1024_h"] = from_union([from_str, from_none], self.thumb_1024__h)
        result["thumb_video"] = from_union([from_str, from_none], self.thumb_video)
        result["thumb_gif"] = from_union([from_str, from_none], self.thumb_gif)
        result["thumb_pdf"] = from_union([from_str, from_none], self.thumb_pdf)
        result["thumb_pdf_w"] = from_union([from_str, from_none], self.thumb_pdf_w)
        result["thumb_pdf_h"] = from_union([from_str, from_none], self.thumb_pdf_h)
        result["thumb_tiny"] = from_union([from_str, from_none], self.thumb_tiny)
        result["converted_pdf"] = from_union([from_str, from_none], self.converted_pdf)
        result["image_exif_rotation"] = from_union([from_int, from_none], self.image_exif_rotation)
        result["original_w"] = from_union([from_str, from_none], self.original_w)
        result["original_h"] = from_union([from_str, from_none], self.original_h)
        result["deanimate"] = from_union([from_str, from_none], self.deanimate)
        result["deanimate_gif"] = from_union([from_str, from_none], self.deanimate_gif)
        result["pjpeg"] = from_union([from_str, from_none], self.pjpeg)
        result["permalink"] = from_union([from_str, from_none], self.permalink)
        result["permalink_public"] = from_union([from_str, from_none], self.permalink_public)
        result["edit_link"] = from_union([from_str, from_none], self.edit_link)
        result["has_rich_preview"] = from_union([from_bool, from_none], self.has_rich_preview)
        result["media_display_type"] = from_union([from_str, from_none], self.media_display_type)
        result["preview_is_truncated"] = from_union([from_bool, from_none], self.preview_is_truncated)
        result["preview"] = from_union([from_str, from_none], self.preview)
        result["preview_highlight"] = from_union([from_str, from_none], self.preview_highlight)
        result["plain_text"] = from_union([from_str, from_none], self.plain_text)
        result["preview_plain_text"] = from_union([from_str, from_none], self.preview_plain_text)
        result["has_more"] = from_union([from_bool, from_none], self.has_more)
        result["sent_to_self"] = from_union([from_bool, from_none], self.sent_to_self)
        result["lines"] = from_union([from_int, from_none], self.lines)
        result["lines_more"] = from_union([from_int, from_none], self.lines_more)
        result["is_public"] = from_union([from_bool, from_none], self.is_public)
        result["public_url_shared"] = from_union([from_bool, from_none], self.public_url_shared)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["shares"] = from_union([lambda x: to_class(Shares, x), from_none], self.shares)
        result["channel_actions_ts"] = from_union([from_str, from_none], self.channel_actions_ts)
        result["channel_actions_count"] = from_union([from_int, from_none], self.channel_actions_count)
        result["headers"] = from_union([lambda x: to_class(Headers, x), from_none], self.headers)
        result["simplified_html"] = from_union([from_str, from_none], self.simplified_html)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["initial_comment"] = from_union([lambda x: to_class(InitialComment, x), from_none], self.initial_comment)
        result["num_stars"] = from_union([from_int, from_none], self.num_stars)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        return result


@dataclass
class MessageIcons:
    emoji: Optional[str] = None
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_64: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'MessageIcons':
        assert isinstance(obj, dict)
        emoji = from_union([from_str, from_none], obj.get("emoji"))
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_64 = from_union([from_str, from_none], obj.get("image_64"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return MessageIcons(emoji, image_36, image_48, image_64, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emoji"] = from_union([from_str, from_none], self.emoji)
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_64"] = from_union([from_str, from_none], self.image_64)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class Reaction:
    name: Optional[str] = None
    count: Optional[int] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reaction':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        count = from_union([from_int, from_none], obj.get("count"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Reaction(name, count, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["count"] = from_union([from_int, from_none], self.count)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class Root:
    text: Optional[str] = None
    user: Optional[str] = None
    parent_user_id: Optional[str] = None
    username: Optional[str] = None
    team: Optional[str] = None
    bot_id: Optional[str] = None
    mrkdwn: Optional[bool] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    thread_ts: Optional[str] = None
    icons: Optional[MessageIcons] = None
    bot_profile: Optional[BotProfile] = None
    edited: Optional[Edited] = None
    reply_count: Optional[int] = None
    reply_users_count: Optional[int] = None
    latest_reply: Optional[str] = None
    subscribed: Optional[bool] = None
    last_read: Optional[str] = None
    unread_count: Optional[int] = None
    ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        username = from_union([from_str, from_none], obj.get("username"))
        team = from_union([from_str, from_none], obj.get("team"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        mrkdwn = from_union([from_bool, from_none], obj.get("mrkdwn"))
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        icons = from_union([MessageIcons.from_dict, from_none], obj.get("icons"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        subscribed = from_union([from_bool, from_none], obj.get("subscribed"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        unread_count = from_union([from_int, from_none], obj.get("unread_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        return Root(text, user, parent_user_id, username, team, bot_id, mrkdwn, type, subtype, thread_ts, icons, bot_profile, edited, reply_count, reply_users_count, latest_reply, subscribed, last_read, unread_count, ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        result["username"] = from_union([from_str, from_none], self.username)
        result["team"] = from_union([from_str, from_none], self.team)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["mrkdwn"] = from_union([from_bool, from_none], self.mrkdwn)
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["icons"] = from_union([lambda x: to_class(MessageIcons, x), from_none], self.icons)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["subscribed"] = from_union([from_bool, from_none], self.subscribed)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["unread_count"] = from_union([from_int, from_none], self.unread_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        return result


@dataclass
class Message:
    type: Optional[str] = None
    subtype: Optional[str] = None
    team: Optional[str] = None
    channel: Optional[str] = None
    user: Optional[str] = None
    username: Optional[str] = None
    text: Optional[str] = None
    blocks: Optional[List[Block]] = None
    attachments: Optional[List[Attachment]] = None
    ts: Optional[str] = None
    thread_ts: Optional[str] = None
    is_intro: Optional[bool] = None
    is_starred: Optional[bool] = None
    wibblr: Optional[bool] = None
    pinned_to: Optional[List[str]] = None
    reactions: Optional[List[Reaction]] = None
    bot_id: Optional[str] = None
    bot_link: Optional[str] = None
    display_as_bot: Optional[bool] = None
    bot_profile: Optional[BotProfile] = None
    icons: Optional[MessageIcons] = None
    file: Optional[File] = None
    files: Optional[List[File]] = None
    upload: Optional[bool] = None
    parent_user_id: Optional[str] = None
    inviter: Optional[str] = None
    client_msg_id: Optional[str] = None
    comment: Optional[Comment] = None
    topic: Optional[str] = None
    purpose: Optional[str] = None
    edited: Optional[Edited] = None
    unfurl_links: Optional[bool] = None
    unfurl_media: Optional[bool] = None
    is_thread_broadcast: Optional[bool] = None
    is_locked: Optional[bool] = None
    reply_count: Optional[int] = None
    reply_users: Optional[List[str]] = None
    reply_users_count: Optional[int] = None
    latest_reply: Optional[str] = None
    subscribed: Optional[bool] = None
    hidden: Optional[bool] = None
    last_read: Optional[str] = None
    root: Optional[Root] = None
    item_type: Optional[str] = None
    item: Optional[Comment] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        team = from_union([from_str, from_none], obj.get("team"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        user = from_union([from_str, from_none], obj.get("user"))
        username = from_union([from_str, from_none], obj.get("username"))
        text = from_union([from_str, from_none], obj.get("text"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        attachments = from_union([lambda x: from_list(Attachment.from_dict, x), from_none], obj.get("attachments"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        is_intro = from_union([from_bool, from_none], obj.get("is_intro"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        wibblr = from_union([from_bool, from_none], obj.get("wibblr"))
        pinned_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pinned_to"))
        reactions = from_union([lambda x: from_list(Reaction.from_dict, x), from_none], obj.get("reactions"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        bot_link = from_union([from_str, from_none], obj.get("bot_link"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        icons = from_union([MessageIcons.from_dict, from_none], obj.get("icons"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        files = from_union([lambda x: from_list(File.from_dict, x), from_none], obj.get("files"))
        upload = from_union([from_bool, from_none], obj.get("upload"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        inviter = from_union([from_str, from_none], obj.get("inviter"))
        client_msg_id = from_union([from_str, from_none], obj.get("client_msg_id"))
        comment = from_union([Comment.from_dict, from_none], obj.get("comment"))
        topic = from_union([from_str, from_none], obj.get("topic"))
        purpose = from_union([from_str, from_none], obj.get("purpose"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        unfurl_links = from_union([from_bool, from_none], obj.get("unfurl_links"))
        unfurl_media = from_union([from_bool, from_none], obj.get("unfurl_media"))
        is_thread_broadcast = from_union([from_bool, from_none], obj.get("is_thread_broadcast"))
        is_locked = from_union([from_bool, from_none], obj.get("is_locked"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        reply_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        subscribed = from_union([from_bool, from_none], obj.get("subscribed"))
        hidden = from_union([from_bool, from_none], obj.get("hidden"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        root = from_union([Root.from_dict, from_none], obj.get("root"))
        item_type = from_union([from_str, from_none], obj.get("item_type"))
        item = from_union([Comment.from_dict, from_none], obj.get("item"))
        return Message(type, subtype, team, channel, user, username, text, blocks, attachments, ts, thread_ts, is_intro, is_starred, wibblr, pinned_to, reactions, bot_id, bot_link, display_as_bot, bot_profile, icons, file, files, upload, parent_user_id, inviter, client_msg_id, comment, topic, purpose, edited, unfurl_links, unfurl_media, is_thread_broadcast, is_locked, reply_count, reply_users, reply_users_count, latest_reply, subscribed, hidden, last_read, root, item_type, item)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["team"] = from_union([from_str, from_none], self.team)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["user"] = from_union([from_str, from_none], self.user)
        result["username"] = from_union([from_str, from_none], self.username)
        result["text"] = from_union([from_str, from_none], self.text)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["attachments"] = from_union([lambda x: from_list(lambda x: to_class(Attachment, x), x), from_none], self.attachments)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["is_intro"] = from_union([from_bool, from_none], self.is_intro)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["wibblr"] = from_union([from_bool, from_none], self.wibblr)
        result["pinned_to"] = from_union([lambda x: from_list(from_str, x), from_none], self.pinned_to)
        result["reactions"] = from_union([lambda x: from_list(lambda x: to_class(Reaction, x), x), from_none], self.reactions)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["bot_link"] = from_union([from_str, from_none], self.bot_link)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["icons"] = from_union([lambda x: to_class(MessageIcons, x), from_none], self.icons)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        result["files"] = from_union([lambda x: from_list(lambda x: to_class(File, x), x), from_none], self.files)
        result["upload"] = from_union([from_bool, from_none], self.upload)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        result["inviter"] = from_union([from_str, from_none], self.inviter)
        result["client_msg_id"] = from_union([from_str, from_none], self.client_msg_id)
        result["comment"] = from_union([lambda x: to_class(Comment, x), from_none], self.comment)
        result["topic"] = from_union([from_str, from_none], self.topic)
        result["purpose"] = from_union([from_str, from_none], self.purpose)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        result["unfurl_links"] = from_union([from_bool, from_none], self.unfurl_links)
        result["unfurl_media"] = from_union([from_bool, from_none], self.unfurl_media)
        result["is_thread_broadcast"] = from_union([from_bool, from_none], self.is_thread_broadcast)
        result["is_locked"] = from_union([from_bool, from_none], self.is_locked)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["reply_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["subscribed"] = from_union([from_bool, from_none], self.subscribed)
        result["hidden"] = from_union([from_bool, from_none], self.hidden)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["root"] = from_union([lambda x: to_class(Root, x), from_none], self.root)
        result["item_type"] = from_union([from_str, from_none], self.item_type)
        result["item"] = from_union([lambda x: to_class(Comment, x), from_none], self.item)
        return result


@dataclass
class State:
    pass

    @staticmethod
    def from_dict(obj: Any) -> 'State':
        assert isinstance(obj, dict)
        return State()

    def to_dict(self) -> dict:
        result: dict = {}
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
    username: Optional[str] = None
    name: Optional[str] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        username = from_union([from_str, from_none], obj.get("username"))
        name = from_union([from_str, from_none], obj.get("name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return User(id, username, name, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["username"] = from_union([from_str, from_none], self.username)
        result["name"] = from_union([from_str, from_none], self.name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class View:
    id: Optional[str] = None
    team_id: Optional[str] = None
    type: Optional[str] = None
    title: Optional[Close] = None
    submit: Optional[Close] = None
    close: Optional[Close] = None
    private_metadata: Optional[str] = None
    callback_id: Optional[str] = None
    external_id: Optional[str] = None
    state: Optional[State] = None
    hash: Optional[str] = None
    clear_on_close: Optional[bool] = None
    notify_on_close: Optional[bool] = None
    submit_disabled: Optional[bool] = None
    root_view_id: Optional[str] = None
    previous_view_id: Optional[str] = None
    app_id: Optional[str] = None
    app_installed_team_id: Optional[str] = None
    bot_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'View':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        title = from_union([Close.from_dict, from_none], obj.get("title"))
        submit = from_union([Close.from_dict, from_none], obj.get("submit"))
        close = from_union([Close.from_dict, from_none], obj.get("close"))
        private_metadata = from_union([from_str, from_none], obj.get("private_metadata"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        state = from_union([State.from_dict, from_none], obj.get("state"))
        hash = from_union([from_str, from_none], obj.get("hash"))
        clear_on_close = from_union([from_bool, from_none], obj.get("clear_on_close"))
        notify_on_close = from_union([from_bool, from_none], obj.get("notify_on_close"))
        submit_disabled = from_union([from_bool, from_none], obj.get("submit_disabled"))
        root_view_id = from_union([from_str, from_none], obj.get("root_view_id"))
        previous_view_id = from_union([from_str, from_none], obj.get("previous_view_id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        app_installed_team_id = from_union([from_str, from_none], obj.get("app_installed_team_id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        return View(id, team_id, type, title, submit, close, private_metadata, callback_id, external_id, state, hash, clear_on_close, notify_on_close, submit_disabled, root_view_id, previous_view_id, app_id, app_installed_team_id, bot_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["title"] = from_union([lambda x: to_class(Close, x), from_none], self.title)
        result["submit"] = from_union([lambda x: to_class(Close, x), from_none], self.submit)
        result["close"] = from_union([lambda x: to_class(Close, x), from_none], self.close)
        result["private_metadata"] = from_union([from_str, from_none], self.private_metadata)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["state"] = from_union([lambda x: to_class(State, x), from_none], self.state)
        result["hash"] = from_union([from_str, from_none], self.hash)
        result["clear_on_close"] = from_union([from_bool, from_none], self.clear_on_close)
        result["notify_on_close"] = from_union([from_bool, from_none], self.notify_on_close)
        result["submit_disabled"] = from_union([from_bool, from_none], self.submit_disabled)
        result["root_view_id"] = from_union([from_str, from_none], self.root_view_id)
        result["previous_view_id"] = from_union([from_str, from_none], self.previous_view_id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["app_installed_team_id"] = from_union([from_str, from_none], self.app_installed_team_id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        return result


@dataclass
class BlockActionPayload:
    type: Optional[str] = None
    enterprise: Optional[Channel] = None
    team: Optional[Team] = None
    user: Optional[User] = None
    api_app_id: Optional[str] = None
    token: Optional[str] = None
    container: Optional[Container] = None
    trigger_id: Optional[str] = None
    channel: Optional[Channel] = None
    message: Optional[Message] = None
    response_url: Optional[str] = None
    view: Optional[View] = None
    state: Optional[State] = None
    actions: Optional[List[BlockActionPayloadAction]] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BlockActionPayload':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        enterprise = from_union([Channel.from_dict, from_none], obj.get("enterprise"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        token = from_union([from_str, from_none], obj.get("token"))
        container = from_union([Container.from_dict, from_none], obj.get("container"))
        trigger_id = from_union([from_str, from_none], obj.get("trigger_id"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        response_url = from_union([from_str, from_none], obj.get("response_url"))
        view = from_union([View.from_dict, from_none], obj.get("view"))
        state = from_union([State.from_dict, from_none], obj.get("state"))
        actions = from_union([lambda x: from_list(BlockActionPayloadAction.from_dict, x), from_none], obj.get("actions"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return BlockActionPayload(type, enterprise, team, user, api_app_id, token, container, trigger_id, channel, message, response_url, view, state, actions, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["enterprise"] = from_union([lambda x: to_class(Channel, x), from_none], self.enterprise)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["token"] = from_union([from_str, from_none], self.token)
        result["container"] = from_union([lambda x: to_class(Container, x), from_none], self.container)
        result["trigger_id"] = from_union([from_str, from_none], self.trigger_id)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["response_url"] = from_union([from_str, from_none], self.response_url)
        result["view"] = from_union([lambda x: to_class(View, x), from_none], self.view)
        result["state"] = from_union([lambda x: to_class(State, x), from_none], self.state)
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(BlockActionPayloadAction, x), x), from_none], self.actions)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


def block_action_payload_from_dict(s: Any) -> BlockActionPayload:
    return BlockActionPayload.from_dict(s)


def block_action_payload_to_dict(x: BlockActionPayload) -> Any:
    return to_class(BlockActionPayload, x)
