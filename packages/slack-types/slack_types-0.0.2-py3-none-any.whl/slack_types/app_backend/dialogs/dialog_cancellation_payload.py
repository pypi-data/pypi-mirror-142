# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = dialog_cancellation_payload_from_dict(json.loads(json_string))

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
class DialogCancellationPayload:
    type: Optional[str] = None
    token: Optional[str] = None
    action_ts: Optional[str] = None
    enterprise: Optional[Channel] = None
    team: Optional[Team] = None
    user: Optional[User] = None
    channel: Optional[Channel] = None
    callback_id: Optional[str] = None
    response_url: Optional[str] = None
    state: Optional[str] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'DialogCancellationPayload':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        token = from_union([from_str, from_none], obj.get("token"))
        action_ts = from_union([from_str, from_none], obj.get("action_ts"))
        enterprise = from_union([Channel.from_dict, from_none], obj.get("enterprise"))
        team = from_union([Team.from_dict, from_none], obj.get("team"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        callback_id = from_union([from_str, from_none], obj.get("callback_id"))
        response_url = from_union([from_str, from_none], obj.get("response_url"))
        state = from_union([from_str, from_none], obj.get("state"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return DialogCancellationPayload(type, token, action_ts, enterprise, team, user, channel, callback_id, response_url, state, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["token"] = from_union([from_str, from_none], self.token)
        result["action_ts"] = from_union([from_str, from_none], self.action_ts)
        result["enterprise"] = from_union([lambda x: to_class(Channel, x), from_none], self.enterprise)
        result["team"] = from_union([lambda x: to_class(Team, x), from_none], self.team)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["callback_id"] = from_union([from_str, from_none], self.callback_id)
        result["response_url"] = from_union([from_str, from_none], self.response_url)
        result["state"] = from_union([from_str, from_none], self.state)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


def dialog_cancellation_payload_from_dict(s: Any) -> DialogCancellationPayload:
    return DialogCancellationPayload.from_dict(s)


def dialog_cancellation_payload_to_dict(x: DialogCancellationPayload) -> Any:
    return to_class(DialogCancellationPayload, x)
