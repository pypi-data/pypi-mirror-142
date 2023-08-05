# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = view_closed_payload_from_dict(json.loads(json_string))

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
class Enterprise:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Enterprise':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Enterprise(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
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
class ViewClosedPayload:
    type: Optional[str] = None
    enterprise: Optional[Enterprise] = None
    team: Optional[Team] = None
    user: Optional[User] = None
    api_app_id: Optional[str] = None
    token: Optional[str] = None
    view: Optional[View] = None
    is_enterprise_install: Optional[bool] = None
    is_cleared: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ViewClosedPayload':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        enterprise = from_union([Enterprise.from_dict, from_none], obj.get("enterprise"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        token = from_union([from_str, from_none], obj.get("token"))
        view = from_union([View.from_dict, from_none], obj.get("view"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        is_cleared = from_union([from_bool, from_none], obj.get("is_cleared"))
        return ViewClosedPayload(type, enterprise, team, user, api_app_id, token, view, is_enterprise_install, is_cleared)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["enterprise"] = from_union([lambda x: to_class(Enterprise, x), from_none], self.enterprise)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["token"] = from_union([from_str, from_none], self.token)
        result["view"] = from_union([lambda x: to_class(View, x), from_none], self.view)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        result["is_cleared"] = from_union([from_bool, from_none], self.is_cleared)
        return result


def view_closed_payload_from_dict(s: Any) -> ViewClosedPayload:
    return ViewClosedPayload.from_dict(s)


def view_closed_payload_to_dict(x: ViewClosedPayload) -> Any:
    return to_class(ViewClosedPayload, x)
