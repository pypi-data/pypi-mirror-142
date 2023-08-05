# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = app_home_opened_payload_from_dict(json.loads(json_string))

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
class Close:
    type: Optional[str] = None
    text: Optional[str] = None
    emoji: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Close':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        text = from_union([from_str, from_none], obj.get("text"))
        emoji = from_union([from_bool, from_none], obj.get("emoji"))
        return Close(type, text, emoji)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["text"] = from_union([from_str, from_none], self.text)
        result["emoji"] = from_union([from_bool, from_none], self.emoji)
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
class Event:
    type: Optional[str] = None
    user: Optional[str] = None
    channel: Optional[str] = None
    tab: Optional[str] = None
    event_ts: Optional[str] = None
    view: Optional[View] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Event':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([from_str, from_none], obj.get("user"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        tab = from_union([from_str, from_none], obj.get("tab"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        view = from_union([View.from_dict, from_none], obj.get("view"))
        return Event(type, user, channel, tab, event_ts, view)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([from_str, from_none], self.user)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["tab"] = from_union([from_str, from_none], self.tab)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        result["view"] = from_union([lambda x: to_class(View, x), from_none], self.view)
        return result


@dataclass
class AppHomeOpenedPayload:
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
    def from_dict(obj: Any) -> 'AppHomeOpenedPayload':
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
        return AppHomeOpenedPayload(token, enterprise_id, team_id, api_app_id, type, authed_users, authed_teams, authorizations, is_ext_shared_channel, event_id, event_time, event_context, event)

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


def app_home_opened_payload_from_dict(s: Any) -> AppHomeOpenedPayload:
    return AppHomeOpenedPayload.from_dict(s)


def app_home_opened_payload_to_dict(x: AppHomeOpenedPayload) -> Any:
    return to_class(AppHomeOpenedPayload, x)
