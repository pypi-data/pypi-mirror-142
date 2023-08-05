# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = schemas_response_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


@dataclass
class App:
    id: Optional[str] = None
    name: Optional[str] = None
    is_distributed: Optional[str] = None
    is_directory_approved: Optional[str] = None
    is_workflow_app: Optional[str] = None
    scopes: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'App':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_distributed = from_union([from_str, from_none], obj.get("is_distributed"))
        is_directory_approved = from_union([from_str, from_none], obj.get("is_directory_approved"))
        is_workflow_app = from_union([from_str, from_none], obj.get("is_workflow_app"))
        scopes = from_union([from_str, from_none], obj.get("scopes"))
        return App(id, name, is_distributed, is_directory_approved, is_workflow_app, scopes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_distributed"] = from_union([from_str, from_none], self.is_distributed)
        result["is_directory_approved"] = from_union([from_str, from_none], self.is_directory_approved)
        result["is_workflow_app"] = from_union([from_str, from_none], self.is_workflow_app)
        result["scopes"] = from_union([from_str, from_none], self.scopes)
        return result


@dataclass
class Barrier:
    id: Optional[str] = None
    primary_usergroup: Optional[str] = None
    barriered_from_usergroup: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Barrier':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        primary_usergroup = from_union([from_str, from_none], obj.get("primary_usergroup"))
        barriered_from_usergroup = from_union([from_str, from_none], obj.get("barriered_from_usergroup"))
        return Barrier(id, primary_usergroup, barriered_from_usergroup)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["primary_usergroup"] = from_union([from_str, from_none], self.primary_usergroup)
        result["barriered_from_usergroup"] = from_union([from_str, from_none], self.barriered_from_usergroup)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    privacy: Optional[str] = None
    is_shared: Optional[str] = None
    is_org_shared: Optional[str] = None
    teams_shared_with: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        privacy = from_union([from_str, from_none], obj.get("privacy"))
        is_shared = from_union([from_str, from_none], obj.get("is_shared"))
        is_org_shared = from_union([from_str, from_none], obj.get("is_org_shared"))
        teams_shared_with = from_union([from_str, from_none], obj.get("teams_shared_with"))
        return Channel(id, name, privacy, is_shared, is_org_shared, teams_shared_with)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["privacy"] = from_union([from_str, from_none], self.privacy)
        result["is_shared"] = from_union([from_str, from_none], self.is_shared)
        result["is_org_shared"] = from_union([from_str, from_none], self.is_org_shared)
        result["teams_shared_with"] = from_union([from_str, from_none], self.teams_shared_with)
        return result


@dataclass
class Enterprise:
    id: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Enterprise':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        return Enterprise(id, name, domain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["domain"] = from_union([from_str, from_none], self.domain)
        return result


@dataclass
class File:
    id: Optional[str] = None
    name: Optional[str] = None
    filetype: Optional[str] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'File':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        filetype = from_union([from_str, from_none], obj.get("filetype"))
        title = from_union([from_str, from_none], obj.get("title"))
        return File(id, name, filetype, title)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["filetype"] = from_union([from_str, from_none], self.filetype)
        result["title"] = from_union([from_str, from_none], self.title)
        return result


@dataclass
class Message:
    team: Optional[str] = None
    channel: Optional[str] = None
    timestamp: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Message':
        assert isinstance(obj, dict)
        team = from_union([from_str, from_none], obj.get("team"))
        channel = from_union([from_str, from_none], obj.get("channel"))
        timestamp = from_union([from_str, from_none], obj.get("timestamp"))
        return Message(team, channel, timestamp)

    def to_dict(self) -> dict:
        result: dict = {}
        result["team"] = from_union([from_str, from_none], self.team)
        result["channel"] = from_union([from_str, from_none], self.channel)
        result["timestamp"] = from_union([from_str, from_none], self.timestamp)
        return result


@dataclass
class User:
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    team: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'User':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        team = from_union([from_str, from_none], obj.get("team"))
        return User(id, name, email, team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["team"] = from_union([from_str, from_none], self.team)
        return result


@dataclass
class Workflow:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Workflow':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Workflow(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Schema:
    type: Optional[str] = None
    workspace: Optional[Enterprise] = None
    enterprise: Optional[Enterprise] = None
    user: Optional[User] = None
    file: Optional[File] = None
    channel: Optional[Channel] = None
    app: Optional[App] = None
    workflow: Optional[Workflow] = None
    barrier: Optional[Barrier] = None
    message: Optional[Message] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Schema':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        workspace = from_union([Enterprise.from_dict, from_none], obj.get("workspace"))
        enterprise = from_union([Enterprise.from_dict, from_none], obj.get("enterprise"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        app = from_union([App.from_dict, from_none], obj.get("app"))
        workflow = from_union([Workflow.from_dict, from_none], obj.get("workflow"))
        barrier = from_union([Barrier.from_dict, from_none], obj.get("barrier"))
        message = from_union([Message.from_dict, from_none], obj.get("message"))
        return Schema(type, workspace, enterprise, user, file, channel, app, workflow, barrier, message)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["workspace"] = from_union([lambda x: to_class(Enterprise, x), from_none], self.workspace)
        result["enterprise"] = from_union([lambda x: to_class(Enterprise, x), from_none], self.enterprise)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["app"] = from_union([lambda x: to_class(App, x), from_none], self.app)
        result["workflow"] = from_union([lambda x: to_class(Workflow, x), from_none], self.workflow)
        result["barrier"] = from_union([lambda x: to_class(Barrier, x), from_none], self.barrier)
        result["message"] = from_union([lambda x: to_class(Message, x), from_none], self.message)
        return result


@dataclass
class SchemasResponse:
    schemas: Optional[List[Schema]] = None
    ok: Optional[bool] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'SchemasResponse':
        assert isinstance(obj, dict)
        schemas = from_union([lambda x: from_list(Schema.from_dict, x), from_none], obj.get("schemas"))
        ok = from_union([from_bool, from_none], obj.get("ok"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        return SchemasResponse(schemas, ok, error, needed, provided)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schemas"] = from_union([lambda x: from_list(lambda x: to_class(Schema, x), x), from_none], self.schemas)
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        return result


def schemas_response_from_dict(s: Any) -> SchemasResponse:
    return SchemasResponse.from_dict(s)


def schemas_response_to_dict(x: SchemasResponse) -> Any:
    return to_class(SchemasResponse, x)
