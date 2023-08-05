# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = logs_response_from_dict(json.loads(json_string))

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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


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
class Actor:
    type: Optional[str] = None
    user: Optional[User] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Actor':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        return Actor(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        return result


@dataclass
class Location:
    type: Optional[str] = None
    id: Optional[str] = None
    name: Optional[str] = None
    domain: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Location':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        domain = from_union([from_str, from_none], obj.get("domain"))
        return Location(type, id, name, domain)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["domain"] = from_union([from_str, from_none], self.domain)
        return result


@dataclass
class Context:
    session_id: Optional[str] = None
    location: Optional[Location] = None
    ua: Optional[str] = None
    ip_address: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Context':
        assert isinstance(obj, dict)
        session_id = from_union([from_str, from_none], obj.get("session_id"))
        location = from_union([Location.from_dict, from_none], obj.get("location"))
        ua = from_union([from_str, from_none], obj.get("ua"))
        ip_address = from_union([from_str, from_none], obj.get("ip_address"))
        return Context(session_id, location, ua, ip_address)

    def to_dict(self) -> dict:
        result: dict = {}
        result["session_id"] = from_union([from_str, from_none], self.session_id)
        result["location"] = from_union([lambda x: to_class(Location, x), from_none], self.location)
        result["ua"] = from_union([from_str, from_none], self.ua)
        result["ip_address"] = from_union([from_str, from_none], self.ip_address)
        return result


@dataclass
class CanThread:
    type: Optional[List[str]] = None
    user: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'CanThread':
        assert isinstance(obj, dict)
        type = from_union([lambda x: from_list(from_str, x), from_none], obj.get("type"))
        user = from_union([lambda x: from_list(from_str, x), from_none], obj.get("user"))
        return CanThread(type, user)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([lambda x: from_list(from_str, x), from_none], self.type)
        result["user"] = from_union([lambda x: from_list(from_str, x), from_none], self.user)
        return result


@dataclass
class Inviter:
    type: Optional[str] = None
    user: Optional[User] = None
    id: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    team: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Inviter':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        email = from_union([from_str, from_none], obj.get("email"))
        team = from_union([from_str, from_none], obj.get("team"))
        return Inviter(type, user, id, name, email, team)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["email"] = from_union([from_str, from_none], self.email)
        result["team"] = from_union([from_str, from_none], self.team)
        return result


@dataclass
class RetentionPolicy:
    type: Optional[str] = None
    duration_days: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RetentionPolicy':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        duration_days = from_union([from_int, from_none], obj.get("duration_days"))
        return RetentionPolicy(type, duration_days)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["duration_days"] = from_union([from_int, from_none], self.duration_days)
        return result


@dataclass
class Wildcard:
    type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Wildcard':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        return Wildcard(type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        return result


@dataclass
class Grant:
    type: Optional[str] = None
    resource_id: Optional[str] = None
    wildcard: Optional[Wildcard] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Grant':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        resource_id = from_union([from_str, from_none], obj.get("resource_id"))
        wildcard = from_union([Wildcard.from_dict, from_none], obj.get("wildcard"))
        return Grant(type, resource_id, wildcard)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["resource_id"] = from_union([from_str, from_none], self.resource_id)
        result["wildcard"] = from_union([lambda x: to_class(Wildcard, x), from_none], self.wildcard)
        return result


@dataclass
class Resource:
    type: Optional[str] = None
    grant: Optional[Grant] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        grant = from_union([Grant.from_dict, from_none], obj.get("grant"))
        return Resource(type, grant)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["grant"] = from_union([lambda x: to_class(Grant, x), from_none], self.grant)
        return result


