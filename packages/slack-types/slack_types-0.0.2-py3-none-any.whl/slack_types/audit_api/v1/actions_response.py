# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = actions_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


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
class Actions:
    workspace_or_org: Optional[List[str]] = None
    user: Optional[List[str]] = None
    file: Optional[List[str]] = None
    channel: Optional[List[str]] = None
    app: Optional[List[str]] = None
    workflow_builder: Optional[List[str]] = None
    message: Optional[List[str]] = None
    barrier: Optional[List[str]] = None
    huddle: Optional[List[str]] = None
    anomaly: Optional[List[str]] = None
    slack_cli: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Actions':
        assert isinstance(obj, dict)
        workspace_or_org = from_union([lambda x: from_list(from_str, x), from_none], obj.get("workspace_or_org"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        file = from_union([lambda x: from_list(from_str, x), from_none], obj.get("file"))
        channel = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channel"))
        app = from_union([lambda x: from_list(from_str, x), from_none], obj.get("app"))
        workflow_builder = from_union([lambda x: from_list(from_str, x), from_none], obj.get("workflow_builder"))
        message = from_union([lambda x: from_list(from_str, x), from_none], obj.get("message"))
        barrier = from_union([lambda x: from_list(from_str, x), from_none], obj.get("barrier"))
        huddle = from_union([lambda x: from_list(from_str, x), from_none], obj.get("huddle"))
        anomaly = from_union([lambda x: from_list(from_str, x), from_none], obj.get("anomaly"))
        slack_cli = from_union([lambda x: from_list(from_str, x), from_none], obj.get("slack_cli"))
        return Actions(workspace_or_org, user, file, channel, app, workflow_builder, message, barrier, huddle, anomaly, slack_cli)

    def to_dict(self) -> dict:
        result: dict = {}
        result["workspace_or_org"] = from_union([lambda x: from_list(from_str, x), from_none], self.workspace_or_org)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        result["file"] = from_union([lambda x: from_list(from_str, x), from_none], self.file)
        result["channel"] = from_union([lambda x: from_list(from_str, x), from_none], self.channel)
        result["app"] = from_union([lambda x: from_list(from_str, x), from_none], self.app)
        result["workflow_builder"] = from_union([lambda x: from_list(from_str, x), from_none], self.workflow_builder)
        result["message"] = from_union([lambda x: from_list(from_str, x), from_none], self.message)
        result["barrier"] = from_union([lambda x: from_list(from_str, x), from_none], self.barrier)
        result["huddle"] = from_union([lambda x: from_list(from_str, x), from_none], self.huddle)
        result["anomaly"] = from_union([lambda x: from_list(from_str, x), from_none], self.anomaly)
        result["slack_cli"] = from_union([lambda x: from_list(from_str, x), from_none], self.slack_cli)
        return result


@dataclass
class ActionsResponse:
    actions: Optional[Actions] = None
    ok: Optional[bool] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ActionsResponse':
        assert isinstance(obj, dict)
        actions = from_union([Actions.from_dict, from_none], obj.get("actions"))
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return ActionsResponse(actions, ok, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actions"] = from_union([lambda x: to_class(Actions, x), from_none], self.actions)
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def actions_response_from_dict(s: Any) -> ActionsResponse:
    return ActionsResponse.from_dict(s)


def actions_response_to_dict(x: ActionsResponse) -> Any:
    return to_class(ActionsResponse, x)
