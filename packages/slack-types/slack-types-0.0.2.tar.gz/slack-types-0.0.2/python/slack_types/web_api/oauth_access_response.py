# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = oauth_access_response_from_dict(json.loads(json_string))

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
class User:
    user_id: Optional[str] = None
    app_home: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        app_home = from_union([from_str, from_none], obj.get("app_home"))
        return User(user_id, app_home)

    def to_dict(self) -> dict:
        result: dict = {}
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["app_home"] = from_union([from_str, from_none], self.app_home)
        return result


@dataclass
class Bot:
    bot_user_id: Optional[str] = None
    bot_access_token: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Bot':
        assert isinstance(obj, dict)
        bot_user_id = from_union([from_str, from_none], obj.get("bot_user_id"))
        bot_access_token = from_union([from_str, from_none], obj.get("bot_access_token"))
        return Bot(bot_user_id, bot_access_token)

    def to_dict(self) -> dict:
        result: dict = {}
        result["bot_user_id"] = from_union([from_str, from_none], self.bot_user_id)
        result["bot_access_token"] = from_union([from_str, from_none], self.bot_access_token)
        return result


@dataclass
class IncomingWebhook:
    url: Optional[str] = None
    channel: Optional[str] = None
    channel_id: Optional[str] = None
    configuration_url: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'IncomingWebhook':
        assert isinstance(obj, dict)
        url = from_union([from_str, from_none], obj.get("url"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        configuration_url = from_union([from_str, from_none], obj.get("configuration_url"))
        return IncomingWebhook(url, channel, channel_id, configuration_url)

    def to_dict(self) -> dict:
        result: dict = {}
        result["url"] = from_union([from_str, from_none], self.url)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["configuration_url"] = from_union([from_str, from_none], self.configuration_url)
        return result


@dataclass
class Scopes:
    app_home: Optional[List[str]] = None
    team: Optional[List[str]] = None
    channel: Optional[List[str]] = None
    group: Optional[List[str]] = None
    mpim: Optional[List[str]] = None
    im: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Scopes':
        assert isinstance(obj, dict)
        app_home = from_union([lambda x: from_list(from_str, x), from_none], obj.get("app_home"))
        team = from_union([lambda x: from_list(from_str, x), from_none], obj.get("team"))
        channel = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel"))
        group = from_union([lambda x: from_list(from_str, x), from_none], obj.get("group"))
        mpim = from_union([lambda x: from_list(from_str, x), from_none], obj.get("mpim"))
        im = from_union([lambda x: from_list(from_str, x), from_none], obj.get("im"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return Scopes(app_home, team, channel, group, mpim, im, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["app_home"] = from_union([lambda x: from_list(from_str, x), from_none], self.app_home)
        result["team"] = from_union([lambda x: from_list(from_str, x), from_none], self.team)
        result["channel"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel)
        result["group"] = from_union([lambda x: from_list(from_str, x), from_none], self.group)
        result["mpim"] = from_union([lambda x: from_list(from_str, x), from_none], self.mpim)
        result["im"] = from_union([lambda x: from_list(from_str, x), from_none], self.im)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class OauthAccessResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    token_type: Optional[str] = None
    access_token: Optional[str] = None
    scope: Optional[str] = None
    enterprise_id: Optional[str] = None
    team_name: Optional[str] = None
    team_id: Optional[str] = None
    user_id: Optional[str] = None
    incoming_webhook: Optional[IncomingWebhook] = None
    bot: Optional[Bot] = None
    authorizing_user: Optional[User] = None
    installer_user: Optional[User] = None
    scopes: Optional[Scopes] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OauthAccessResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        token_type = from_union([from_str, from_none], obj.get("token_type"))
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        scope = from_union([from_str, from_none], obj.get("scope"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        team_name = from_union([from_str, from_none], obj.get("team_name"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        incoming_webhook = from_union([IncomingWebhook.from_dict, from_none], obj.get("incoming_webhook"))
        bot = from_union([Bot.from_dict, from_none], obj.get("bot"))
        authorizing_user = from_union([User.from_dict, from_none], obj.get("authorizing_user"))
        installer_user = from_union([User.from_dict, from_none], obj.get("installer_user"))
        scopes = from_union([Scopes.from_dict, from_none], obj.get("scopes"))
        return OauthAccessResponse(ok, warning, error, needed, provided, token_type, access_token, scope, enterprise_id, team_name, team_id, user_id, incoming_webhook, bot, authorizing_user, installer_user, scopes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["token_type"] = from_union([from_str, from_none], self.token_type)
        result["access_token"] = from_union([from_str, from_none], self.access_token)
        result["scope"] = from_union([from_str, from_none], self.scope)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["team_name"] = from_union([from_str, from_none], self.team_name)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["incoming_webhook"] = from_union([lambda x: to_class(IncomingWebhook, x), from_none], self.incoming_webhook)
        result["bot"] = from_union([lambda x: to_class(Bot, x), from_none], self.bot)
        result["authorizing_user"] = from_union([lambda x: to_class(User, x), from_none], self.authorizing_user)
        result["installer_user"] = from_union([lambda x: to_class(User, x), from_none], self.installer_user)
        result["scopes"] = from_union([lambda x: to_class(Scopes, x), from_none], self.scopes)
        return result


def oauth_access_response_from_dict(s: Any) -> OauthAccessResponse:
    return OauthAccessResponse.from_dict(s)


def oauth_access_response_to_dict(x: OauthAccessResponse) -> Any:
    return to_class(OauthAccessResponse, x)
