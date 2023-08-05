# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = slash_command_payload_from_dict(json.loads(json_string))

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
class SlashCommandPayload:
    token: Optional[str] = None
    api_app_id: Optional[str] = None
    team_id: Optional[str] = None
    team_domain: Optional[str] = None
    enterprise_id: Optional[str] = None
    enterprise_name: Optional[str] = None
    channel_id: Optional[str] = None
    channel_name: Optional[str] = None
    user_id: Optional[str] = None
    user_name: Optional[str] = None
    command: Optional[str] = None
    text: Optional[str] = None
    response_url: Optional[str] = None
    trigger_id: Optional[str] = None
    is_enterprise_install: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SlashCommandPayload':
        assert isinstance(obj, dict)
        token = from_union([from_str, from_none], obj.get("token"))
        api_app_id = from_union([from_str, from_none], obj.get("api_app_id"))
        team_id = from_union([from_str, from_none], obj.get("team_id"))
        team_domain = from_union([from_str, from_none], obj.get("team_domain"))
        enterprise_id = from_union([from_str, from_none], obj.get("enterprise_id"))
        enterprise_name = from_union([from_str, from_none], obj.get("enterprise_name"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        channel_name = from_union([from_str, from_none], obj.get("channel_name"))
        user_id = from_union([from_str, from_none], obj.get("user_id"))
        user_name = from_union([from_str, from_none], obj.get("user_name"))
        command = from_union([from_str, from_none], obj.get("command"))
        text = from_union([from_str, from_none], obj.get("text"))
        response_url = from_union([from_str, from_none], obj.get("response_url"))
        trigger_id = from_union([from_str, from_none], obj.get("trigger_id"))
        is_enterprise_install = from_union([from_bool, from_none], obj.get("is_enterprise_install"))
        return SlashCommandPayload(token, api_app_id, team_id, team_domain, enterprise_id, enterprise_name, channel_id, channel_name, user_id, user_name, command, text, response_url, trigger_id, is_enterprise_install)

    def to_dict(self) -> dict:
        result: dict = {}
        result["token"] = from_union([from_str, from_none], self.token)
        result["api_app_id"] = from_union([from_str, from_none], self.api_app_id)
        result["team_id"] = from_union([from_str, from_none], self.team_id)
        result["team_domain"] = from_union([from_str, from_none], self.team_domain)
        result["enterprise_id"] = from_union([from_str, from_none], self.enterprise_id)
        result["enterprise_name"] = from_union([from_str, from_none], self.enterprise_name)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["channel_name"] = from_union([from_str, from_none], self.channel_name)
        result["user_id"] = from_union([from_str, from_none], self.user_id)
        result["user_name"] = from_union([from_str, from_none], self.user_name)
        result["command"] = from_union([from_str, from_none], self.command)
        result["text"] = from_union([from_str, from_none], self.text)
        result["response_url"] = from_union([from_str, from_none], self.response_url)
        result["trigger_id"] = from_union([from_str, from_none], self.trigger_id)
        result["is_enterprise_install"] = from_union([from_bool, from_none], self.is_enterprise_install)
        return result


def slash_command_payload_from_dict(s: Any) -> SlashCommandPayload:
    return SlashCommandPayload.from_dict(s)


def slash_command_payload_to_dict(x: SlashCommandPayload) -> Any:
    return to_class(SlashCommandPayload, x)