@dataclass
class Permission:
    resource: Optional[Resource] = None
    scopes: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Permission':
        assert isinstance(obj, dict)
        resource = from_union([Resource.from_dict, from_none], obj.get("resource"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        return Permission(resource, scopes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["resource"] = from_union([lambda x: to_class(Resource, x), from_none], self.resource)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        return result


@dataclass
class Details:
    type: Optional[str] = None
    app_owner_id: Optional[str] = None
    scopes: Optional[List[str]] = None
    bot_scopes: Optional[List[str]] = None
    new_scopes: Optional[List[str]] = None
    previous_scopes: Optional[List[str]] = None
    inviter: Optional[Inviter] = None
    kicker: Optional[Inviter] = None
    installer_user_id: Optional[str] = None
    approver_id: Optional[str] = None
    approval_type: Optional[str] = None
    app_previously_approved: Optional[bool] = None
    old_scopes: Optional[List[str]] = None
    name: Optional[str] = None
    bot_id: Optional[str] = None
    channels: Optional[List[str]] = None
    permissions: Optional[List[Permission]] = None
    shared_to: Optional[str] = None
    reason: Optional[str] = None
    is_internal_integration: Optional[bool] = None
    cleared_resolution: Optional[str] = None
    is_workflow: Optional[bool] = None
    mobile_only: Optional[bool] = None
    web_only: Optional[bool] = None
    non_sso_only: Optional[bool] = None
    expires_on: Optional[int] = None
    new_version_id: Optional[str] = None
    trigger: Optional[str] = None
    granular_bot_token: Optional[bool] = None
    origin_team: Optional[str] = None
    target_team: Optional[str] = None
    resolution: Optional[str] = None
    app_previously_resolved: Optional[bool] = None
    admin_app_id: Optional[str] = None
    export_type: Optional[str] = None
    export_start_ts: Optional[str] = None
    export_end_ts: Optional[str] = None
    barrier_id: Optional[str] = None
    primary_usergroup_id: Optional[str] = None
    barriered_from_usergroup_ids: Optional[List[str]] = None
    restricted_subjects: Optional[List[str]] = None
    duration: Optional[int] = None
    desktop_app_browser_quit: Optional[bool] = None
    invite_id: Optional[str] = None
    external_organization_id: Optional[str] = None
    external_organization_name: Optional[str] = None
    external_user_id: Optional[str] = None
    external_user_email: Optional[str] = None
    channel_id: Optional[str] = None
    added_team_id: Optional[str] = None
    is_token_rotation_enabled_app: Optional[bool] = None
    old_retention_policy: Optional[RetentionPolicy] = None
    new_retention_policy: Optional[RetentionPolicy] = None
    who_can_post: Optional[CanThread] = None
    can_thread: Optional[CanThread] = None
    is_external_limited: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Details':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        app_owner_id = from_union([from_str, from_none], obj.get("app_owner_id"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        bot_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("bot_scopes"))
        new_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("new_scopes"))
        previous_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("previous_scopes"))
        inviter = from_union([Inviter.from_dict, from_none], obj.get("inviter"))
        kicker = from_union([Inviter.from_dict, from_none], obj.get("kicker"))
        installer_user_id = from_union([from_str, from_none], obj.get("installer_user_id"))
        approver_id = from_union([from_str, from_none], obj.get("approver_id"))
        approval_type = from_union([from_str, from_none], obj.get("approval_type"))
        app_previously_approved = from_union([from_bool, from_none], obj.get("app_previously_approved"))
        old_scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("old_scopes"))
        name = from_union([from_str, from_none], obj.get("name"))
        bot_id = from_union([from_str, from_none], obj.get("bot_id"))
        channels = from_union([lambda x: from_list(from_str, x), from_none], obj.get("channels"))
        permissions = from_union([lambda x: from_list(Permission.from_dict, x), from_none], obj.get("permissions"))
        shared_to = from_union([from_str, from_none], obj.get("shared_to"))
        reason = from_union([from_str, from_none], obj.get("reason"))
        is_internal_integration = from_union([from_bool, from_none], obj.get("is_internal_integration"))
        cleared_resolution = from_union([from_str, from_none], obj.get("cleared_resolution"))
        is_workflow = from_union([from_bool, from_none], obj.get("is_workflow"))
        mobile_only = from_union([from_bool, from_none], obj.get("mobile_only"))
        web_only = from_union([from_bool, from_none], obj.get("web_only"))
        non_sso_only = from_union([from_bool, from_none], obj.get("non_sso_only"))
        expires_on = from_union([from_int, from_none], obj.get("expires_on"))
        new_version_id = from_union([from_str, from_none], obj.get("new_version_id"))
        trigger = from_union([from_str, from_none], obj.get("trigger"))
        granular_bot_token = from_union([from_bool, from_none], obj.get("granular_bot_token"))
        origin_team = from_union([from_str, from_none], obj.get("origin_team"))
        target_team = from_union([from_str, from_none], obj.get("target_team"))
        resolution = from_union([from_str, from_none], obj.get("resolution"))
        app_previously_resolved = from_union([from_bool, from_none], obj.get("app_previously_resolved"))
        admin_app_id = from_union([from_str, from_none], obj.get("admin_app_id"))
        export_type = from_union([from_str, from_none], obj.get("export_type"))
        export_start_ts = from_union([from_str, from_none], obj.get("export_start_ts"))
        export_end_ts = from_union([from_str, from_none], obj.get("export_end_ts"))
        barrier_id = from_union([from_str, from_none], obj.get("barrier_id"))
        primary_usergroup_id = from_union([from_str, from_none], obj.get("primary_usergroup_id"))
        barriered_from_usergroup_ids = from_union([lambda x: from_list(from_str, x), from_none], obj.get("barriered_from_usergroup_ids"))
        restricted_subjects = from_union([lambda x: from_list(from_str, x), from_none], obj.get("restricted_subjects"))
        duration = from_union([from_int, from_none], obj.get("duration"))
        desktop_app_browser_quit = from_union([from_bool, from_none], obj.get("desktop_app_browser_quit"))
        invite_id = from_union([from_str, from_none], obj.get("invite_id"))
        external_organization_id = from_union([from_str, from_none], obj.get("external_organization_id"))
        external_organization_name = from_union([from_str, from_none], obj.get("external_organization_name"))
        external_user_id = from_union([from_str, from_none], obj.get("external_user_id"))
        external_user_email = from_union([from_str, from_none], obj.get("external_user_email"))
        channel_id = from_union([from_str, from_none], obj.get("channel_id"))
        added_team_id = from_union([from_str, from_none], obj.get("added_team_id"))
        is_token_rotation_enabled_app = from_union([from_bool, from_none], obj.get("is_token_rotation_enabled_app"))
        old_retention_policy = from_union([RetentionPolicy.from_dict, from_none], obj.get("old_retention_policy"))
        new_retention_policy = from_union([RetentionPolicy.from_dict, from_none], obj.get("new_retention_policy"))
        who_can_post = from_union([CanThread.from_dict, from_none], obj.get("who_can_post"))
        can_thread = from_union([CanThread.from_dict, from_none], obj.get("can_thread"))
        is_external_limited = from_union([from_bool, from_none], obj.get("is_external_limited"))
        return Details(type, app_owner_id, scopes, bot_scopes, new_scopes, previous_scopes, inviter, kicker, installer_user_id, approver_id, approval_type, app_previously_approved, old_scopes, name, bot_id, channels, permissions, shared_to, reason, is_internal_integration, cleared_resolution, is_workflow, mobile_only, web_only, non_sso_only, expires_on, new_version_id, trigger, granular_bot_token, origin_team, target_team, resolution, app_previously_resolved, admin_app_id, export_type, export_start_ts, export_end_ts, barrier_id, primary_usergroup_id, barriered_from_usergroup_ids, restricted_subjects, duration, desktop_app_browser_quit, invite_id, external_organization_id, external_organization_name, external_user_id, external_user_email, channel_id, added_team_id, is_token_rotation_enabled_app, old_retention_policy, new_retention_policy, who_can_post, can_thread, is_external_limited)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["app_owner_id"] = from_union([from_str, from_none], self.app_owner_id)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        result["bot_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.bot_scopes)
        result["new_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.new_scopes)
        result["previous_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.previous_scopes)
        result["inviter"] = from_union([lambda x: to_class(Inviter, x), from_none], self.inviter)
        result["kicker"] = from_union([lambda x: to_class(Inviter, x), from_none], self.kicker)
        result["installer_user_id"] = from_union([from_str, from_none], self.installer_user_id)
        result["approver_id"] = from_union([from_str, from_none], self.approver_id)
        result["approval_type"] = from_union([from_str, from_none], self.approval_type)
        result["app_previously_approved"] = from_union([from_bool, from_none], self.app_previously_approved)
        result["old_scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.old_scopes)
        result["name"] = from_union([from_str, from_none], self.name)
        result["bot_id"] = from_union([from_str, from_none], self.bot_id)
        result["channels"] = from_union([lambda x: from_list(from_str, x), from_none], self.channels)
        result["permissions"] = from_union([lambda x: from_list(lambda x: to_class(Permission, x), x), from_none], self.permissions)
        result["shared_to"] = from_union([from_str, from_none], self.shared_to)
        result["reason"] = from_union([from_str, from_none], self.reason)
        result["is_internal_integration"] = from_union([from_bool, from_none], self.is_internal_integration)
        result["cleared_resolution"] = from_union([from_str, from_none], self.cleared_resolution)
        result["is_workflow"] = from_union([from_bool, from_none], self.is_workflow)
        result["mobile_only"] = from_union([from_bool, from_none], self.mobile_only)
        result["web_only"] = from_union([from_bool, from_none], self.web_only)
        result["non_sso_only"] = from_union([from_bool, from_none], self.non_sso_only)
        result["expires_on"] = from_union([from_int, from_none], self.expires_on)
        result["new_version_id"] = from_union([from_str, from_none], self.new_version_id)
        result["trigger"] = from_union([from_str, from_none], self.trigger)
        result["granular_bot_token"] = from_union([from_bool, from_none], self.granular_bot_token)
        result["origin_team"] = from_union([from_str, from_none], self.origin_team)
        result["target_team"] = from_union([from_str, from_none], self.target_team)
        result["resolution"] = from_union([from_str, from_none], self.resolution)
        result["app_previously_resolved"] = from_union([from_bool, from_none], self.app_previously_resolved)
        result["admin_app_id"] = from_union([from_str, from_none], self.admin_app_id)
        result["export_type"] = from_union([from_str, from_none], self.export_type)
        result["export_start_ts"] = from_union([from_str, from_none], self.export_start_ts)
        result["export_end_ts"] = from_union([from_str, from_none], self.export_end_ts)
        result["barrier_id"] = from_union([from_str, from_none], self.barrier_id)
        result["primary_usergroup_id"] = from_union([from_str, from_none], self.primary_usergroup_id)
        result["barriered_from_usergroup_ids"] = from_union([lambda x: from_list(from_str, x), from_none], self.barriered_from_usergroup_ids)
        result["restricted_subjects"] = from_union([lambda x: from_list(from_str, x), from_none], self.restricted_subjects)
        result["duration"] = from_union([from_int, from_none], self.duration)
        result["desktop_app_browser_quit"] = from_union([from_bool, from_none], self.desktop_app_browser_quit)
        result["invite_id"] = from_union([from_str, from_none], self.invite_id)
        result["external_organization_id"] = from_union([from_str, from_none], self.external_organization_id)
        result["external_organization_name"] = from_union([from_str, from_none], self.external_organization_name)
        result["external_user_id"] = from_union([from_str, from_none], self.external_user_id)
        result["external_user_email"] = from_union([from_str, from_none], self.external_user_email)
        result["channel_id"] = from_union([from_str, from_none], self.channel_id)
        result["added_team_id"] = from_union([from_str, from_none], self.added_team_id)
        result["is_token_rotation_enabled_app"] = from_union([from_bool, from_none], self.is_token_rotation_enabled_app)
        result["old_retention_policy"] = from_union([lambda x: to_class(RetentionPolicy, x), from_none], self.old_retention_policy)
        result["new_retention_policy"] = from_union([lambda x: to_class(RetentionPolicy, x), from_none], self.new_retention_policy)
        result["who_can_post"] = from_union([lambda x: to_class(CanThread, x), from_none], self.who_can_post)
        result["can_thread"] = from_union([lambda x: to_class(CanThread, x), from_none], self.can_thread)
        result["is_external_limited"] = from_union([from_bool, from_none], self.is_external_limited)
        return result


@dataclass
class App:
    id: Optional[str] = None
    name: Optional[str] = None
    is_distributed: Optional[bool] = None
    is_directory_approved: Optional[bool] = None
    is_workflow_app: Optional[bool] = None
    scopes: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'App':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        is_distributed = from_union([from_bool, from_none], obj.get("is_distributed"))
        is_directory_approved = from_union([from_bool, from_none], obj.get("is_directory_approved"))
        is_workflow_app = from_union([from_bool, from_none], obj.get("is_workflow_app"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        return App(id, name, is_distributed, is_directory_approved, is_workflow_app, scopes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["is_distributed"] = from_union([from_bool, from_none], self.is_distributed)
        result["is_directory_approved"] = from_union([from_bool, from_none], self.is_directory_approved)
        result["is_workflow_app"] = from_union([from_bool, from_none], self.is_workflow_app)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        return result


@dataclass
class Barrier:
    id: Optional[str] = None
    primary_usergroup: Optional[str] = None
    barriered_from_usergroups: Optional[List[str]] = None
    restricted_subjects: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Barrier':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        primary_usergroup = from_union([from_str, from_none], obj.get("primary_usergroup"))
        barriered_from_usergroups = from_union([lambda x: from_list(from_str, x), from_none], obj.get("barriered_from_usergroups"))
        restricted_subjects = from_union([lambda x: from_list(from_str, x), from_none], obj.get("restricted_subjects"))
        return Barrier(id, primary_usergroup, barriered_from_usergroups, restricted_subjects)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["primary_usergroup"] = from_union([from_str, from_none], self.primary_usergroup)
        result["barriered_from_usergroups"] = from_union([lambda x: from_list(from_str, x), from_none], self.barriered_from_usergroups)
        result["restricted_subjects"] = from_union([lambda x: from_list(from_str, x), from_none], self.restricted_subjects)
        return result


@dataclass
class Channel:
    id: Optional[str] = None
    name: Optional[str] = None
    privacy: Optional[str] = None
    is_shared: Optional[bool] = None
    is_org_shared: Optional[bool] = None
    teams_shared_with: Optional[List[str]] = None
    original_connected_channel_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Channel':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        privacy = from_union([from_str, from_none], obj.get("privacy"))
        is_shared = from_union([from_bool, from_none], obj.get("is_shared"))
        is_org_shared = from_union([from_bool, from_none], obj.get("is_org_shared"))
        teams_shared_with = from_union([lambda x: from_list(from_str, x), from_none], obj.get("teams_shared_with"))
        original_connected_channel_id = from_union([from_str, from_none], obj.get("original_connected_channel_id"))
        return Channel(id, name, privacy, is_shared, is_org_shared, teams_shared_with, original_connected_channel_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["privacy"] = from_union([from_str, from_none], self.privacy)
        result["is_shared"] = from_union([from_bool, from_none], self.is_shared)
        result["is_org_shared"] = from_union([from_bool, from_none], self.is_org_shared)
        result["teams_shared_with"] = from_union([lambda x: from_list(from_str, x), from_none], self.teams_shared_with)
        result["original_connected_channel_id"] = from_union([from_str, from_none], self.original_connected_channel_id)
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
class Usergroup:
    id: Optional[str] = None
    name: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Usergroup':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        return Usergroup(id, name)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        return result


@dataclass
class Entity:
    type: Optional[str] = None
    app: Optional[App] = None
    user: Optional[User] = None
    usergroup: Optional[Usergroup] = None
    workspace: Optional[Location] = None
    enterprise: Optional[Location] = None
    file: Optional[File] = None
    channel: Optional[Channel] = None
    workflow: Optional[Usergroup] = None
    barrier: Optional[Barrier] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entity':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        app = from_union([App.from_dict, from_none], obj.get("app"))
        user = from_union([User.from_dict, from_none], obj.get("user"))
        usergroup = from_union([Usergroup.from_dict, from_none], obj.get("usergroup"))
        workspace = from_union([Location.from_dict, from_none], obj.get("workspace"))
        enterprise = from_union([Location.from_dict, from_none], obj.get("enterprise"))
        file = from_union([File.from_dict, from_none], obj.get("file"))
        channel = from_union([Channel.from_dict, from_none], obj.get("channel"))
        workflow = from_union([Usergroup.from_dict, from_none], obj.get("workflow"))
        barrier = from_union([Barrier.from_dict, from_none], obj.get("barrier"))
        return Entity(type, app, user, usergroup, workspace, enterprise, file, channel, workflow, barrier)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["app"] = from_union([lambda x: to_class(App, x), from_none], self.app)
        result["user"] = from_union([lambda x: to_class(User, x), from_none], self.user)
        result["usergroup"] = from_union([lambda x: to_class(Usergroup, x), from_none], self.usergroup)
        result["workspace"] = from_union([lambda x: to_class(Location, x), from_none], self.workspace)
        result["enterprise"] = from_union([lambda x: to_class(Location, x), from_none], self.enterprise)
        result["file"] = from_union([lambda x: to_class(File, x), from_none], self.file)
        result["channel"] = from_union([lambda x: to_class(Channel, x), from_none], self.channel)
        result["workflow"] = from_union([lambda x: to_class(Usergroup, x), from_none], self.workflow)
        result["barrier"] = from_union([lambda x: to_class(Barrier, x), from_none], self.barrier)
        return result


@dataclass
class Entry:
    id: Optional[str] = None
    date_create: Optional[int] = None
    action: Optional[str] = None
    actor: Optional[Actor] = None
    entity: Optional[Entity] = None
    context: Optional[Context] = None
    details: Optional[Details] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Entry':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        date_create = from_union([from_int, from_none], obj.get("date_create"))
        action = from_union([from_str, from_none], obj.get("action"))
        actor = from_union([Actor.from_dict, from_none], obj.get("actor"))
        entity = from_union([Entity.from_dict, from_none], obj.get("entity"))
        context = from_union([Context.from_dict, from_none], obj.get("context"))
        details = from_union([Details.from_dict, from_none], obj.get("details"))
        return Entry(id, date_create, action, actor, entity, context, details)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["date_create"] = from_union([from_int, from_none], self.date_create)
        result["action"] = from_union([from_str, from_none], self.action)
        result["actor"] = from_union([lambda x: to_class(Actor, x), from_none], self.actor)
        result["entity"] = from_union([lambda x: to_class(Entity, x), from_none], self.entity)
        result["context"] = from_union([lambda x: to_class(Context, x), from_none], self.context)
        result["details"] = from_union([lambda x: to_class(Details, x), from_none], self.details)
        return result


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None
    messages: Optional[List[Any]] = None
    warnings: Optional[List[Any]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        messages = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(lambda x: x, x), from_none], obj.get("warnings"))
        return ResponseMetadata(next_cursor, messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["messages"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(lambda x: x, x), from_none], self.warnings)
        return result


@dataclass
class LogsResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    response_metadata: Optional[ResponseMetadata] = None
    entries: Optional[List[Entry]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LogsResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        entries = from_union([lambda x: from_list(Entry.from_dict, x), from_none], obj.get("entries"))
        return LogsResponse(ok, warning, error, needed, provided, response_metadata, entries)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        result["entries"] = from_union([lambda x: from_list(lambda x: to_class(Entry, x), x), from_none], self.entries)
        return result


def logs_response_from_dict(s: Any) -> LogsResponse:
    return LogsResponse.from_dict(s)


def logs_response_to_dict(x: LogsResponse) -> Any:
    return to_class(LogsResponse, x)
