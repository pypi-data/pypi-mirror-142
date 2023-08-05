# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = chat_schedule_message_response_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class Hint:
    type: Optional[str] = None
    text: Optional[str] = None
    emoji: Optional[bool] = None
    verbatim: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Hint':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        emoji = from_union([from_bool, from_none], obj.get("emoji"))
        verbatim = from_union([from_bool, from_none], obj.get("verbatim"))
        return Hint(type, text, emoji, verbatim)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["emoji"] = from_union([from_bool, from_none], self.emoji)
        result["verbatim"] = from_union([from_bool, from_none], self.verbatim)
        return result


@dataclass
class Confirm:
    title: Optional[Hint] = None
    text: Optional[Hint] = None
    confirm: Optional[Hint] = None
    deny: Optional[Hint] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Confirm':
        assert isinstance(obj, dict)
        title = from_union([Hint.from_dict, from_none], obj.get("title"))
        text = from_union([Hint.from_dict, from_none], obj.get("text"))
        confirm = from_union([Hint.from_dict, from_none], obj.get("confirm"))
        deny = from_union([Hint.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return Confirm(title, text, confirm, deny, style)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([lambda x: to_class(Hint, x), from_none], self.title)
        result["text"] = from_union([lambda x: to_class(Hint, x), from_none], self.text)
        result["confirm"] = from_union([lambda x: to_class(Hint, x), from_none], self.confirm)
        result["deny"] = from_union([lambda x: to_class(Hint, x), from_none], self.deny)
        result["style"] = from_union([from_str, from_none], self.style)
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
class Option:
    text: Optional[Hint] = None
    value: Optional[str] = None
    description: Optional[Hint] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Option':
        assert isinstance(obj, dict)
        text = from_union([Hint.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([Hint.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Option(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(Hint, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(Hint, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class OptionGroup:
    label: Optional[Hint] = None
    options: Optional[List[Option]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OptionGroup':
        assert isinstance(obj, dict)
        label = from_union([Hint.from_dict, from_none], obj.get("label"))
        options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("options"))
        return OptionGroup(label, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_union([lambda x: to_class(Hint, x), from_none], self.label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.options)
        return result


@dataclass
class Accessory:
    type: Optional[str] = None
    text: Optional[Hint] = None
    action_id: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[Confirm] = None
    accessibility_label: Optional[str] = None
    options: Optional[List[Option]] = None
    initial_options: Optional[List[Option]] = None
    focus_on_load: Optional[bool] = None
    initial_option: Optional[Option] = None
    placeholder: Optional[Hint] = None
    initial_channel: Optional[str] = None
    response_url_enabled: Optional[bool] = None
    initial_channels: Optional[List[str]] = None
    max_selected_items: Optional[int] = None
    initial_conversation: Optional[str] = None
    default_to_current_conversation: Optional[bool] = None
    filter: Optional[Filter] = None
    initial_conversations: Optional[List[str]] = None
    initial_date: Optional[str] = None
    initial_time: Optional[str] = None
    min_query_length: Optional[int] = None
    image_url: Optional[str] = None
    alt_text: Optional[str] = None
    fallback: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    option_groups: Optional[List[OptionGroup]] = None
    initial_user: Optional[str] = None
    initial_users: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Accessory':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([Hint.from_dict, from_none], obj.get("text"))
        action_id = from_union([from_str, from_none], obj.get("action_id"))
        url = from_union([from_str, from_none], obj.get("url"))
        value = from_union([from_str, from_none], obj.get("value"))
        style = from_union([from_str, from_none], obj.get("style"))
        confirm = from_union([Confirm.from_dict, from_none], obj.get("confirm"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("options"))
        initial_options = from_union([lambda x: from_list(Option.from_dict, x), from_none], obj.get("initial_options"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        initial_option = from_union([Option.from_dict, from_none], obj.get("initial_option"))
        placeholder = from_union([Hint.from_dict, from_none], obj.get("placeholder"))
        initial_channel = from_union([from_str, from_none], obj.get("initial_channel"))
        response_url_enabled = from_union([from_bool, from_none], obj.get("response_url_enabled"))
        initial_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_channels"))
        max_selected_items = from_union([from_int, from_none], obj.get("max_selected_items"))
        initial_conversation = from_union([from_str, from_none], obj.get("initial_conversation"))
        default_to_current_conversation = from_union([from_bool, from_none], obj.get("default_to_current_conversation"))
        filter = from_union([Filter.from_dict, from_none], obj.get("filter"))
        initial_conversations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_conversations"))
        initial_date = from_union([from_str, from_none], obj.get("initial_date"))
        initial_time = from_union([from_str, from_none], obj.get("initial_time"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        option_groups = from_union([lambda x: from_list(OptionGroup.from_dict, x), from_none], obj.get("option_groups"))
        initial_user = from_union([from_str, from_none], obj.get("initial_user"))
        initial_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("initial_users"))
        return Accessory(type, text, action_id, url, value, style, confirm, accessibility_label, options, initial_options, focus_on_load, initial_option, placeholder, initial_channel, response_url_enabled, initial_channels, max_selected_items, initial_conversation, default_to_current_conversation, filter, initial_conversations, initial_date, initial_time, min_query_length, image_url, alt_text, fallback, image_width, image_height, image_bytes, option_groups, initial_user, initial_users)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([lambda x: to_class(Hint, x), from_none], self.text)
        result["action_id"] = from_union([from_str, from_none], self.action_id)
        result["url"] = from_union([from_str, from_none], self.url)
        result["value"] = from_union([from_str, from_none], self.value)
        result["style"] = from_union([from_str, from_none], self.style)
        result["confirm"] = from_union([lambda x: to_class(Confirm, x), from_none], self.confirm)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.options)
        result["initial_options"] = from_union([lambda x: from_list(lambda x: to_class(Option, x), x), from_none], self.initial_options)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["initial_option"] = from_union([lambda x: to_class(Option, x), from_none], self.initial_option)
        result["placeholder"] = from_union([lambda x: to_class(Hint, x), from_none], self.placeholder)
        result["initial_channel"] = from_union([from_str, from_none], self.initial_channel)
        result["response_url_enabled"] = from_union([from_bool, from_none], self.response_url_enabled)
        result["initial_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_channels)
        result["max_selected_items"] = from_union([from_int, from_none], self.max_selected_items)
        result["initial_conversation"] = from_union([from_str, from_none], self.initial_conversation)
        result["default_to_current_conversation"] = from_union([from_bool, from_none], self.default_to_current_conversation)
        result["filter"] = from_union([lambda x: to_class(Filter, x), from_none], self.filter)
        result["initial_conversations"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_conversations)
        result["initial_date"] = from_union([from_str, from_none], self.initial_date)
        result["initial_time"] = from_union([from_str, from_none], self.initial_time)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(OptionGroup, x), x), from_none], self.option_groups)
        result["initial_user"] = from_union([from_str, from_none], self.initial_user)
        result["initial_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.initial_users)
        return result


@dataclass
class Participant:
    slack_id: Optional[str] = None
    external_id: Optional[str] = None
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Participant':
        assert isinstance(obj, dict)
        slack_id = from_union([from_str, from_none], obj.get("slack_id"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        avatar_url = from_union([from_str, from_none], obj.get("avatar_url"))
        return Participant(slack_id, external_id, display_name, avatar_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["slack_id"] = from_union([from_str, from_none], self.slack_id)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["avatar_url"] = from_union([from_str, from_none], self.avatar_url)
        return result


@dataclass
class AppIconUrls:
    image_32: Optional[str] = None
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_64: Optional[str] = None
    image_72: Optional[str] = None
    image_96: Optional[str] = None
    image_128: Optional[str] = None
    image_192: Optional[str] = None
    image_512: Optional[str] = None
    image_1024: Optional[str] = None
    image_original: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AppIconUrls':
        assert isinstance(obj, dict)
        image_32 = from_union([from_str, from_none], obj.get("image_32"))
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_64 = from_union([from_str, from_none], obj.get("image_64"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        image_96 = from_union([from_str, from_none], obj.get("image_96"))
        image_128 = from_union([from_str, from_none], obj.get("image_128"))
        image_192 = from_union([from_str, from_none], obj.get("image_192"))
        image_512 = from_union([from_str, from_none], obj.get("image_512"))
        image_1024 = from_union([from_str, from_none], obj.get("image_1024"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        return AppIconUrls(image_32, image_36, image_48, image_64, image_72, image_96, image_128, image_192, image_512, image_1024, image_original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_32"] = from_union([from_str, from_none], self.image_32)
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_64"] = from_union([from_str, from_none], self.image_64)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        result["image_96"] = from_union([from_str, from_none], self.image_96)
        result["image_128"] = from_union([from_str, from_none], self.image_128)
        result["image_192"] = from_union([from_str, from_none], self.image_192)
        result["image_512"] = from_union([from_str, from_none], self.image_512)
        result["image_1024"] = from_union([from_str, from_none], self.image_1024)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        return result


@dataclass
class V1:
    id: Optional[str] = None
    app_id: Optional[str] = None
    app_icon_urls: Optional[AppIconUrls] = None
    date_start: Optional[int] = None
    active_participants: Optional[List[Participant]] = None
    all_participants: Optional[List[Participant]] = None
    display_id: Optional[str] = None
    join_url: Optional[str] = None
    desktop_app_join_url: Optional[str] = None
    name: Optional[str] = None
    created_by: Optional[str] = None
    date_end: Optional[int] = None
    channels: Optional[List[str]] = None
    is_dm_call: Optional[bool] = None
    was_rejected: Optional[bool] = None
    was_missed: Optional[bool] = None
    was_accepted: Optional[bool] = None
    has_ended: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'V1':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        app_icon_urls = from_union([AppIconUrls.from_dict, from_none], obj.get("app_icon_urls"))
        date_start = from_union([from_int, from_none], obj.get("date_start"))
        active_participants = from_union([lambda x: from_list(Participant.from_dict, x), from_none], obj.get("active_participants"))
        all_participants = from_union([lambda x: from_list(Participant.from_dict, x), from_none], obj.get("all_participants"))
        display_id = from_union([from_str, from_none], obj.get("display_id"))
        join_url = from_union([from_str, from_none], obj.get("join_url"))
        desktop_app_join_url = from_union([from_str, from_none], obj.get("desktop_app_join_url"))
        name = from_union([from_str, from_none], obj.get("name"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        date_end = from_union([from_int, from_none], obj.get("date_end"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        is_dm_call = from_union([from_bool, from_none], obj.get("is_dm_call"))
        was_rejected = from_union([from_bool, from_none], obj.get("was_rejected"))
        was_missed = from_union([from_bool, from_none], obj.get("was_missed"))
        was_accepted = from_union([from_bool, from_none], obj.get("was_accepted"))
        has_ended = from_union([from_bool, from_none], obj.get("has_ended"))
        return V1(id, app_id, app_icon_urls, date_start, active_participants, all_participants, display_id, join_url, desktop_app_join_url, name, created_by, date_end, channels, is_dm_call, was_rejected, was_missed, was_accepted, has_ended)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["app_icon_urls"] = from_union([lambda x: to_class(AppIconUrls, x), from_none], self.app_icon_urls)
        result["date_start"] = from_union([from_int, from_none], self.date_start)
        result["active_participants"] = from_union([lambda x: from_list(lambda x: to_class(Participant, x), x), from_none], self.active_participants)
        result["all_participants"] = from_union([lambda x: from_list(lambda x: to_class(Participant, x), x), from_none], self.all_participants)
        result["display_id"] = from_union([from_str, from_none], self.display_id)
        result["join_url"] = from_union([from_str, from_none], self.join_url)
        result["desktop_app_join_url"] = from_union([from_str, from_none], self.desktop_app_join_url)
        result["name"] = from_union([from_str, from_none], self.name)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["date_end"] = from_union([from_int, from_none], self.date_end)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["is_dm_call"] = from_union([from_bool, from_none], self.is_dm_call)
        result["was_rejected"] = from_union([from_bool, from_none], self.was_rejected)
        result["was_missed"] = from_union([from_bool, from_none], self.was_missed)
        result["was_accepted"] = from_union([from_bool, from_none], self.was_accepted)
        result["has_ended"] = from_union([from_bool, from_none], self.has_ended)
        return result


@dataclass
class Call:
    v1: Optional[V1] = None
    media_backend_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Call':
        assert isinstance(obj, dict)
        v1 = from_union([V1.from_dict, from_none], obj.get("v1"))
        media_backend_type = from_union([from_str, from_none], obj.get("media_backend_type"))
        return Call(v1, media_backend_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["v1"] = from_union([lambda x: to_class(V1, x), from_none], self.v1)
        result["media_backend_type"] = from_union([from_str, from_none], self.media_backend_type)
        return result


@dataclass
class Block:
    type: Optional[str] = None
    elements: Optional[List[Accessory]] = None
    block_id: Optional[str] = None
    call_id: Optional[str] = None
    api_decoration_available: Optional[bool] = None
    call: Optional[Call] = None
    external_id: Optional[str] = None
    source: Optional[str] = None
    text: Optional[Hint] = None
    fallback: Optional[str] = None
    image_url: Optional[str] = None
    image_width: Optional[int] = None
    image_height: Optional[int] = None
    image_bytes: Optional[int] = None
    alt_text: Optional[str] = None
    title: Optional[Hint] = None
    fields: Optional[List[Hint]] = None
    accessory: Optional[Accessory] = None
    label: Optional[Hint] = None
    element: Optional[Accessory] = None
    dispatch_action: Optional[bool] = None
    hint: Optional[Hint] = None
    optional: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Block':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        elements = from_union([lambda x: from_list(Accessory.from_dict, x), from_none], obj.get("elements"))
        block_id = from_union([from_str, from_none], obj.get("block_id"))
        call_id = from_union([from_str, from_none], obj.get("call_id"))
        api_decoration_available = from_union([from_bool, from_none], obj.get("api_decoration_available"))
        call = from_union([Call.from_dict, from_none], obj.get("call"))
        external_id = from_union([from_str, from_none], obj.get("external_id"))
        source = from_union([from_str, from_none], obj.get("source"))
        text = from_union([Hint.from_dict, from_none], obj.get("text"))
        fallback = from_union([from_str, from_none], obj.get("fallback"))
        image_url = from_union([from_str, from_none], obj.get("image_url"))
        image_width = from_union([from_int, from_none], obj.get("image_width"))
        image_height = from_union([from_int, from_none], obj.get("image_height"))
        image_bytes = from_union([from_int, from_none], obj.get("image_bytes"))
        alt_text = from_union([from_str, from_none], obj.get("alt_text"))
        title = from_union([Hint.from_dict, from_none], obj.get("title"))
        fields = from_union([lambda x: from_list(Hint.from_dict, x), from_none], obj.get("fields"))
        accessory = from_union([Accessory.from_dict, from_none], obj.get("accessory"))
        label = from_union([Hint.from_dict, from_none], obj.get("label"))
        element = from_union([Accessory.from_dict, from_none], obj.get("element"))
        dispatch_action = from_union([from_bool, from_none], obj.get("dispatch_action"))
        hint = from_union([Hint.from_dict, from_none], obj.get("hint"))
        optional = from_union([from_bool, from_none], obj.get("optional"))
        return Block(type, elements, block_id, call_id, api_decoration_available, call, external_id, source, text, fallback, image_url, image_width, image_height, image_bytes, alt_text, title, fields, accessory, label, element, dispatch_action, hint, optional)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["elements"] = from_union([lambda x: from_list(lambda x: to_class(Accessory, x), x), from_none], self.elements)
        result["block_id"] = from_union([from_str, from_none], self.block_id)
        result["call_id"] = from_union([from_str, from_none], self.call_id)
        result["api_decoration_available"] = from_union([from_bool, from_none], self.api_decoration_available)
        result["call"] = from_union([lambda x: to_class(Call, x), from_none], self.call)
        result["external_id"] = from_union([from_str, from_none], self.external_id)
        result["source"] = from_union([from_str, from_none], self.source)
        result["text"] = from_union([lambda x: to_class(Hint, x), from_none], self.text)
        result["fallback"] = from_union([from_str, from_none], self.fallback)
        result["image_url"] = from_union([from_str, from_none], self.image_url)
        result["image_width"] = from_union([from_int, from_none], self.image_width)
        result["image_height"] = from_union([from_int, from_none], self.image_height)
        result["image_bytes"] = from_union([from_int, from_none], self.image_bytes)
        result["alt_text"] = from_union([from_str, from_none], self.alt_text)
        result["title"] = from_union([lambda x: to_class(Hint, x), from_none], self.title)
        result["fields"] = from_union([lambda x: from_list(lambda x: to_class(Hint, x), x), from_none], self.fields)
        result["accessory"] = from_union([lambda x: to_class(Accessory, x), from_none], self.accessory)
        result["label"] = from_union([lambda x: to_class(Hint, x), from_none], self.label)
        result["element"] = from_union([lambda x: to_class(Accessory, x), from_none], self.element)
        result["dispatch_action"] = from_union([from_bool, from_none], self.dispatch_action)
        result["hint"] = from_union([lambda x: to_class(Hint, x), from_none], self.hint)
        result["optional"] = from_union([from_bool, from_none], self.optional)
        return result


@dataclass
class Icons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return Icons(image_36, image_48, image_72)

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
    icons: Optional[Icons] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotProfile':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return BotProfile(id, deleted, name, updated, app_id, icons, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class Message:
    bot_id: Optional[str] = None
    type: Optional[str] = None
    text: Optional[str] = None
    user: Optional[str] = None
    team: Optional[str] = None
    bot_profile: Optional[BotProfile] = None
    blocks: Optional[List[Block]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        user = from_union([from_str, from_none], obj.get("user"))
        team = from_union([from_str, from_none], obj.get("team"))
        bot_profile = from_union([BotProfile.from_dict, from_none], obj.get("bot_profile"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        return Message(bot_id, type, text, user, team, bot_profile, blocks)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["user"] = from_union([from_str, from_none], self.user)
        result["team"] = from_union([from_str, from_none], self.team)
        result["bot_profile"] = from_union([lambda x: to_class(BotProfile, x), from_none], self.bot_profile)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        return result


@dataclass
class ResponseMetadata:
    messages: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        return ResponseMetadata(messages)

    def to_dict(self) -> dict:
        result: dict = {}
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        return result


@dataclass
class ChatScheduleMessageResponse:
    ok: Optional[bool] = None
    scheduled_message_id: Optional[str] = None
    channel: Optional[str] = None
    post_at: Optional[int] = None
    message: Optional[Message] = None
    error: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChatScheduleMessageResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        scheduled_message_id = from_union([from_str, from_none], obj.get("scheduled_message_id"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        post_at = from_union([from_int, from_none], obj.get("post_at"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        error = from_union([from_str, from_none], obj.get("error"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ChatScheduleMessageResponse(ok, scheduled_message_id, channel, post_at, message, error, response_metadata, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["scheduled_message_id"] = from_union([from_str, from_none], self.scheduled_message_id)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["post_at"] = from_union([from_int, from_none], self.post_at)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        result["error"] = from_union([from_str, from_none], self.error)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def chat_schedule_message_response_from_dict(s: Any) -> ChatScheduleMessageResponse:
    return ChatScheduleMessageResponse.from_dict(s)


def chat_schedule_message_response_to_dict(x: ChatScheduleMessageResponse) -> Any:
    return to_class(ChatScheduleMessageResponse, x)
