# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = oauth_v2_access_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AuthedUser:
    id: Optional[str] = None
    scope: Optional[str] = None
    token_type: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthedUser':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        scope = from_union([from_str, from_none], obj.get("scope"))
        token_type = from_union([from_str, from_none], obj.get("token_type"))
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        refresh_token = from_union([from_str, from_none], obj.get("refresh_token"))
        expires_in = from_union([from_int, from_none], obj.get("expires_in"))
        return AuthedUser(id, scope, token_type, access_token, refresh_token, expires_in)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["scope"] = from_union([from_str, from_none], self.scope)
        result["token_type"] = from_union([from_str, from_none], self.token_type)
        result["access_token"] = from_union([from_str, from_none], self.access_token)
        result["refresh_token"] = from_union([from_str, from_none], self.refresh_token)
        result["expires_in"] = from_union([from_int, from_none], self.expires_in)
        return result


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
class OauthV2AccessResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    app_id: Optional[str] = None
    authed_user: Optional[AuthedUser] = None
    scope: Optional[str] = None
    token_type: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_in: Optional[int] = None
    bot_user_id: Optional[str] = None
    team: Optional[Enterprise] = None
    enterprise: Optional[Enterprise] = None
    is_enterprise_install: Optional[bool] = None
    incoming_webhook: Optional[IncomingWebhook] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OauthV2AccessResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        authed_user = from_union([AuthedUser.from_dict, from_none], obj.get("authed_user"))
        scope = from_union([from_str, from_none], obj.get("scope"))
        token_type = from_union([from_str, from_none], obj.get("token_type"))
        access_token = from_union([from_str, from_none], obj.get("access_token"))
        refresh_token = from_union([from_str, from_none], obj.get("refresh_token"))
        expires_in = from_union([from_int, from_none], obj.get("expires_in"))
        bot_user_id = from_union([from_str, from_none], obj.get("bot_user_id"))
        team = from_union([Enterprise.from_dict, from_none], obj.get("team"))
        enterprise = from_union([Enterprise.from_dict, from_none], obj.get("enterprise"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        incoming_webhook = from_union([IncomingWebhook.from_dict, from_none], obj.get("incoming_webhook"))
        return OauthV2AccessResponse(ok, warning, error, needed, provided, app_id, authed_user, scope, token_type, access_token, refresh_token, expires_in, bot_user_id, team, enterprise, is_enterprise_install, incoming_webhook)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["authed_user"] = from_union([lambda x: to_class(AuthedUser, x), from_none], self.authed_user)
        result["scope"] = from_union([from_str, from_none], self.scope)
        result["token_type"] = from_union([from_str, from_none], self.token_type)
        result["access_token"] = from_union([from_str, from_none], self.access_token)
        result["refresh_token"] = from_union([from_str, from_none], self.refresh_token)
        result["expires_in"] = from_union([from_int, from_none], self.expires_in)
        result["bot_user_id"] = from_union([from_str, from_none], self.bot_user_id)
        result["team"] = from_union([lambda x: to_class(Enterprise, x), from_none], self.team)
        result["enterprise"] = from_union([lambda x: to_class(Enterprise, x), from_none], self.enterprise)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        result["incoming_webhook"] = from_union([lambda x: to_class(IncomingWebhook, x), from_none], self.incoming_webhook)
        return result


def oauth_v2_access_response_from_dict(s: Any) -> OauthV2AccessResponse:
    return OauthV2AccessResponse.from_dict(s)


def oauth_v2_access_response_to_dict(x: OauthV2AccessResponse) -> Any:
    return to_class(OauthV2AccessResponse, x)
