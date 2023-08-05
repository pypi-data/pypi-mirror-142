# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = admin_apps_restricted_list_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, List, Any, TypeVar, Callable, Type, cast


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


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


@dataclass
class ResponseMetadata:
    next_cursor: Optional[str] = None
    messages: Optional[List[str]] = None
    warnings: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResponseMetadata':
        assert isinstance(obj, dict)
        next_cursor = from_union([from_str, from_none], obj.get("next_cursor"))
        messages = from_union([lambda x: from_list(from_str, x), from_none], obj.get("messages"))
        warnings = from_union([lambda x: from_list(from_str, x), from_none], obj.get("warnings"))
        return ResponseMetadata(next_cursor, messages, warnings)

    def to_dict(self) -> dict:
        result: dict = {}
        result["next_cursor"] = from_union([from_str, from_none], self.next_cursor)
        result["messages"] = from_union([lambda x: from_list(from_str, x), from_none], self.messages)
        result["warnings"] = from_union([lambda x: from_list(from_str, x), from_none], self.warnings)
        return result


@dataclass
class Icons:
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
    def from_dict(obj: Any) -> 'Icons':
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
        return Icons(image_32, image_36, image_48, image_64, image_72, image_96, image_128, image_192, image_512, image_1024, image_original)

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
class App:
    id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    help_url: Optional[str] = None
    privacy_policy_url: Optional[str] = None
    app_homepage_url: Optional[str] = None
    app_directory_url: Optional[str] = None
    is_app_directory_approved: Optional[bool] = None
    is_internal: Optional[bool] = None
    additional_info: Optional[str] = None
    icons: Optional[Icons] = None

    @staticmethod
    def from_dict(obj: Any) -> 'App':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        help_url = from_union([from_str, from_none], obj.get("help_url"))
        privacy_policy_url = from_union([from_str, from_none], obj.get("privacy_policy_url"))
        app_homepage_url = from_union([from_str, from_none], obj.get("app_homepage_url"))
        app_directory_url = from_union([from_str, from_none], obj.get("app_directory_url"))
        is_app_directory_approved = from_union([from_bool, from_none], obj.get("is_app_directory_approved"))
        is_internal = from_union([from_bool, from_none], obj.get("is_internal"))
        additional_info = from_union([from_str, from_none], obj.get("additional_info"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        return App(id, name, description, help_url, privacy_policy_url, app_homepage_url, app_directory_url, is_app_directory_approved, is_internal, additional_info, icons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["help_url"] = from_union([from_str, from_none], self.help_url)
        result["privacy_policy_url"] = from_union([from_str, from_none], self.privacy_policy_url)
        result["app_homepage_url"] = from_union([from_str, from_none], self.app_homepage_url)
        result["app_directory_url"] = from_union([from_str, from_none], self.app_directory_url)
        result["is_app_directory_approved"] = from_union([from_bool, from_none], self.is_app_directory_approved)
        result["is_internal"] = from_union([from_bool, from_none], self.is_internal)
        result["additional_info"] = from_union([from_str, from_none], self.additional_info)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        return result


@dataclass
class LastResolvedBy:
    actor_id: Optional[str] = None
    actor_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'LastResolvedBy':
        assert isinstance(obj, dict)
        actor_id = from_union([from_str, from_none], obj.get("actor_id"))
        actor_type = from_union([from_str, from_none], obj.get("actor_type"))
        return LastResolvedBy(actor_id, actor_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["actor_id"] = from_union([from_str, from_none], self.actor_id)
        result["actor_type"] = from_union([from_str, from_none], self.actor_type)
        return result


@dataclass
class Scope:
    name: Optional[str] = None
    description: Optional[str] = None
    is_sensitive: Optional[bool] = None
    token_type: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Scope':
        assert isinstance(obj, dict)
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        is_sensitive = from_union([from_bool, from_none], obj.get("is_sensitive"))
        token_type = from_union([from_str, from_none], obj.get("token_type"))
        return Scope(name, description, is_sensitive, token_type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["is_sensitive"] = from_union([from_bool, from_none], self.is_sensitive)
        result["token_type"] = from_union([from_str, from_none], self.token_type)
        return result


@dataclass
class RestrictedApp:
    app: Optional[App] = None
    scopes: Optional[List[Scope]] = None
    date_updated: Optional[int] = None
    last_resolved_by: Optional[LastResolvedBy] = None

    @staticmethod
    def from_dict(obj: Any) -> 'RestrictedApp':
        assert isinstance(obj, dict)
        app = from_union([App.from_dict, from_none], obj.get("app"))
        scopes = from_union([lambda x: from_list(Scope.from_dict, x), from_none], obj.get("scopes"))
        date_updated = from_union([from_int, from_none], obj.get("date_updated"))
        last_resolved_by = from_union([LastResolvedBy.from_dict, from_none], obj.get("last_resolved_by"))
        return RestrictedApp(app, scopes, date_updated, last_resolved_by)

    def to_dict(self) -> dict:
        result: dict = {}
        result["app"] = from_union([lambda x: to_class(App, x), from_none], self.app)
        result["scopes"] = from_union([lambda x: from_list(lambda x: to_class(Scope, x), x), from_none], self.scopes)
        result["date_updated"] = from_union([from_int, from_none], self.date_updated)
        result["last_resolved_by"] = from_union([lambda x: to_class(LastResolvedBy, x), from_none], self.last_resolved_by)
        return result


@dataclass
class AdminAppsRestrictedListResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    restricted_apps: Optional[List[RestrictedApp]] = None
    response_metadata: Optional[ResponseMetadata] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AdminAppsRestrictedListResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        restricted_apps = from_union([lambda x: from_list(RestrictedApp.from_dict, x), from_none], obj.get("restricted_apps"))
        response_metadata = from_union([ResponseMetadata.from_dict, from_none], obj.get("response_metadata"))
        return AdminAppsRestrictedListResponse(ok, warning, error, needed, provided, restricted_apps, response_metadata)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["restricted_apps"] = from_union([lambda x: from_list(lambda x: to_class(RestrictedApp, x), x), from_none], self.restricted_apps)
        result["response_metadata"] = from_union([lambda x: to_class(ResponseMetadata, x), from_none], self.response_metadata)
        return result


def admin_apps_restricted_list_response_from_dict(s: Any) -> AdminAppsRestrictedListResponse:
    return AdminAppsRestrictedListResponse.from_dict(s)


def admin_apps_restricted_list_response_to_dict(x: AdminAppsRestrictedListResponse) -> Any:
    return to_class(AdminAppsRestrictedListResponse, x)
