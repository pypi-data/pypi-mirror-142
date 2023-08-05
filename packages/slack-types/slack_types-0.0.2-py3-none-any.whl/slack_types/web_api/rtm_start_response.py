# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = rtm_start_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, List, Dict, TypeVar, Type, cast, Callable


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


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return { k: f(v) for (k, v) in x.items() }


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


@dataclass
class BotIcons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotIcons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return BotIcons(image_36, image_48, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class Bot:
    id: Optional[str] = None
    deleted: Optional[bool] = None
    name: Optional[str] = None
    updated: Optional[int] = None
    app_id: Optional[str] = None
    icons: Optional[BotIcons] = None
    is_workflow_bot: Optional[bool] = None
    team_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Bot':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        deleted = from_union([from_bool, from_none], obj.get("deleted"))
        name = from_union([from_str, from_none], obj.get("name"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        icons = from_union([BotIcons.from_dict, from_none], obj.get("icons"))
        is_workflow_bot = from_union([from_bool, from_none], obj.get("is_workflow_bot"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        return Bot(id, deleted, name, updated, app_id, icons, is_workflow_bot, team_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["deleted"] = from_union([from_bool, from_none], self.deleted)
        result["name"] = from_union([from_str, from_none], self.name)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["icons"] = from_union([lambda x: to_class(BotIcons, x), from_none], self.icons)
        result["is_workflow_bot"] = from_union([from_bool, from_none], self.is_workflow_bot)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        return result


@dataclass
class Purpose:
    value: Optional[str] = None
    creator: Optional[str] = None
    last_set: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Purpose':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        last_set = from_union([from_int, from_none], obj.get("last_set"))
        return Purpose(value, creator, last_set)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["last_set"] = from_union([from_int, from_none], self.last_set)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    is_channel: Optional[bool] = None
    is_group: Optional[bool] = None
    is_im: Optional[bool] = None
    is_mpim: Optional[bool] = None
    is_private: Optional[bool] = None
    created: Optional[int] = None
    is_archived: Optional[bool] = None
    is_general: Optional[bool] = None
    unlinked: Optional[int] = None
    name_normalized: Optional[str] = None
    is_shared: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    is_pending_ext_shared: Optional[bool] = None
    pending_shared: Optional[List[str]] = None
    creator: Optional[str] = None
    is_ext_shared: Optional[bool] = None
    shared_team_ids: Optional[List[str]] = None
    pending_connected_team_ids: Optional[List[str]] = None
    has_pins: Optional[bool] = None
    is_member: Optional[bool] = None
    last_read: Optional[str] = None
    topic: Optional[Purpose] = None
    purpose: Optional[Purpose] = None
    previous_names: Optional[List[str]] = None
    priority: Optional[int] = None
    internal_team_ids: Optional[List[str]] = None
    connected_team_ids: Optional[List[str]] = None
    connected_limited_team_ids: Optional[List[str]] = None
    conversation_host_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_channel = from_union([from_bool, from_none], obj.get("is_channel"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        is_im = from_union([from_bool, from_none], obj.get("is_im"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        is_private = from_union([from_bool, from_none], obj.get("is_private"))
        created = from_union([from_int, from_none], obj.get("created"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_general = from_union([from_bool, from_none], obj.get("is_general"))
        unlinked = from_union([from_int, from_none], obj.get("unlinked"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_shared = from_union([from_bool, from_none], obj.get("is_shared"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        is_pending_ext_shared = from_union([from_bool, from_none], obj.get("is_pending_ext_shared"))
        pending_shared = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_shared"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_ext_shared = from_union([from_bool, from_none], obj.get("is_ext_shared"))
        shared_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("shared_team_ids"))
        pending_connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pending_connected_team_ids"))
        has_pins = from_union([from_bool, from_none], obj.get("has_pins"))
        is_member = from_union([from_bool, from_none], obj.get("is_member"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        topic = from_union([Purpose.from_dict, from_none], obj.get("topic"))
        purpose = from_union([Purpose.from_dict, from_none], obj.get("purpose"))
        previous_names = from_union([lambda x: from_list(from_str, x), from_none], obj.get("previous_names"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        internal_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("internal_team_ids"))
        connected_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_team_ids"))
        connected_limited_team_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("connected_limited_team_ids"))
        conversation_host_id = from_union([from_str, from_none], obj.get("conversation_host_id"))
        return Channel(id, name, is_channel, is_group, is_im, is_mpim, is_private, created, is_archived, is_general, unlinked, name_normalized, is_shared, is_org_shared, is_pending_ext_shared, pending_shared, creator, is_ext_shared, shared_team_ids, pending_connected_team_ids, has_pins, is_member, last_read, topic, purpose, previous_names, priority, internal_team_ids, connected_team_ids, connected_limited_team_ids, conversation_host_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_channel"] = from_union([from_bool, from_none], self.is_channel)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["is_im"] = from_union([from_bool, from_none], self.is_im)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["is_private"] = from_union([from_bool, from_none], self.is_private)
        result["created"] = from_union([from_int, from_none], self.created)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_general"] = from_union([from_bool, from_none], self.is_general)
        result["unlinked"] = from_union([from_int, from_none], self.unlinked)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_shared"] = from_union([from_bool, from_none], self.is_shared)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["is_pending_ext_shared"] = from_union([from_bool, from_none], self.is_pending_ext_shared)
        result["pending_shared"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_shared)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_ext_shared"] = from_union([from_bool, from_none], self.is_ext_shared)
        result["shared_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.shared_team_ids)
        result["pending_connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.pending_connected_team_ids)
        result["has_pins"] = from_union([from_bool, from_none], self.has_pins)
        result["is_member"] = from_union([from_bool, from_none], self.is_member)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["topic"] = from_union([lambda x: to_class(Purpose, x), from_none], self.topic)
        result["purpose"] = from_union([lambda x: to_class(Purpose, x), from_none], self.purpose)
        result["previous_names"] = from_union([lambda x: from_list(from_str, x), from_none], self.previous_names)
        result["priority"] = from_union([from_int, from_none], self.priority)
        result["internal_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.internal_team_ids)
        result["connected_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_team_ids)
        result["connected_limited_team_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.connected_limited_team_ids)
        result["conversation_host_id"] = from_union([from_str, from_none], self.conversation_host_id)
        return result


@dataclass
class DND:
    dnd_enabled: Optional[bool] = None
    next_dnd_start_ts: Optional[int] = None
    next_dnd_end_ts: Optional[int] = None
    snooze_enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DND':
        assert isinstance(obj, dict)
        dnd_enabled = from_union([from_bool, from_none], obj.get("dnd_enabled"))
        next_dnd_start_ts = from_union([from_int, from_none], obj.get("next_dnd_start_ts"))
        next_dnd_end_ts = from_union([from_int, from_none], obj.get("next_dnd_end_ts"))
        snooze_enabled = from_union([from_bool, from_none], obj.get("snooze_enabled"))
        return DND(dnd_enabled, next_dnd_start_ts, next_dnd_end_ts, snooze_enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["dnd_enabled"] = from_union([from_bool, from_none], self.dnd_enabled)
        result["next_dnd_start_ts"] = from_union([from_int, from_none], self.next_dnd_start_ts)
        result["next_dnd_end_ts"] = from_union([from_int, from_none], self.next_dnd_end_ts)
        result["snooze_enabled"] = from_union([from_bool, from_none], self.snooze_enabled)
        return result


@dataclass
class ActionConfirm:
    title: Optional[str] = None
    text: Optional[str] = None
    ok_text: Optional[str] = None
    dismiss_text: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActionConfirm':
        assert isinstance(obj, dict)
        title = from_union([from_str, from_none], obj.get("title"))
        text = from_union([from_str, from_none], obj.get("text"))
        ok_text = from_union([from_str, from_none], obj.get("ok_text"))
        dismiss_text = from_union([from_str, from_none], obj.get("dismiss_text"))
        return ActionConfirm(title, text, ok_text, dismiss_text)

    def to_dict(self) -> dict:
        result: dict = {}
        result["title"] = from_union([from_str, from_none], self.title)
        result["text"] = from_union([from_str, from_none], self.text)
        result["ok_text"] = from_union([from_str, from_none], self.ok_text)
        result["dismiss_text"] = from_union([from_str, from_none], self.dismiss_text)
        return result


@dataclass
class SelectedOptionElement:
    text: Optional[str] = None
    value: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SelectedOptionElement':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        return SelectedOptionElement(text, value)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        return result


@dataclass
class ActionOptionGroup:
    text: Optional[str] = None
    options: Optional[List[SelectedOptionElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActionOptionGroup':
        assert isinstance(obj, dict)
        text = from_union([from_str, from_none], obj.get("text"))
        options = from_union([lambda x: from_list(SelectedOptionElement.from_dict, x), from_none], obj.get("options"))
        return ActionOptionGroup(text, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([from_str, from_none], self.text)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOptionElement, x), x), from_none], self.options)
        return result


@dataclass
class Action:
    id: Optional[str] = None
    name: Optional[str] = None
    text: Optional[str] = None
    style: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    confirm: Optional[ActionConfirm] = None
    options: Optional[List[SelectedOptionElement]] = None
    selected_options: Optional[List[SelectedOptionElement]] = None
    data_source: Optional[str] = None
    min_query_length: Optional[int] = None
    option_groups: Optional[List[ActionOptionGroup]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Action':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        text = from_union([from_str, from_none], obj.get("text"))
        style = from_union([from_str, from_none], obj.get("style"))
        type = from_union([from_str, from_none], obj.get("type"))
        value = from_union([from_str, from_none], obj.get("value"))
        confirm = from_union([ActionConfirm.from_dict, from_none], obj.get("confirm"))
        options = from_union([lambda x: from_list(SelectedOptionElement.from_dict, x), from_none], obj.get("options"))
        selected_options = from_union([lambda x: from_list(SelectedOptionElement.from_dict, x), from_none], obj.get("selected_options"))
        data_source = from_union([from_str, from_none], obj.get("data_source"))
        min_query_length = from_union([from_int, from_none], obj.get("min_query_length"))
        option_groups = from_union([lambda x: from_list(ActionOptionGroup.from_dict, x), from_none], obj.get("option_groups"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Action(id, name, text, style, type, value, confirm, options, selected_options, data_source, min_query_length, option_groups, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["text"] = from_union([from_str, from_none], self.text)
        result["style"] = from_union([from_str, from_none], self.style)
        result["type"] = from_union([from_str, from_none], self.type)
        result["value"] = from_union([from_str, from_none], self.value)
        result["confirm"] = from_union([lambda x: to_class(ActionConfirm, x), from_none], self.confirm)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOptionElement, x), x), from_none], self.options)
        result["selected_options"] = from_union([lambda x: from_list(lambda x: to_class(SelectedOptionElement, x), x), from_none], self.selected_options)
        result["data_source"] = from_union([from_str, from_none], self.data_source)
        result["min_query_length"] = from_union([from_int, from_none], self.min_query_length)
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(ActionOptionGroup, x), x), from_none], self.option_groups)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


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
class AccessoryConfirm:
    title: Optional[Hint] = None
    text: Optional[Hint] = None
    confirm: Optional[Hint] = None
    deny: Optional[Hint] = None
    style: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccessoryConfirm':
        assert isinstance(obj, dict)
        title = from_union([Hint.from_dict, from_none], obj.get("title"))
        text = from_union([Hint.from_dict, from_none], obj.get("text"))
        confirm = from_union([Hint.from_dict, from_none], obj.get("confirm"))
        deny = from_union([Hint.from_dict, from_none], obj.get("deny"))
        style = from_union([from_str, from_none], obj.get("style"))
        return AccessoryConfirm(title, text, confirm, deny, style)

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
class InitialOptionElement:
    text: Optional[Hint] = None
    value: Optional[str] = None
    description: Optional[Hint] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InitialOptionElement':
        assert isinstance(obj, dict)
        text = from_union([Hint.from_dict, from_none], obj.get("text"))
        value = from_union([from_str, from_none], obj.get("value"))
        description = from_union([Hint.from_dict, from_none], obj.get("description"))
        url = from_union([from_str, from_none], obj.get("url"))
        return InitialOptionElement(text, value, description, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["text"] = from_union([lambda x: to_class(Hint, x), from_none], self.text)
        result["value"] = from_union([from_str, from_none], self.value)
        result["description"] = from_union([lambda x: to_class(Hint, x), from_none], self.description)
        result["url"] = from_union([from_str, from_none], self.url)
        return result


@dataclass
class AccessoryOptionGroup:
    label: Optional[Hint] = None
    options: Optional[List[InitialOptionElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AccessoryOptionGroup':
        assert isinstance(obj, dict)
        label = from_union([Hint.from_dict, from_none], obj.get("label"))
        options = from_union([lambda x: from_list(InitialOptionElement.from_dict, x), from_none], obj.get("options"))
        return AccessoryOptionGroup(label, options)

    def to_dict(self) -> dict:
        result: dict = {}
        result["label"] = from_union([lambda x: to_class(Hint, x), from_none], self.label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(InitialOptionElement, x), x), from_none], self.options)
        return result


@dataclass
class Accessory:
    type: Optional[str] = None
    text: Optional[Hint] = None
    action_id: Optional[str] = None
    url: Optional[str] = None
    value: Optional[str] = None
    style: Optional[str] = None
    confirm: Optional[AccessoryConfirm] = None
    accessibility_label: Optional[str] = None
    options: Optional[List[InitialOptionElement]] = None
    initial_options: Optional[List[InitialOptionElement]] = None
    focus_on_load: Optional[bool] = None
    initial_option: Optional[InitialOptionElement] = None
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
    option_groups: Optional[List[AccessoryOptionGroup]] = None
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
        confirm = from_union([AccessoryConfirm.from_dict, from_none], obj.get("confirm"))
        accessibility_label = from_union([from_str, from_none], obj.get("accessibility_label"))
        options = from_union([lambda x: from_list(InitialOptionElement.from_dict, x), from_none], obj.get("options"))
        initial_options = from_union([lambda x: from_list(InitialOptionElement.from_dict, x), from_none], obj.get("initial_options"))
        focus_on_load = from_union([from_bool, from_none], obj.get("focus_on_load"))
        initial_option = from_union([InitialOptionElement.from_dict, from_none], obj.get("initial_option"))
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
        option_groups = from_union([lambda x: from_list(AccessoryOptionGroup.from_dict, x), from_none], obj.get("option_groups"))
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
        result["confirm"] = from_union([lambda x: to_class(AccessoryConfirm, x), from_none], self.confirm)
        result["accessibility_label"] = from_union([from_str, from_none], self.accessibility_label)
        result["options"] = from_union([lambda x: from_list(lambda x: to_class(InitialOptionElement, x), x), from_none], self.options)
        result["initial_options"] = from_union([lambda x: from_list(lambda x: to_class(InitialOptionElement, x), x), from_none], self.initial_options)
        result["focus_on_load"] = from_union([from_bool, from_none], self.focus_on_load)
        result["initial_option"] = from_union([lambda x: to_class(InitialOptionElement, x), from_none], self.initial_option)
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
        result["option_groups"] = from_union([lambda x: from_list(lambda x: to_class(AccessoryOptionGroup, x), x), from_none], self.option_groups)
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
class Cc:
    address: Optional[str] = None
    name: Optional[str] = None
    original: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Cc':
        assert isinstance(obj, dict)
        address = from_union([from_str, from_none], obj.get("address"))
        name = from_union([from_str, from_none], obj.get("name"))
        original = from_union([from_str, from_none], obj.get("original"))
        return Cc(address, name, original)

    def to_dict(self) -> dict:
        result: dict = {}
        result["address"] = from_union([from_str, from_none], self.address)
        result["name"] = from_union([from_str, from_none], self.name)
        result["original"] = from_union([from_str, from_none], self.original)
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
class Reaction:
    name: Optional[str] = None
    count: Optional[int] = None
    users: Optional[List[str]] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Reaction':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        count = from_union([from_int, from_none], obj.get("count"))
        users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("users"))
        url = from_union([from_str, from_none], obj.get("url"))
        return Reaction(name, count, users, url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["count"] = from_union([from_int, from_none], self.count)
        result["users"] = from_union([lambda x: from_list(from_str, x), from_none], self.users)
        result["url"] = from_union([from_str, from_none], self.url)
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
    channels: Optional[List[str]] = None
    groups: Optional[List[str]] = None
    ims: Optional[List[str]] = None
    shares: Optional[Shares] = None
    to: Optional[List[Cc]] = None
    file_from: Optional[List[Cc]] = None
    cc: Optional[List[Cc]] = None
    channel_actions_ts: Optional[str] = None
    channel_actions_count: Optional[int] = None
    headers: Optional[Headers] = None
    simplified_html: Optional[str] = None
    bot_id: Optional[str] = None
    initial_comment: Optional[InitialComment] = None
    num_stars: Optional[int] = None
    is_starred: Optional[bool] = None
    pinned_to: Optional[List[str]] = None
    reactions: Optional[List[Reaction]] = None
    comments_count: Optional[int] = None
    blocks: Optional[List[Block]] = None

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
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("groups"))
        ims = from_union([lambda x: from_list(from_str, x), from_none], obj.get("ims"))
        shares = from_union([Shares.from_dict, from_none], obj.get("shares"))
        to = from_union([lambda x: from_list(Cc.from_dict, x), from_none], obj.get("to"))
        file_from = from_union([lambda x: from_list(Cc.from_dict, x), from_none], obj.get("from"))
        cc = from_union([lambda x: from_list(Cc.from_dict, x), from_none], obj.get("cc"))
        channel_actions_ts = from_union([from_str, from_none], obj.get("channel_actions_ts"))
        channel_actions_count = from_union([from_int, from_none], obj.get("channel_actions_count"))
        headers = from_union([Headers.from_dict, from_none], obj.get("headers"))
        simplified_html = from_union([from_str, from_none], obj.get("simplified_html"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        initial_comment = from_union([InitialComment.from_dict, from_none], obj.get("initial_comment"))
        num_stars = from_union([from_int, from_none], obj.get("num_stars"))
        is_starred = from_union([from_bool, from_none], obj.get("is_starred"))
        pinned_to = from_union([lambda x: from_list(from_str, x), from_none], obj.get("pinned_to"))
        reactions = from_union([lambda x: from_list(Reaction.from_dict, x), from_none], obj.get("reactions"))
        comments_count = from_union([from_int, from_none], obj.get("comments_count"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        return File(id, created, timestamp, name, title, subject, mimetype, filetype, pretty_type, user, mode, editable, non_owner_editable, editor, last_editor, updated, original_attachment_count, is_external, external_type, external_id, external_url, username, size, url_private, url_private_download, app_id, app_name, thumb_64, thumb_64__gif, thumb_64__w, thumb_64__h, thumb_80, thumb_80__gif, thumb_80__w, thumb_80__h, thumb_160, thumb_160__gif, thumb_160__w, thumb_160__h, thumb_360, thumb_360__gif, thumb_360__w, thumb_360__h, thumb_480, thumb_480__gif, thumb_480__w, thumb_480__h, thumb_720, thumb_720__gif, thumb_720__w, thumb_720__h, thumb_800, thumb_800__gif, thumb_800__w, thumb_800__h, thumb_960, thumb_960__gif, thumb_960__w, thumb_960__h, thumb_1024, thumb_1024__gif, thumb_1024__w, thumb_1024__h, thumb_video, thumb_gif, thumb_pdf, thumb_pdf_w, thumb_pdf_h, thumb_tiny, converted_pdf, image_exif_rotation, original_w, original_h, deanimate, deanimate_gif, pjpeg, permalink, permalink_public, edit_link, has_rich_preview, media_display_type, preview_is_truncated, preview, preview_highlight, plain_text, preview_plain_text, has_more, sent_to_self, lines, lines_more, is_public, public_url_shared, display_as_bot, channels, groups, ims, shares, to, file_from, cc, channel_actions_ts, channel_actions_count, headers, simplified_html, bot_id, initial_comment, num_stars, is_starred, pinned_to, reactions, comments_count, blocks)

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
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(from_str, x), from_none], self.groups)
        result["ims"] = from_union([lambda x: from_list(from_str, x), from_none], self.ims)
        result["shares"] = from_union([lambda x: to_class(Shares, x), from_none], self.shares)
        result["to"] = from_union([lambda x: from_list(lambda x: to_class(Cc, x), x), from_none], self.to)
        result["from"] = from_union([lambda x: from_list(lambda x: to_class(Cc, x), x), from_none], self.file_from)
        result["cc"] = from_union([lambda x: from_list(lambda x: to_class(Cc, x), x), from_none], self.cc)
        result["channel_actions_ts"] = from_union([from_str, from_none], self.channel_actions_ts)
        result["channel_actions_count"] = from_union([from_int, from_none], self.channel_actions_count)
        result["headers"] = from_union([lambda x: to_class(Headers, x), from_none], self.headers)
        result["simplified_html"] = from_union([from_str, from_none], self.simplified_html)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["initial_comment"] = from_union([lambda x: to_class(InitialComment, x), from_none], self.initial_comment)
        result["num_stars"] = from_union([from_int, from_none], self.num_stars)
        result["is_starred"] = from_union([from_bool, from_none], self.is_starred)
        result["pinned_to"] = from_union([lambda x: from_list(from_str, x), from_none], self.pinned_to)
        result["reactions"] = from_union([lambda x: from_list(lambda x: to_class(Reaction, x), x), from_none], self.reactions)
        result["comments_count"] = from_union([from_int, from_none], self.comments_count)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
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
    actions: Optional[List[Action]] = None
    blocks: Optional[List[Block]] = None
    files: Optional[List[File]] = None
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
        actions = from_union([lambda x: from_list(Action.from_dict, x), from_none], obj.get("actions"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        files = from_union([lambda x: from_list(File.from_dict, x), from_none], obj.get("files"))
        filename = from_union([from_str, from_none], obj.get("filename"))
        size = from_union([from_int, from_none], obj.get("size"))
        mimetype = from_union([from_str, from_none], obj.get("mimetype"))
        url = from_union([from_str, from_none], obj.get("url"))
        metadata = from_union([Metadata.from_dict, from_none], obj.get("metadata"))
        return Attachment(msg_subtype, fallback, callback_id, color, pretext, service_url, service_name, service_icon, author_id, author_name, author_link, author_icon, from_url, original_url, author_subname, channel_id, channel_name, id, bot_id, indent, is_msg_unfurl, is_reply_unfurl, is_thread_root_unfurl, is_app_unfurl, app_unfurl_url, title, title_link, text, fields, image_url, image_width, image_height, image_bytes, thumb_url, thumb_width, thumb_height, video_url, video_html, video_html_width, video_html_height, footer, footer_icon, ts, mrkdwn_in, actions, blocks, files, filename, size, mimetype, url, metadata)

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
        result["actions"] = from_union([lambda x: from_list(lambda x: to_class(Action, x), x), from_none], self.actions)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["files"] = from_union([lambda x: from_list(lambda x: to_class(File, x), x), from_none], self.files)
        result["filename"] = from_union([from_str, from_none], self.filename)
        result["size"] = from_union([from_int, from_none], self.size)
        result["mimetype"] = from_union([from_str, from_none], self.mimetype)
        result["url"] = from_union([from_str, from_none], self.url)
        result["metadata"] = from_union([lambda x: to_class(Metadata, x), from_none], self.metadata)
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
class LatestIcons:
    emoji: Optional[str] = None
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_64: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LatestIcons':
        assert isinstance(obj, dict)
        emoji = from_union([from_str, from_none], obj.get("emoji"))
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_64 = from_union([from_str, from_none], obj.get("image_64"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return LatestIcons(emoji, image_36, image_48, image_64, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["emoji"] = from_union([from_str, from_none], self.emoji)
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_64"] = from_union([from_str, from_none], self.image_64)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
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
    icons: Optional[LatestIcons] = None
    bot_profile: Optional[Bot] = None
    edited: Optional[Edited] = None
    replies: Optional[List[Edited]] = None
    reply_count: Optional[int] = None
    reply_users: Optional[List[str]] = None
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
        icons = from_union([LatestIcons.from_dict, from_none], obj.get("icons"))
        bot_profile = from_union([Bot.from_dict, from_none], obj.get("bot_profile"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        replies = from_union([lambda x: from_list(Edited.from_dict, x), from_none], obj.get("replies"))
        reply_count = from_union([from_int, from_none], obj.get("reply_count"))
        reply_users = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reply_users"))
        reply_users_count = from_union([from_int, from_none], obj.get("reply_users_count"))
        latest_reply = from_union([from_str, from_none], obj.get("latest_reply"))
        subscribed = from_union([from_bool, from_none], obj.get("subscribed"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        unread_count = from_union([from_int, from_none], obj.get("unread_count"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        return Root(text, user, parent_user_id, username, team, bot_id, mrkdwn, type, subtype, thread_ts, icons, bot_profile, edited, replies, reply_count, reply_users, reply_users_count, latest_reply, subscribed, last_read, unread_count, ts)

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
        result["icons"] = from_union([lambda x: to_class(LatestIcons, x), from_none], self.icons)
        result["bot_profile"] = from_union([lambda x: to_class(Bot, x), from_none], self.bot_profile)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        result["replies"] = from_union([lambda x: from_list(lambda x: to_class(Edited, x), x), from_none], self.replies)
        result["reply_count"] = from_union([from_int, from_none], self.reply_count)
        result["reply_users"] = from_union([lambda x: from_list(from_str, x), from_none], self.reply_users)
        result["reply_users_count"] = from_union([from_int, from_none], self.reply_users_count)
        result["latest_reply"] = from_union([from_str, from_none], self.latest_reply)
        result["subscribed"] = from_union([from_bool, from_none], self.subscribed)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["unread_count"] = from_union([from_int, from_none], self.unread_count)
        result["ts"] = from_union([from_str, from_none], self.ts)
        return result


@dataclass
class Latest:
    client_msg_id: Optional[str] = None
    type: Optional[str] = None
    subtype: Optional[str] = None
    team: Optional[str] = None
    user: Optional[str] = None
    username: Optional[str] = None
    parent_user_id: Optional[str] = None
    text: Optional[str] = None
    topic: Optional[str] = None
    attachments: Optional[List[Attachment]] = None
    blocks: Optional[List[Block]] = None
    files: Optional[List[File]] = None
    reactions: Optional[List[str]] = None
    root: Optional[Root] = None
    upload: Optional[bool] = None
    display_as_bot: Optional[bool] = None
    bot_id: Optional[str] = None
    bot_link: Optional[str] = None
    bot_profile: Optional[Bot] = None
    thread_ts: Optional[str] = None
    ts: Optional[str] = None
    icons: Optional[LatestIcons] = None
    x_files: Optional[List[str]] = None
    edited: Optional[Edited] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Latest':
        assert isinstance(obj, dict)
        client_msg_id = from_union([from_str, from_none], obj.get("client_msg_id"))
        type = from_union([from_str, from_none], obj.get("type"))
        subtype = from_union([from_str, from_none], obj.get("subtype"))
        team = from_union([from_str, from_none], obj.get("team"))
        user = from_union([from_str, from_none], obj.get("user"))
        username = from_union([from_str, from_none], obj.get("username"))
        parent_user_id = from_union([from_str, from_none], obj.get("parent_user_id"))
        text = from_union([from_str, from_none], obj.get("text"))
        topic = from_union([from_str, from_none], obj.get("topic"))
        attachments = from_union([lambda x: from_list(Attachment.from_dict, x), from_none], obj.get("attachments"))
        blocks = from_union([lambda x: from_list(Block.from_dict, x), from_none], obj.get("blocks"))
        files = from_union([lambda x: from_list(File.from_dict, x), from_none], obj.get("files"))
        reactions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("reactions"))
        root = from_union([Root.from_dict, from_none], obj.get("root"))
        upload = from_union([from_bool, from_none], obj.get("upload"))
        display_as_bot = from_union([from_bool, from_none], obj.get("display_as_bot"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        bot_link = from_union([from_str, from_none], obj.get("bot_link"))
        bot_profile = from_union([Bot.from_dict, from_none], obj.get("bot_profile"))
        thread_ts = from_union([from_str, from_none], obj.get("thread_ts"))
        ts = from_union([from_str, from_none], obj.get("ts"))
        icons = from_union([LatestIcons.from_dict, from_none], obj.get("icons"))
        x_files = from_union([lambda x: from_list(from_str, x), from_none], obj.get("x_files"))
        edited = from_union([Edited.from_dict, from_none], obj.get("edited"))
        return Latest(client_msg_id, type, subtype, team, user, username, parent_user_id, text, topic, attachments, blocks, files, reactions, root, upload, display_as_bot, bot_id, bot_link, bot_profile, thread_ts, ts, icons, x_files, edited)

    def to_dict(self) -> dict:
        result: dict = {}
        result["client_msg_id"] = from_union([from_str, from_none], self.client_msg_id)
        result["type"] = from_union([from_str, from_none], self.type)
        result["subtype"] = from_union([from_str, from_none], self.subtype)
        result["team"] = from_union([from_str, from_none], self.team)
        result["user"] = from_union([from_str, from_none], self.user)
        result["username"] = from_union([from_str, from_none], self.username)
        result["parent_user_id"] = from_union([from_str, from_none], self.parent_user_id)
        result["text"] = from_union([from_str, from_none], self.text)
        result["topic"] = from_union([from_str, from_none], self.topic)
        result["attachments"] = from_union([lambda x: from_list(lambda x: to_class(Attachment, x), x), from_none], self.attachments)
        result["blocks"] = from_union([lambda x: from_list(lambda x: to_class(Block, x), x), from_none], self.blocks)
        result["files"] = from_union([lambda x: from_list(lambda x: to_class(File, x), x), from_none], self.files)
        result["reactions"] = from_union([lambda x: from_list(from_str, x), from_none], self.reactions)
        result["root"] = from_union([lambda x: to_class(Root, x), from_none], self.root)
        result["upload"] = from_union([from_bool, from_none], self.upload)
        result["display_as_bot"] = from_union([from_bool, from_none], self.display_as_bot)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["bot_link"] = from_union([from_str, from_none], self.bot_link)
        result["bot_profile"] = from_union([lambda x: to_class(Bot, x), from_none], self.bot_profile)
        result["thread_ts"] = from_union([from_str, from_none], self.thread_ts)
        result["ts"] = from_union([from_str, from_none], self.ts)
        result["icons"] = from_union([lambda x: to_class(LatestIcons, x), from_none], self.icons)
        result["x_files"] = from_union([lambda x: from_list(from_str, x), from_none], self.x_files)
        result["edited"] = from_union([lambda x: to_class(Edited, x), from_none], self.edited)
        return result


@dataclass
class Group:
    id: Optional[str] = None
    name: Optional[str] = None
    name_normalized: Optional[str] = None
    is_group: Optional[bool] = None
    created: Optional[int] = None
    creator: Optional[str] = None
    is_archived: Optional[bool] = None
    is_mpim: Optional[bool] = None
    is_open: Optional[bool] = None
    is_read_only: Optional[bool] = None
    is_thread_only: Optional[bool] = None
    members: Optional[List[str]] = None
    parent_group: Optional[str] = None
    topic: Optional[Purpose] = None
    purpose: Optional[Purpose] = None
    last_read: Optional[str] = None
    latest: Optional[Latest] = None
    unread_count: Optional[int] = None
    unread_count_display: Optional[int] = None
    priority: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Group':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        name_normalized = from_union([from_str, from_none], obj.get("name_normalized"))
        is_group = from_union([from_bool, from_none], obj.get("is_group"))
        created = from_union([from_int, from_none], obj.get("created"))
        creator = from_union([from_str, from_none], obj.get("creator"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_mpim = from_union([from_bool, from_none], obj.get("is_mpim"))
        is_open = from_union([from_bool, from_none], obj.get("is_open"))
        is_read_only = from_union([from_bool, from_none], obj.get("is_read_only"))
        is_thread_only = from_union([from_bool, from_none], obj.get("is_thread_only"))
        members = from_union([lambda x: from_list(from_str, x), from_none], obj.get("members"))
        parent_group = from_union([from_str, from_none], obj.get("parent_group"))
        topic = from_union([Purpose.from_dict, from_none], obj.get("topic"))
        purpose = from_union([Purpose.from_dict, from_none], obj.get("purpose"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        latest = from_union([Latest.from_dict, from_none], obj.get("latest"))
        unread_count = from_union([from_int, from_none], obj.get("unread_count"))
        unread_count_display = from_union([from_int, from_none], obj.get("unread_count_display"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        return Group(id, name, name_normalized, is_group, created, creator, is_archived, is_mpim, is_open, is_read_only, is_thread_only, members, parent_group, topic, purpose, last_read, latest, unread_count, unread_count_display, priority)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["name_normalized"] = from_union([from_str, from_none], self.name_normalized)
        result["is_group"] = from_union([from_bool, from_none], self.is_group)
        result["created"] = from_union([from_int, from_none], self.created)
        result["creator"] = from_union([from_str, from_none], self.creator)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_mpim"] = from_union([from_bool, from_none], self.is_mpim)
        result["is_open"] = from_union([from_bool, from_none], self.is_open)
        result["is_read_only"] = from_union([from_bool, from_none], self.is_read_only)
        result["is_thread_only"] = from_union([from_bool, from_none], self.is_thread_only)
        result["members"] = from_union([lambda x: from_list(from_str, x), from_none], self.members)
        result["parent_group"] = from_union([from_str, from_none], self.parent_group)
        result["topic"] = from_union([lambda x: to_class(Purpose, x), from_none], self.topic)
        result["purpose"] = from_union([lambda x: to_class(Purpose, x), from_none], self.purpose)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["latest"] = from_union([lambda x: to_class(Latest, x), from_none], self.latest)
        result["unread_count"] = from_union([from_int, from_none], self.unread_count)
        result["unread_count_display"] = from_union([from_int, from_none], self.unread_count_display)
        result["priority"] = from_union([from_int, from_none], self.priority)
        return result


@dataclass
class IM:
    id: Optional[str] = None
    created: Optional[int] = None
    is_archived: Optional[bool] = None
    is_im: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    user: Optional[str] = None
    last_read: Optional[str] = None
    is_open: Optional[bool] = None
    has_pins: Optional[bool] = None
    priority: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IM':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        created = from_union([from_int, from_none], obj.get("created"))
        is_archived = from_union([from_bool, from_none], obj.get("is_archived"))
        is_im = from_union([from_bool, from_none], obj.get("is_im"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        user = from_union([from_str, from_none], obj.get("user"))
        last_read = from_union([from_str, from_none], obj.get("last_read"))
        is_open = from_union([from_bool, from_none], obj.get("is_open"))
        has_pins = from_union([from_bool, from_none], obj.get("has_pins"))
        priority = from_union([from_int, from_none], obj.get("priority"))
        return IM(id, created, is_archived, is_im, is_org_shared, user, last_read, is_open, has_pins, priority)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["created"] = from_union([from_int, from_none], self.created)
        result["is_archived"] = from_union([from_bool, from_none], self.is_archived)
        result["is_im"] = from_union([from_bool, from_none], self.is_im)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["user"] = from_union([from_str, from_none], self.user)
        result["last_read"] = from_union([from_str, from_none], self.last_read)
        result["is_open"] = from_union([from_bool, from_none], self.is_open)
        result["has_pins"] = from_union([from_bool, from_none], self.has_pins)
        result["priority"] = from_union([from_int, from_none], self.priority)
        return result


@dataclass
class Links:
    domains_ts: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Links':
        assert isinstance(obj, dict)
        domains_ts = from_union([from_int, from_none], obj.get("domains_ts"))
        return Links(domains_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["domains_ts"] = from_union([from_int, from_none], self.domains_ts)
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
class LocalesEnabled:
    de_de: Optional[str] = None
    en_gb: Optional[str] = None
    en_us: Optional[str] = None
    es_es: Optional[str] = None
    es_la: Optional[str] = None
    fr_fr: Optional[str] = None
    it_it: Optional[str] = None
    pt_br: Optional[str] = None
    ru_ru: Optional[str] = None
    ja_jp: Optional[str] = None
    zh_cn: Optional[str] = None
    zh_tw: Optional[str] = None
    ko_kr: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LocalesEnabled':
        assert isinstance(obj, dict)
        de_de = from_union([from_str, from_none], obj.get("de-DE"))
        en_gb = from_union([from_str, from_none], obj.get("en-GB"))
        en_us = from_union([from_str, from_none], obj.get("en-US"))
        es_es = from_union([from_str, from_none], obj.get("es-ES"))
        es_la = from_union([from_str, from_none], obj.get("es-LA"))
        fr_fr = from_union([from_str, from_none], obj.get("fr-FR"))
        it_it = from_union([from_str, from_none], obj.get("it-IT"))
        pt_br = from_union([from_str, from_none], obj.get("pt-BR"))
        ru_ru = from_union([from_str, from_none], obj.get("ru-RU"))
        ja_jp = from_union([from_str, from_none], obj.get("ja-JP"))
        zh_cn = from_union([from_str, from_none], obj.get("zh-CN"))
        zh_tw = from_union([from_str, from_none], obj.get("zh-TW"))
        ko_kr = from_union([from_str, from_none], obj.get("ko-KR"))
        return LocalesEnabled(de_de, en_gb, en_us, es_es, es_la, fr_fr, it_it, pt_br, ru_ru, ja_jp, zh_cn, zh_tw, ko_kr)

    def to_dict(self) -> dict:
        result: dict = {}
        result["de-DE"] = from_union([from_str, from_none], self.de_de)
        result["en-GB"] = from_union([from_str, from_none], self.en_gb)
        result["en-US"] = from_union([from_str, from_none], self.en_us)
        result["es-ES"] = from_union([from_str, from_none], self.es_es)
        result["es-LA"] = from_union([from_str, from_none], self.es_la)
        result["fr-FR"] = from_union([from_str, from_none], self.fr_fr)
        result["it-IT"] = from_union([from_str, from_none], self.it_it)
        result["pt-BR"] = from_union([from_str, from_none], self.pt_br)
        result["ru-RU"] = from_union([from_str, from_none], self.ru_ru)
        result["ja-JP"] = from_union([from_str, from_none], self.ja_jp)
        result["zh-CN"] = from_union([from_str, from_none], self.zh_cn)
        result["zh-TW"] = from_union([from_str, from_none], self.zh_tw)
        result["ko-KR"] = from_union([from_str, from_none], self.ko_kr)
        return result


@dataclass
class SelfPrefs:
    underline_links: Optional[bool] = None
    user_colors: Optional[str] = None
    color_names_in_list: Optional[bool] = None
    email_alerts: Optional[str] = None
    email_alerts_sleep_until: Optional[int] = None
    email_tips: Optional[bool] = None
    email_weekly: Optional[bool] = None
    email_offers: Optional[bool] = None
    email_research: Optional[bool] = None
    email_developer: Optional[bool] = None
    welcome_message_hidden: Optional[bool] = None
    search_sort: Optional[str] = None
    search_file_sort: Optional[str] = None
    search_channel_sort: Optional[str] = None
    search_people_sort: Optional[str] = None
    expand_inline_imgs: Optional[bool] = None
    expand_internal_inline_imgs: Optional[bool] = None
    expand_snippets: Optional[bool] = None
    posts_formatting_guide: Optional[bool] = None
    seen_welcome_2: Optional[bool] = None
    seen_ssb_prompt: Optional[bool] = None
    spaces_new_xp_banner_dismissed: Optional[bool] = None
    search_only_my_channels: Optional[bool] = None
    search_only_current_team: Optional[bool] = None
    search_hide_my_channels: Optional[bool] = None
    search_only_show_online: Optional[bool] = None
    search_hide_deactivated_users: Optional[bool] = None
    emoji_mode: Optional[str] = None
    emoji_use: Optional[str] = None
    emoji_use_org: Optional[str] = None
    has_invited: Optional[bool] = None
    has_uploaded: Optional[bool] = None
    has_created_channel: Optional[bool] = None
    has_created_channel_section: Optional[bool] = None
    has_searched: Optional[bool] = None
    search_exclude_channels: Optional[str] = None
    messages_theme: Optional[str] = None
    webapp_spellcheck: Optional[bool] = None
    no_joined_overlays: Optional[bool] = None
    no_created_overlays: Optional[bool] = None
    dropbox_enabled: Optional[bool] = None
    seen_domain_invite_reminder: Optional[bool] = None
    seen_member_invite_reminder: Optional[bool] = None
    mute_sounds: Optional[bool] = None
    arrow_history: Optional[bool] = None
    tab_ui_return_selects: Optional[bool] = None
    obey_inline_img_limit: Optional[bool] = None
    require_at: Optional[bool] = None
    ssb_space_window: Optional[str] = None
    mac_ssb_bounce: Optional[str] = None
    mac_ssb_bullet: Optional[bool] = None
    expand_non_media_attachments: Optional[bool] = None
    show_typing: Optional[bool] = None
    pagekeys_handled: Optional[bool] = None
    last_snippet_type: Optional[str] = None
    display_real_names_override: Optional[int] = None
    display_display_names: Optional[bool] = None
    time24: Optional[bool] = None
    enter_is_special_in_tbt: Optional[bool] = None
    msg_input_send_btn: Optional[bool] = None
    msg_input_send_btn_auto_set: Optional[bool] = None
    msg_input_sticky_composer: Optional[bool] = None
    composer_nux: Optional[str] = None
    graphic_emoticons: Optional[bool] = None
    convert_emoticons: Optional[bool] = None
    ss_emojis: Optional[bool] = None
    seen_onboarding_start: Optional[bool] = None
    onboarding_cancelled: Optional[bool] = None
    seen_onboarding_slackbot_conversation: Optional[bool] = None
    seen_onboarding_channels: Optional[bool] = None
    seen_onboarding_direct_messages: Optional[bool] = None
    seen_onboarding_invites: Optional[bool] = None
    seen_onboarding_search: Optional[bool] = None
    seen_onboarding_recent_mentions: Optional[bool] = None
    seen_onboarding_starred_items: Optional[bool] = None
    seen_onboarding_private_groups: Optional[bool] = None
    seen_onboarding_banner: Optional[bool] = None
    onboarding_slackbot_conversation_step: Optional[int] = None
    set_tz_automatically: Optional[bool] = None
    suppress_link_warning: Optional[bool] = None
    suppress_external_invites_from_compose_warning: Optional[bool] = None
    seen_emoji_pack_cta: Optional[int] = None
    seen_emoji_pack_dialog: Optional[bool] = None
    seen_schedule_send_coachmark: Optional[bool] = None
    emoji_packs_most_recent_available_time: Optional[int] = None
    emoji_packs_clicked_picker_cta: Optional[bool] = None
    emoji_packs_clicked_picker_post_install_cta: Optional[bool] = None
    emoji_packs_clicked_collection_cta: Optional[bool] = None
    dnd_enabled: Optional[bool] = None
    dnd_start_hour: Optional[str] = None
    dnd_end_hour: Optional[str] = None
    dnd_before_monday: Optional[str] = None
    dnd_after_monday: Optional[str] = None
    dnd_enabled_monday: Optional[str] = None
    dnd_before_tuesday: Optional[str] = None
    dnd_after_tuesday: Optional[str] = None
    dnd_enabled_tuesday: Optional[str] = None
    dnd_before_wednesday: Optional[str] = None
    dnd_after_wednesday: Optional[str] = None
    dnd_enabled_wednesday: Optional[str] = None
    dnd_before_thursday: Optional[str] = None
    dnd_after_thursday: Optional[str] = None
    dnd_enabled_thursday: Optional[str] = None
    dnd_before_friday: Optional[str] = None
    dnd_after_friday: Optional[str] = None
    dnd_enabled_friday: Optional[str] = None
    dnd_before_saturday: Optional[str] = None
    dnd_after_saturday: Optional[str] = None
    dnd_enabled_saturday: Optional[str] = None
    dnd_before_sunday: Optional[str] = None
    dnd_after_sunday: Optional[str] = None
    dnd_enabled_sunday: Optional[str] = None
    dnd_days: Optional[str] = None
    dnd_weekdays_off_allday: Optional[bool] = None
    reminder_notification_time: Optional[str] = None
    dnd_custom_new_badge_seen: Optional[bool] = None
    dnd_notification_schedule_new_badge_seen: Optional[bool] = None
    notification_center_filters: Optional[str] = None
    calls_survey_last_seen: Optional[str] = None
    huddle_survey_last_seen: Optional[str] = None
    sidebar_behavior: Optional[str] = None
    channel_sort: Optional[str] = None
    separate_private_channels: Optional[bool] = None
    separate_shared_channels: Optional[bool] = None
    sidebar_theme: Optional[str] = None
    sidebar_theme_custom_values: Optional[str] = None
    no_invites_widget_in_sidebar: Optional[bool] = None
    no_omnibox_in_channels: Optional[bool] = None
    k_key_omnibox_auto_hide_count: Optional[int] = None
    show_sidebar_quickswitcher_button: Optional[bool] = None
    ent_org_wide_channels_sidebar: Optional[bool] = None
    mark_msgs_read_immediately: Optional[bool] = None
    start_scroll_at_oldest: Optional[bool] = None
    snippet_editor_wrap_long_lines: Optional[bool] = None
    ls_disabled: Optional[bool] = None
    f_key_search: Optional[bool] = None
    k_key_omnibox: Optional[bool] = None
    prompted_for_email_disabling: Optional[bool] = None
    no_macelectron_banner: Optional[bool] = None
    no_macssb1_banner: Optional[bool] = None
    no_macssb2_banner: Optional[bool] = None
    no_winssb1_banner: Optional[bool] = None
    hide_user_group_info_pane: Optional[bool] = None
    mentions_exclude_at_user_groups: Optional[bool] = None
    mentions_exclude_reactions: Optional[bool] = None
    privacy_policy_seen: Optional[bool] = None
    enterprise_migration_seen: Optional[bool] = None
    search_exclude_bots: Optional[bool] = None
    load_lato_2: Optional[bool] = None
    fuller_timestamps: Optional[bool] = None
    last_seen_at_channel_warning: Optional[int] = None
    emoji_autocomplete_big: Optional[bool] = None
    two_factor_auth_enabled: Optional[bool] = None
    hide_hex_swatch: Optional[bool] = None
    show_jumper_scores: Optional[bool] = None
    enterprise_mdm_custom_msg: Optional[str] = None
    client_logs_pri: Optional[str] = None
    flannel_server_pool: Optional[str] = None
    mentions_exclude_at_channels: Optional[bool] = None
    confirm_clear_all_unreads: Optional[bool] = None
    confirm_user_marked_away: Optional[bool] = None
    box_enabled: Optional[bool] = None
    seen_single_emoji_msg: Optional[bool] = None
    confirm_sh_call_start: Optional[bool] = None
    preferred_skin_tone: Optional[str] = None
    show_all_skin_tones: Optional[bool] = None
    whats_new_read: Optional[int] = None
    help_modal_open_timestamp: Optional[int] = None
    help_modal_consult_banner_dismissed: Optional[bool] = None
    help_flexpane_slack_connect_card_seen: Optional[bool] = None
    help_flexpane_clips_card_seen: Optional[bool] = None
    help_menu_open_timestamp: Optional[int] = None
    frecency_jumper: Optional[str] = None
    frecency_ent_jumper: Optional[str] = None
    jumbomoji: Optional[bool] = None
    newxp_seen_last_message: Optional[int] = None
    show_memory_instrument: Optional[bool] = None
    enable_unread_view: Optional[bool] = None
    seen_unread_view_coachmark: Optional[bool] = None
    seen_connect_dm_coachmark: Optional[bool] = None
    seen_connect_section_coachmark: Optional[bool] = None
    should_show_connect_section: Optional[bool] = None
    enable_react_emoji_picker: Optional[bool] = None
    seen_custom_status_badge: Optional[bool] = None
    seen_custom_status_callout: Optional[bool] = None
    seen_custom_status_expiration_badge: Optional[bool] = None
    used_custom_status_kb_shortcut: Optional[bool] = None
    seen_guest_admin_slackbot_announcement: Optional[bool] = None
    seen_threads_notification_banner: Optional[bool] = None
    seen_name_tagging_coachmark: Optional[bool] = None
    all_unreads_sort_order: Optional[str] = None
    all_unreads_section_filter: Optional[str] = None
    locale: Optional[str] = None
    seen_intl_channel_names_coachmark: Optional[bool] = None
    seen_p3_locale_change_message_ko_kr: Optional[int] = None
    seen_toast_new_locale_launch: Optional[str] = None
    seen_toast_new_locale_launch_ts: Optional[int] = None
    seen_locale_change_message: Optional[int] = None
    seen_japanese_locale_change_message: Optional[bool] = None
    seen_shared_channels_coachmark: Optional[bool] = None
    seen_shared_channels_opt_in_change_message: Optional[bool] = None
    has_recently_shared_a_channel: Optional[bool] = None
    seen_channel_browser_admin_coachmark: Optional[bool] = None
    seen_administration_menu: Optional[bool] = None
    seen_drafts_section_coachmark: Optional[bool] = None
    seen_emoji_update_overlay_coachmark: Optional[bool] = None
    seen_sonic_deluxe_toast: Optional[int] = None
    seen_wysiwyg_deluxe_toast: Optional[bool] = None
    seen_markdown_paste_toast: Optional[int] = None
    seen_markdown_paste_shortcut: Optional[int] = None
    seen_ia_education: Optional[bool] = None
    show_ia_tour_relaunch: Optional[int] = None
    plain_text_mode: Optional[bool] = None
    show_shared_channels_education_banner: Optional[bool] = None
    ia_slackbot_survey_timestamp_48_h: Optional[int] = None
    ia_slackbot_survey_timestamp_7_d: Optional[int] = None
    enable_streamline_view: Optional[bool] = None
    enable_sent_view: Optional[bool] = None
    allow_calls_to_set_current_status: Optional[bool] = None
    in_interactive_mas_migration_flow: Optional[bool] = None
    sunset_interactive_message_views: Optional[int] = None
    shdep_promo_code_submitted: Optional[bool] = None
    seen_shdep_slackbot_message: Optional[bool] = None
    seen_calls_interactive_coachmark: Optional[bool] = None
    allow_cmd_tab_iss: Optional[bool] = None
    join_calls_device_settings: Optional[str] = None
    calls_disconnect_on_lock: Optional[bool] = None
    seen_workflow_builder_deluxe_toast: Optional[bool] = None
    workflow_builder_intro_modal_clicked_through: Optional[bool] = None
    workflow_builder_coachmarks: Optional[str] = None
    seen_gdrive_coachmark: Optional[bool] = None
    seen_first_install_coachmark: Optional[bool] = None
    seen_existing_install_coachmark: Optional[bool] = None
    seen_link_unfurl_coachmark: Optional[bool] = None
    file_picker_variant: Optional[int] = None
    open_quip_doc_in_flexpane: Optional[bool] = None
    saved_searches: Optional[str] = None
    huddles_variant: Optional[int] = None
    huddles_cc_by_default: Optional[bool] = None
    huddles_mute_by_default: Optional[bool] = None
    huddles_global_mute: Optional[bool] = None
    huddles_mini_panel: Optional[bool] = None
    huddles_set_status: Optional[bool] = None
    huddles_show_shouty_rooster: Optional[bool] = None
    huddles_disconnect_on_lock: Optional[bool] = None
    huddles_play_music_when_last: Optional[bool] = None
    huddles_allow_smart_notif: Optional[bool] = None
    huddles_reactions_play_sound: Optional[bool] = None
    huddles_reactions_read_out_loud: Optional[bool] = None
    huddles_chime_new_endpoints_check_completed: Optional[int] = None
    xws_sidebar_variant: Optional[int] = None
    inbox_views_workspace_filter: Optional[str] = None
    overloaded_message_enabled: Optional[bool] = None
    seen_highlights_coachmark: Optional[bool] = None
    seen_highlights_arrows_coachmark: Optional[bool] = None
    seen_highlights_warm_welcome: Optional[bool] = None
    seen_new_search_ui: Optional[bool] = None
    seen_channel_search: Optional[bool] = None
    seen_people_search: Optional[bool] = None
    seen_people_search_count: Optional[int] = None
    dismissed_scroll_search_tooltip_count: Optional[int] = None
    last_dismissed_scroll_search_tooltip_timestamp: Optional[int] = None
    has_used_quickswitcher_shortcut: Optional[bool] = None
    seen_quickswitcher_shortcut_tip_count: Optional[int] = None
    browsers_dismissed_channels_low_results_education: Optional[bool] = None
    browsers_seen_initial_channels_education: Optional[bool] = None
    browsers_dismissed_people_low_results_education: Optional[bool] = None
    browsers_seen_initial_people_education: Optional[bool] = None
    browsers_dismissed_user_groups_low_results_education: Optional[bool] = None
    browsers_seen_initial_user_groups_education: Optional[bool] = None
    browsers_dismissed_files_low_results_education: Optional[bool] = None
    browsers_seen_initial_files_education: Optional[bool] = None
    browsers_dismissed_initial_drafts_education: Optional[bool] = None
    browsers_seen_initial_drafts_education: Optional[bool] = None
    browsers_dismissed_initial_activity_education: Optional[bool] = None
    browsers_seen_initial_activity_education: Optional[bool] = None
    browsers_dismissed_initial_saved_education: Optional[bool] = None
    browsers_seen_initial_saved_education: Optional[bool] = None
    seen_edit_mode: Optional[bool] = None
    seen_edit_mode_edu: Optional[bool] = None
    xws_dismissed_education: Optional[bool] = None
    xws_seen_education: Optional[int] = None
    sidebar_pref_dismissed_tip: Optional[bool] = None
    a11_y_dyslexic: Optional[bool] = None
    a11_y_animations: Optional[bool] = None
    seen_keyboard_shortcuts_coachmark: Optional[bool] = None
    needs_initial_password_set: Optional[bool] = None
    lessons_enabled: Optional[bool] = None
    tractor_enabled: Optional[bool] = None
    tractor_experiment_group: Optional[str] = None
    opened_slackbot_dm: Optional[bool] = None
    newxp_seen_help_message: Optional[int] = None
    newxp_suggested_channels: Optional[str] = None
    onboarding_complete: Optional[bool] = None
    welcome_place_state: Optional[str] = None
    has_received_threaded_message: Optional[bool] = None
    joiner_notifications_muted: Optional[bool] = None
    invite_accepted_notifications_muted: Optional[bool] = None
    joiner_message_suggestion_dismissed: Optional[bool] = None
    dismissed_fullscreen_download_ssb_prompt: Optional[bool] = None
    dismissed_banner_download_ssb_prompt: Optional[bool] = None
    onboarding_state: Optional[int] = None
    whocanseethis_dm_mpdm_badge: Optional[bool] = None
    highlight_words: Optional[str] = None
    threads_everything: Optional[bool] = None
    no_text_in_notifications: Optional[bool] = None
    push_show_preview: Optional[bool] = None
    growls_enabled: Optional[bool] = None
    all_channels_loud: Optional[bool] = None
    push_dm_alert: Optional[bool] = None
    push_mention_alert: Optional[bool] = None
    push_everything: Optional[bool] = None
    push_idle_wait: Optional[int] = None
    push_sound: Optional[str] = None
    new_msg_snd: Optional[str] = None
    huddle_invite_sound: Optional[str] = None
    push_loud_channels: Optional[str] = None
    push_mention_channels: Optional[str] = None
    push_loud_channels_set: Optional[str] = None
    loud_channels: Optional[str] = None
    never_channels: Optional[str] = None
    loud_channels_set: Optional[str] = None
    at_channel_suppressed_channels: Optional[str] = None
    push_at_channel_suppressed_channels: Optional[str] = None
    muted_channels: Optional[str] = None
    all_notifications_prefs: Optional[str] = None
    growth_msg_limit_approaching_cta_count: Optional[int] = None
    growth_msg_limit_approaching_cta_ts: Optional[int] = None
    growth_msg_limit_reached_cta_count: Optional[int] = None
    growth_msg_limit_reached_cta_last_ts: Optional[int] = None
    growth_msg_limit_long_reached_cta_count: Optional[int] = None
    growth_msg_limit_long_reached_cta_last_ts: Optional[int] = None
    growth_msg_limit_sixty_day_banner_cta_count: Optional[int] = None
    growth_msg_limit_sixty_day_banner_cta_last_ts: Optional[int] = None
    growth_all_banners_prefs: Optional[str] = None
    analytics_upsell_coachmark_seen: Optional[bool] = None
    seen_app_space_coachmark: Optional[bool] = None
    seen_app_space_tutorial: Optional[bool] = None
    dismissed_app_launcher_welcome: Optional[bool] = None
    dismissed_app_launcher_limit: Optional[bool] = None
    dismissed_app_launcher_atlassian_promo: Optional[bool] = None
    enable_app_config_redesign: Optional[bool] = None
    dismissed_app_config_redesign_coachmark: Optional[bool] = None
    dismissed_app_manifest_description: Optional[bool] = None
    dismissed_app_manifest_coachmark: Optional[bool] = None
    purchaser: Optional[bool] = None
    seen_channel_email_tooltip: Optional[bool] = None
    show_ent_onboarding: Optional[bool] = None
    folders_enabled: Optional[bool] = None
    folder_data: Optional[str] = None
    seen_corporate_export_alert: Optional[bool] = None
    show_autocomplete_help: Optional[int] = None
    deprecation_toast_last_seen: Optional[int] = None
    deprecation_modal_last_seen: Optional[int] = None
    deprecation_banner_last_seen: Optional[int] = None
    iap1_lab: Optional[int] = None
    ia_top_nav_theme: Optional[str] = None
    ia_platform_actions_lab: Optional[int] = None
    activity_view: Optional[str] = None
    saved_view: Optional[str] = None
    seen_floating_sidebar_coachmark: Optional[bool] = None
    desktop_client_ids: Optional[str] = None
    failover_proxy_check_completed: Optional[int] = None
    chime_access_check_completed: Optional[int] = None
    mx_calendar_type: Optional[str] = None
    edge_upload_proxy_check_completed: Optional[int] = None
    app_subdomain_check_completed: Optional[int] = None
    add_prompt_interacted: Optional[bool] = None
    add_apps_prompt_dismissed: Optional[bool] = None
    add_channel_prompt_dismissed: Optional[bool] = None
    channel_sidebar_hide_invite: Optional[bool] = None
    channel_sidebar_hide_browse_dms_link: Optional[bool] = None
    in_prod_surveys_enabled: Optional[bool] = None
    connect_dm_early_access: Optional[bool] = None
    dismissed_installed_app_dm_suggestions: Optional[str] = None
    seen_contextual_message_shortcuts_modal: Optional[bool] = None
    seen_message_navigation_educational_toast: Optional[bool] = None
    contextual_message_shortcuts_modal_was_seen: Optional[bool] = None
    message_navigation_toast_was_seen: Optional[bool] = None
    up_to_browse_kb_shortcut: Optional[bool] = None
    set_a11_y_prefs_new_user: Optional[bool] = None
    a11_y_play_sound_for_incoming_dm: Optional[bool] = None
    a11_y_play_sound_for_sent_dm: Optional[bool] = None
    a11_y_read_out_incoming_dm: Optional[bool] = None
    a11_y_screen_reader_message_label_date_time_first: Optional[bool] = None
    should_show_contextual_help_for_conversation_navigation: Optional[bool] = None
    should_show_contextual_help_for_jump_to_conversation: Optional[bool] = None
    should_show_contextual_help_for_section_navigation: Optional[bool] = None
    should_show_contextual_help_for_thread_navigation: Optional[bool] = None
    should_show_unsend_message_confirmation: Optional[bool] = None
    channel_sections: Optional[str] = None
    show_quick_reactions: Optional[bool] = None
    user_customized_quick_reactions_display_feature: Optional[int] = None
    user_customized_quick_reactions_has_customized: Optional[bool] = None
    user_customized_quick_reactions_use_frequently_used_emoji: Optional[bool] = None
    reaction_notifications: Optional[str] = None
    has_received_mention_or_reaction: Optional[bool] = None
    has_starred_item: Optional[bool] = None
    has_drafted_message: Optional[bool] = None
    enable_mentions_and_reactions_view: Optional[bool] = None
    enable_reminders_view: Optional[bool] = None
    enable_saved_items_view: Optional[bool] = None
    enable_hq_view: Optional[bool] = None
    enable_all_dms_view: Optional[bool] = None
    enable_channel_browser_view: Optional[bool] = None
    enable_file_browser_view: Optional[bool] = None
    enable_people_browser_view: Optional[bool] = None
    enable_app_browser_view: Optional[bool] = None
    reached_all_dms_disclosure: Optional[bool] = None
    enable_slack_connect_view: Optional[bool] = None
    enable_slack_connect_view_2: Optional[int] = None
    has_acknowledged_shortcut_speedbump: Optional[bool] = None
    enable_media_captions: Optional[bool] = None
    media_playback_speed: Optional[int] = None
    media_muted: Optional[bool] = None
    media_volume: Optional[int] = None
    dismissed_connect_auto_approval_modal: Optional[str] = None
    tasks_view: Optional[str] = None
    show_sidebar_avatars: Optional[bool] = None
    has_dismissed_google_directory_coachmark: Optional[bool] = None
    seen_sc_page_banner: Optional[bool] = None
    seen_sc_menu_coachmark: Optional[bool] = None
    seen_sc_page: Optional[bool] = None
    dismissed_scdm_education: Optional[bool] = None
    seen_bookmarks_intro: Optional[bool] = None
    scdm_trial_offer_banner: Optional[str] = None
    identity_links_prefs: Optional[str] = None
    identity_links_global_prefs: Optional[str] = None
    seen_sections_unreads_only_prompt_count: Optional[int] = None
    last_seen_sections_unreads_only_prompt_timestamp: Optional[int] = None
    notifications_view: Optional[str] = None
    progressive_disclosure_state: Optional[str] = None
    suggestions_request_id: Optional[str] = None
    allowed_unfurl_senders: Optional[str] = None
    ia_details_coachmark_seen: Optional[bool] = None
    hide_external_members_sharing_speed_bump: Optional[bool] = None
    who_can_share_contact_card: Optional[str] = None
    slack_connect_invite_should_badge_sidebar: Optional[bool] = None
    phc_dismissed: Optional[str] = None
    dismissed_gov_slack_first_time_popup: Optional[bool] = None
    mobile_channel_list_sort: Optional[str] = None
    user_expectations_survey_last_trigger_attempt: Optional[int] = None
    tz: Optional[str] = None
    locales_enabled: Optional[LocalesEnabled] = None
    phc_viewed: Optional[str] = None
    seen_a11_y_pref_setup_coachmark: Optional[bool] = None
    enable_file_browser_view_for_docs: Optional[bool] = None
    enable_shortcuts_view: Optional[bool] = None
    show_gov_slack_context_bar_banner: Optional[bool] = None
    who_can_see_account_by_searching_email: Optional[str] = None
    contextual_help_reset_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SelfPrefs':
        assert isinstance(obj, dict)
        underline_links = from_union([from_bool, from_none], obj.get("underline_links"))
        user_colors = from_union([from_str, from_none], obj.get("user_colors"))
        color_names_in_list = from_union([from_bool, from_none], obj.get("color_names_in_list"))
        email_alerts = from_union([from_str, from_none], obj.get("email_alerts"))
        email_alerts_sleep_until = from_union([from_int, from_none], obj.get("email_alerts_sleep_until"))
        email_tips = from_union([from_bool, from_none], obj.get("email_tips"))
        email_weekly = from_union([from_bool, from_none], obj.get("email_weekly"))
        email_offers = from_union([from_bool, from_none], obj.get("email_offers"))
        email_research = from_union([from_bool, from_none], obj.get("email_research"))
        email_developer = from_union([from_bool, from_none], obj.get("email_developer"))
        welcome_message_hidden = from_union([from_bool, from_none], obj.get("welcome_message_hidden"))
        search_sort = from_union([from_str, from_none], obj.get("search_sort"))
        search_file_sort = from_union([from_str, from_none], obj.get("search_file_sort"))
        search_channel_sort = from_union([from_str, from_none], obj.get("search_channel_sort"))
        search_people_sort = from_union([from_str, from_none], obj.get("search_people_sort"))
        expand_inline_imgs = from_union([from_bool, from_none], obj.get("expand_inline_imgs"))
        expand_internal_inline_imgs = from_union([from_bool, from_none], obj.get("expand_internal_inline_imgs"))
        expand_snippets = from_union([from_bool, from_none], obj.get("expand_snippets"))
        posts_formatting_guide = from_union([from_bool, from_none], obj.get("posts_formatting_guide"))
        seen_welcome_2 = from_union([from_bool, from_none], obj.get("seen_welcome_2"))
        seen_ssb_prompt = from_union([from_bool, from_none], obj.get("seen_ssb_prompt"))
        spaces_new_xp_banner_dismissed = from_union([from_bool, from_none], obj.get("spaces_new_xp_banner_dismissed"))
        search_only_my_channels = from_union([from_bool, from_none], obj.get("search_only_my_channels"))
        search_only_current_team = from_union([from_bool, from_none], obj.get("search_only_current_team"))
        search_hide_my_channels = from_union([from_bool, from_none], obj.get("search_hide_my_channels"))
        search_only_show_online = from_union([from_bool, from_none], obj.get("search_only_show_online"))
        search_hide_deactivated_users = from_union([from_bool, from_none], obj.get("search_hide_deactivated_users"))
        emoji_mode = from_union([from_str, from_none], obj.get("emoji_mode"))
        emoji_use = from_union([from_str, from_none], obj.get("emoji_use"))
        emoji_use_org = from_union([from_str, from_none], obj.get("emoji_use_org"))
        has_invited = from_union([from_bool, from_none], obj.get("has_invited"))
        has_uploaded = from_union([from_bool, from_none], obj.get("has_uploaded"))
        has_created_channel = from_union([from_bool, from_none], obj.get("has_created_channel"))
        has_created_channel_section = from_union([from_bool, from_none], obj.get("has_created_channel_section"))
        has_searched = from_union([from_bool, from_none], obj.get("has_searched"))
        search_exclude_channels = from_union([from_str, from_none], obj.get("search_exclude_channels"))
        messages_theme = from_union([from_str, from_none], obj.get("messages_theme"))
        webapp_spellcheck = from_union([from_bool, from_none], obj.get("webapp_spellcheck"))
        no_joined_overlays = from_union([from_bool, from_none], obj.get("no_joined_overlays"))
        no_created_overlays = from_union([from_bool, from_none], obj.get("no_created_overlays"))
        dropbox_enabled = from_union([from_bool, from_none], obj.get("dropbox_enabled"))
        seen_domain_invite_reminder = from_union([from_bool, from_none], obj.get("seen_domain_invite_reminder"))
        seen_member_invite_reminder = from_union([from_bool, from_none], obj.get("seen_member_invite_reminder"))
        mute_sounds = from_union([from_bool, from_none], obj.get("mute_sounds"))
        arrow_history = from_union([from_bool, from_none], obj.get("arrow_history"))
        tab_ui_return_selects = from_union([from_bool, from_none], obj.get("tab_ui_return_selects"))
        obey_inline_img_limit = from_union([from_bool, from_none], obj.get("obey_inline_img_limit"))
        require_at = from_union([from_bool, from_none], obj.get("require_at"))
        ssb_space_window = from_union([from_str, from_none], obj.get("ssb_space_window"))
        mac_ssb_bounce = from_union([from_str, from_none], obj.get("mac_ssb_bounce"))
        mac_ssb_bullet = from_union([from_bool, from_none], obj.get("mac_ssb_bullet"))
        expand_non_media_attachments = from_union([from_bool, from_none], obj.get("expand_non_media_attachments"))
        show_typing = from_union([from_bool, from_none], obj.get("show_typing"))
        pagekeys_handled = from_union([from_bool, from_none], obj.get("pagekeys_handled"))
        last_snippet_type = from_union([from_str, from_none], obj.get("last_snippet_type"))
        display_real_names_override = from_union([from_int, from_none], obj.get("display_real_names_override"))
        display_display_names = from_union([from_bool, from_none], obj.get("display_display_names"))
        time24 = from_union([from_bool, from_none], obj.get("time24"))
        enter_is_special_in_tbt = from_union([from_bool, from_none], obj.get("enter_is_special_in_tbt"))
        msg_input_send_btn = from_union([from_bool, from_none], obj.get("msg_input_send_btn"))
        msg_input_send_btn_auto_set = from_union([from_bool, from_none], obj.get("msg_input_send_btn_auto_set"))
        msg_input_sticky_composer = from_union([from_bool, from_none], obj.get("msg_input_sticky_composer"))
        composer_nux = from_union([from_str, from_none], obj.get("composer_nux"))
        graphic_emoticons = from_union([from_bool, from_none], obj.get("graphic_emoticons"))
        convert_emoticons = from_union([from_bool, from_none], obj.get("convert_emoticons"))
        ss_emojis = from_union([from_bool, from_none], obj.get("ss_emojis"))
        seen_onboarding_start = from_union([from_bool, from_none], obj.get("seen_onboarding_start"))
        onboarding_cancelled = from_union([from_bool, from_none], obj.get("onboarding_cancelled"))
        seen_onboarding_slackbot_conversation = from_union([from_bool, from_none], obj.get("seen_onboarding_slackbot_conversation"))
        seen_onboarding_channels = from_union([from_bool, from_none], obj.get("seen_onboarding_channels"))
        seen_onboarding_direct_messages = from_union([from_bool, from_none], obj.get("seen_onboarding_direct_messages"))
        seen_onboarding_invites = from_union([from_bool, from_none], obj.get("seen_onboarding_invites"))
        seen_onboarding_search = from_union([from_bool, from_none], obj.get("seen_onboarding_search"))
        seen_onboarding_recent_mentions = from_union([from_bool, from_none], obj.get("seen_onboarding_recent_mentions"))
        seen_onboarding_starred_items = from_union([from_bool, from_none], obj.get("seen_onboarding_starred_items"))
        seen_onboarding_private_groups = from_union([from_bool, from_none], obj.get("seen_onboarding_private_groups"))
        seen_onboarding_banner = from_union([from_bool, from_none], obj.get("seen_onboarding_banner"))
        onboarding_slackbot_conversation_step = from_union([from_int, from_none], obj.get("onboarding_slackbot_conversation_step"))
        set_tz_automatically = from_union([from_bool, from_none], obj.get("set_tz_automatically"))
        suppress_link_warning = from_union([from_bool, from_none], obj.get("suppress_link_warning"))
        suppress_external_invites_from_compose_warning = from_union([from_bool, from_none], obj.get("suppress_external_invites_from_compose_warning"))
        seen_emoji_pack_cta = from_union([from_int, from_none], obj.get("seen_emoji_pack_cta"))
        seen_emoji_pack_dialog = from_union([from_bool, from_none], obj.get("seen_emoji_pack_dialog"))
        seen_schedule_send_coachmark = from_union([from_bool, from_none], obj.get("seen_schedule_send_coachmark"))
        emoji_packs_most_recent_available_time = from_union([from_int, from_none], obj.get("emoji_packs_most_recent_available_time"))
        emoji_packs_clicked_picker_cta = from_union([from_bool, from_none], obj.get("emoji_packs_clicked_picker_cta"))
        emoji_packs_clicked_picker_post_install_cta = from_union([from_bool, from_none], obj.get("emoji_packs_clicked_picker_post_install_cta"))
        emoji_packs_clicked_collection_cta = from_union([from_bool, from_none], obj.get("emoji_packs_clicked_collection_cta"))
        dnd_enabled = from_union([from_bool, from_none], obj.get("dnd_enabled"))
        dnd_start_hour = from_union([from_str, from_none], obj.get("dnd_start_hour"))
        dnd_end_hour = from_union([from_str, from_none], obj.get("dnd_end_hour"))
        dnd_before_monday = from_union([from_str, from_none], obj.get("dnd_before_monday"))
        dnd_after_monday = from_union([from_str, from_none], obj.get("dnd_after_monday"))
        dnd_enabled_monday = from_union([from_str, from_none], obj.get("dnd_enabled_monday"))
        dnd_before_tuesday = from_union([from_str, from_none], obj.get("dnd_before_tuesday"))
        dnd_after_tuesday = from_union([from_str, from_none], obj.get("dnd_after_tuesday"))
        dnd_enabled_tuesday = from_union([from_str, from_none], obj.get("dnd_enabled_tuesday"))
        dnd_before_wednesday = from_union([from_str, from_none], obj.get("dnd_before_wednesday"))
        dnd_after_wednesday = from_union([from_str, from_none], obj.get("dnd_after_wednesday"))
        dnd_enabled_wednesday = from_union([from_str, from_none], obj.get("dnd_enabled_wednesday"))
        dnd_before_thursday = from_union([from_str, from_none], obj.get("dnd_before_thursday"))
        dnd_after_thursday = from_union([from_str, from_none], obj.get("dnd_after_thursday"))
        dnd_enabled_thursday = from_union([from_str, from_none], obj.get("dnd_enabled_thursday"))
        dnd_before_friday = from_union([from_str, from_none], obj.get("dnd_before_friday"))
        dnd_after_friday = from_union([from_str, from_none], obj.get("dnd_after_friday"))
        dnd_enabled_friday = from_union([from_str, from_none], obj.get("dnd_enabled_friday"))
        dnd_before_saturday = from_union([from_str, from_none], obj.get("dnd_before_saturday"))
        dnd_after_saturday = from_union([from_str, from_none], obj.get("dnd_after_saturday"))
        dnd_enabled_saturday = from_union([from_str, from_none], obj.get("dnd_enabled_saturday"))
        dnd_before_sunday = from_union([from_str, from_none], obj.get("dnd_before_sunday"))
        dnd_after_sunday = from_union([from_str, from_none], obj.get("dnd_after_sunday"))
        dnd_enabled_sunday = from_union([from_str, from_none], obj.get("dnd_enabled_sunday"))
        dnd_days = from_union([from_str, from_none], obj.get("dnd_days"))
        dnd_weekdays_off_allday = from_union([from_bool, from_none], obj.get("dnd_weekdays_off_allday"))
        reminder_notification_time = from_union([from_str, from_none], obj.get("reminder_notification_time"))
        dnd_custom_new_badge_seen = from_union([from_bool, from_none], obj.get("dnd_custom_new_badge_seen"))
        dnd_notification_schedule_new_badge_seen = from_union([from_bool, from_none], obj.get("dnd_notification_schedule_new_badge_seen"))
        notification_center_filters = from_union([from_str, from_none], obj.get("notification_center_filters"))
        calls_survey_last_seen = from_union([from_str, from_none], obj.get("calls_survey_last_seen"))
        huddle_survey_last_seen = from_union([from_str, from_none], obj.get("huddle_survey_last_seen"))
        sidebar_behavior = from_union([from_str, from_none], obj.get("sidebar_behavior"))
        channel_sort = from_union([from_str, from_none], obj.get("channel_sort"))
        separate_private_channels = from_union([from_bool, from_none], obj.get("separate_private_channels"))
        separate_shared_channels = from_union([from_bool, from_none], obj.get("separate_shared_channels"))
        sidebar_theme = from_union([from_str, from_none], obj.get("sidebar_theme"))
        sidebar_theme_custom_values = from_union([from_str, from_none], obj.get("sidebar_theme_custom_values"))
        no_invites_widget_in_sidebar = from_union([from_bool, from_none], obj.get("no_invites_widget_in_sidebar"))
        no_omnibox_in_channels = from_union([from_bool, from_none], obj.get("no_omnibox_in_channels"))
        k_key_omnibox_auto_hide_count = from_union([from_int, from_none], obj.get("k_key_omnibox_auto_hide_count"))
        show_sidebar_quickswitcher_button = from_union([from_bool, from_none], obj.get("show_sidebar_quickswitcher_button"))
        ent_org_wide_channels_sidebar = from_union([from_bool, from_none], obj.get("ent_org_wide_channels_sidebar"))
        mark_msgs_read_immediately = from_union([from_bool, from_none], obj.get("mark_msgs_read_immediately"))
        start_scroll_at_oldest = from_union([from_bool, from_none], obj.get("start_scroll_at_oldest"))
        snippet_editor_wrap_long_lines = from_union([from_bool, from_none], obj.get("snippet_editor_wrap_long_lines"))
        ls_disabled = from_union([from_bool, from_none], obj.get("ls_disabled"))
        f_key_search = from_union([from_bool, from_none], obj.get("f_key_search"))
        k_key_omnibox = from_union([from_bool, from_none], obj.get("k_key_omnibox"))
        prompted_for_email_disabling = from_union([from_bool, from_none], obj.get("prompted_for_email_disabling"))
        no_macelectron_banner = from_union([from_bool, from_none], obj.get("no_macelectron_banner"))
        no_macssb1_banner = from_union([from_bool, from_none], obj.get("no_macssb1_banner"))
        no_macssb2_banner = from_union([from_bool, from_none], obj.get("no_macssb2_banner"))
        no_winssb1_banner = from_union([from_bool, from_none], obj.get("no_winssb1_banner"))
        hide_user_group_info_pane = from_union([from_bool, from_none], obj.get("hide_user_group_info_pane"))
        mentions_exclude_at_user_groups = from_union([from_bool, from_none], obj.get("mentions_exclude_at_user_groups"))
        mentions_exclude_reactions = from_union([from_bool, from_none], obj.get("mentions_exclude_reactions"))
        privacy_policy_seen = from_union([from_bool, from_none], obj.get("privacy_policy_seen"))
        enterprise_migration_seen = from_union([from_bool, from_none], obj.get("enterprise_migration_seen"))
        search_exclude_bots = from_union([from_bool, from_none], obj.get("search_exclude_bots"))
        load_lato_2 = from_union([from_bool, from_none], obj.get("load_lato_2"))
        fuller_timestamps = from_union([from_bool, from_none], obj.get("fuller_timestamps"))
        last_seen_at_channel_warning = from_union([from_int, from_none], obj.get("last_seen_at_channel_warning"))
        emoji_autocomplete_big = from_union([from_bool, from_none], obj.get("emoji_autocomplete_big"))
        two_factor_auth_enabled = from_union([from_bool, from_none], obj.get("two_factor_auth_enabled"))
        hide_hex_swatch = from_union([from_bool, from_none], obj.get("hide_hex_swatch"))
        show_jumper_scores = from_union([from_bool, from_none], obj.get("show_jumper_scores"))
        enterprise_mdm_custom_msg = from_union([from_str, from_none], obj.get("enterprise_mdm_custom_msg"))
        client_logs_pri = from_union([from_str, from_none], obj.get("client_logs_pri"))
        flannel_server_pool = from_union([from_str, from_none], obj.get("flannel_server_pool"))
        mentions_exclude_at_channels = from_union([from_bool, from_none], obj.get("mentions_exclude_at_channels"))
        confirm_clear_all_unreads = from_union([from_bool, from_none], obj.get("confirm_clear_all_unreads"))
        confirm_user_marked_away = from_union([from_bool, from_none], obj.get("confirm_user_marked_away"))
        box_enabled = from_union([from_bool, from_none], obj.get("box_enabled"))
        seen_single_emoji_msg = from_union([from_bool, from_none], obj.get("seen_single_emoji_msg"))
        confirm_sh_call_start = from_union([from_bool, from_none], obj.get("confirm_sh_call_start"))
        preferred_skin_tone = from_union([from_str, from_none], obj.get("preferred_skin_tone"))
        show_all_skin_tones = from_union([from_bool, from_none], obj.get("show_all_skin_tones"))
        whats_new_read = from_union([from_int, from_none], obj.get("whats_new_read"))
        help_modal_open_timestamp = from_union([from_int, from_none], obj.get("help_modal_open_timestamp"))
        help_modal_consult_banner_dismissed = from_union([from_bool, from_none], obj.get("help_modal_consult_banner_dismissed"))
        help_flexpane_slack_connect_card_seen = from_union([from_bool, from_none], obj.get("help_flexpane_slack_connect_card_seen"))
        help_flexpane_clips_card_seen = from_union([from_bool, from_none], obj.get("help_flexpane_clips_card_seen"))
        help_menu_open_timestamp = from_union([from_int, from_none], obj.get("help_menu_open_timestamp"))
        frecency_jumper = from_union([from_str, from_none], obj.get("frecency_jumper"))
        frecency_ent_jumper = from_union([from_str, from_none], obj.get("frecency_ent_jumper"))
        jumbomoji = from_union([from_bool, from_none], obj.get("jumbomoji"))
        newxp_seen_last_message = from_union([from_int, from_none], obj.get("newxp_seen_last_message"))
        show_memory_instrument = from_union([from_bool, from_none], obj.get("show_memory_instrument"))
        enable_unread_view = from_union([from_bool, from_none], obj.get("enable_unread_view"))
        seen_unread_view_coachmark = from_union([from_bool, from_none], obj.get("seen_unread_view_coachmark"))
        seen_connect_dm_coachmark = from_union([from_bool, from_none], obj.get("seen_connect_dm_coachmark"))
        seen_connect_section_coachmark = from_union([from_bool, from_none], obj.get("seen_connect_section_coachmark"))
        should_show_connect_section = from_union([from_bool, from_none], obj.get("should_show_connect_section"))
        enable_react_emoji_picker = from_union([from_bool, from_none], obj.get("enable_react_emoji_picker"))
        seen_custom_status_badge = from_union([from_bool, from_none], obj.get("seen_custom_status_badge"))
        seen_custom_status_callout = from_union([from_bool, from_none], obj.get("seen_custom_status_callout"))
        seen_custom_status_expiration_badge = from_union([from_bool, from_none], obj.get("seen_custom_status_expiration_badge"))
        used_custom_status_kb_shortcut = from_union([from_bool, from_none], obj.get("used_custom_status_kb_shortcut"))
        seen_guest_admin_slackbot_announcement = from_union([from_bool, from_none], obj.get("seen_guest_admin_slackbot_announcement"))
        seen_threads_notification_banner = from_union([from_bool, from_none], obj.get("seen_threads_notification_banner"))
        seen_name_tagging_coachmark = from_union([from_bool, from_none], obj.get("seen_name_tagging_coachmark"))
        all_unreads_sort_order = from_union([from_str, from_none], obj.get("all_unreads_sort_order"))
        all_unreads_section_filter = from_union([from_str, from_none], obj.get("all_unreads_section_filter"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        seen_intl_channel_names_coachmark = from_union([from_bool, from_none], obj.get("seen_intl_channel_names_coachmark"))
        seen_p3_locale_change_message_ko_kr = from_union([from_int, from_none], obj.get("seen_p3_locale_change_message_ko_kr"))
        seen_toast_new_locale_launch = from_union([from_str, from_none], obj.get("seen_toast_new_locale_launch"))
        seen_toast_new_locale_launch_ts = from_union([from_int, from_none], obj.get("seen_toast_new_locale_launch_ts"))
        seen_locale_change_message = from_union([from_int, from_none], obj.get("seen_locale_change_message"))
        seen_japanese_locale_change_message = from_union([from_bool, from_none], obj.get("seen_japanese_locale_change_message"))
        seen_shared_channels_coachmark = from_union([from_bool, from_none], obj.get("seen_shared_channels_coachmark"))
        seen_shared_channels_opt_in_change_message = from_union([from_bool, from_none], obj.get("seen_shared_channels_opt_in_change_message"))
        has_recently_shared_a_channel = from_union([from_bool, from_none], obj.get("has_recently_shared_a_channel"))
        seen_channel_browser_admin_coachmark = from_union([from_bool, from_none], obj.get("seen_channel_browser_admin_coachmark"))
        seen_administration_menu = from_union([from_bool, from_none], obj.get("seen_administration_menu"))
        seen_drafts_section_coachmark = from_union([from_bool, from_none], obj.get("seen_drafts_section_coachmark"))
        seen_emoji_update_overlay_coachmark = from_union([from_bool, from_none], obj.get("seen_emoji_update_overlay_coachmark"))
        seen_sonic_deluxe_toast = from_union([from_int, from_none], obj.get("seen_sonic_deluxe_toast"))
        seen_wysiwyg_deluxe_toast = from_union([from_bool, from_none], obj.get("seen_wysiwyg_deluxe_toast"))
        seen_markdown_paste_toast = from_union([from_int, from_none], obj.get("seen_markdown_paste_toast"))
        seen_markdown_paste_shortcut = from_union([from_int, from_none], obj.get("seen_markdown_paste_shortcut"))
        seen_ia_education = from_union([from_bool, from_none], obj.get("seen_ia_education"))
        show_ia_tour_relaunch = from_union([from_int, from_none], obj.get("show_ia_tour_relaunch"))
        plain_text_mode = from_union([from_bool, from_none], obj.get("plain_text_mode"))
        show_shared_channels_education_banner = from_union([from_bool, from_none], obj.get("show_shared_channels_education_banner"))
        ia_slackbot_survey_timestamp_48_h = from_union([from_int, from_none], obj.get("ia_slackbot_survey_timestamp_48h"))
        ia_slackbot_survey_timestamp_7_d = from_union([from_int, from_none], obj.get("ia_slackbot_survey_timestamp_7d"))
        enable_streamline_view = from_union([from_bool, from_none], obj.get("enable_streamline_view"))
        enable_sent_view = from_union([from_bool, from_none], obj.get("enable_sent_view"))
        allow_calls_to_set_current_status = from_union([from_bool, from_none], obj.get("allow_calls_to_set_current_status"))
        in_interactive_mas_migration_flow = from_union([from_bool, from_none], obj.get("in_interactive_mas_migration_flow"))
        sunset_interactive_message_views = from_union([from_int, from_none], obj.get("sunset_interactive_message_views"))
        shdep_promo_code_submitted = from_union([from_bool, from_none], obj.get("shdep_promo_code_submitted"))
        seen_shdep_slackbot_message = from_union([from_bool, from_none], obj.get("seen_shdep_slackbot_message"))
        seen_calls_interactive_coachmark = from_union([from_bool, from_none], obj.get("seen_calls_interactive_coachmark"))
        allow_cmd_tab_iss = from_union([from_bool, from_none], obj.get("allow_cmd_tab_iss"))
        join_calls_device_settings = from_union([from_str, from_none], obj.get("join_calls_device_settings"))
        calls_disconnect_on_lock = from_union([from_bool, from_none], obj.get("calls_disconnect_on_lock"))
        seen_workflow_builder_deluxe_toast = from_union([from_bool, from_none], obj.get("seen_workflow_builder_deluxe_toast"))
        workflow_builder_intro_modal_clicked_through = from_union([from_bool, from_none], obj.get("workflow_builder_intro_modal_clicked_through"))
        workflow_builder_coachmarks = from_union([from_str, from_none], obj.get("workflow_builder_coachmarks"))
        seen_gdrive_coachmark = from_union([from_bool, from_none], obj.get("seen_gdrive_coachmark"))
        seen_first_install_coachmark = from_union([from_bool, from_none], obj.get("seen_first_install_coachmark"))
        seen_existing_install_coachmark = from_union([from_bool, from_none], obj.get("seen_existing_install_coachmark"))
        seen_link_unfurl_coachmark = from_union([from_bool, from_none], obj.get("seen_link_unfurl_coachmark"))
        file_picker_variant = from_union([from_int, from_none], obj.get("file_picker_variant"))
        open_quip_doc_in_flexpane = from_union([from_bool, from_none], obj.get("open_quip_doc_in_flexpane"))
        saved_searches = from_union([from_str, from_none], obj.get("saved_searches"))
        huddles_variant = from_union([from_int, from_none], obj.get("huddles_variant"))
        huddles_cc_by_default = from_union([from_bool, from_none], obj.get("huddles_cc_by_default"))
        huddles_mute_by_default = from_union([from_bool, from_none], obj.get("huddles_mute_by_default"))
        huddles_global_mute = from_union([from_bool, from_none], obj.get("huddles_global_mute"))
        huddles_mini_panel = from_union([from_bool, from_none], obj.get("huddles_mini_panel"))
        huddles_set_status = from_union([from_bool, from_none], obj.get("huddles_set_status"))
        huddles_show_shouty_rooster = from_union([from_bool, from_none], obj.get("huddles_show_shouty_rooster"))
        huddles_disconnect_on_lock = from_union([from_bool, from_none], obj.get("huddles_disconnect_on_lock"))
        huddles_play_music_when_last = from_union([from_bool, from_none], obj.get("huddles_play_music_when_last"))
        huddles_allow_smart_notif = from_union([from_bool, from_none], obj.get("huddles_allow_smart_notif"))
        huddles_reactions_play_sound = from_union([from_bool, from_none], obj.get("huddles_reactions_play_sound"))
        huddles_reactions_read_out_loud = from_union([from_bool, from_none], obj.get("huddles_reactions_read_out_loud"))
        huddles_chime_new_endpoints_check_completed = from_union([from_int, from_none], obj.get("huddles_chime_new_endpoints_check_completed"))
        xws_sidebar_variant = from_union([from_int, from_none], obj.get("xws_sidebar_variant"))
        inbox_views_workspace_filter = from_union([from_str, from_none], obj.get("inbox_views_workspace_filter"))
        overloaded_message_enabled = from_union([from_bool, from_none], obj.get("overloaded_message_enabled"))
        seen_highlights_coachmark = from_union([from_bool, from_none], obj.get("seen_highlights_coachmark"))
        seen_highlights_arrows_coachmark = from_union([from_bool, from_none], obj.get("seen_highlights_arrows_coachmark"))
        seen_highlights_warm_welcome = from_union([from_bool, from_none], obj.get("seen_highlights_warm_welcome"))
        seen_new_search_ui = from_union([from_bool, from_none], obj.get("seen_new_search_ui"))
        seen_channel_search = from_union([from_bool, from_none], obj.get("seen_channel_search"))
        seen_people_search = from_union([from_bool, from_none], obj.get("seen_people_search"))
        seen_people_search_count = from_union([from_int, from_none], obj.get("seen_people_search_count"))
        dismissed_scroll_search_tooltip_count = from_union([from_int, from_none], obj.get("dismissed_scroll_search_tooltip_count"))
        last_dismissed_scroll_search_tooltip_timestamp = from_union([from_int, from_none], obj.get("last_dismissed_scroll_search_tooltip_timestamp"))
        has_used_quickswitcher_shortcut = from_union([from_bool, from_none], obj.get("has_used_quickswitcher_shortcut"))
        seen_quickswitcher_shortcut_tip_count = from_union([from_int, from_none], obj.get("seen_quickswitcher_shortcut_tip_count"))
        browsers_dismissed_channels_low_results_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_channels_low_results_education"))
        browsers_seen_initial_channels_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_channels_education"))
        browsers_dismissed_people_low_results_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_people_low_results_education"))
        browsers_seen_initial_people_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_people_education"))
        browsers_dismissed_user_groups_low_results_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_user_groups_low_results_education"))
        browsers_seen_initial_user_groups_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_user_groups_education"))
        browsers_dismissed_files_low_results_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_files_low_results_education"))
        browsers_seen_initial_files_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_files_education"))
        browsers_dismissed_initial_drafts_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_initial_drafts_education"))
        browsers_seen_initial_drafts_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_drafts_education"))
        browsers_dismissed_initial_activity_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_initial_activity_education"))
        browsers_seen_initial_activity_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_activity_education"))
        browsers_dismissed_initial_saved_education = from_union([from_bool, from_none], obj.get("browsers_dismissed_initial_saved_education"))
        browsers_seen_initial_saved_education = from_union([from_bool, from_none], obj.get("browsers_seen_initial_saved_education"))
        seen_edit_mode = from_union([from_bool, from_none], obj.get("seen_edit_mode"))
        seen_edit_mode_edu = from_union([from_bool, from_none], obj.get("seen_edit_mode_edu"))
        xws_dismissed_education = from_union([from_bool, from_none], obj.get("xws_dismissed_education"))
        xws_seen_education = from_union([from_int, from_none], obj.get("xws_seen_education"))
        sidebar_pref_dismissed_tip = from_union([from_bool, from_none], obj.get("sidebar_pref_dismissed_tip"))
        a11_y_dyslexic = from_union([from_bool, from_none], obj.get("a11y_dyslexic"))
        a11_y_animations = from_union([from_bool, from_none], obj.get("a11y_animations"))
        seen_keyboard_shortcuts_coachmark = from_union([from_bool, from_none], obj.get("seen_keyboard_shortcuts_coachmark"))
        needs_initial_password_set = from_union([from_bool, from_none], obj.get("needs_initial_password_set"))
        lessons_enabled = from_union([from_bool, from_none], obj.get("lessons_enabled"))
        tractor_enabled = from_union([from_bool, from_none], obj.get("tractor_enabled"))
        tractor_experiment_group = from_union([from_str, from_none], obj.get("tractor_experiment_group"))
        opened_slackbot_dm = from_union([from_bool, from_none], obj.get("opened_slackbot_dm"))
        newxp_seen_help_message = from_union([from_int, from_none], obj.get("newxp_seen_help_message"))
        newxp_suggested_channels = from_union([from_str, from_none], obj.get("newxp_suggested_channels"))
        onboarding_complete = from_union([from_bool, from_none], obj.get("onboarding_complete"))
        welcome_place_state = from_union([from_str, from_none], obj.get("welcome_place_state"))
        has_received_threaded_message = from_union([from_bool, from_none], obj.get("has_received_threaded_message"))
        joiner_notifications_muted = from_union([from_bool, from_none], obj.get("joiner_notifications_muted"))
        invite_accepted_notifications_muted = from_union([from_bool, from_none], obj.get("invite_accepted_notifications_muted"))
        joiner_message_suggestion_dismissed = from_union([from_bool, from_none], obj.get("joiner_message_suggestion_dismissed"))
        dismissed_fullscreen_download_ssb_prompt = from_union([from_bool, from_none], obj.get("dismissed_fullscreen_download_ssb_prompt"))
        dismissed_banner_download_ssb_prompt = from_union([from_bool, from_none], obj.get("dismissed_banner_download_ssb_prompt"))
        onboarding_state = from_union([from_int, from_none], obj.get("onboarding_state"))
        whocanseethis_dm_mpdm_badge = from_union([from_bool, from_none], obj.get("whocanseethis_dm_mpdm_badge"))
        highlight_words = from_union([from_str, from_none], obj.get("highlight_words"))
        threads_everything = from_union([from_bool, from_none], obj.get("threads_everything"))
        no_text_in_notifications = from_union([from_bool, from_none], obj.get("no_text_in_notifications"))
        push_show_preview = from_union([from_bool, from_none], obj.get("push_show_preview"))
        growls_enabled = from_union([from_bool, from_none], obj.get("growls_enabled"))
        all_channels_loud = from_union([from_bool, from_none], obj.get("all_channels_loud"))
        push_dm_alert = from_union([from_bool, from_none], obj.get("push_dm_alert"))
        push_mention_alert = from_union([from_bool, from_none], obj.get("push_mention_alert"))
        push_everything = from_union([from_bool, from_none], obj.get("push_everything"))
        push_idle_wait = from_union([from_int, from_none], obj.get("push_idle_wait"))
        push_sound = from_union([from_str, from_none], obj.get("push_sound"))
        new_msg_snd = from_union([from_str, from_none], obj.get("new_msg_snd"))
        huddle_invite_sound = from_union([from_str, from_none], obj.get("huddle_invite_sound"))
        push_loud_channels = from_union([from_str, from_none], obj.get("push_loud_channels"))
        push_mention_channels = from_union([from_str, from_none], obj.get("push_mention_channels"))
        push_loud_channels_set = from_union([from_str, from_none], obj.get("push_loud_channels_set"))
        loud_channels = from_union([from_str, from_none], obj.get("loud_channels"))
        never_channels = from_union([from_str, from_none], obj.get("never_channels"))
        loud_channels_set = from_union([from_str, from_none], obj.get("loud_channels_set"))
        at_channel_suppressed_channels = from_union([from_str, from_none], obj.get("at_channel_suppressed_channels"))
        push_at_channel_suppressed_channels = from_union([from_str, from_none], obj.get("push_at_channel_suppressed_channels"))
        muted_channels = from_union([from_str, from_none], obj.get("muted_channels"))
        all_notifications_prefs = from_union([from_str, from_none], obj.get("all_notifications_prefs"))
        growth_msg_limit_approaching_cta_count = from_union([from_int, from_none], obj.get("growth_msg_limit_approaching_cta_count"))
        growth_msg_limit_approaching_cta_ts = from_union([from_int, from_none], obj.get("growth_msg_limit_approaching_cta_ts"))
        growth_msg_limit_reached_cta_count = from_union([from_int, from_none], obj.get("growth_msg_limit_reached_cta_count"))
        growth_msg_limit_reached_cta_last_ts = from_union([from_int, from_none], obj.get("growth_msg_limit_reached_cta_last_ts"))
        growth_msg_limit_long_reached_cta_count = from_union([from_int, from_none], obj.get("growth_msg_limit_long_reached_cta_count"))
        growth_msg_limit_long_reached_cta_last_ts = from_union([from_int, from_none], obj.get("growth_msg_limit_long_reached_cta_last_ts"))
        growth_msg_limit_sixty_day_banner_cta_count = from_union([from_int, from_none], obj.get("growth_msg_limit_sixty_day_banner_cta_count"))
        growth_msg_limit_sixty_day_banner_cta_last_ts = from_union([from_int, from_none], obj.get("growth_msg_limit_sixty_day_banner_cta_last_ts"))
        growth_all_banners_prefs = from_union([from_str, from_none], obj.get("growth_all_banners_prefs"))
        analytics_upsell_coachmark_seen = from_union([from_bool, from_none], obj.get("analytics_upsell_coachmark_seen"))
        seen_app_space_coachmark = from_union([from_bool, from_none], obj.get("seen_app_space_coachmark"))
        seen_app_space_tutorial = from_union([from_bool, from_none], obj.get("seen_app_space_tutorial"))
        dismissed_app_launcher_welcome = from_union([from_bool, from_none], obj.get("dismissed_app_launcher_welcome"))
        dismissed_app_launcher_limit = from_union([from_bool, from_none], obj.get("dismissed_app_launcher_limit"))
        dismissed_app_launcher_atlassian_promo = from_union([from_bool, from_none], obj.get("dismissed_app_launcher_atlassian_promo"))
        enable_app_config_redesign = from_union([from_bool, from_none], obj.get("enable_app_config_redesign"))
        dismissed_app_config_redesign_coachmark = from_union([from_bool, from_none], obj.get("dismissed_app_config_redesign_coachmark"))
        dismissed_app_manifest_description = from_union([from_bool, from_none], obj.get("dismissed_app_manifest_description"))
        dismissed_app_manifest_coachmark = from_union([from_bool, from_none], obj.get("dismissed_app_manifest_coachmark"))
        purchaser = from_union([from_bool, from_none], obj.get("purchaser"))
        seen_channel_email_tooltip = from_union([from_bool, from_none], obj.get("seen_channel_email_tooltip"))
        show_ent_onboarding = from_union([from_bool, from_none], obj.get("show_ent_onboarding"))
        folders_enabled = from_union([from_bool, from_none], obj.get("folders_enabled"))
        folder_data = from_union([from_str, from_none], obj.get("folder_data"))
        seen_corporate_export_alert = from_union([from_bool, from_none], obj.get("seen_corporate_export_alert"))
        show_autocomplete_help = from_union([from_int, from_none], obj.get("show_autocomplete_help"))
        deprecation_toast_last_seen = from_union([from_int, from_none], obj.get("deprecation_toast_last_seen"))
        deprecation_modal_last_seen = from_union([from_int, from_none], obj.get("deprecation_modal_last_seen"))
        deprecation_banner_last_seen = from_union([from_int, from_none], obj.get("deprecation_banner_last_seen"))
        iap1_lab = from_union([from_int, from_none], obj.get("iap1_lab"))
        ia_top_nav_theme = from_union([from_str, from_none], obj.get("ia_top_nav_theme"))
        ia_platform_actions_lab = from_union([from_int, from_none], obj.get("ia_platform_actions_lab"))
        activity_view = from_union([from_str, from_none], obj.get("activity_view"))
        saved_view = from_union([from_str, from_none], obj.get("saved_view"))
        seen_floating_sidebar_coachmark = from_union([from_bool, from_none], obj.get("seen_floating_sidebar_coachmark"))
        desktop_client_ids = from_union([from_str, from_none], obj.get("desktop_client_ids"))
        failover_proxy_check_completed = from_union([from_int, from_none], obj.get("failover_proxy_check_completed"))
        chime_access_check_completed = from_union([from_int, from_none], obj.get("chime_access_check_completed"))
        mx_calendar_type = from_union([from_str, from_none], obj.get("mx_calendar_type"))
        edge_upload_proxy_check_completed = from_union([from_int, from_none], obj.get("edge_upload_proxy_check_completed"))
        app_subdomain_check_completed = from_union([from_int, from_none], obj.get("app_subdomain_check_completed"))
        add_prompt_interacted = from_union([from_bool, from_none], obj.get("add_prompt_interacted"))
        add_apps_prompt_dismissed = from_union([from_bool, from_none], obj.get("add_apps_prompt_dismissed"))
        add_channel_prompt_dismissed = from_union([from_bool, from_none], obj.get("add_channel_prompt_dismissed"))
        channel_sidebar_hide_invite = from_union([from_bool, from_none], obj.get("channel_sidebar_hide_invite"))
        channel_sidebar_hide_browse_dms_link = from_union([from_bool, from_none], obj.get("channel_sidebar_hide_browse_dms_link"))
        in_prod_surveys_enabled = from_union([from_bool, from_none], obj.get("in_prod_surveys_enabled"))
        connect_dm_early_access = from_union([from_bool, from_none], obj.get("connect_dm_early_access"))
        dismissed_installed_app_dm_suggestions = from_union([from_str, from_none], obj.get("dismissed_installed_app_dm_suggestions"))
        seen_contextual_message_shortcuts_modal = from_union([from_bool, from_none], obj.get("seen_contextual_message_shortcuts_modal"))
        seen_message_navigation_educational_toast = from_union([from_bool, from_none], obj.get("seen_message_navigation_educational_toast"))
        contextual_message_shortcuts_modal_was_seen = from_union([from_bool, from_none], obj.get("contextual_message_shortcuts_modal_was_seen"))
        message_navigation_toast_was_seen = from_union([from_bool, from_none], obj.get("message_navigation_toast_was_seen"))
        up_to_browse_kb_shortcut = from_union([from_bool, from_none], obj.get("up_to_browse_kb_shortcut"))
        set_a11_y_prefs_new_user = from_union([from_bool, from_none], obj.get("set_a11y_prefs_new_user"))
        a11_y_play_sound_for_incoming_dm = from_union([from_bool, from_none], obj.get("a11y_play_sound_for_incoming_dm"))
        a11_y_play_sound_for_sent_dm = from_union([from_bool, from_none], obj.get("a11y_play_sound_for_sent_dm"))
        a11_y_read_out_incoming_dm = from_union([from_bool, from_none], obj.get("a11y_read_out_incoming_dm"))
        a11_y_screen_reader_message_label_date_time_first = from_union([from_bool, from_none], obj.get("a11y_screen_reader_message_label_date_time_first"))
        should_show_contextual_help_for_conversation_navigation = from_union([from_bool, from_none], obj.get("should_show_contextual_help_for_conversation_navigation"))
        should_show_contextual_help_for_jump_to_conversation = from_union([from_bool, from_none], obj.get("should_show_contextual_help_for_jump_to_conversation"))
        should_show_contextual_help_for_section_navigation = from_union([from_bool, from_none], obj.get("should_show_contextual_help_for_section_navigation"))
        should_show_contextual_help_for_thread_navigation = from_union([from_bool, from_none], obj.get("should_show_contextual_help_for_thread_navigation"))
        should_show_unsend_message_confirmation = from_union([from_bool, from_none], obj.get("should_show_unsend_message_confirmation"))
        channel_sections = from_union([from_str, from_none], obj.get("channel_sections"))
        show_quick_reactions = from_union([from_bool, from_none], obj.get("show_quick_reactions"))
        user_customized_quick_reactions_display_feature = from_union([from_int, from_none], obj.get("user_customized_quick_reactions_display_feature"))
        user_customized_quick_reactions_has_customized = from_union([from_bool, from_none], obj.get("user_customized_quick_reactions_has_customized"))
        user_customized_quick_reactions_use_frequently_used_emoji = from_union([from_bool, from_none], obj.get("user_customized_quick_reactions_use_frequently_used_emoji"))
        reaction_notifications = from_union([from_str, from_none], obj.get("reaction_notifications"))
        has_received_mention_or_reaction = from_union([from_bool, from_none], obj.get("has_received_mention_or_reaction"))
        has_starred_item = from_union([from_bool, from_none], obj.get("has_starred_item"))
        has_drafted_message = from_union([from_bool, from_none], obj.get("has_drafted_message"))
        enable_mentions_and_reactions_view = from_union([from_bool, from_none], obj.get("enable_mentions_and_reactions_view"))
        enable_reminders_view = from_union([from_bool, from_none], obj.get("enable_reminders_view"))
        enable_saved_items_view = from_union([from_bool, from_none], obj.get("enable_saved_items_view"))
        enable_hq_view = from_union([from_bool, from_none], obj.get("enable_hq_view"))
        enable_all_dms_view = from_union([from_bool, from_none], obj.get("enable_all_dms_view"))
        enable_channel_browser_view = from_union([from_bool, from_none], obj.get("enable_channel_browser_view"))
        enable_file_browser_view = from_union([from_bool, from_none], obj.get("enable_file_browser_view"))
        enable_people_browser_view = from_union([from_bool, from_none], obj.get("enable_people_browser_view"))
        enable_app_browser_view = from_union([from_bool, from_none], obj.get("enable_app_browser_view"))
        reached_all_dms_disclosure = from_union([from_bool, from_none], obj.get("reached_all_dms_disclosure"))
        enable_slack_connect_view = from_union([from_bool, from_none], obj.get("enable_slack_connect_view"))
        enable_slack_connect_view_2 = from_union([from_int, from_none], obj.get("enable_slack_connect_view_2"))
        has_acknowledged_shortcut_speedbump = from_union([from_bool, from_none], obj.get("has_acknowledged_shortcut_speedbump"))
        enable_media_captions = from_union([from_bool, from_none], obj.get("enable_media_captions"))
        media_playback_speed = from_union([from_int, from_none], obj.get("media_playback_speed"))
        media_muted = from_union([from_bool, from_none], obj.get("media_muted"))
        media_volume = from_union([from_int, from_none], obj.get("media_volume"))
        dismissed_connect_auto_approval_modal = from_union([from_str, from_none], obj.get("dismissed_connect_auto_approval_modal"))
        tasks_view = from_union([from_str, from_none], obj.get("tasks_view"))
        show_sidebar_avatars = from_union([from_bool, from_none], obj.get("show_sidebar_avatars"))
        has_dismissed_google_directory_coachmark = from_union([from_bool, from_none], obj.get("has_dismissed_google_directory_coachmark"))
        seen_sc_page_banner = from_union([from_bool, from_none], obj.get("seen_sc_page_banner"))
        seen_sc_menu_coachmark = from_union([from_bool, from_none], obj.get("seen_sc_menu_coachmark"))
        seen_sc_page = from_union([from_bool, from_none], obj.get("seen_sc_page"))
        dismissed_scdm_education = from_union([from_bool, from_none], obj.get("dismissed_scdm_education"))
        seen_bookmarks_intro = from_union([from_bool, from_none], obj.get("seen_bookmarks_intro"))
        scdm_trial_offer_banner = from_union([from_str, from_none], obj.get("scdm_trial_offer_banner"))
        identity_links_prefs = from_union([from_str, from_none], obj.get("identity_links_prefs"))
        identity_links_global_prefs = from_union([from_str, from_none], obj.get("identity_links_global_prefs"))
        seen_sections_unreads_only_prompt_count = from_union([from_int, from_none], obj.get("seen_sections_unreads_only_prompt_count"))
        last_seen_sections_unreads_only_prompt_timestamp = from_union([from_int, from_none], obj.get("last_seen_sections_unreads_only_prompt_timestamp"))
        notifications_view = from_union([from_str, from_none], obj.get("notifications_view"))
        progressive_disclosure_state = from_union([from_str, from_none], obj.get("progressive_disclosure_state"))
        suggestions_request_id = from_union([from_str, from_none], obj.get("suggestions_request_id"))
        allowed_unfurl_senders = from_union([from_str, from_none], obj.get("allowed_unfurl_senders"))
        ia_details_coachmark_seen = from_union([from_bool, from_none], obj.get("ia_details_coachmark_seen"))
        hide_external_members_sharing_speed_bump = from_union([from_bool, from_none], obj.get("hide_external_members_sharing_speed_bump"))
        who_can_share_contact_card = from_union([from_str, from_none], obj.get("who_can_share_contact_card"))
        slack_connect_invite_should_badge_sidebar = from_union([from_bool, from_none], obj.get("slack_connect_invite_should_badge_sidebar"))
        phc_dismissed = from_union([from_str, from_none], obj.get("phc_dismissed"))
        dismissed_gov_slack_first_time_popup = from_union([from_bool, from_none], obj.get("dismissed_gov_slack_first_time_popup"))
        mobile_channel_list_sort = from_union([from_str, from_none], obj.get("mobile_channel_list_sort"))
        user_expectations_survey_last_trigger_attempt = from_union([from_int, from_none], obj.get("user_expectations_survey_last_trigger_attempt"))
        tz = from_union([from_str, from_none], obj.get("tz"))
        locales_enabled = from_union([LocalesEnabled.from_dict, from_none], obj.get("locales_enabled"))
        phc_viewed = from_union([from_str, from_none], obj.get("phc_viewed"))
        seen_a11_y_pref_setup_coachmark = from_union([from_bool, from_none], obj.get("seen_a11y_pref_setup_coachmark"))
        enable_file_browser_view_for_docs = from_union([from_bool, from_none], obj.get("enable_file_browser_view_for_docs"))
        enable_shortcuts_view = from_union([from_bool, from_none], obj.get("enable_shortcuts_view"))
        show_gov_slack_context_bar_banner = from_union([from_bool, from_none], obj.get("show_gov_slack_context_bar_banner"))
        who_can_see_account_by_searching_email = from_union([from_str, from_none], obj.get("who_can_see_account_by_searching_email"))
        contextual_help_reset_count = from_union([from_int, from_none], obj.get("contextual_help_reset_count"))
        return SelfPrefs(underline_links, user_colors, color_names_in_list, email_alerts, email_alerts_sleep_until, email_tips, email_weekly, email_offers, email_research, email_developer, welcome_message_hidden, search_sort, search_file_sort, search_channel_sort, search_people_sort, expand_inline_imgs, expand_internal_inline_imgs, expand_snippets, posts_formatting_guide, seen_welcome_2, seen_ssb_prompt, spaces_new_xp_banner_dismissed, search_only_my_channels, search_only_current_team, search_hide_my_channels, search_only_show_online, search_hide_deactivated_users, emoji_mode, emoji_use, emoji_use_org, has_invited, has_uploaded, has_created_channel, has_created_channel_section, has_searched, search_exclude_channels, messages_theme, webapp_spellcheck, no_joined_overlays, no_created_overlays, dropbox_enabled, seen_domain_invite_reminder, seen_member_invite_reminder, mute_sounds, arrow_history, tab_ui_return_selects, obey_inline_img_limit, require_at, ssb_space_window, mac_ssb_bounce, mac_ssb_bullet, expand_non_media_attachments, show_typing, pagekeys_handled, last_snippet_type, display_real_names_override, display_display_names, time24, enter_is_special_in_tbt, msg_input_send_btn, msg_input_send_btn_auto_set, msg_input_sticky_composer, composer_nux, graphic_emoticons, convert_emoticons, ss_emojis, seen_onboarding_start, onboarding_cancelled, seen_onboarding_slackbot_conversation, seen_onboarding_channels, seen_onboarding_direct_messages, seen_onboarding_invites, seen_onboarding_search, seen_onboarding_recent_mentions, seen_onboarding_starred_items, seen_onboarding_private_groups, seen_onboarding_banner, onboarding_slackbot_conversation_step, set_tz_automatically, suppress_link_warning, suppress_external_invites_from_compose_warning, seen_emoji_pack_cta, seen_emoji_pack_dialog, seen_schedule_send_coachmark, emoji_packs_most_recent_available_time, emoji_packs_clicked_picker_cta, emoji_packs_clicked_picker_post_install_cta, emoji_packs_clicked_collection_cta, dnd_enabled, dnd_start_hour, dnd_end_hour, dnd_before_monday, dnd_after_monday, dnd_enabled_monday, dnd_before_tuesday, dnd_after_tuesday, dnd_enabled_tuesday, dnd_before_wednesday, dnd_after_wednesday, dnd_enabled_wednesday, dnd_before_thursday, dnd_after_thursday, dnd_enabled_thursday, dnd_before_friday, dnd_after_friday, dnd_enabled_friday, dnd_before_saturday, dnd_after_saturday, dnd_enabled_saturday, dnd_before_sunday, dnd_after_sunday, dnd_enabled_sunday, dnd_days, dnd_weekdays_off_allday, reminder_notification_time, dnd_custom_new_badge_seen, dnd_notification_schedule_new_badge_seen, notification_center_filters, calls_survey_last_seen, huddle_survey_last_seen, sidebar_behavior, channel_sort, separate_private_channels, separate_shared_channels, sidebar_theme, sidebar_theme_custom_values, no_invites_widget_in_sidebar, no_omnibox_in_channels, k_key_omnibox_auto_hide_count, show_sidebar_quickswitcher_button, ent_org_wide_channels_sidebar, mark_msgs_read_immediately, start_scroll_at_oldest, snippet_editor_wrap_long_lines, ls_disabled, f_key_search, k_key_omnibox, prompted_for_email_disabling, no_macelectron_banner, no_macssb1_banner, no_macssb2_banner, no_winssb1_banner, hide_user_group_info_pane, mentions_exclude_at_user_groups, mentions_exclude_reactions, privacy_policy_seen, enterprise_migration_seen, search_exclude_bots, load_lato_2, fuller_timestamps, last_seen_at_channel_warning, emoji_autocomplete_big, two_factor_auth_enabled, hide_hex_swatch, show_jumper_scores, enterprise_mdm_custom_msg, client_logs_pri, flannel_server_pool, mentions_exclude_at_channels, confirm_clear_all_unreads, confirm_user_marked_away, box_enabled, seen_single_emoji_msg, confirm_sh_call_start, preferred_skin_tone, show_all_skin_tones, whats_new_read, help_modal_open_timestamp, help_modal_consult_banner_dismissed, help_flexpane_slack_connect_card_seen, help_flexpane_clips_card_seen, help_menu_open_timestamp, frecency_jumper, frecency_ent_jumper, jumbomoji, newxp_seen_last_message, show_memory_instrument, enable_unread_view, seen_unread_view_coachmark, seen_connect_dm_coachmark, seen_connect_section_coachmark, should_show_connect_section, enable_react_emoji_picker, seen_custom_status_badge, seen_custom_status_callout, seen_custom_status_expiration_badge, used_custom_status_kb_shortcut, seen_guest_admin_slackbot_announcement, seen_threads_notification_banner, seen_name_tagging_coachmark, all_unreads_sort_order, all_unreads_section_filter, locale, seen_intl_channel_names_coachmark, seen_p3_locale_change_message_ko_kr, seen_toast_new_locale_launch, seen_toast_new_locale_launch_ts, seen_locale_change_message, seen_japanese_locale_change_message, seen_shared_channels_coachmark, seen_shared_channels_opt_in_change_message, has_recently_shared_a_channel, seen_channel_browser_admin_coachmark, seen_administration_menu, seen_drafts_section_coachmark, seen_emoji_update_overlay_coachmark, seen_sonic_deluxe_toast, seen_wysiwyg_deluxe_toast, seen_markdown_paste_toast, seen_markdown_paste_shortcut, seen_ia_education, show_ia_tour_relaunch, plain_text_mode, show_shared_channels_education_banner, ia_slackbot_survey_timestamp_48_h, ia_slackbot_survey_timestamp_7_d, enable_streamline_view, enable_sent_view, allow_calls_to_set_current_status, in_interactive_mas_migration_flow, sunset_interactive_message_views, shdep_promo_code_submitted, seen_shdep_slackbot_message, seen_calls_interactive_coachmark, allow_cmd_tab_iss, join_calls_device_settings, calls_disconnect_on_lock, seen_workflow_builder_deluxe_toast, workflow_builder_intro_modal_clicked_through, workflow_builder_coachmarks, seen_gdrive_coachmark, seen_first_install_coachmark, seen_existing_install_coachmark, seen_link_unfurl_coachmark, file_picker_variant, open_quip_doc_in_flexpane, saved_searches, huddles_variant, huddles_cc_by_default, huddles_mute_by_default, huddles_global_mute, huddles_mini_panel, huddles_set_status, huddles_show_shouty_rooster, huddles_disconnect_on_lock, huddles_play_music_when_last, huddles_allow_smart_notif, huddles_reactions_play_sound, huddles_reactions_read_out_loud, huddles_chime_new_endpoints_check_completed, xws_sidebar_variant, inbox_views_workspace_filter, overloaded_message_enabled, seen_highlights_coachmark, seen_highlights_arrows_coachmark, seen_highlights_warm_welcome, seen_new_search_ui, seen_channel_search, seen_people_search, seen_people_search_count, dismissed_scroll_search_tooltip_count, last_dismissed_scroll_search_tooltip_timestamp, has_used_quickswitcher_shortcut, seen_quickswitcher_shortcut_tip_count, browsers_dismissed_channels_low_results_education, browsers_seen_initial_channels_education, browsers_dismissed_people_low_results_education, browsers_seen_initial_people_education, browsers_dismissed_user_groups_low_results_education, browsers_seen_initial_user_groups_education, browsers_dismissed_files_low_results_education, browsers_seen_initial_files_education, browsers_dismissed_initial_drafts_education, browsers_seen_initial_drafts_education, browsers_dismissed_initial_activity_education, browsers_seen_initial_activity_education, browsers_dismissed_initial_saved_education, browsers_seen_initial_saved_education, seen_edit_mode, seen_edit_mode_edu, xws_dismissed_education, xws_seen_education, sidebar_pref_dismissed_tip, a11_y_dyslexic, a11_y_animations, seen_keyboard_shortcuts_coachmark, needs_initial_password_set, lessons_enabled, tractor_enabled, tractor_experiment_group, opened_slackbot_dm, newxp_seen_help_message, newxp_suggested_channels, onboarding_complete, welcome_place_state, has_received_threaded_message, joiner_notifications_muted, invite_accepted_notifications_muted, joiner_message_suggestion_dismissed, dismissed_fullscreen_download_ssb_prompt, dismissed_banner_download_ssb_prompt, onboarding_state, whocanseethis_dm_mpdm_badge, highlight_words, threads_everything, no_text_in_notifications, push_show_preview, growls_enabled, all_channels_loud, push_dm_alert, push_mention_alert, push_everything, push_idle_wait, push_sound, new_msg_snd, huddle_invite_sound, push_loud_channels, push_mention_channels, push_loud_channels_set, loud_channels, never_channels, loud_channels_set, at_channel_suppressed_channels, push_at_channel_suppressed_channels, muted_channels, all_notifications_prefs, growth_msg_limit_approaching_cta_count, growth_msg_limit_approaching_cta_ts, growth_msg_limit_reached_cta_count, growth_msg_limit_reached_cta_last_ts, growth_msg_limit_long_reached_cta_count, growth_msg_limit_long_reached_cta_last_ts, growth_msg_limit_sixty_day_banner_cta_count, growth_msg_limit_sixty_day_banner_cta_last_ts, growth_all_banners_prefs, analytics_upsell_coachmark_seen, seen_app_space_coachmark, seen_app_space_tutorial, dismissed_app_launcher_welcome, dismissed_app_launcher_limit, dismissed_app_launcher_atlassian_promo, enable_app_config_redesign, dismissed_app_config_redesign_coachmark, dismissed_app_manifest_description, dismissed_app_manifest_coachmark, purchaser, seen_channel_email_tooltip, show_ent_onboarding, folders_enabled, folder_data, seen_corporate_export_alert, show_autocomplete_help, deprecation_toast_last_seen, deprecation_modal_last_seen, deprecation_banner_last_seen, iap1_lab, ia_top_nav_theme, ia_platform_actions_lab, activity_view, saved_view, seen_floating_sidebar_coachmark, desktop_client_ids, failover_proxy_check_completed, chime_access_check_completed, mx_calendar_type, edge_upload_proxy_check_completed, app_subdomain_check_completed, add_prompt_interacted, add_apps_prompt_dismissed, add_channel_prompt_dismissed, channel_sidebar_hide_invite, channel_sidebar_hide_browse_dms_link, in_prod_surveys_enabled, connect_dm_early_access, dismissed_installed_app_dm_suggestions, seen_contextual_message_shortcuts_modal, seen_message_navigation_educational_toast, contextual_message_shortcuts_modal_was_seen, message_navigation_toast_was_seen, up_to_browse_kb_shortcut, set_a11_y_prefs_new_user, a11_y_play_sound_for_incoming_dm, a11_y_play_sound_for_sent_dm, a11_y_read_out_incoming_dm, a11_y_screen_reader_message_label_date_time_first, should_show_contextual_help_for_conversation_navigation, should_show_contextual_help_for_jump_to_conversation, should_show_contextual_help_for_section_navigation, should_show_contextual_help_for_thread_navigation, should_show_unsend_message_confirmation, channel_sections, show_quick_reactions, user_customized_quick_reactions_display_feature, user_customized_quick_reactions_has_customized, user_customized_quick_reactions_use_frequently_used_emoji, reaction_notifications, has_received_mention_or_reaction, has_starred_item, has_drafted_message, enable_mentions_and_reactions_view, enable_reminders_view, enable_saved_items_view, enable_hq_view, enable_all_dms_view, enable_channel_browser_view, enable_file_browser_view, enable_people_browser_view, enable_app_browser_view, reached_all_dms_disclosure, enable_slack_connect_view, enable_slack_connect_view_2, has_acknowledged_shortcut_speedbump, enable_media_captions, media_playback_speed, media_muted, media_volume, dismissed_connect_auto_approval_modal, tasks_view, show_sidebar_avatars, has_dismissed_google_directory_coachmark, seen_sc_page_banner, seen_sc_menu_coachmark, seen_sc_page, dismissed_scdm_education, seen_bookmarks_intro, scdm_trial_offer_banner, identity_links_prefs, identity_links_global_prefs, seen_sections_unreads_only_prompt_count, last_seen_sections_unreads_only_prompt_timestamp, notifications_view, progressive_disclosure_state, suggestions_request_id, allowed_unfurl_senders, ia_details_coachmark_seen, hide_external_members_sharing_speed_bump, who_can_share_contact_card, slack_connect_invite_should_badge_sidebar, phc_dismissed, dismissed_gov_slack_first_time_popup, mobile_channel_list_sort, user_expectations_survey_last_trigger_attempt, tz, locales_enabled, phc_viewed, seen_a11_y_pref_setup_coachmark, enable_file_browser_view_for_docs, enable_shortcuts_view, show_gov_slack_context_bar_banner, who_can_see_account_by_searching_email, contextual_help_reset_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["underline_links"] = from_union([from_bool, from_none], self.underline_links)
        result["user_colors"] = from_union([from_str, from_none], self.user_colors)
        result["color_names_in_list"] = from_union([from_bool, from_none], self.color_names_in_list)
        result["email_alerts"] = from_union([from_str, from_none], self.email_alerts)
        result["email_alerts_sleep_until"] = from_union([from_int, from_none], self.email_alerts_sleep_until)
        result["email_tips"] = from_union([from_bool, from_none], self.email_tips)
        result["email_weekly"] = from_union([from_bool, from_none], self.email_weekly)
        result["email_offers"] = from_union([from_bool, from_none], self.email_offers)
        result["email_research"] = from_union([from_bool, from_none], self.email_research)
        result["email_developer"] = from_union([from_bool, from_none], self.email_developer)
        result["welcome_message_hidden"] = from_union([from_bool, from_none], self.welcome_message_hidden)
        result["search_sort"] = from_union([from_str, from_none], self.search_sort)
        result["search_file_sort"] = from_union([from_str, from_none], self.search_file_sort)
        result["search_channel_sort"] = from_union([from_str, from_none], self.search_channel_sort)
        result["search_people_sort"] = from_union([from_str, from_none], self.search_people_sort)
        result["expand_inline_imgs"] = from_union([from_bool, from_none], self.expand_inline_imgs)
        result["expand_internal_inline_imgs"] = from_union([from_bool, from_none], self.expand_internal_inline_imgs)
        result["expand_snippets"] = from_union([from_bool, from_none], self.expand_snippets)
        result["posts_formatting_guide"] = from_union([from_bool, from_none], self.posts_formatting_guide)
        result["seen_welcome_2"] = from_union([from_bool, from_none], self.seen_welcome_2)
        result["seen_ssb_prompt"] = from_union([from_bool, from_none], self.seen_ssb_prompt)
        result["spaces_new_xp_banner_dismissed"] = from_union([from_bool, from_none], self.spaces_new_xp_banner_dismissed)
        result["search_only_my_channels"] = from_union([from_bool, from_none], self.search_only_my_channels)
        result["search_only_current_team"] = from_union([from_bool, from_none], self.search_only_current_team)
        result["search_hide_my_channels"] = from_union([from_bool, from_none], self.search_hide_my_channels)
        result["search_only_show_online"] = from_union([from_bool, from_none], self.search_only_show_online)
        result["search_hide_deactivated_users"] = from_union([from_bool, from_none], self.search_hide_deactivated_users)
        result["emoji_mode"] = from_union([from_str, from_none], self.emoji_mode)
        result["emoji_use"] = from_union([from_str, from_none], self.emoji_use)
        result["emoji_use_org"] = from_union([from_str, from_none], self.emoji_use_org)
        result["has_invited"] = from_union([from_bool, from_none], self.has_invited)
        result["has_uploaded"] = from_union([from_bool, from_none], self.has_uploaded)
        result["has_created_channel"] = from_union([from_bool, from_none], self.has_created_channel)
        result["has_created_channel_section"] = from_union([from_bool, from_none], self.has_created_channel_section)
        result["has_searched"] = from_union([from_bool, from_none], self.has_searched)
        result["search_exclude_channels"] = from_union([from_str, from_none], self.search_exclude_channels)
        result["messages_theme"] = from_union([from_str, from_none], self.messages_theme)
        result["webapp_spellcheck"] = from_union([from_bool, from_none], self.webapp_spellcheck)
        result["no_joined_overlays"] = from_union([from_bool, from_none], self.no_joined_overlays)
        result["no_created_overlays"] = from_union([from_bool, from_none], self.no_created_overlays)
        result["dropbox_enabled"] = from_union([from_bool, from_none], self.dropbox_enabled)
        result["seen_domain_invite_reminder"] = from_union([from_bool, from_none], self.seen_domain_invite_reminder)
        result["seen_member_invite_reminder"] = from_union([from_bool, from_none], self.seen_member_invite_reminder)
        result["mute_sounds"] = from_union([from_bool, from_none], self.mute_sounds)
        result["arrow_history"] = from_union([from_bool, from_none], self.arrow_history)
        result["tab_ui_return_selects"] = from_union([from_bool, from_none], self.tab_ui_return_selects)
        result["obey_inline_img_limit"] = from_union([from_bool, from_none], self.obey_inline_img_limit)
        result["require_at"] = from_union([from_bool, from_none], self.require_at)
        result["ssb_space_window"] = from_union([from_str, from_none], self.ssb_space_window)
        result["mac_ssb_bounce"] = from_union([from_str, from_none], self.mac_ssb_bounce)
        result["mac_ssb_bullet"] = from_union([from_bool, from_none], self.mac_ssb_bullet)
        result["expand_non_media_attachments"] = from_union([from_bool, from_none], self.expand_non_media_attachments)
        result["show_typing"] = from_union([from_bool, from_none], self.show_typing)
        result["pagekeys_handled"] = from_union([from_bool, from_none], self.pagekeys_handled)
        result["last_snippet_type"] = from_union([from_str, from_none], self.last_snippet_type)
        result["display_real_names_override"] = from_union([from_int, from_none], self.display_real_names_override)
        result["display_display_names"] = from_union([from_bool, from_none], self.display_display_names)
        result["time24"] = from_union([from_bool, from_none], self.time24)
        result["enter_is_special_in_tbt"] = from_union([from_bool, from_none], self.enter_is_special_in_tbt)
        result["msg_input_send_btn"] = from_union([from_bool, from_none], self.msg_input_send_btn)
        result["msg_input_send_btn_auto_set"] = from_union([from_bool, from_none], self.msg_input_send_btn_auto_set)
        result["msg_input_sticky_composer"] = from_union([from_bool, from_none], self.msg_input_sticky_composer)
        result["composer_nux"] = from_union([from_str, from_none], self.composer_nux)
        result["graphic_emoticons"] = from_union([from_bool, from_none], self.graphic_emoticons)
        result["convert_emoticons"] = from_union([from_bool, from_none], self.convert_emoticons)
        result["ss_emojis"] = from_union([from_bool, from_none], self.ss_emojis)
        result["seen_onboarding_start"] = from_union([from_bool, from_none], self.seen_onboarding_start)
        result["onboarding_cancelled"] = from_union([from_bool, from_none], self.onboarding_cancelled)
        result["seen_onboarding_slackbot_conversation"] = from_union([from_bool, from_none], self.seen_onboarding_slackbot_conversation)
        result["seen_onboarding_channels"] = from_union([from_bool, from_none], self.seen_onboarding_channels)
        result["seen_onboarding_direct_messages"] = from_union([from_bool, from_none], self.seen_onboarding_direct_messages)
        result["seen_onboarding_invites"] = from_union([from_bool, from_none], self.seen_onboarding_invites)
        result["seen_onboarding_search"] = from_union([from_bool, from_none], self.seen_onboarding_search)
        result["seen_onboarding_recent_mentions"] = from_union([from_bool, from_none], self.seen_onboarding_recent_mentions)
        result["seen_onboarding_starred_items"] = from_union([from_bool, from_none], self.seen_onboarding_starred_items)
        result["seen_onboarding_private_groups"] = from_union([from_bool, from_none], self.seen_onboarding_private_groups)
        result["seen_onboarding_banner"] = from_union([from_bool, from_none], self.seen_onboarding_banner)
        result["onboarding_slackbot_conversation_step"] = from_union([from_int, from_none], self.onboarding_slackbot_conversation_step)
        result["set_tz_automatically"] = from_union([from_bool, from_none], self.set_tz_automatically)
        result["suppress_link_warning"] = from_union([from_bool, from_none], self.suppress_link_warning)
        result["suppress_external_invites_from_compose_warning"] = from_union([from_bool, from_none], self.suppress_external_invites_from_compose_warning)
        result["seen_emoji_pack_cta"] = from_union([from_int, from_none], self.seen_emoji_pack_cta)
        result["seen_emoji_pack_dialog"] = from_union([from_bool, from_none], self.seen_emoji_pack_dialog)
        result["seen_schedule_send_coachmark"] = from_union([from_bool, from_none], self.seen_schedule_send_coachmark)
        result["emoji_packs_most_recent_available_time"] = from_union([from_int, from_none], self.emoji_packs_most_recent_available_time)
        result["emoji_packs_clicked_picker_cta"] = from_union([from_bool, from_none], self.emoji_packs_clicked_picker_cta)
        result["emoji_packs_clicked_picker_post_install_cta"] = from_union([from_bool, from_none], self.emoji_packs_clicked_picker_post_install_cta)
        result["emoji_packs_clicked_collection_cta"] = from_union([from_bool, from_none], self.emoji_packs_clicked_collection_cta)
        result["dnd_enabled"] = from_union([from_bool, from_none], self.dnd_enabled)
        result["dnd_start_hour"] = from_union([from_str, from_none], self.dnd_start_hour)
        result["dnd_end_hour"] = from_union([from_str, from_none], self.dnd_end_hour)
        result["dnd_before_monday"] = from_union([from_str, from_none], self.dnd_before_monday)
        result["dnd_after_monday"] = from_union([from_str, from_none], self.dnd_after_monday)
        result["dnd_enabled_monday"] = from_union([from_str, from_none], self.dnd_enabled_monday)
        result["dnd_before_tuesday"] = from_union([from_str, from_none], self.dnd_before_tuesday)
        result["dnd_after_tuesday"] = from_union([from_str, from_none], self.dnd_after_tuesday)
        result["dnd_enabled_tuesday"] = from_union([from_str, from_none], self.dnd_enabled_tuesday)
        result["dnd_before_wednesday"] = from_union([from_str, from_none], self.dnd_before_wednesday)
        result["dnd_after_wednesday"] = from_union([from_str, from_none], self.dnd_after_wednesday)
        result["dnd_enabled_wednesday"] = from_union([from_str, from_none], self.dnd_enabled_wednesday)
        result["dnd_before_thursday"] = from_union([from_str, from_none], self.dnd_before_thursday)
        result["dnd_after_thursday"] = from_union([from_str, from_none], self.dnd_after_thursday)
        result["dnd_enabled_thursday"] = from_union([from_str, from_none], self.dnd_enabled_thursday)
        result["dnd_before_friday"] = from_union([from_str, from_none], self.dnd_before_friday)
        result["dnd_after_friday"] = from_union([from_str, from_none], self.dnd_after_friday)
        result["dnd_enabled_friday"] = from_union([from_str, from_none], self.dnd_enabled_friday)
        result["dnd_before_saturday"] = from_union([from_str, from_none], self.dnd_before_saturday)
        result["dnd_after_saturday"] = from_union([from_str, from_none], self.dnd_after_saturday)
        result["dnd_enabled_saturday"] = from_union([from_str, from_none], self.dnd_enabled_saturday)
        result["dnd_before_sunday"] = from_union([from_str, from_none], self.dnd_before_sunday)
        result["dnd_after_sunday"] = from_union([from_str, from_none], self.dnd_after_sunday)
        result["dnd_enabled_sunday"] = from_union([from_str, from_none], self.dnd_enabled_sunday)
        result["dnd_days"] = from_union([from_str, from_none], self.dnd_days)
        result["dnd_weekdays_off_allday"] = from_union([from_bool, from_none], self.dnd_weekdays_off_allday)
        result["reminder_notification_time"] = from_union([from_str, from_none], self.reminder_notification_time)
        result["dnd_custom_new_badge_seen"] = from_union([from_bool, from_none], self.dnd_custom_new_badge_seen)
        result["dnd_notification_schedule_new_badge_seen"] = from_union([from_bool, from_none], self.dnd_notification_schedule_new_badge_seen)
        result["notification_center_filters"] = from_union([from_str, from_none], self.notification_center_filters)
        result["calls_survey_last_seen"] = from_union([from_str, from_none], self.calls_survey_last_seen)
        result["huddle_survey_last_seen"] = from_union([from_str, from_none], self.huddle_survey_last_seen)
        result["sidebar_behavior"] = from_union([from_str, from_none], self.sidebar_behavior)
        result["channel_sort"] = from_union([from_str, from_none], self.channel_sort)
        result["separate_private_channels"] = from_union([from_bool, from_none], self.separate_private_channels)
        result["separate_shared_channels"] = from_union([from_bool, from_none], self.separate_shared_channels)
        result["sidebar_theme"] = from_union([from_str, from_none], self.sidebar_theme)
        result["sidebar_theme_custom_values"] = from_union([from_str, from_none], self.sidebar_theme_custom_values)
        result["no_invites_widget_in_sidebar"] = from_union([from_bool, from_none], self.no_invites_widget_in_sidebar)
        result["no_omnibox_in_channels"] = from_union([from_bool, from_none], self.no_omnibox_in_channels)
        result["k_key_omnibox_auto_hide_count"] = from_union([from_int, from_none], self.k_key_omnibox_auto_hide_count)
        result["show_sidebar_quickswitcher_button"] = from_union([from_bool, from_none], self.show_sidebar_quickswitcher_button)
        result["ent_org_wide_channels_sidebar"] = from_union([from_bool, from_none], self.ent_org_wide_channels_sidebar)
        result["mark_msgs_read_immediately"] = from_union([from_bool, from_none], self.mark_msgs_read_immediately)
        result["start_scroll_at_oldest"] = from_union([from_bool, from_none], self.start_scroll_at_oldest)
        result["snippet_editor_wrap_long_lines"] = from_union([from_bool, from_none], self.snippet_editor_wrap_long_lines)
        result["ls_disabled"] = from_union([from_bool, from_none], self.ls_disabled)
        result["f_key_search"] = from_union([from_bool, from_none], self.f_key_search)
        result["k_key_omnibox"] = from_union([from_bool, from_none], self.k_key_omnibox)
        result["prompted_for_email_disabling"] = from_union([from_bool, from_none], self.prompted_for_email_disabling)
        result["no_macelectron_banner"] = from_union([from_bool, from_none], self.no_macelectron_banner)
        result["no_macssb1_banner"] = from_union([from_bool, from_none], self.no_macssb1_banner)
        result["no_macssb2_banner"] = from_union([from_bool, from_none], self.no_macssb2_banner)
        result["no_winssb1_banner"] = from_union([from_bool, from_none], self.no_winssb1_banner)
        result["hide_user_group_info_pane"] = from_union([from_bool, from_none], self.hide_user_group_info_pane)
        result["mentions_exclude_at_user_groups"] = from_union([from_bool, from_none], self.mentions_exclude_at_user_groups)
        result["mentions_exclude_reactions"] = from_union([from_bool, from_none], self.mentions_exclude_reactions)
        result["privacy_policy_seen"] = from_union([from_bool, from_none], self.privacy_policy_seen)
        result["enterprise_migration_seen"] = from_union([from_bool, from_none], self.enterprise_migration_seen)
        result["search_exclude_bots"] = from_union([from_bool, from_none], self.search_exclude_bots)
        result["load_lato_2"] = from_union([from_bool, from_none], self.load_lato_2)
        result["fuller_timestamps"] = from_union([from_bool, from_none], self.fuller_timestamps)
        result["last_seen_at_channel_warning"] = from_union([from_int, from_none], self.last_seen_at_channel_warning)
        result["emoji_autocomplete_big"] = from_union([from_bool, from_none], self.emoji_autocomplete_big)
        result["two_factor_auth_enabled"] = from_union([from_bool, from_none], self.two_factor_auth_enabled)
        result["hide_hex_swatch"] = from_union([from_bool, from_none], self.hide_hex_swatch)
        result["show_jumper_scores"] = from_union([from_bool, from_none], self.show_jumper_scores)
        result["enterprise_mdm_custom_msg"] = from_union([from_str, from_none], self.enterprise_mdm_custom_msg)
        result["client_logs_pri"] = from_union([from_str, from_none], self.client_logs_pri)
        result["flannel_server_pool"] = from_union([from_str, from_none], self.flannel_server_pool)
        result["mentions_exclude_at_channels"] = from_union([from_bool, from_none], self.mentions_exclude_at_channels)
        result["confirm_clear_all_unreads"] = from_union([from_bool, from_none], self.confirm_clear_all_unreads)
        result["confirm_user_marked_away"] = from_union([from_bool, from_none], self.confirm_user_marked_away)
        result["box_enabled"] = from_union([from_bool, from_none], self.box_enabled)
        result["seen_single_emoji_msg"] = from_union([from_bool, from_none], self.seen_single_emoji_msg)
        result["confirm_sh_call_start"] = from_union([from_bool, from_none], self.confirm_sh_call_start)
        result["preferred_skin_tone"] = from_union([from_str, from_none], self.preferred_skin_tone)
        result["show_all_skin_tones"] = from_union([from_bool, from_none], self.show_all_skin_tones)
        result["whats_new_read"] = from_union([from_int, from_none], self.whats_new_read)
        result["help_modal_open_timestamp"] = from_union([from_int, from_none], self.help_modal_open_timestamp)
        result["help_modal_consult_banner_dismissed"] = from_union([from_bool, from_none], self.help_modal_consult_banner_dismissed)
        result["help_flexpane_slack_connect_card_seen"] = from_union([from_bool, from_none], self.help_flexpane_slack_connect_card_seen)
        result["help_flexpane_clips_card_seen"] = from_union([from_bool, from_none], self.help_flexpane_clips_card_seen)
        result["help_menu_open_timestamp"] = from_union([from_int, from_none], self.help_menu_open_timestamp)
        result["frecency_jumper"] = from_union([from_str, from_none], self.frecency_jumper)
        result["frecency_ent_jumper"] = from_union([from_str, from_none], self.frecency_ent_jumper)
        result["jumbomoji"] = from_union([from_bool, from_none], self.jumbomoji)
        result["newxp_seen_last_message"] = from_union([from_int, from_none], self.newxp_seen_last_message)
        result["show_memory_instrument"] = from_union([from_bool, from_none], self.show_memory_instrument)
        result["enable_unread_view"] = from_union([from_bool, from_none], self.enable_unread_view)
        result["seen_unread_view_coachmark"] = from_union([from_bool, from_none], self.seen_unread_view_coachmark)
        result["seen_connect_dm_coachmark"] = from_union([from_bool, from_none], self.seen_connect_dm_coachmark)
        result["seen_connect_section_coachmark"] = from_union([from_bool, from_none], self.seen_connect_section_coachmark)
        result["should_show_connect_section"] = from_union([from_bool, from_none], self.should_show_connect_section)
        result["enable_react_emoji_picker"] = from_union([from_bool, from_none], self.enable_react_emoji_picker)
        result["seen_custom_status_badge"] = from_union([from_bool, from_none], self.seen_custom_status_badge)
        result["seen_custom_status_callout"] = from_union([from_bool, from_none], self.seen_custom_status_callout)
        result["seen_custom_status_expiration_badge"] = from_union([from_bool, from_none], self.seen_custom_status_expiration_badge)
        result["used_custom_status_kb_shortcut"] = from_union([from_bool, from_none], self.used_custom_status_kb_shortcut)
        result["seen_guest_admin_slackbot_announcement"] = from_union([from_bool, from_none], self.seen_guest_admin_slackbot_announcement)
        result["seen_threads_notification_banner"] = from_union([from_bool, from_none], self.seen_threads_notification_banner)
        result["seen_name_tagging_coachmark"] = from_union([from_bool, from_none], self.seen_name_tagging_coachmark)
        result["all_unreads_sort_order"] = from_union([from_str, from_none], self.all_unreads_sort_order)
        result["all_unreads_section_filter"] = from_union([from_str, from_none], self.all_unreads_section_filter)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["seen_intl_channel_names_coachmark"] = from_union([from_bool, from_none], self.seen_intl_channel_names_coachmark)
        result["seen_p3_locale_change_message_ko_kr"] = from_union([from_int, from_none], self.seen_p3_locale_change_message_ko_kr)
        result["seen_toast_new_locale_launch"] = from_union([from_str, from_none], self.seen_toast_new_locale_launch)
        result["seen_toast_new_locale_launch_ts"] = from_union([from_int, from_none], self.seen_toast_new_locale_launch_ts)
        result["seen_locale_change_message"] = from_union([from_int, from_none], self.seen_locale_change_message)
        result["seen_japanese_locale_change_message"] = from_union([from_bool, from_none], self.seen_japanese_locale_change_message)
        result["seen_shared_channels_coachmark"] = from_union([from_bool, from_none], self.seen_shared_channels_coachmark)
        result["seen_shared_channels_opt_in_change_message"] = from_union([from_bool, from_none], self.seen_shared_channels_opt_in_change_message)
        result["has_recently_shared_a_channel"] = from_union([from_bool, from_none], self.has_recently_shared_a_channel)
        result["seen_channel_browser_admin_coachmark"] = from_union([from_bool, from_none], self.seen_channel_browser_admin_coachmark)
        result["seen_administration_menu"] = from_union([from_bool, from_none], self.seen_administration_menu)
        result["seen_drafts_section_coachmark"] = from_union([from_bool, from_none], self.seen_drafts_section_coachmark)
        result["seen_emoji_update_overlay_coachmark"] = from_union([from_bool, from_none], self.seen_emoji_update_overlay_coachmark)
        result["seen_sonic_deluxe_toast"] = from_union([from_int, from_none], self.seen_sonic_deluxe_toast)
        result["seen_wysiwyg_deluxe_toast"] = from_union([from_bool, from_none], self.seen_wysiwyg_deluxe_toast)
        result["seen_markdown_paste_toast"] = from_union([from_int, from_none], self.seen_markdown_paste_toast)
        result["seen_markdown_paste_shortcut"] = from_union([from_int, from_none], self.seen_markdown_paste_shortcut)
        result["seen_ia_education"] = from_union([from_bool, from_none], self.seen_ia_education)
        result["show_ia_tour_relaunch"] = from_union([from_int, from_none], self.show_ia_tour_relaunch)
        result["plain_text_mode"] = from_union([from_bool, from_none], self.plain_text_mode)
        result["show_shared_channels_education_banner"] = from_union([from_bool, from_none], self.show_shared_channels_education_banner)
        result["ia_slackbot_survey_timestamp_48h"] = from_union([from_int, from_none], self.ia_slackbot_survey_timestamp_48_h)
        result["ia_slackbot_survey_timestamp_7d"] = from_union([from_int, from_none], self.ia_slackbot_survey_timestamp_7_d)
        result["enable_streamline_view"] = from_union([from_bool, from_none], self.enable_streamline_view)
        result["enable_sent_view"] = from_union([from_bool, from_none], self.enable_sent_view)
        result["allow_calls_to_set_current_status"] = from_union([from_bool, from_none], self.allow_calls_to_set_current_status)
        result["in_interactive_mas_migration_flow"] = from_union([from_bool, from_none], self.in_interactive_mas_migration_flow)
        result["sunset_interactive_message_views"] = from_union([from_int, from_none], self.sunset_interactive_message_views)
        result["shdep_promo_code_submitted"] = from_union([from_bool, from_none], self.shdep_promo_code_submitted)
        result["seen_shdep_slackbot_message"] = from_union([from_bool, from_none], self.seen_shdep_slackbot_message)
        result["seen_calls_interactive_coachmark"] = from_union([from_bool, from_none], self.seen_calls_interactive_coachmark)
        result["allow_cmd_tab_iss"] = from_union([from_bool, from_none], self.allow_cmd_tab_iss)
        result["join_calls_device_settings"] = from_union([from_str, from_none], self.join_calls_device_settings)
        result["calls_disconnect_on_lock"] = from_union([from_bool, from_none], self.calls_disconnect_on_lock)
        result["seen_workflow_builder_deluxe_toast"] = from_union([from_bool, from_none], self.seen_workflow_builder_deluxe_toast)
        result["workflow_builder_intro_modal_clicked_through"] = from_union([from_bool, from_none], self.workflow_builder_intro_modal_clicked_through)
        result["workflow_builder_coachmarks"] = from_union([from_str, from_none], self.workflow_builder_coachmarks)
        result["seen_gdrive_coachmark"] = from_union([from_bool, from_none], self.seen_gdrive_coachmark)
        result["seen_first_install_coachmark"] = from_union([from_bool, from_none], self.seen_first_install_coachmark)
        result["seen_existing_install_coachmark"] = from_union([from_bool, from_none], self.seen_existing_install_coachmark)
        result["seen_link_unfurl_coachmark"] = from_union([from_bool, from_none], self.seen_link_unfurl_coachmark)
        result["file_picker_variant"] = from_union([from_int, from_none], self.file_picker_variant)
        result["open_quip_doc_in_flexpane"] = from_union([from_bool, from_none], self.open_quip_doc_in_flexpane)
        result["saved_searches"] = from_union([from_str, from_none], self.saved_searches)
        result["huddles_variant"] = from_union([from_int, from_none], self.huddles_variant)
        result["huddles_cc_by_default"] = from_union([from_bool, from_none], self.huddles_cc_by_default)
        result["huddles_mute_by_default"] = from_union([from_bool, from_none], self.huddles_mute_by_default)
        result["huddles_global_mute"] = from_union([from_bool, from_none], self.huddles_global_mute)
        result["huddles_mini_panel"] = from_union([from_bool, from_none], self.huddles_mini_panel)
        result["huddles_set_status"] = from_union([from_bool, from_none], self.huddles_set_status)
        result["huddles_show_shouty_rooster"] = from_union([from_bool, from_none], self.huddles_show_shouty_rooster)
        result["huddles_disconnect_on_lock"] = from_union([from_bool, from_none], self.huddles_disconnect_on_lock)
        result["huddles_play_music_when_last"] = from_union([from_bool, from_none], self.huddles_play_music_when_last)
        result["huddles_allow_smart_notif"] = from_union([from_bool, from_none], self.huddles_allow_smart_notif)
        result["huddles_reactions_play_sound"] = from_union([from_bool, from_none], self.huddles_reactions_play_sound)
        result["huddles_reactions_read_out_loud"] = from_union([from_bool, from_none], self.huddles_reactions_read_out_loud)
        result["huddles_chime_new_endpoints_check_completed"] = from_union([from_int, from_none], self.huddles_chime_new_endpoints_check_completed)
        result["xws_sidebar_variant"] = from_union([from_int, from_none], self.xws_sidebar_variant)
        result["inbox_views_workspace_filter"] = from_union([from_str, from_none], self.inbox_views_workspace_filter)
        result["overloaded_message_enabled"] = from_union([from_bool, from_none], self.overloaded_message_enabled)
        result["seen_highlights_coachmark"] = from_union([from_bool, from_none], self.seen_highlights_coachmark)
        result["seen_highlights_arrows_coachmark"] = from_union([from_bool, from_none], self.seen_highlights_arrows_coachmark)
        result["seen_highlights_warm_welcome"] = from_union([from_bool, from_none], self.seen_highlights_warm_welcome)
        result["seen_new_search_ui"] = from_union([from_bool, from_none], self.seen_new_search_ui)
        result["seen_channel_search"] = from_union([from_bool, from_none], self.seen_channel_search)
        result["seen_people_search"] = from_union([from_bool, from_none], self.seen_people_search)
        result["seen_people_search_count"] = from_union([from_int, from_none], self.seen_people_search_count)
        result["dismissed_scroll_search_tooltip_count"] = from_union([from_int, from_none], self.dismissed_scroll_search_tooltip_count)
        result["last_dismissed_scroll_search_tooltip_timestamp"] = from_union([from_int, from_none], self.last_dismissed_scroll_search_tooltip_timestamp)
        result["has_used_quickswitcher_shortcut"] = from_union([from_bool, from_none], self.has_used_quickswitcher_shortcut)
        result["seen_quickswitcher_shortcut_tip_count"] = from_union([from_int, from_none], self.seen_quickswitcher_shortcut_tip_count)
        result["browsers_dismissed_channels_low_results_education"] = from_union([from_bool, from_none], self.browsers_dismissed_channels_low_results_education)
        result["browsers_seen_initial_channels_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_channels_education)
        result["browsers_dismissed_people_low_results_education"] = from_union([from_bool, from_none], self.browsers_dismissed_people_low_results_education)
        result["browsers_seen_initial_people_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_people_education)
        result["browsers_dismissed_user_groups_low_results_education"] = from_union([from_bool, from_none], self.browsers_dismissed_user_groups_low_results_education)
        result["browsers_seen_initial_user_groups_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_user_groups_education)
        result["browsers_dismissed_files_low_results_education"] = from_union([from_bool, from_none], self.browsers_dismissed_files_low_results_education)
        result["browsers_seen_initial_files_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_files_education)
        result["browsers_dismissed_initial_drafts_education"] = from_union([from_bool, from_none], self.browsers_dismissed_initial_drafts_education)
        result["browsers_seen_initial_drafts_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_drafts_education)
        result["browsers_dismissed_initial_activity_education"] = from_union([from_bool, from_none], self.browsers_dismissed_initial_activity_education)
        result["browsers_seen_initial_activity_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_activity_education)
        result["browsers_dismissed_initial_saved_education"] = from_union([from_bool, from_none], self.browsers_dismissed_initial_saved_education)
        result["browsers_seen_initial_saved_education"] = from_union([from_bool, from_none], self.browsers_seen_initial_saved_education)
        result["seen_edit_mode"] = from_union([from_bool, from_none], self.seen_edit_mode)
        result["seen_edit_mode_edu"] = from_union([from_bool, from_none], self.seen_edit_mode_edu)
        result["xws_dismissed_education"] = from_union([from_bool, from_none], self.xws_dismissed_education)
        result["xws_seen_education"] = from_union([from_int, from_none], self.xws_seen_education)
        result["sidebar_pref_dismissed_tip"] = from_union([from_bool, from_none], self.sidebar_pref_dismissed_tip)
        result["a11y_dyslexic"] = from_union([from_bool, from_none], self.a11_y_dyslexic)
        result["a11y_animations"] = from_union([from_bool, from_none], self.a11_y_animations)
        result["seen_keyboard_shortcuts_coachmark"] = from_union([from_bool, from_none], self.seen_keyboard_shortcuts_coachmark)
        result["needs_initial_password_set"] = from_union([from_bool, from_none], self.needs_initial_password_set)
        result["lessons_enabled"] = from_union([from_bool, from_none], self.lessons_enabled)
        result["tractor_enabled"] = from_union([from_bool, from_none], self.tractor_enabled)
        result["tractor_experiment_group"] = from_union([from_str, from_none], self.tractor_experiment_group)
        result["opened_slackbot_dm"] = from_union([from_bool, from_none], self.opened_slackbot_dm)
        result["newxp_seen_help_message"] = from_union([from_int, from_none], self.newxp_seen_help_message)
        result["newxp_suggested_channels"] = from_union([from_str, from_none], self.newxp_suggested_channels)
        result["onboarding_complete"] = from_union([from_bool, from_none], self.onboarding_complete)
        result["welcome_place_state"] = from_union([from_str, from_none], self.welcome_place_state)
        result["has_received_threaded_message"] = from_union([from_bool, from_none], self.has_received_threaded_message)
        result["joiner_notifications_muted"] = from_union([from_bool, from_none], self.joiner_notifications_muted)
        result["invite_accepted_notifications_muted"] = from_union([from_bool, from_none], self.invite_accepted_notifications_muted)
        result["joiner_message_suggestion_dismissed"] = from_union([from_bool, from_none], self.joiner_message_suggestion_dismissed)
        result["dismissed_fullscreen_download_ssb_prompt"] = from_union([from_bool, from_none], self.dismissed_fullscreen_download_ssb_prompt)
        result["dismissed_banner_download_ssb_prompt"] = from_union([from_bool, from_none], self.dismissed_banner_download_ssb_prompt)
        result["onboarding_state"] = from_union([from_int, from_none], self.onboarding_state)
        result["whocanseethis_dm_mpdm_badge"] = from_union([from_bool, from_none], self.whocanseethis_dm_mpdm_badge)
        result["highlight_words"] = from_union([from_str, from_none], self.highlight_words)
        result["threads_everything"] = from_union([from_bool, from_none], self.threads_everything)
        result["no_text_in_notifications"] = from_union([from_bool, from_none], self.no_text_in_notifications)
        result["push_show_preview"] = from_union([from_bool, from_none], self.push_show_preview)
        result["growls_enabled"] = from_union([from_bool, from_none], self.growls_enabled)
        result["all_channels_loud"] = from_union([from_bool, from_none], self.all_channels_loud)
        result["push_dm_alert"] = from_union([from_bool, from_none], self.push_dm_alert)
        result["push_mention_alert"] = from_union([from_bool, from_none], self.push_mention_alert)
        result["push_everything"] = from_union([from_bool, from_none], self.push_everything)
        result["push_idle_wait"] = from_union([from_int, from_none], self.push_idle_wait)
        result["push_sound"] = from_union([from_str, from_none], self.push_sound)
        result["new_msg_snd"] = from_union([from_str, from_none], self.new_msg_snd)
        result["huddle_invite_sound"] = from_union([from_str, from_none], self.huddle_invite_sound)
        result["push_loud_channels"] = from_union([from_str, from_none], self.push_loud_channels)
        result["push_mention_channels"] = from_union([from_str, from_none], self.push_mention_channels)
        result["push_loud_channels_set"] = from_union([from_str, from_none], self.push_loud_channels_set)
        result["loud_channels"] = from_union([from_str, from_none], self.loud_channels)
        result["never_channels"] = from_union([from_str, from_none], self.never_channels)
        result["loud_channels_set"] = from_union([from_str, from_none], self.loud_channels_set)
        result["at_channel_suppressed_channels"] = from_union([from_str, from_none], self.at_channel_suppressed_channels)
        result["push_at_channel_suppressed_channels"] = from_union([from_str, from_none], self.push_at_channel_suppressed_channels)
        result["muted_channels"] = from_union([from_str, from_none], self.muted_channels)
        result["all_notifications_prefs"] = from_union([from_str, from_none], self.all_notifications_prefs)
        result["growth_msg_limit_approaching_cta_count"] = from_union([from_int, from_none], self.growth_msg_limit_approaching_cta_count)
        result["growth_msg_limit_approaching_cta_ts"] = from_union([from_int, from_none], self.growth_msg_limit_approaching_cta_ts)
        result["growth_msg_limit_reached_cta_count"] = from_union([from_int, from_none], self.growth_msg_limit_reached_cta_count)
        result["growth_msg_limit_reached_cta_last_ts"] = from_union([from_int, from_none], self.growth_msg_limit_reached_cta_last_ts)
        result["growth_msg_limit_long_reached_cta_count"] = from_union([from_int, from_none], self.growth_msg_limit_long_reached_cta_count)
        result["growth_msg_limit_long_reached_cta_last_ts"] = from_union([from_int, from_none], self.growth_msg_limit_long_reached_cta_last_ts)
        result["growth_msg_limit_sixty_day_banner_cta_count"] = from_union([from_int, from_none], self.growth_msg_limit_sixty_day_banner_cta_count)
        result["growth_msg_limit_sixty_day_banner_cta_last_ts"] = from_union([from_int, from_none], self.growth_msg_limit_sixty_day_banner_cta_last_ts)
        result["growth_all_banners_prefs"] = from_union([from_str, from_none], self.growth_all_banners_prefs)
        result["analytics_upsell_coachmark_seen"] = from_union([from_bool, from_none], self.analytics_upsell_coachmark_seen)
        result["seen_app_space_coachmark"] = from_union([from_bool, from_none], self.seen_app_space_coachmark)
        result["seen_app_space_tutorial"] = from_union([from_bool, from_none], self.seen_app_space_tutorial)
        result["dismissed_app_launcher_welcome"] = from_union([from_bool, from_none], self.dismissed_app_launcher_welcome)
        result["dismissed_app_launcher_limit"] = from_union([from_bool, from_none], self.dismissed_app_launcher_limit)
        result["dismissed_app_launcher_atlassian_promo"] = from_union([from_bool, from_none], self.dismissed_app_launcher_atlassian_promo)
        result["enable_app_config_redesign"] = from_union([from_bool, from_none], self.enable_app_config_redesign)
        result["dismissed_app_config_redesign_coachmark"] = from_union([from_bool, from_none], self.dismissed_app_config_redesign_coachmark)
        result["dismissed_app_manifest_description"] = from_union([from_bool, from_none], self.dismissed_app_manifest_description)
        result["dismissed_app_manifest_coachmark"] = from_union([from_bool, from_none], self.dismissed_app_manifest_coachmark)
        result["purchaser"] = from_union([from_bool, from_none], self.purchaser)
        result["seen_channel_email_tooltip"] = from_union([from_bool, from_none], self.seen_channel_email_tooltip)
        result["show_ent_onboarding"] = from_union([from_bool, from_none], self.show_ent_onboarding)
        result["folders_enabled"] = from_union([from_bool, from_none], self.folders_enabled)
        result["folder_data"] = from_union([from_str, from_none], self.folder_data)
        result["seen_corporate_export_alert"] = from_union([from_bool, from_none], self.seen_corporate_export_alert)
        result["show_autocomplete_help"] = from_union([from_int, from_none], self.show_autocomplete_help)
        result["deprecation_toast_last_seen"] = from_union([from_int, from_none], self.deprecation_toast_last_seen)
        result["deprecation_modal_last_seen"] = from_union([from_int, from_none], self.deprecation_modal_last_seen)
        result["deprecation_banner_last_seen"] = from_union([from_int, from_none], self.deprecation_banner_last_seen)
        result["iap1_lab"] = from_union([from_int, from_none], self.iap1_lab)
        result["ia_top_nav_theme"] = from_union([from_str, from_none], self.ia_top_nav_theme)
        result["ia_platform_actions_lab"] = from_union([from_int, from_none], self.ia_platform_actions_lab)
        result["activity_view"] = from_union([from_str, from_none], self.activity_view)
        result["saved_view"] = from_union([from_str, from_none], self.saved_view)
        result["seen_floating_sidebar_coachmark"] = from_union([from_bool, from_none], self.seen_floating_sidebar_coachmark)
        result["desktop_client_ids"] = from_union([from_str, from_none], self.desktop_client_ids)
        result["failover_proxy_check_completed"] = from_union([from_int, from_none], self.failover_proxy_check_completed)
        result["chime_access_check_completed"] = from_union([from_int, from_none], self.chime_access_check_completed)
        result["mx_calendar_type"] = from_union([from_str, from_none], self.mx_calendar_type)
        result["edge_upload_proxy_check_completed"] = from_union([from_int, from_none], self.edge_upload_proxy_check_completed)
        result["app_subdomain_check_completed"] = from_union([from_int, from_none], self.app_subdomain_check_completed)
        result["add_prompt_interacted"] = from_union([from_bool, from_none], self.add_prompt_interacted)
        result["add_apps_prompt_dismissed"] = from_union([from_bool, from_none], self.add_apps_prompt_dismissed)
        result["add_channel_prompt_dismissed"] = from_union([from_bool, from_none], self.add_channel_prompt_dismissed)
        result["channel_sidebar_hide_invite"] = from_union([from_bool, from_none], self.channel_sidebar_hide_invite)
        result["channel_sidebar_hide_browse_dms_link"] = from_union([from_bool, from_none], self.channel_sidebar_hide_browse_dms_link)
        result["in_prod_surveys_enabled"] = from_union([from_bool, from_none], self.in_prod_surveys_enabled)
        result["connect_dm_early_access"] = from_union([from_bool, from_none], self.connect_dm_early_access)
        result["dismissed_installed_app_dm_suggestions"] = from_union([from_str, from_none], self.dismissed_installed_app_dm_suggestions)
        result["seen_contextual_message_shortcuts_modal"] = from_union([from_bool, from_none], self.seen_contextual_message_shortcuts_modal)
        result["seen_message_navigation_educational_toast"] = from_union([from_bool, from_none], self.seen_message_navigation_educational_toast)
        result["contextual_message_shortcuts_modal_was_seen"] = from_union([from_bool, from_none], self.contextual_message_shortcuts_modal_was_seen)
        result["message_navigation_toast_was_seen"] = from_union([from_bool, from_none], self.message_navigation_toast_was_seen)
        result["up_to_browse_kb_shortcut"] = from_union([from_bool, from_none], self.up_to_browse_kb_shortcut)
        result["set_a11y_prefs_new_user"] = from_union([from_bool, from_none], self.set_a11_y_prefs_new_user)
        result["a11y_play_sound_for_incoming_dm"] = from_union([from_bool, from_none], self.a11_y_play_sound_for_incoming_dm)
        result["a11y_play_sound_for_sent_dm"] = from_union([from_bool, from_none], self.a11_y_play_sound_for_sent_dm)
        result["a11y_read_out_incoming_dm"] = from_union([from_bool, from_none], self.a11_y_read_out_incoming_dm)
        result["a11y_screen_reader_message_label_date_time_first"] = from_union([from_bool, from_none], self.a11_y_screen_reader_message_label_date_time_first)
        result["should_show_contextual_help_for_conversation_navigation"] = from_union([from_bool, from_none], self.should_show_contextual_help_for_conversation_navigation)
        result["should_show_contextual_help_for_jump_to_conversation"] = from_union([from_bool, from_none], self.should_show_contextual_help_for_jump_to_conversation)
        result["should_show_contextual_help_for_section_navigation"] = from_union([from_bool, from_none], self.should_show_contextual_help_for_section_navigation)
        result["should_show_contextual_help_for_thread_navigation"] = from_union([from_bool, from_none], self.should_show_contextual_help_for_thread_navigation)
        result["should_show_unsend_message_confirmation"] = from_union([from_bool, from_none], self.should_show_unsend_message_confirmation)
        result["channel_sections"] = from_union([from_str, from_none], self.channel_sections)
        result["show_quick_reactions"] = from_union([from_bool, from_none], self.show_quick_reactions)
        result["user_customized_quick_reactions_display_feature"] = from_union([from_int, from_none], self.user_customized_quick_reactions_display_feature)
        result["user_customized_quick_reactions_has_customized"] = from_union([from_bool, from_none], self.user_customized_quick_reactions_has_customized)
        result["user_customized_quick_reactions_use_frequently_used_emoji"] = from_union([from_bool, from_none], self.user_customized_quick_reactions_use_frequently_used_emoji)
        result["reaction_notifications"] = from_union([from_str, from_none], self.reaction_notifications)
        result["has_received_mention_or_reaction"] = from_union([from_bool, from_none], self.has_received_mention_or_reaction)
        result["has_starred_item"] = from_union([from_bool, from_none], self.has_starred_item)
        result["has_drafted_message"] = from_union([from_bool, from_none], self.has_drafted_message)
        result["enable_mentions_and_reactions_view"] = from_union([from_bool, from_none], self.enable_mentions_and_reactions_view)
        result["enable_reminders_view"] = from_union([from_bool, from_none], self.enable_reminders_view)
        result["enable_saved_items_view"] = from_union([from_bool, from_none], self.enable_saved_items_view)
        result["enable_hq_view"] = from_union([from_bool, from_none], self.enable_hq_view)
        result["enable_all_dms_view"] = from_union([from_bool, from_none], self.enable_all_dms_view)
        result["enable_channel_browser_view"] = from_union([from_bool, from_none], self.enable_channel_browser_view)
        result["enable_file_browser_view"] = from_union([from_bool, from_none], self.enable_file_browser_view)
        result["enable_people_browser_view"] = from_union([from_bool, from_none], self.enable_people_browser_view)
        result["enable_app_browser_view"] = from_union([from_bool, from_none], self.enable_app_browser_view)
        result["reached_all_dms_disclosure"] = from_union([from_bool, from_none], self.reached_all_dms_disclosure)
        result["enable_slack_connect_view"] = from_union([from_bool, from_none], self.enable_slack_connect_view)
        result["enable_slack_connect_view_2"] = from_union([from_int, from_none], self.enable_slack_connect_view_2)
        result["has_acknowledged_shortcut_speedbump"] = from_union([from_bool, from_none], self.has_acknowledged_shortcut_speedbump)
        result["enable_media_captions"] = from_union([from_bool, from_none], self.enable_media_captions)
        result["media_playback_speed"] = from_union([from_int, from_none], self.media_playback_speed)
        result["media_muted"] = from_union([from_bool, from_none], self.media_muted)
        result["media_volume"] = from_union([from_int, from_none], self.media_volume)
        result["dismissed_connect_auto_approval_modal"] = from_union([from_str, from_none], self.dismissed_connect_auto_approval_modal)
        result["tasks_view"] = from_union([from_str, from_none], self.tasks_view)
        result["show_sidebar_avatars"] = from_union([from_bool, from_none], self.show_sidebar_avatars)
        result["has_dismissed_google_directory_coachmark"] = from_union([from_bool, from_none], self.has_dismissed_google_directory_coachmark)
        result["seen_sc_page_banner"] = from_union([from_bool, from_none], self.seen_sc_page_banner)
        result["seen_sc_menu_coachmark"] = from_union([from_bool, from_none], self.seen_sc_menu_coachmark)
        result["seen_sc_page"] = from_union([from_bool, from_none], self.seen_sc_page)
        result["dismissed_scdm_education"] = from_union([from_bool, from_none], self.dismissed_scdm_education)
        result["seen_bookmarks_intro"] = from_union([from_bool, from_none], self.seen_bookmarks_intro)
        result["scdm_trial_offer_banner"] = from_union([from_str, from_none], self.scdm_trial_offer_banner)
        result["identity_links_prefs"] = from_union([from_str, from_none], self.identity_links_prefs)
        result["identity_links_global_prefs"] = from_union([from_str, from_none], self.identity_links_global_prefs)
        result["seen_sections_unreads_only_prompt_count"] = from_union([from_int, from_none], self.seen_sections_unreads_only_prompt_count)
        result["last_seen_sections_unreads_only_prompt_timestamp"] = from_union([from_int, from_none], self.last_seen_sections_unreads_only_prompt_timestamp)
        result["notifications_view"] = from_union([from_str, from_none], self.notifications_view)
        result["progressive_disclosure_state"] = from_union([from_str, from_none], self.progressive_disclosure_state)
        result["suggestions_request_id"] = from_union([from_str, from_none], self.suggestions_request_id)
        result["allowed_unfurl_senders"] = from_union([from_str, from_none], self.allowed_unfurl_senders)
        result["ia_details_coachmark_seen"] = from_union([from_bool, from_none], self.ia_details_coachmark_seen)
        result["hide_external_members_sharing_speed_bump"] = from_union([from_bool, from_none], self.hide_external_members_sharing_speed_bump)
        result["who_can_share_contact_card"] = from_union([from_str, from_none], self.who_can_share_contact_card)
        result["slack_connect_invite_should_badge_sidebar"] = from_union([from_bool, from_none], self.slack_connect_invite_should_badge_sidebar)
        result["phc_dismissed"] = from_union([from_str, from_none], self.phc_dismissed)
        result["dismissed_gov_slack_first_time_popup"] = from_union([from_bool, from_none], self.dismissed_gov_slack_first_time_popup)
        result["mobile_channel_list_sort"] = from_union([from_str, from_none], self.mobile_channel_list_sort)
        result["user_expectations_survey_last_trigger_attempt"] = from_union([from_int, from_none], self.user_expectations_survey_last_trigger_attempt)
        result["tz"] = from_union([from_str, from_none], self.tz)
        result["locales_enabled"] = from_union([lambda x: to_class(LocalesEnabled, x), from_none], self.locales_enabled)
        result["phc_viewed"] = from_union([from_str, from_none], self.phc_viewed)
        result["seen_a11y_pref_setup_coachmark"] = from_union([from_bool, from_none], self.seen_a11_y_pref_setup_coachmark)
        result["enable_file_browser_view_for_docs"] = from_union([from_bool, from_none], self.enable_file_browser_view_for_docs)
        result["enable_shortcuts_view"] = from_union([from_bool, from_none], self.enable_shortcuts_view)
        result["show_gov_slack_context_bar_banner"] = from_union([from_bool, from_none], self.show_gov_slack_context_bar_banner)
        result["who_can_see_account_by_searching_email"] = from_union([from_str, from_none], self.who_can_see_account_by_searching_email)
        result["contextual_help_reset_count"] = from_union([from_int, from_none], self.contextual_help_reset_count)
        return result


@dataclass
class Self:
    id: Optional[str] = None
    name: Optional[str] = None
    prefs: Optional[SelfPrefs] = None
    created: Optional[int] = None
    first_login: Optional[int] = None
    manual_presence: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Self':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        prefs = from_union([SelfPrefs.from_dict, from_none], obj.get("prefs"))
        created = from_union([from_int, from_none], obj.get("created"))
        first_login = from_union([from_int, from_none], obj.get("first_login"))
        manual_presence = from_union([from_str, from_none], obj.get("manual_presence"))
        return Self(id, name, prefs, created, first_login, manual_presence)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["prefs"] = from_union([lambda x: to_class(SelfPrefs, x), from_none], self.prefs)
        result["created"] = from_union([from_int, from_none], self.created)
        result["first_login"] = from_union([from_int, from_none], self.first_login)
        result["manual_presence"] = from_union([from_str, from_none], self.manual_presence)
        return result


@dataclass
class AllPrefs:
    channels: Optional[List[str]] = None
    groups: Optional[List[Group]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AllPrefs':
        assert isinstance(obj, dict)
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(Group.from_dict, x), from_none], obj.get("groups"))
        return AllPrefs(channels, groups)

    def to_dict(self) -> dict:
        result: dict = {}
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(lambda x: to_class(Group, x), x), from_none], self.groups)
        return result


@dataclass
class All:
    id: Optional[str] = None
    team_id: Optional[str] = None
    is_usergroup: Optional[bool] = None
    is_subteam: Optional[bool] = None
    name: Optional[str] = None
    description: Optional[str] = None
    handle: Optional[str] = None
    is_external: Optional[bool] = None
    date_create: Optional[int] = None
    date_update: Optional[int] = None
    date_delete: Optional[int] = None
    auto_provision: Optional[bool] = None
    enterprise_subteam_id: Optional[str] = None
    created_by: Optional[str] = None
    updated_by: Optional[str] = None
    prefs: Optional[AllPrefs] = None
    user_count: Optional[int] = None
    channel_count: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'All':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        is_usergroup = from_union([from_bool, from_none], obj.get("is_usergroup"))
        is_subteam = from_union([from_bool, from_none], obj.get("is_subteam"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        handle = from_union([from_str, from_none], obj.get("handle"))
        is_external = from_union([from_bool, from_none], obj.get("is_external"))
        date_create = from_union([from_int, from_none], obj.get("date_create"))
        date_update = from_union([from_int, from_none], obj.get("date_update"))
        date_delete = from_union([from_int, from_none], obj.get("date_delete"))
        auto_provision = from_union([from_bool, from_none], obj.get("auto_provision"))
        enterprise_subteam_id = from_union([from_str, from_none], obj.get("enterprise_subteam_id"))
        created_by = from_union([from_str, from_none], obj.get("created_by"))
        updated_by = from_union([from_str, from_none], obj.get("updated_by"))
        prefs = from_union([AllPrefs.from_dict, from_none], obj.get("prefs"))
        user_count = from_union([from_int, from_none], obj.get("user_count"))
        channel_count = from_union([from_int, from_none], obj.get("channel_count"))
        return All(id, team_id, is_usergroup, is_subteam, name, description, handle, is_external, date_create, date_update, date_delete, auto_provision, enterprise_subteam_id, created_by, updated_by, prefs, user_count, channel_count)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["is_usergroup"] = from_union([from_bool, from_none], self.is_usergroup)
        result["is_subteam"] = from_union([from_bool, from_none], self.is_subteam)
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["handle"] = from_union([from_str, from_none], self.handle)
        result["is_external"] = from_union([from_bool, from_none], self.is_external)
        result["date_create"] = from_union([from_int, from_none], self.date_create)
        result["date_update"] = from_union([from_int, from_none], self.date_update)
        result["date_delete"] = from_union([from_int, from_none], self.date_delete)
        result["auto_provision"] = from_union([from_bool, from_none], self.auto_provision)
        result["enterprise_subteam_id"] = from_union([from_str, from_none], self.enterprise_subteam_id)
        result["created_by"] = from_union([from_str, from_none], self.created_by)
        result["updated_by"] = from_union([from_str, from_none], self.updated_by)
        result["prefs"] = from_union([lambda x: to_class(AllPrefs, x), from_none], self.prefs)
        result["user_count"] = from_union([from_int, from_none], self.user_count)
        result["channel_count"] = from_union([from_int, from_none], self.channel_count)
        return result


@dataclass
class Subteams:
    subteams_self: Optional[List[str]] = None
    all: Optional[List[All]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Subteams':
        assert isinstance(obj, dict)
        subteams_self = from_union([lambda x: from_list(from_str, x), from_none], obj.get("self"))
        all = from_union([lambda x: from_list(All.from_dict, x), from_none], obj.get("all"))
        return Subteams(subteams_self, all)

    def to_dict(self) -> dict:
        result: dict = {}
        result["self"] = from_union([lambda x: from_list(from_str, x), from_none], self.subteams_self)
        result["all"] = from_union([lambda x: from_list(lambda x: to_class(All, x), x), from_none], self.all)
        return result


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
        return Icon(image_102, image_132, image_230, image_34, image_44, image_68, image_88, image_original)

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
        return result


@dataclass
class Video:
    id: Optional[str] = None
    name: Optional[str] = None
    image: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Video':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        image = from_union([from_str, from_none], obj.get("image"))
        return Video(id, name, image)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["image"] = from_union([from_str, from_none], self.image)
        return result


@dataclass
class CallsApps:
    video: Optional[List[Video]] = None
    audio: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CallsApps':
        assert isinstance(obj, dict)
        video = from_union([lambda x: from_list(Video.from_dict, x), from_none], obj.get("video"))
        audio = from_union([lambda x: from_list(from_str, x), from_none], obj.get("audio"))
        return CallsApps(video, audio)

    def to_dict(self) -> dict:
        result: dict = {}
        result["video"] = from_union([lambda x: from_list(lambda x: to_class(Video, x), x), from_none], self.video)
        result["audio"] = from_union([lambda x: from_list(from_str, x), from_none], self.audio)
        return result


@dataclass
class EnterpriseTeamCreationRequest:
    is_enabled: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EnterpriseTeamCreationRequest':
        assert isinstance(obj, dict)
        is_enabled = from_union([from_bool, from_none], obj.get("is_enabled"))
        return EnterpriseTeamCreationRequest(is_enabled)

    def to_dict(self) -> dict:
        result: dict = {}
        result["is_enabled"] = from_union([from_bool, from_none], self.is_enabled)
        return result


@dataclass
class InvitedUserPreset:
    enable_invited_user: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'InvitedUserPreset':
        assert isinstance(obj, dict)
        enable_invited_user = from_union([from_bool, from_none], obj.get("enable_invited_user"))
        return InvitedUserPreset(enable_invited_user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["enable_invited_user"] = from_union([from_bool, from_none], self.enable_invited_user)
        return result


@dataclass
class SlackConnectAllowedWorkspaces:
    type: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlackConnectAllowedWorkspaces':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        return SlackConnectAllowedWorkspaces(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        return result


@dataclass
class WhoCanManageP:
    user: Optional[List[str]] = None
    type: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'WhoCanManageP':
        assert isinstance(obj, dict)
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        return WhoCanManageP(user, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        return result


@dataclass
class TeamPrefs:
    default_channels: Optional[List[str]] = None
    allow_calls: Optional[bool] = None
    display_email_addresses: Optional[bool] = None
    gdrive_enabled_team: Optional[bool] = None
    all_users_can_purchase: Optional[bool] = None
    enable_shared_channels: Optional[int] = None
    can_receive_shared_channels_invites: Optional[bool] = None
    invited_user_preset: Optional[InvitedUserPreset] = None
    dropbox_legacy_picker: Optional[bool] = None
    app_whitelist_enabled: Optional[bool] = None
    who_can_manage_integrations: Optional[SlackConnectAllowedWorkspaces] = None
    welcome_place_enabled: Optional[bool] = None
    msg_edit_window_mins: Optional[int] = None
    allow_message_deletion: Optional[bool] = None
    display_external_email_addresses: Optional[bool] = None
    joiner_notifications_enabled: Optional[bool] = None
    received_esc_route_to_channel_awareness_message: Optional[bool] = None
    who_can_create_channels: Optional[str] = None
    who_can_archive_channels: Optional[str] = None
    who_can_create_groups: Optional[str] = None
    who_can_manage_channel_posting_prefs: Optional[str] = None
    who_can_kick_channels: Optional[str] = None
    who_can_kick_groups: Optional[str] = None
    locale: Optional[str] = None
    display_pronouns: Optional[bool] = None
    admin_customized_quick_reactions: Optional[List[str]] = None
    allow_admin_retention_override: Optional[int] = None
    allow_audio_clip_sharing_slack_connect: Optional[bool] = None
    allow_audio_clips: Optional[bool] = None
    allow_box_cfs: Optional[bool] = None
    allow_calls_interactive_screen_sharing: Optional[bool] = None
    allow_clip_downloads: Optional[str] = None
    allow_huddles: Optional[bool] = None
    allow_huddles_transcriptions: Optional[bool] = None
    allow_media_transcriptions: Optional[bool] = None
    allow_retention_override: Optional[bool] = None
    allow_sponsored_slack_connections: Optional[bool] = None
    allow_video_clip_sharing_slack_connect: Optional[bool] = None
    allow_video_clips: Optional[bool] = None
    app_dir_only: Optional[bool] = None
    app_management_apps: Optional[List[str]] = None
    block_file_download: Optional[bool] = None
    box_app_installed: Optional[bool] = None
    calls_apps: Optional[CallsApps] = None
    calls_locations: Optional[List[str]] = None
    can_accept_slack_connect_channel_invites: Optional[bool] = None
    can_create_external_limited_invite: Optional[bool] = None
    can_create_slack_connect_channel_invite: Optional[bool] = None
    channel_email_addresses_enabled: Optional[bool] = None
    compliance_export_start: Optional[int] = None
    content_review_enabled: Optional[bool] = None
    created_with_google: Optional[bool] = None
    custom_status_default_emoji: Optional[str] = None
    custom_status_presets: Optional[List[List[str]]] = None
    default_channel_creation_enabled: Optional[bool] = None
    default_rxns: Optional[List[str]] = None
    disable_email_ingestion: Optional[bool] = None
    disable_file_deleting: Optional[bool] = None
    disable_file_editing: Optional[bool] = None
    disable_file_uploads: Optional[str] = None
    disable_sidebar_connect_prompts: Optional[List[str]] = None
    disable_sidebar_install_prompts: Optional[List[str]] = None
    disallow_public_file_urls: Optional[bool] = None
    discoverable: Optional[str] = None
    display_default_phone: Optional[bool] = None
    display_name_pronunciation: Optional[bool] = None
    display_real_names: Optional[bool] = None
    dm_retention_duration: Optional[int] = None
    dm_retention_type: Optional[int] = None
    dnd_days: Optional[str] = None
    enable_connect_dm_early_access: Optional[bool] = None
    enable_domain_allowlist_for_cea: Optional[bool] = None
    enable_info_barriers: Optional[bool] = None
    enable_mpdm_to_private_channel_conversion: Optional[bool] = None
    enterprise_default_channels: Optional[List[str]] = None
    enterprise_has_corporate_exports: Optional[bool] = None
    enterprise_intune_enabled: Optional[bool] = None
    enterprise_mandatory_channels: Optional[List[str]] = None
    enterprise_mdm_date_enabled: Optional[int] = None
    enterprise_mdm_disable_file_download: Optional[bool] = None
    enterprise_mdm_level: Optional[int] = None
    enterprise_mobile_device_check: Optional[bool] = None
    enterprise_team_creation_request: Optional[EnterpriseTeamCreationRequest] = None
    file_limit_whitelisted: Optional[bool] = None
    file_retention_duration: Optional[int] = None
    file_retention_type: Optional[int] = None
    filepicker_app_first_install: Optional[bool] = None
    gg_enabled: Optional[bool] = None
    group_retention_duration: Optional[int] = None
    group_retention_type: Optional[int] = None
    has_compliance_export: Optional[bool] = None
    has_hipaa_compliance: Optional[bool] = None
    has_seen_partner_promo: Optional[bool] = None
    hermes_has_accepted_tos: Optional[bool] = None
    hermes_triggers_trippable_by_slack_connected_teams: Optional[bool] = None
    hide_gsuite_invite_option: Optional[bool] = None
    hide_referers: Optional[bool] = None
    invite_requests_enabled: Optional[bool] = None
    invites_only_admins: Optional[bool] = None
    loud_channel_mentions_limit: Optional[int] = None
    member_analytics_disabled: Optional[bool] = None
    ml_opt_out: Optional[bool] = None
    mobile_passcode_timeout_in_seconds: Optional[int] = None
    notification_redaction_type: Optional[str] = None
    notify_pending_enabled: Optional[bool] = None
    ntlm_credential_domains: Optional[str] = None
    onedrive_app_installed: Optional[bool] = None
    onedrive_enabled_team: Optional[bool] = None
    private_channel_membership_limit: Optional[int] = None
    retention_duration: Optional[int] = None
    retention_type: Optional[int] = None
    search_feedback_opt_out: Optional[bool] = None
    self_serve_select: Optional[bool] = None
    session_duration: Optional[int] = None
    session_duration_type: Optional[int] = None
    show_join_leave: Optional[bool] = None
    show_legacy_paid_benefits_page: Optional[bool] = None
    sign_in_with_slack_disabled: Optional[bool] = None
    single_user_exports: Optional[bool] = None
    slack_connect_allowed_workspaces: Optional[SlackConnectAllowedWorkspaces] = None
    slack_connect_approval_type: Optional[str] = None
    slack_connect_dm_only_verified_orgs: Optional[bool] = None
    slack_connect_file_upload_sharing_enabled: Optional[bool] = None
    slackbot_responses_disabled: Optional[bool] = None
    sso_disable_emails: Optional[bool] = None
    sso_optional: Optional[bool] = None
    sso_signup_restrictions: Optional[int] = None
    sso_sync_with_provider: Optional[bool] = None
    subteams_auto_create_admin: Optional[bool] = None
    subteams_auto_create_owner: Optional[bool] = None
    use_browser_picker: Optional[bool] = None
    uses_customized_custom_status_presets: Optional[bool] = None
    warn_before_at_channel: Optional[str] = None
    who_can_accept_slack_connect_channel_invites: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_at_channel: Optional[str] = None
    who_can_at_everyone: Optional[str] = None
    who_can_change_team_profile: Optional[str] = None
    who_can_create_delete_user_groups: Optional[str] = None
    who_can_create_external_limited_invite: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_create_shared_channels: Optional[str] = None
    who_can_create_slack_connect_channel_invite: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_dm_anyone: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_edit_user_groups: Optional[str] = None
    who_can_manage_ext_shared_channels: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_manage_guests: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_manage_private_channels: Optional[WhoCanManageP] = None
    who_can_manage_private_channels_at_workspace_level: Optional[WhoCanManageP] = None
    who_can_manage_public_channels: Optional[WhoCanManageP] = None
    who_can_manage_shared_channels: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_post_general: Optional[str] = None
    who_can_post_in_shared_channels: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_request_ext_shared_channels: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_review_flagged_content: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_view_message_activity: Optional[SlackConnectAllowedWorkspaces] = None
    workflow_builder_enabled: Optional[bool] = None
    workflow_extension_steps_beta_opt_in: Optional[bool] = None
    dnd_enabled: Optional[bool] = None
    dnd_start_hour: Optional[str] = None
    dnd_end_hour: Optional[str] = None
    dnd_before_monday: Optional[str] = None
    dnd_after_monday: Optional[str] = None
    dnd_before_tuesday: Optional[str] = None
    dnd_after_tuesday: Optional[str] = None
    dnd_before_wednesday: Optional[str] = None
    dnd_after_wednesday: Optional[str] = None
    dnd_before_thursday: Optional[str] = None
    dnd_after_thursday: Optional[str] = None
    dnd_before_friday: Optional[str] = None
    dnd_after_friday: Optional[str] = None
    dnd_before_saturday: Optional[str] = None
    dnd_after_saturday: Optional[str] = None
    dnd_before_sunday: Optional[str] = None
    dnd_after_sunday: Optional[str] = None
    dnd_enabled_monday: Optional[str] = None
    dnd_enabled_tuesday: Optional[str] = None
    dnd_enabled_wednesday: Optional[str] = None
    dnd_enabled_thursday: Optional[str] = None
    dnd_enabled_friday: Optional[str] = None
    dnd_enabled_saturday: Optional[str] = None
    dnd_enabled_sunday: Optional[str] = None
    dnd_weekdays_off_allday: Optional[bool] = None
    auth_mode: Optional[str] = None
    who_can_create_workflows: Optional[SlackConnectAllowedWorkspaces] = None
    workflows_webhook_trigger_enabled: Optional[bool] = None
    workflow_extension_steps_enabled: Optional[bool] = None
    workflows_export_csv_enabled: Optional[bool] = None
    who_can_use_hermes: Optional[SlackConnectAllowedWorkspaces] = None
    who_can_create_channel_email_addresses: Optional[SlackConnectAllowedWorkspaces] = None
    identity_links_prefs: Optional[EnterpriseTeamCreationRequest] = None
    magic_unfurls_enabled: Optional[bool] = None
    invites_limit: Optional[bool] = None
    show_mobile_promos: Optional[bool] = None
    dm_retention_redaction_duration: Optional[int] = None
    private_retention_redaction_duration: Optional[int] = None
    public_retention_redaction_duration: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'TeamPrefs':
        assert isinstance(obj, dict)
        default_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("default_channels"))
        allow_calls = from_union([from_bool, from_none], obj.get("allow_calls"))
        display_email_addresses = from_union([from_bool, from_none], obj.get("display_email_addresses"))
        gdrive_enabled_team = from_union([from_bool, from_none], obj.get("gdrive_enabled_team"))
        all_users_can_purchase = from_union([from_bool, from_none], obj.get("all_users_can_purchase"))
        enable_shared_channels = from_union([from_int, from_none], obj.get("enable_shared_channels"))
        can_receive_shared_channels_invites = from_union([from_bool, from_none], obj.get("can_receive_shared_channels_invites"))
        invited_user_preset = from_union([InvitedUserPreset.from_dict, from_none], obj.get("invited_user_preset"))
        dropbox_legacy_picker = from_union([from_bool, from_none], obj.get("dropbox_legacy_picker"))
        app_whitelist_enabled = from_union([from_bool, from_none], obj.get("app_whitelist_enabled"))
        who_can_manage_integrations = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_manage_integrations"))
        welcome_place_enabled = from_union([from_bool, from_none], obj.get("welcome_place_enabled"))
        msg_edit_window_mins = from_union([from_int, from_none], obj.get("msg_edit_window_mins"))
        allow_message_deletion = from_union([from_bool, from_none], obj.get("allow_message_deletion"))
        display_external_email_addresses = from_union([from_bool, from_none], obj.get("display_external_email_addresses"))
        joiner_notifications_enabled = from_union([from_bool, from_none], obj.get("joiner_notifications_enabled"))
        received_esc_route_to_channel_awareness_message = from_union([from_bool, from_none], obj.get("received_esc_route_to_channel_awareness_message"))
        who_can_create_channels = from_union([from_str, from_none], obj.get("who_can_create_channels"))
        who_can_archive_channels = from_union([from_str, from_none], obj.get("who_can_archive_channels"))
        who_can_create_groups = from_union([from_str, from_none], obj.get("who_can_create_groups"))
        who_can_manage_channel_posting_prefs = from_union([from_str, from_none], obj.get("who_can_manage_channel_posting_prefs"))
        who_can_kick_channels = from_union([from_str, from_none], obj.get("who_can_kick_channels"))
        who_can_kick_groups = from_union([from_str, from_none], obj.get("who_can_kick_groups"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        display_pronouns = from_union([from_bool, from_none], obj.get("display_pronouns"))
        admin_customized_quick_reactions = from_union([lambda x: from_list(from_str, x), from_none], obj.get("admin_customized_quick_reactions"))
        allow_admin_retention_override = from_union([from_int, from_none], obj.get("allow_admin_retention_override"))
        allow_audio_clip_sharing_slack_connect = from_union([from_bool, from_none], obj.get("allow_audio_clip_sharing_slack_connect"))
        allow_audio_clips = from_union([from_bool, from_none], obj.get("allow_audio_clips"))
        allow_box_cfs = from_union([from_bool, from_none], obj.get("allow_box_cfs"))
        allow_calls_interactive_screen_sharing = from_union([from_bool, from_none], obj.get("allow_calls_interactive_screen_sharing"))
        allow_clip_downloads = from_union([from_str, from_none], obj.get("allow_clip_downloads"))
        allow_huddles = from_union([from_bool, from_none], obj.get("allow_huddles"))
        allow_huddles_transcriptions = from_union([from_bool, from_none], obj.get("allow_huddles_transcriptions"))
        allow_media_transcriptions = from_union([from_bool, from_none], obj.get("allow_media_transcriptions"))
        allow_retention_override = from_union([from_bool, from_none], obj.get("allow_retention_override"))
        allow_sponsored_slack_connections = from_union([from_bool, from_none], obj.get("allow_sponsored_slack_connections"))
        allow_video_clip_sharing_slack_connect = from_union([from_bool, from_none], obj.get("allow_video_clip_sharing_slack_connect"))
        allow_video_clips = from_union([from_bool, from_none], obj.get("allow_video_clips"))
        app_dir_only = from_union([from_bool, from_none], obj.get("app_dir_only"))
        app_management_apps = from_union([lambda x: from_list(from_str, x), from_none], obj.get("app_management_apps"))
        block_file_download = from_union([from_bool, from_none], obj.get("block_file_download"))
        box_app_installed = from_union([from_bool, from_none], obj.get("box_app_installed"))
        calls_apps = from_union([CallsApps.from_dict, from_none], obj.get("calls_apps"))
        calls_locations = from_union([lambda x: from_list(from_str, x), from_none], obj.get("calls_locations"))
        can_accept_slack_connect_channel_invites = from_union([from_bool, from_none], obj.get("can_accept_slack_connect_channel_invites"))
        can_create_external_limited_invite = from_union([from_bool, from_none], obj.get("can_create_external_limited_invite"))
        can_create_slack_connect_channel_invite = from_union([from_bool, from_none], obj.get("can_create_slack_connect_channel_invite"))
        channel_email_addresses_enabled = from_union([from_bool, from_none], obj.get("channel_email_addresses_enabled"))
        compliance_export_start = from_union([from_int, from_none], obj.get("compliance_export_start"))
        content_review_enabled = from_union([from_bool, from_none], obj.get("content_review_enabled"))
        created_with_google = from_union([from_bool, from_none], obj.get("created_with_google"))
        custom_status_default_emoji = from_union([from_str, from_none], obj.get("custom_status_default_emoji"))
        custom_status_presets = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], obj.get("custom_status_presets"))
        default_channel_creation_enabled = from_union([from_bool, from_none], obj.get("default_channel_creation_enabled"))
        default_rxns = from_union([lambda x: from_list(from_str, x), from_none], obj.get("default_rxns"))
        disable_email_ingestion = from_union([from_bool, from_none], obj.get("disable_email_ingestion"))
        disable_file_deleting = from_union([from_bool, from_none], obj.get("disable_file_deleting"))
        disable_file_editing = from_union([from_bool, from_none], obj.get("disable_file_editing"))
        disable_file_uploads = from_union([from_str, from_none], obj.get("disable_file_uploads"))
        disable_sidebar_connect_prompts = from_union([lambda x: from_list(from_str, x), from_none], obj.get("disable_sidebar_connect_prompts"))
        disable_sidebar_install_prompts = from_union([lambda x: from_list(from_str, x), from_none], obj.get("disable_sidebar_install_prompts"))
        disallow_public_file_urls = from_union([from_bool, from_none], obj.get("disallow_public_file_urls"))
        discoverable = from_union([from_str, from_none], obj.get("discoverable"))
        display_default_phone = from_union([from_bool, from_none], obj.get("display_default_phone"))
        display_name_pronunciation = from_union([from_bool, from_none], obj.get("display_name_pronunciation"))
        display_real_names = from_union([from_bool, from_none], obj.get("display_real_names"))
        dm_retention_duration = from_union([from_int, from_none], obj.get("dm_retention_duration"))
        dm_retention_type = from_union([from_int, from_none], obj.get("dm_retention_type"))
        dnd_days = from_union([from_str, from_none], obj.get("dnd_days"))
        enable_connect_dm_early_access = from_union([from_bool, from_none], obj.get("enable_connect_dm_early_access"))
        enable_domain_allowlist_for_cea = from_union([from_bool, from_none], obj.get("enable_domain_allowlist_for_cea"))
        enable_info_barriers = from_union([from_bool, from_none], obj.get("enable_info_barriers"))
        enable_mpdm_to_private_channel_conversion = from_union([from_bool, from_none], obj.get("enable_mpdm_to_private_channel_conversion"))
        enterprise_default_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enterprise_default_channels"))
        enterprise_has_corporate_exports = from_union([from_bool, from_none], obj.get("enterprise_has_corporate_exports"))
        enterprise_intune_enabled = from_union([from_bool, from_none], obj.get("enterprise_intune_enabled"))
        enterprise_mandatory_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("enterprise_mandatory_channels"))
        enterprise_mdm_date_enabled = from_union([from_int, from_none], obj.get("enterprise_mdm_date_enabled"))
        enterprise_mdm_disable_file_download = from_union([from_bool, from_none], obj.get("enterprise_mdm_disable_file_download"))
        enterprise_mdm_level = from_union([from_int, from_none], obj.get("enterprise_mdm_level"))
        enterprise_mobile_device_check = from_union([from_bool, from_none], obj.get("enterprise_mobile_device_check"))
        enterprise_team_creation_request = from_union([EnterpriseTeamCreationRequest.from_dict, from_none], obj.get("enterprise_team_creation_request"))
        file_limit_whitelisted = from_union([from_bool, from_none], obj.get("file_limit_whitelisted"))
        file_retention_duration = from_union([from_int, from_none], obj.get("file_retention_duration"))
        file_retention_type = from_union([from_int, from_none], obj.get("file_retention_type"))
        filepicker_app_first_install = from_union([from_bool, from_none], obj.get("filepicker_app_first_install"))
        gg_enabled = from_union([from_bool, from_none], obj.get("gg_enabled"))
        group_retention_duration = from_union([from_int, from_none], obj.get("group_retention_duration"))
        group_retention_type = from_union([from_int, from_none], obj.get("group_retention_type"))
        has_compliance_export = from_union([from_bool, from_none], obj.get("has_compliance_export"))
        has_hipaa_compliance = from_union([from_bool, from_none], obj.get("has_hipaa_compliance"))
        has_seen_partner_promo = from_union([from_bool, from_none], obj.get("has_seen_partner_promo"))
        hermes_has_accepted_tos = from_union([from_bool, from_none], obj.get("hermes_has_accepted_tos"))
        hermes_triggers_trippable_by_slack_connected_teams = from_union([from_bool, from_none], obj.get("hermes_triggers_trippable_by_slack_connected_teams"))
        hide_gsuite_invite_option = from_union([from_bool, from_none], obj.get("hide_gsuite_invite_option"))
        hide_referers = from_union([from_bool, from_none], obj.get("hide_referers"))
        invite_requests_enabled = from_union([from_bool, from_none], obj.get("invite_requests_enabled"))
        invites_only_admins = from_union([from_bool, from_none], obj.get("invites_only_admins"))
        loud_channel_mentions_limit = from_union([from_int, from_none], obj.get("loud_channel_mentions_limit"))
        member_analytics_disabled = from_union([from_bool, from_none], obj.get("member_analytics_disabled"))
        ml_opt_out = from_union([from_bool, from_none], obj.get("ml_opt_out"))
        mobile_passcode_timeout_in_seconds = from_union([from_int, from_none], obj.get("mobile_passcode_timeout_in_seconds"))
        notification_redaction_type = from_union([from_str, from_none], obj.get("notification_redaction_type"))
        notify_pending_enabled = from_union([from_bool, from_none], obj.get("notify_pending_enabled"))
        ntlm_credential_domains = from_union([from_str, from_none], obj.get("ntlm_credential_domains"))
        onedrive_app_installed = from_union([from_bool, from_none], obj.get("onedrive_app_installed"))
        onedrive_enabled_team = from_union([from_bool, from_none], obj.get("onedrive_enabled_team"))
        private_channel_membership_limit = from_union([from_int, from_none], obj.get("private_channel_membership_limit"))
        retention_duration = from_union([from_int, from_none], obj.get("retention_duration"))
        retention_type = from_union([from_int, from_none], obj.get("retention_type"))
        search_feedback_opt_out = from_union([from_bool, from_none], obj.get("search_feedback_opt_out"))
        self_serve_select = from_union([from_bool, from_none], obj.get("self_serve_select"))
        session_duration = from_union([from_int, from_none], obj.get("session_duration"))
        session_duration_type = from_union([from_int, from_none], obj.get("session_duration_type"))
        show_join_leave = from_union([from_bool, from_none], obj.get("show_join_leave"))
        show_legacy_paid_benefits_page = from_union([from_bool, from_none], obj.get("show_legacy_paid_benefits_page"))
        sign_in_with_slack_disabled = from_union([from_bool, from_none], obj.get("sign_in_with_slack_disabled"))
        single_user_exports = from_union([from_bool, from_none], obj.get("single_user_exports"))
        slack_connect_allowed_workspaces = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("slack_connect_allowed_workspaces"))
        slack_connect_approval_type = from_union([from_str, from_none], obj.get("slack_connect_approval_type"))
        slack_connect_dm_only_verified_orgs = from_union([from_bool, from_none], obj.get("slack_connect_dm_only_verified_orgs"))
        slack_connect_file_upload_sharing_enabled = from_union([from_bool, from_none], obj.get("slack_connect_file_upload_sharing_enabled"))
        slackbot_responses_disabled = from_union([from_bool, from_none], obj.get("slackbot_responses_disabled"))
        sso_disable_emails = from_union([from_bool, from_none], obj.get("sso_disable_emails"))
        sso_optional = from_union([from_bool, from_none], obj.get("sso_optional"))
        sso_signup_restrictions = from_union([from_int, from_none], obj.get("sso_signup_restrictions"))
        sso_sync_with_provider = from_union([from_bool, from_none], obj.get("sso_sync_with_provider"))
        subteams_auto_create_admin = from_union([from_bool, from_none], obj.get("subteams_auto_create_admin"))
        subteams_auto_create_owner = from_union([from_bool, from_none], obj.get("subteams_auto_create_owner"))
        use_browser_picker = from_union([from_bool, from_none], obj.get("use_browser_picker"))
        uses_customized_custom_status_presets = from_union([from_bool, from_none], obj.get("uses_customized_custom_status_presets"))
        warn_before_at_channel = from_union([from_str, from_none], obj.get("warn_before_at_channel"))
        who_can_accept_slack_connect_channel_invites = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_accept_slack_connect_channel_invites"))
        who_can_at_channel = from_union([from_str, from_none], obj.get("who_can_at_channel"))
        who_can_at_everyone = from_union([from_str, from_none], obj.get("who_can_at_everyone"))
        who_can_change_team_profile = from_union([from_str, from_none], obj.get("who_can_change_team_profile"))
        who_can_create_delete_user_groups = from_union([from_str, from_none], obj.get("who_can_create_delete_user_groups"))
        who_can_create_external_limited_invite = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_create_external_limited_invite"))
        who_can_create_shared_channels = from_union([from_str, from_none], obj.get("who_can_create_shared_channels"))
        who_can_create_slack_connect_channel_invite = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_create_slack_connect_channel_invite"))
        who_can_dm_anyone = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_dm_anyone"))
        who_can_edit_user_groups = from_union([from_str, from_none], obj.get("who_can_edit_user_groups"))
        who_can_manage_ext_shared_channels = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_manage_ext_shared_channels"))
        who_can_manage_guests = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_manage_guests"))
        who_can_manage_private_channels = from_union([WhoCanManageP.from_dict, from_none], obj.get("who_can_manage_private_channels"))
        who_can_manage_private_channels_at_workspace_level = from_union([WhoCanManageP.from_dict, from_none], obj.get("who_can_manage_private_channels_at_workspace_level"))
        who_can_manage_public_channels = from_union([WhoCanManageP.from_dict, from_none], obj.get("who_can_manage_public_channels"))
        who_can_manage_shared_channels = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_manage_shared_channels"))
        who_can_post_general = from_union([from_str, from_none], obj.get("who_can_post_general"))
        who_can_post_in_shared_channels = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_post_in_shared_channels"))
        who_can_request_ext_shared_channels = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_request_ext_shared_channels"))
        who_can_review_flagged_content = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_review_flagged_content"))
        who_can_view_message_activity = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_view_message_activity"))
        workflow_builder_enabled = from_union([from_bool, from_none], obj.get("workflow_builder_enabled"))
        workflow_extension_steps_beta_opt_in = from_union([from_bool, from_none], obj.get("workflow_extension_steps_beta_opt_in"))
        dnd_enabled = from_union([from_bool, from_none], obj.get("dnd_enabled"))
        dnd_start_hour = from_union([from_str, from_none], obj.get("dnd_start_hour"))
        dnd_end_hour = from_union([from_str, from_none], obj.get("dnd_end_hour"))
        dnd_before_monday = from_union([from_str, from_none], obj.get("dnd_before_monday"))
        dnd_after_monday = from_union([from_str, from_none], obj.get("dnd_after_monday"))
        dnd_before_tuesday = from_union([from_str, from_none], obj.get("dnd_before_tuesday"))
        dnd_after_tuesday = from_union([from_str, from_none], obj.get("dnd_after_tuesday"))
        dnd_before_wednesday = from_union([from_str, from_none], obj.get("dnd_before_wednesday"))
        dnd_after_wednesday = from_union([from_str, from_none], obj.get("dnd_after_wednesday"))
        dnd_before_thursday = from_union([from_str, from_none], obj.get("dnd_before_thursday"))
        dnd_after_thursday = from_union([from_str, from_none], obj.get("dnd_after_thursday"))
        dnd_before_friday = from_union([from_str, from_none], obj.get("dnd_before_friday"))
        dnd_after_friday = from_union([from_str, from_none], obj.get("dnd_after_friday"))
        dnd_before_saturday = from_union([from_str, from_none], obj.get("dnd_before_saturday"))
        dnd_after_saturday = from_union([from_str, from_none], obj.get("dnd_after_saturday"))
        dnd_before_sunday = from_union([from_str, from_none], obj.get("dnd_before_sunday"))
        dnd_after_sunday = from_union([from_str, from_none], obj.get("dnd_after_sunday"))
        dnd_enabled_monday = from_union([from_str, from_none], obj.get("dnd_enabled_monday"))
        dnd_enabled_tuesday = from_union([from_str, from_none], obj.get("dnd_enabled_tuesday"))
        dnd_enabled_wednesday = from_union([from_str, from_none], obj.get("dnd_enabled_wednesday"))
        dnd_enabled_thursday = from_union([from_str, from_none], obj.get("dnd_enabled_thursday"))
        dnd_enabled_friday = from_union([from_str, from_none], obj.get("dnd_enabled_friday"))
        dnd_enabled_saturday = from_union([from_str, from_none], obj.get("dnd_enabled_saturday"))
        dnd_enabled_sunday = from_union([from_str, from_none], obj.get("dnd_enabled_sunday"))
        dnd_weekdays_off_allday = from_union([from_bool, from_none], obj.get("dnd_weekdays_off_allday"))
        auth_mode = from_union([from_str, from_none], obj.get("auth_mode"))
        who_can_create_workflows = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_create_workflows"))
        workflows_webhook_trigger_enabled = from_union([from_bool, from_none], obj.get("workflows_webhook_trigger_enabled"))
        workflow_extension_steps_enabled = from_union([from_bool, from_none], obj.get("workflow_extension_steps_enabled"))
        workflows_export_csv_enabled = from_union([from_bool, from_none], obj.get("workflows_export_csv_enabled"))
        who_can_use_hermes = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_use_hermes"))
        who_can_create_channel_email_addresses = from_union([SlackConnectAllowedWorkspaces.from_dict, from_none], obj.get("who_can_create_channel_email_addresses"))
        identity_links_prefs = from_union([EnterpriseTeamCreationRequest.from_dict, from_none], obj.get("identity_links_prefs"))
        magic_unfurls_enabled = from_union([from_bool, from_none], obj.get("magic_unfurls_enabled"))
        invites_limit = from_union([from_bool, from_none], obj.get("invites_limit"))
        show_mobile_promos = from_union([from_bool, from_none], obj.get("show_mobile_promos"))
        dm_retention_redaction_duration = from_union([from_int, from_none], obj.get("dm_retention_redaction_duration"))
        private_retention_redaction_duration = from_union([from_int, from_none], obj.get("private_retention_redaction_duration"))
        public_retention_redaction_duration = from_union([from_int, from_none], obj.get("public_retention_redaction_duration"))
        return TeamPrefs(default_channels, allow_calls, display_email_addresses, gdrive_enabled_team, all_users_can_purchase, enable_shared_channels, can_receive_shared_channels_invites, invited_user_preset, dropbox_legacy_picker, app_whitelist_enabled, who_can_manage_integrations, welcome_place_enabled, msg_edit_window_mins, allow_message_deletion, display_external_email_addresses, joiner_notifications_enabled, received_esc_route_to_channel_awareness_message, who_can_create_channels, who_can_archive_channels, who_can_create_groups, who_can_manage_channel_posting_prefs, who_can_kick_channels, who_can_kick_groups, locale, display_pronouns, admin_customized_quick_reactions, allow_admin_retention_override, allow_audio_clip_sharing_slack_connect, allow_audio_clips, allow_box_cfs, allow_calls_interactive_screen_sharing, allow_clip_downloads, allow_huddles, allow_huddles_transcriptions, allow_media_transcriptions, allow_retention_override, allow_sponsored_slack_connections, allow_video_clip_sharing_slack_connect, allow_video_clips, app_dir_only, app_management_apps, block_file_download, box_app_installed, calls_apps, calls_locations, can_accept_slack_connect_channel_invites, can_create_external_limited_invite, can_create_slack_connect_channel_invite, channel_email_addresses_enabled, compliance_export_start, content_review_enabled, created_with_google, custom_status_default_emoji, custom_status_presets, default_channel_creation_enabled, default_rxns, disable_email_ingestion, disable_file_deleting, disable_file_editing, disable_file_uploads, disable_sidebar_connect_prompts, disable_sidebar_install_prompts, disallow_public_file_urls, discoverable, display_default_phone, display_name_pronunciation, display_real_names, dm_retention_duration, dm_retention_type, dnd_days, enable_connect_dm_early_access, enable_domain_allowlist_for_cea, enable_info_barriers, enable_mpdm_to_private_channel_conversion, enterprise_default_channels, enterprise_has_corporate_exports, enterprise_intune_enabled, enterprise_mandatory_channels, enterprise_mdm_date_enabled, enterprise_mdm_disable_file_download, enterprise_mdm_level, enterprise_mobile_device_check, enterprise_team_creation_request, file_limit_whitelisted, file_retention_duration, file_retention_type, filepicker_app_first_install, gg_enabled, group_retention_duration, group_retention_type, has_compliance_export, has_hipaa_compliance, has_seen_partner_promo, hermes_has_accepted_tos, hermes_triggers_trippable_by_slack_connected_teams, hide_gsuite_invite_option, hide_referers, invite_requests_enabled, invites_only_admins, loud_channel_mentions_limit, member_analytics_disabled, ml_opt_out, mobile_passcode_timeout_in_seconds, notification_redaction_type, notify_pending_enabled, ntlm_credential_domains, onedrive_app_installed, onedrive_enabled_team, private_channel_membership_limit, retention_duration, retention_type, search_feedback_opt_out, self_serve_select, session_duration, session_duration_type, show_join_leave, show_legacy_paid_benefits_page, sign_in_with_slack_disabled, single_user_exports, slack_connect_allowed_workspaces, slack_connect_approval_type, slack_connect_dm_only_verified_orgs, slack_connect_file_upload_sharing_enabled, slackbot_responses_disabled, sso_disable_emails, sso_optional, sso_signup_restrictions, sso_sync_with_provider, subteams_auto_create_admin, subteams_auto_create_owner, use_browser_picker, uses_customized_custom_status_presets, warn_before_at_channel, who_can_accept_slack_connect_channel_invites, who_can_at_channel, who_can_at_everyone, who_can_change_team_profile, who_can_create_delete_user_groups, who_can_create_external_limited_invite, who_can_create_shared_channels, who_can_create_slack_connect_channel_invite, who_can_dm_anyone, who_can_edit_user_groups, who_can_manage_ext_shared_channels, who_can_manage_guests, who_can_manage_private_channels, who_can_manage_private_channels_at_workspace_level, who_can_manage_public_channels, who_can_manage_shared_channels, who_can_post_general, who_can_post_in_shared_channels, who_can_request_ext_shared_channels, who_can_review_flagged_content, who_can_view_message_activity, workflow_builder_enabled, workflow_extension_steps_beta_opt_in, dnd_enabled, dnd_start_hour, dnd_end_hour, dnd_before_monday, dnd_after_monday, dnd_before_tuesday, dnd_after_tuesday, dnd_before_wednesday, dnd_after_wednesday, dnd_before_thursday, dnd_after_thursday, dnd_before_friday, dnd_after_friday, dnd_before_saturday, dnd_after_saturday, dnd_before_sunday, dnd_after_sunday, dnd_enabled_monday, dnd_enabled_tuesday, dnd_enabled_wednesday, dnd_enabled_thursday, dnd_enabled_friday, dnd_enabled_saturday, dnd_enabled_sunday, dnd_weekdays_off_allday, auth_mode, who_can_create_workflows, workflows_webhook_trigger_enabled, workflow_extension_steps_enabled, workflows_export_csv_enabled, who_can_use_hermes, who_can_create_channel_email_addresses, identity_links_prefs, magic_unfurls_enabled, invites_limit, show_mobile_promos, dm_retention_redaction_duration, private_retention_redaction_duration, public_retention_redaction_duration)

    def to_dict(self) -> dict:
        result: dict = {}
        result["default_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.default_channels)
        result["allow_calls"] = from_union([from_bool, from_none], self.allow_calls)
        result["display_email_addresses"] = from_union([from_bool, from_none], self.display_email_addresses)
        result["gdrive_enabled_team"] = from_union([from_bool, from_none], self.gdrive_enabled_team)
        result["all_users_can_purchase"] = from_union([from_bool, from_none], self.all_users_can_purchase)
        result["enable_shared_channels"] = from_union([from_int, from_none], self.enable_shared_channels)
        result["can_receive_shared_channels_invites"] = from_union([from_bool, from_none], self.can_receive_shared_channels_invites)
        result["invited_user_preset"] = from_union([lambda x: to_class(InvitedUserPreset, x), from_none], self.invited_user_preset)
        result["dropbox_legacy_picker"] = from_union([from_bool, from_none], self.dropbox_legacy_picker)
        result["app_whitelist_enabled"] = from_union([from_bool, from_none], self.app_whitelist_enabled)
        result["who_can_manage_integrations"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_manage_integrations)
        result["welcome_place_enabled"] = from_union([from_bool, from_none], self.welcome_place_enabled)
        result["msg_edit_window_mins"] = from_union([from_int, from_none], self.msg_edit_window_mins)
        result["allow_message_deletion"] = from_union([from_bool, from_none], self.allow_message_deletion)
        result["display_external_email_addresses"] = from_union([from_bool, from_none], self.display_external_email_addresses)
        result["joiner_notifications_enabled"] = from_union([from_bool, from_none], self.joiner_notifications_enabled)
        result["received_esc_route_to_channel_awareness_message"] = from_union([from_bool, from_none], self.received_esc_route_to_channel_awareness_message)
        result["who_can_create_channels"] = from_union([from_str, from_none], self.who_can_create_channels)
        result["who_can_archive_channels"] = from_union([from_str, from_none], self.who_can_archive_channels)
        result["who_can_create_groups"] = from_union([from_str, from_none], self.who_can_create_groups)
        result["who_can_manage_channel_posting_prefs"] = from_union([from_str, from_none], self.who_can_manage_channel_posting_prefs)
        result["who_can_kick_channels"] = from_union([from_str, from_none], self.who_can_kick_channels)
        result["who_can_kick_groups"] = from_union([from_str, from_none], self.who_can_kick_groups)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["display_pronouns"] = from_union([from_bool, from_none], self.display_pronouns)
        result["admin_customized_quick_reactions"] = from_union([lambda x: from_list(from_str, x), from_none], self.admin_customized_quick_reactions)
        result["allow_admin_retention_override"] = from_union([from_int, from_none], self.allow_admin_retention_override)
        result["allow_audio_clip_sharing_slack_connect"] = from_union([from_bool, from_none], self.allow_audio_clip_sharing_slack_connect)
        result["allow_audio_clips"] = from_union([from_bool, from_none], self.allow_audio_clips)
        result["allow_box_cfs"] = from_union([from_bool, from_none], self.allow_box_cfs)
        result["allow_calls_interactive_screen_sharing"] = from_union([from_bool, from_none], self.allow_calls_interactive_screen_sharing)
        result["allow_clip_downloads"] = from_union([from_str, from_none], self.allow_clip_downloads)
        result["allow_huddles"] = from_union([from_bool, from_none], self.allow_huddles)
        result["allow_huddles_transcriptions"] = from_union([from_bool, from_none], self.allow_huddles_transcriptions)
        result["allow_media_transcriptions"] = from_union([from_bool, from_none], self.allow_media_transcriptions)
        result["allow_retention_override"] = from_union([from_bool, from_none], self.allow_retention_override)
        result["allow_sponsored_slack_connections"] = from_union([from_bool, from_none], self.allow_sponsored_slack_connections)
        result["allow_video_clip_sharing_slack_connect"] = from_union([from_bool, from_none], self.allow_video_clip_sharing_slack_connect)
        result["allow_video_clips"] = from_union([from_bool, from_none], self.allow_video_clips)
        result["app_dir_only"] = from_union([from_bool, from_none], self.app_dir_only)
        result["app_management_apps"] = from_union([lambda x: from_list(from_str, x), from_none], self.app_management_apps)
        result["block_file_download"] = from_union([from_bool, from_none], self.block_file_download)
        result["box_app_installed"] = from_union([from_bool, from_none], self.box_app_installed)
        result["calls_apps"] = from_union([lambda x: to_class(CallsApps, x), from_none], self.calls_apps)
        result["calls_locations"] = from_union([lambda x: from_list(from_str, x), from_none], self.calls_locations)
        result["can_accept_slack_connect_channel_invites"] = from_union([from_bool, from_none], self.can_accept_slack_connect_channel_invites)
        result["can_create_external_limited_invite"] = from_union([from_bool, from_none], self.can_create_external_limited_invite)
        result["can_create_slack_connect_channel_invite"] = from_union([from_bool, from_none], self.can_create_slack_connect_channel_invite)
        result["channel_email_addresses_enabled"] = from_union([from_bool, from_none], self.channel_email_addresses_enabled)
        result["compliance_export_start"] = from_union([from_int, from_none], self.compliance_export_start)
        result["content_review_enabled"] = from_union([from_bool, from_none], self.content_review_enabled)
        result["created_with_google"] = from_union([from_bool, from_none], self.created_with_google)
        result["custom_status_default_emoji"] = from_union([from_str, from_none], self.custom_status_default_emoji)
        result["custom_status_presets"] = from_union([lambda x: from_list(lambda x: from_list(from_str, x), x), from_none], self.custom_status_presets)
        result["default_channel_creation_enabled"] = from_union([from_bool, from_none], self.default_channel_creation_enabled)
        result["default_rxns"] = from_union([lambda x: from_list(from_str, x), from_none], self.default_rxns)
        result["disable_email_ingestion"] = from_union([from_bool, from_none], self.disable_email_ingestion)
        result["disable_file_deleting"] = from_union([from_bool, from_none], self.disable_file_deleting)
        result["disable_file_editing"] = from_union([from_bool, from_none], self.disable_file_editing)
        result["disable_file_uploads"] = from_union([from_str, from_none], self.disable_file_uploads)
        result["disable_sidebar_connect_prompts"] = from_union([lambda x: from_list(from_str, x), from_none], self.disable_sidebar_connect_prompts)
        result["disable_sidebar_install_prompts"] = from_union([lambda x: from_list(from_str, x), from_none], self.disable_sidebar_install_prompts)
        result["disallow_public_file_urls"] = from_union([from_bool, from_none], self.disallow_public_file_urls)
        result["discoverable"] = from_union([from_str, from_none], self.discoverable)
        result["display_default_phone"] = from_union([from_bool, from_none], self.display_default_phone)
        result["display_name_pronunciation"] = from_union([from_bool, from_none], self.display_name_pronunciation)
        result["display_real_names"] = from_union([from_bool, from_none], self.display_real_names)
        result["dm_retention_duration"] = from_union([from_int, from_none], self.dm_retention_duration)
        result["dm_retention_type"] = from_union([from_int, from_none], self.dm_retention_type)
        result["dnd_days"] = from_union([from_str, from_none], self.dnd_days)
        result["enable_connect_dm_early_access"] = from_union([from_bool, from_none], self.enable_connect_dm_early_access)
        result["enable_domain_allowlist_for_cea"] = from_union([from_bool, from_none], self.enable_domain_allowlist_for_cea)
        result["enable_info_barriers"] = from_union([from_bool, from_none], self.enable_info_barriers)
        result["enable_mpdm_to_private_channel_conversion"] = from_union([from_bool, from_none], self.enable_mpdm_to_private_channel_conversion)
        result["enterprise_default_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.enterprise_default_channels)
        result["enterprise_has_corporate_exports"] = from_union([from_bool, from_none], self.enterprise_has_corporate_exports)
        result["enterprise_intune_enabled"] = from_union([from_bool, from_none], self.enterprise_intune_enabled)
        result["enterprise_mandatory_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.enterprise_mandatory_channels)
        result["enterprise_mdm_date_enabled"] = from_union([from_int, from_none], self.enterprise_mdm_date_enabled)
        result["enterprise_mdm_disable_file_download"] = from_union([from_bool, from_none], self.enterprise_mdm_disable_file_download)
        result["enterprise_mdm_level"] = from_union([from_int, from_none], self.enterprise_mdm_level)
        result["enterprise_mobile_device_check"] = from_union([from_bool, from_none], self.enterprise_mobile_device_check)
        result["enterprise_team_creation_request"] = from_union([lambda x: to_class(EnterpriseTeamCreationRequest, x), from_none], self.enterprise_team_creation_request)
        result["file_limit_whitelisted"] = from_union([from_bool, from_none], self.file_limit_whitelisted)
        result["file_retention_duration"] = from_union([from_int, from_none], self.file_retention_duration)
        result["file_retention_type"] = from_union([from_int, from_none], self.file_retention_type)
        result["filepicker_app_first_install"] = from_union([from_bool, from_none], self.filepicker_app_first_install)
        result["gg_enabled"] = from_union([from_bool, from_none], self.gg_enabled)
        result["group_retention_duration"] = from_union([from_int, from_none], self.group_retention_duration)
        result["group_retention_type"] = from_union([from_int, from_none], self.group_retention_type)
        result["has_compliance_export"] = from_union([from_bool, from_none], self.has_compliance_export)
        result["has_hipaa_compliance"] = from_union([from_bool, from_none], self.has_hipaa_compliance)
        result["has_seen_partner_promo"] = from_union([from_bool, from_none], self.has_seen_partner_promo)
        result["hermes_has_accepted_tos"] = from_union([from_bool, from_none], self.hermes_has_accepted_tos)
        result["hermes_triggers_trippable_by_slack_connected_teams"] = from_union([from_bool, from_none], self.hermes_triggers_trippable_by_slack_connected_teams)
        result["hide_gsuite_invite_option"] = from_union([from_bool, from_none], self.hide_gsuite_invite_option)
        result["hide_referers"] = from_union([from_bool, from_none], self.hide_referers)
        result["invite_requests_enabled"] = from_union([from_bool, from_none], self.invite_requests_enabled)
        result["invites_only_admins"] = from_union([from_bool, from_none], self.invites_only_admins)
        result["loud_channel_mentions_limit"] = from_union([from_int, from_none], self.loud_channel_mentions_limit)
        result["member_analytics_disabled"] = from_union([from_bool, from_none], self.member_analytics_disabled)
        result["ml_opt_out"] = from_union([from_bool, from_none], self.ml_opt_out)
        result["mobile_passcode_timeout_in_seconds"] = from_union([from_int, from_none], self.mobile_passcode_timeout_in_seconds)
        result["notification_redaction_type"] = from_union([from_str, from_none], self.notification_redaction_type)
        result["notify_pending_enabled"] = from_union([from_bool, from_none], self.notify_pending_enabled)
        result["ntlm_credential_domains"] = from_union([from_str, from_none], self.ntlm_credential_domains)
        result["onedrive_app_installed"] = from_union([from_bool, from_none], self.onedrive_app_installed)
        result["onedrive_enabled_team"] = from_union([from_bool, from_none], self.onedrive_enabled_team)
        result["private_channel_membership_limit"] = from_union([from_int, from_none], self.private_channel_membership_limit)
        result["retention_duration"] = from_union([from_int, from_none], self.retention_duration)
        result["retention_type"] = from_union([from_int, from_none], self.retention_type)
        result["search_feedback_opt_out"] = from_union([from_bool, from_none], self.search_feedback_opt_out)
        result["self_serve_select"] = from_union([from_bool, from_none], self.self_serve_select)
        result["session_duration"] = from_union([from_int, from_none], self.session_duration)
        result["session_duration_type"] = from_union([from_int, from_none], self.session_duration_type)
        result["show_join_leave"] = from_union([from_bool, from_none], self.show_join_leave)
        result["show_legacy_paid_benefits_page"] = from_union([from_bool, from_none], self.show_legacy_paid_benefits_page)
        result["sign_in_with_slack_disabled"] = from_union([from_bool, from_none], self.sign_in_with_slack_disabled)
        result["single_user_exports"] = from_union([from_bool, from_none], self.single_user_exports)
        result["slack_connect_allowed_workspaces"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.slack_connect_allowed_workspaces)
        result["slack_connect_approval_type"] = from_union([from_str, from_none], self.slack_connect_approval_type)
        result["slack_connect_dm_only_verified_orgs"] = from_union([from_bool, from_none], self.slack_connect_dm_only_verified_orgs)
        result["slack_connect_file_upload_sharing_enabled"] = from_union([from_bool, from_none], self.slack_connect_file_upload_sharing_enabled)
        result["slackbot_responses_disabled"] = from_union([from_bool, from_none], self.slackbot_responses_disabled)
        result["sso_disable_emails"] = from_union([from_bool, from_none], self.sso_disable_emails)
        result["sso_optional"] = from_union([from_bool, from_none], self.sso_optional)
        result["sso_signup_restrictions"] = from_union([from_int, from_none], self.sso_signup_restrictions)
        result["sso_sync_with_provider"] = from_union([from_bool, from_none], self.sso_sync_with_provider)
        result["subteams_auto_create_admin"] = from_union([from_bool, from_none], self.subteams_auto_create_admin)
        result["subteams_auto_create_owner"] = from_union([from_bool, from_none], self.subteams_auto_create_owner)
        result["use_browser_picker"] = from_union([from_bool, from_none], self.use_browser_picker)
        result["uses_customized_custom_status_presets"] = from_union([from_bool, from_none], self.uses_customized_custom_status_presets)
        result["warn_before_at_channel"] = from_union([from_str, from_none], self.warn_before_at_channel)
        result["who_can_accept_slack_connect_channel_invites"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_accept_slack_connect_channel_invites)
        result["who_can_at_channel"] = from_union([from_str, from_none], self.who_can_at_channel)
        result["who_can_at_everyone"] = from_union([from_str, from_none], self.who_can_at_everyone)
        result["who_can_change_team_profile"] = from_union([from_str, from_none], self.who_can_change_team_profile)
        result["who_can_create_delete_user_groups"] = from_union([from_str, from_none], self.who_can_create_delete_user_groups)
        result["who_can_create_external_limited_invite"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_create_external_limited_invite)
        result["who_can_create_shared_channels"] = from_union([from_str, from_none], self.who_can_create_shared_channels)
        result["who_can_create_slack_connect_channel_invite"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_create_slack_connect_channel_invite)
        result["who_can_dm_anyone"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_dm_anyone)
        result["who_can_edit_user_groups"] = from_union([from_str, from_none], self.who_can_edit_user_groups)
        result["who_can_manage_ext_shared_channels"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_manage_ext_shared_channels)
        result["who_can_manage_guests"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_manage_guests)
        result["who_can_manage_private_channels"] = from_union([lambda x: to_class(WhoCanManageP, x), from_none], self.who_can_manage_private_channels)
        result["who_can_manage_private_channels_at_workspace_level"] = from_union([lambda x: to_class(WhoCanManageP, x), from_none], self.who_can_manage_private_channels_at_workspace_level)
        result["who_can_manage_public_channels"] = from_union([lambda x: to_class(WhoCanManageP, x), from_none], self.who_can_manage_public_channels)
        result["who_can_manage_shared_channels"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_manage_shared_channels)
        result["who_can_post_general"] = from_union([from_str, from_none], self.who_can_post_general)
        result["who_can_post_in_shared_channels"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_post_in_shared_channels)
        result["who_can_request_ext_shared_channels"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_request_ext_shared_channels)
        result["who_can_review_flagged_content"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_review_flagged_content)
        result["who_can_view_message_activity"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_view_message_activity)
        result["workflow_builder_enabled"] = from_union([from_bool, from_none], self.workflow_builder_enabled)
        result["workflow_extension_steps_beta_opt_in"] = from_union([from_bool, from_none], self.workflow_extension_steps_beta_opt_in)
        result["dnd_enabled"] = from_union([from_bool, from_none], self.dnd_enabled)
        result["dnd_start_hour"] = from_union([from_str, from_none], self.dnd_start_hour)
        result["dnd_end_hour"] = from_union([from_str, from_none], self.dnd_end_hour)
        result["dnd_before_monday"] = from_union([from_str, from_none], self.dnd_before_monday)
        result["dnd_after_monday"] = from_union([from_str, from_none], self.dnd_after_monday)
        result["dnd_before_tuesday"] = from_union([from_str, from_none], self.dnd_before_tuesday)
        result["dnd_after_tuesday"] = from_union([from_str, from_none], self.dnd_after_tuesday)
        result["dnd_before_wednesday"] = from_union([from_str, from_none], self.dnd_before_wednesday)
        result["dnd_after_wednesday"] = from_union([from_str, from_none], self.dnd_after_wednesday)
        result["dnd_before_thursday"] = from_union([from_str, from_none], self.dnd_before_thursday)
        result["dnd_after_thursday"] = from_union([from_str, from_none], self.dnd_after_thursday)
        result["dnd_before_friday"] = from_union([from_str, from_none], self.dnd_before_friday)
        result["dnd_after_friday"] = from_union([from_str, from_none], self.dnd_after_friday)
        result["dnd_before_saturday"] = from_union([from_str, from_none], self.dnd_before_saturday)
        result["dnd_after_saturday"] = from_union([from_str, from_none], self.dnd_after_saturday)
        result["dnd_before_sunday"] = from_union([from_str, from_none], self.dnd_before_sunday)
        result["dnd_after_sunday"] = from_union([from_str, from_none], self.dnd_after_sunday)
        result["dnd_enabled_monday"] = from_union([from_str, from_none], self.dnd_enabled_monday)
        result["dnd_enabled_tuesday"] = from_union([from_str, from_none], self.dnd_enabled_tuesday)
        result["dnd_enabled_wednesday"] = from_union([from_str, from_none], self.dnd_enabled_wednesday)
        result["dnd_enabled_thursday"] = from_union([from_str, from_none], self.dnd_enabled_thursday)
        result["dnd_enabled_friday"] = from_union([from_str, from_none], self.dnd_enabled_friday)
        result["dnd_enabled_saturday"] = from_union([from_str, from_none], self.dnd_enabled_saturday)
        result["dnd_enabled_sunday"] = from_union([from_str, from_none], self.dnd_enabled_sunday)
        result["dnd_weekdays_off_allday"] = from_union([from_bool, from_none], self.dnd_weekdays_off_allday)
        result["auth_mode"] = from_union([from_str, from_none], self.auth_mode)
        result["who_can_create_workflows"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_create_workflows)
        result["workflows_webhook_trigger_enabled"] = from_union([from_bool, from_none], self.workflows_webhook_trigger_enabled)
        result["workflow_extension_steps_enabled"] = from_union([from_bool, from_none], self.workflow_extension_steps_enabled)
        result["workflows_export_csv_enabled"] = from_union([from_bool, from_none], self.workflows_export_csv_enabled)
        result["who_can_use_hermes"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_use_hermes)
        result["who_can_create_channel_email_addresses"] = from_union([lambda x: to_class(SlackConnectAllowedWorkspaces, x), from_none], self.who_can_create_channel_email_addresses)
        result["identity_links_prefs"] = from_union([lambda x: to_class(EnterpriseTeamCreationRequest, x), from_none], self.identity_links_prefs)
        result["magic_unfurls_enabled"] = from_union([from_bool, from_none], self.magic_unfurls_enabled)
        result["invites_limit"] = from_union([from_bool, from_none], self.invites_limit)
        result["show_mobile_promos"] = from_union([from_bool, from_none], self.show_mobile_promos)
        result["dm_retention_redaction_duration"] = from_union([from_int, from_none], self.dm_retention_redaction_duration)
        result["private_retention_redaction_duration"] = from_union([from_int, from_none], self.private_retention_redaction_duration)
        result["public_retention_redaction_duration"] = from_union([from_int, from_none], self.public_retention_redaction_duration)
        return result


@dataclass
class Team:
    id: Optional[str] = None
    name: Optional[str] = None
    url: Optional[str] = None
    email_domain: Optional[str] = None
    domain: Optional[str] = None
    msg_edit_window_mins: Optional[int] = None
    prefs: Optional[TeamPrefs] = None
    icon: Optional[Icon] = None
    over_storage_limit: Optional[bool] = None
    messages_count: Optional[int] = None
    plan: Optional[str] = None
    onboarding_channel_id: Optional[str] = None
    date_create: Optional[int] = None
    limit_ts: Optional[int] = None
    is_verified: Optional[bool] = None
    avatar_base_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Team':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        url = from_union([from_str, from_none], obj.get("url"))
        email_domain = from_union([from_str, from_none], obj.get("email_domain"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        msg_edit_window_mins = from_union([from_int, from_none], obj.get("msg_edit_window_mins"))
        prefs = from_union([TeamPrefs.from_dict, from_none], obj.get("prefs"))
        icon = from_union([Icon.from_dict, from_none], obj.get("icon"))
        over_storage_limit = from_union([from_bool, from_none], obj.get("over_storage_limit"))
        messages_count = from_union([from_int, from_none], obj.get("messages_count"))
        plan = from_union([from_str, from_none], obj.get("plan"))
        onboarding_channel_id = from_union([from_str, from_none], obj.get("onboarding_channel_id"))
        date_create = from_union([from_int, from_none], obj.get("date_create"))
        limit_ts = from_union([from_int, from_none], obj.get("limit_ts"))
        is_verified = from_union([from_bool, from_none], obj.get("is_verified"))
        avatar_base_url = from_union([from_str, from_none], obj.get("avatar_base_url"))
        return Team(id, name, url, email_domain, domain, msg_edit_window_mins, prefs, icon, over_storage_limit, messages_count, plan, onboarding_channel_id, date_create, limit_ts, is_verified, avatar_base_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["url"] = from_union([from_str, from_none], self.url)
        result["email_domain"] = from_union([from_str, from_none], self.email_domain)
        result["domain"] = from_union([from_str, from_none], self.domain)
        result["msg_edit_window_mins"] = from_union([from_int, from_none], self.msg_edit_window_mins)
        result["prefs"] = from_union([lambda x: to_class(TeamPrefs, x), from_none], self.prefs)
        result["icon"] = from_union([lambda x: to_class(Icon, x), from_none], self.icon)
        result["over_storage_limit"] = from_union([from_bool, from_none], self.over_storage_limit)
        result["messages_count"] = from_union([from_int, from_none], self.messages_count)
        result["plan"] = from_union([from_str, from_none], self.plan)
        result["onboarding_channel_id"] = from_union([from_str, from_none], self.onboarding_channel_id)
        result["date_create"] = from_union([from_int, from_none], self.date_create)
        result["limit_ts"] = from_union([from_int, from_none], self.limit_ts)
        result["is_verified"] = from_union([from_bool, from_none], self.is_verified)
        result["avatar_base_url"] = from_union([from_str, from_none], self.avatar_base_url)
        return result


@dataclass
class Xf019LT13Z16:
    value: Optional[str] = None
    alt: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Xf019LT13Z16':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        alt = from_union([from_str, from_none], obj.get("alt"))
        return Xf019LT13Z16(value, alt)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["alt"] = from_union([from_str, from_none], self.alt)
        return result


@dataclass
class Fields:
    xf019_lt13_z16: Optional[Xf019LT13Z16] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Fields':
        assert isinstance(obj, dict)
        xf019_lt13_z16 = from_union([Xf019LT13Z16.from_dict, from_none], obj.get("Xf019LT13Z16"))
        return Fields(xf019_lt13_z16)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Xf019LT13Z16"] = from_union([lambda x: to_class(Xf019LT13Z16, x), from_none], self.xf019_lt13_z16)
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
    phone: Optional[int] = None
    title: Optional[str] = None
    skype: Optional[str] = None
    real_name: Optional[str] = None
    real_name_normalized: Optional[str] = None
    display_name: Optional[str] = None
    display_name_normalized: Optional[str] = None
    fields: Optional[Fields] = None
    status_text: Optional[str] = None
    status_emoji: Optional[str] = None
    status_emoji_display_info: Optional[List[StatusEmojiDisplayInfo]] = None
    status_expiration: Optional[int] = None
    avatar_hash: Optional[str] = None
    image_original: Optional[str] = None
    is_custom_image: Optional[bool] = None
    email: Optional[str] = None
    pronouns: Optional[str] = None
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
    team: Optional[str] = None
    api_app_id: Optional[str] = None
    bot_id: Optional[str] = None
    always_active: Optional[bool] = None
    guest_invited_by: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Profile':
        assert isinstance(obj, dict)
        phone = from_union([from_none, lambda x: int(from_str(x))], obj.get("phone"))
        title = from_union([from_str, from_none], obj.get("title"))
        skype = from_union([from_str, from_none], obj.get("skype"))
        real_name = from_union([from_str, from_none], obj.get("real_name"))
        real_name_normalized = from_union([from_str, from_none], obj.get("real_name_normalized"))
        display_name = from_union([from_str, from_none], obj.get("display_name"))
        display_name_normalized = from_union([from_str, from_none], obj.get("display_name_normalized"))
        fields = from_union([Fields.from_dict, from_none], obj.get("fields"))
        status_text = from_union([from_str, from_none], obj.get("status_text"))
        status_emoji = from_union([from_str, from_none], obj.get("status_emoji"))
        status_emoji_display_info = from_union([lambda x: from_list(StatusEmojiDisplayInfo.from_dict, x), from_none], obj.get("status_emoji_display_info"))
        status_expiration = from_union([from_int, from_none], obj.get("status_expiration"))
        avatar_hash = from_union([from_str, from_none], obj.get("avatar_hash"))
        image_original = from_union([from_str, from_none], obj.get("image_original"))
        is_custom_image = from_union([from_bool, from_none], obj.get("is_custom_image"))
        email = from_union([from_str, from_none], obj.get("email"))
        pronouns = from_union([from_str, from_none], obj.get("pronouns"))
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
        team = from_union([from_str, from_none], obj.get("team"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        always_active = from_union([from_bool, from_none], obj.get("always_active"))
        guest_invited_by = from_union([from_str, from_none], obj.get("guest_invited_by"))
        return Profile(phone, title, skype, real_name, real_name_normalized, display_name, display_name_normalized, fields, status_text, status_emoji, status_emoji_display_info, status_expiration, avatar_hash, image_original, is_custom_image, email, pronouns, first_name, last_name, image_24, image_32, image_48, image_72, image_192, image_512, image_1024, status_text_canonical, team, api_app_id, bot_id, always_active, guest_invited_by)

    def to_dict(self) -> dict:
        result: dict = {}
        result["phone"] = from_union([lambda x: from_none((lambda x: is_type(type(None), x))(x)), lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.phone)
        result["title"] = from_union([from_str, from_none], self.title)
        result["skype"] = from_union([from_str, from_none], self.skype)
        result["real_name"] = from_union([from_str, from_none], self.real_name)
        result["real_name_normalized"] = from_union([from_str, from_none], self.real_name_normalized)
        result["display_name"] = from_union([from_str, from_none], self.display_name)
        result["display_name_normalized"] = from_union([from_str, from_none], self.display_name_normalized)
        result["fields"] = from_union([lambda x: to_class(Fields, x), from_none], self.fields)
        result["status_text"] = from_union([from_str, from_none], self.status_text)
        result["status_emoji"] = from_union([from_str, from_none], self.status_emoji)
        result["status_emoji_display_info"] = from_union([lambda x: from_list(lambda x: to_class(StatusEmojiDisplayInfo, x), x), from_none], self.status_emoji_display_info)
        result["status_expiration"] = from_union([from_int, from_none], self.status_expiration)
        result["avatar_hash"] = from_union([from_str, from_none], self.avatar_hash)
        result["image_original"] = from_union([from_str, from_none], self.image_original)
        result["is_custom_image"] = from_union([from_bool, from_none], self.is_custom_image)
        result["email"] = from_union([from_str, from_none], self.email)
        result["pronouns"] = from_union([from_str, from_none], self.pronouns)
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
        result["team"] = from_union([from_str, from_none], self.team)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["always_active"] = from_union([from_bool, from_none], self.always_active)
        result["guest_invited_by"] = from_union([from_str, from_none], self.guest_invited_by)
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
    is_restricted: Optional[bool] = None
    is_ultra_restricted: Optional[bool] = None
    is_bot: Optional[bool] = None
    is_app_user: Optional[bool] = None
    updated: Optional[int] = None
    is_email_confirmed: Optional[bool] = None
    who_can_share_contact_card: Optional[str] = None
    presence: Optional[str] = None
    is_workflow_bot: Optional[bool] = None

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
        is_restricted = from_union([from_bool, from_none], obj.get("is_restricted"))
        is_ultra_restricted = from_union([from_bool, from_none], obj.get("is_ultra_restricted"))
        is_bot = from_union([from_bool, from_none], obj.get("is_bot"))
        is_app_user = from_union([from_bool, from_none], obj.get("is_app_user"))
        updated = from_union([from_int, from_none], obj.get("updated"))
        is_email_confirmed = from_union([from_bool, from_none], obj.get("is_email_confirmed"))
        who_can_share_contact_card = from_union([from_str, from_none], obj.get("who_can_share_contact_card"))
        presence = from_union([from_str, from_none], obj.get("presence"))
        is_workflow_bot = from_union([from_bool, from_none], obj.get("is_workflow_bot"))
        return User(id, team_id, name, deleted, color, real_name, tz, tz_label, tz_offset, profile, is_admin, is_owner, is_primary_owner, is_restricted, is_ultra_restricted, is_bot, is_app_user, updated, is_email_confirmed, who_can_share_contact_card, presence, is_workflow_bot)

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
        result["is_restricted"] = from_union([from_bool, from_none], self.is_restricted)
        result["is_ultra_restricted"] = from_union([from_bool, from_none], self.is_ultra_restricted)
        result["is_bot"] = from_union([from_bool, from_none], self.is_bot)
        result["is_app_user"] = from_union([from_bool, from_none], self.is_app_user)
        result["updated"] = from_union([from_int, from_none], self.updated)
        result["is_email_confirmed"] = from_union([from_bool, from_none], self.is_email_confirmed)
        result["who_can_share_contact_card"] = from_union([from_str, from_none], self.who_can_share_contact_card)
        result["presence"] = from_union([from_str, from_none], self.presence)
        result["is_workflow_bot"] = from_union([from_bool, from_none], self.is_workflow_bot)
        return result


@dataclass
class RtmStartResponse:
    ok: Optional[bool] = None
    rtm_start_response_self: Optional[Self] = None
    team: Optional[Team] = None
    accept_tos_url: Optional[str] = None
    latest_event_ts: Optional[str] = None
    channels: Optional[List[Channel]] = None
    groups: Optional[List[Group]] = None
    ims: Optional[List[IM]] = None
    cache_ts: Optional[int] = None
    mobile_app_requires_upgrade: Optional[bool] = None
    read_only_channels: Optional[List[str]] = None
    non_threadable_channels: Optional[List[str]] = None
    thread_only_channels: Optional[List[str]] = None
    can_manage_shared_channels: Optional[bool] = None
    subteams: Optional[Subteams] = None
    dnd: Optional[DND] = None
    users: Optional[List[User]] = None
    cache_version: Optional[str] = None
    cache_ts_version: Optional[str] = None
    bots: Optional[List[Bot]] = None
    url: Optional[str] = None
    is_europe: Optional[bool] = None
    links: Optional[Links] = None
    response_metadata: Optional[ResponseMetadata] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RtmStartResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        rtm_start_response_self = from_union([Self.from_dict, from_none], obj.get("self"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        accept_tos_url = from_union([from_str, from_none], obj.get("accept_tos_url"))
        latest_event_ts = from_union([from_str, from_none], obj.get("latest_event_ts"))
        channels = from_union([lambda x: from_list(Channel.from_dict, x), from_none], obj.get("channels"))
        groups = from_union([lambda x: from_list(Group.from_dict, x), from_none], obj.get("groups"))
        ims = from_union([lambda x: from_list(IM.from_dict, x), from_none], obj.get("ims"))
        cache_ts = from_union([from_int, from_none], obj.get("cache_ts"))
        mobile_app_requires_upgrade = from_union([from_bool, from_none], obj.get("mobile_app_requires_upgrade"))
        read_only_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("read_only_channels"))
        non_threadable_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("non_threadable_channels"))
        thread_only_channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("thread_only_channels"))
        can_manage_shared_channels = from_union([from_bool, from_none], obj.get("can_manage_shared_channels"))
        subteams = from_union([Subteams.from_dict, from_none], obj.get("subteams"))
        dnd = from_union([DND.from_dict, from_none], obj.get("dnd"))
        users = from_union([lambda x: from_list(User.from_dict, x), from_none], obj.get("users"))
        cache_version = from_union([from_str, from_none], obj.get("cache_version"))
        cache_ts_version = from_union([from_str, from_none], obj.get("cache_ts_version"))
        bots = from_union([lambda x: from_list(Bot.from_dict, x), from_none], obj.get("bots"))
        url = from_union([from_str, from_none], obj.get("url"))
        is_europe = from_union([from_bool, from_none], obj.get("is_europe"))
        links = from_union([Links.from_dict, from_none], obj.get("links"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return RtmStartResponse(ok, rtm_start_response_self, team, accept_tos_url, latest_event_ts, channels, groups, ims, cache_ts, mobile_app_requires_upgrade, read_only_channels, non_threadable_channels, thread_only_channels, can_manage_shared_channels, subteams, dnd, users, cache_version, cache_ts_version, bots, url, is_europe, links, response_metadata, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["self"] = from_union([lambda x: to_class(Self, x), from_none], self.rtm_start_response_self)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["accept_tos_url"] = from_union([from_str, from_none], self.accept_tos_url)
        result["latest_event_ts"] = from_union([from_str, from_none], self.latest_event_ts)
        result["channels"] = from_union([lambda x: from_list(lambda x: to_class(Channel, x), x), from_none], self.channels)
        result["groups"] = from_union([lambda x: from_list(lambda x: to_class(Group, x), x), from_none], self.groups)
        result["ims"] = from_union([lambda x: from_list(lambda x: to_class(IM, x), x), from_none], self.ims)
        result["cache_ts"] = from_union([from_int, from_none], self.cache_ts)
        result["mobile_app_requires_upgrade"] = from_union([from_bool, from_none], self.mobile_app_requires_upgrade)
        result["read_only_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.read_only_channels)
        result["non_threadable_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.non_threadable_channels)
        result["thread_only_channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.thread_only_channels)
        result["can_manage_shared_channels"] = from_union([from_bool, from_none], self.can_manage_shared_channels)
        result["subteams"] = from_union([lambda x: to_class(Subteams, x), from_none], self.subteams)
        result["dnd"] = from_union([lambda x: to_class(DND, x), from_none], self.dnd)
        result["users"] = from_union([lambda x: from_list(lambda x: to_class(User, x), x), from_none], self.users)
        result["cache_version"] = from_union([from_str, from_none], self.cache_version)
        result["cache_ts_version"] = from_union([from_str, from_none], self.cache_ts_version)
        result["bots"] = from_union([lambda x: from_list(lambda x: to_class(Bot, x), x), from_none], self.bots)
        result["url"] = from_union([from_str, from_none], self.url)
        result["is_europe"] = from_union([from_bool, from_none], self.is_europe)
        result["links"] = from_union([lambda x: to_class(Links, x), from_none], self.links)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def rtm_start_response_from_dict(s: Any) -> RtmStartResponse:
    return RtmStartResponse.from_dict(s)


def rtm_start_response_to_dict(x: RtmStartResponse) -> Any:
    return to_class(RtmStartResponse, x)
