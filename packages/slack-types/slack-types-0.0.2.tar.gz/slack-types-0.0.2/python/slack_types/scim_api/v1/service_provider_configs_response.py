# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = service_provider_configs_response_from_dict(json.loads(json_string))

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


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class AuthenticationScheme:
    type: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    spec_url: Optional[str] = None
    primary: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'AuthenticationScheme':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        name = from_union([from_str, from_none], obj.get("name"))
        description = from_union([from_str, from_none], obj.get("description"))
        spec_url = from_union([from_str, from_none], obj.get("specUrl"))
        primary = from_union([from_bool, from_none], obj.get("primary"))
        return AuthenticationScheme(type, name, description, spec_url, primary)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["name"] = from_union([from_str, from_none], self.name)
        result["description"] = from_union([from_str, from_none], self.description)
        result["specUrl"] = from_union([from_str, from_none], self.spec_url)
        result["primary"] = from_union([from_bool, from_none], self.primary)
        return result


@dataclass
class Bulk:
    supported: Optional[bool] = None
    max_operations: Optional[int] = None
    max_payload_size: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Bulk':
        assert isinstance(obj, dict)
        supported = from_union([from_bool, from_none], obj.get("supported"))
        max_operations = from_union([from_int, from_none], obj.get("maxOperations"))
        max_payload_size = from_union([from_int, from_none], obj.get("maxPayloadSize"))
        return Bulk(supported, max_operations, max_payload_size)

    def to_dict(self) -> dict:
        result: dict = {}
        result["supported"] = from_union([from_bool, from_none], self.supported)
        result["maxOperations"] = from_union([from_int, from_none], self.max_operations)
        result["maxPayloadSize"] = from_union([from_int, from_none], self.max_payload_size)
        return result


@dataclass
class ChangePassword:
    supported: Optional[bool] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ChangePassword':
        assert isinstance(obj, dict)
        supported = from_union([from_bool, from_none], obj.get("supported"))
        return ChangePassword(supported)

    def to_dict(self) -> dict:
        result: dict = {}
        result["supported"] = from_union([from_bool, from_none], self.supported)
        return result


@dataclass
class Filter:
    supported: Optional[bool] = None
    max_results: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Filter':
        assert isinstance(obj, dict)
        supported = from_union([from_bool, from_none], obj.get("supported"))
        max_results = from_union([from_int, from_none], obj.get("maxResults"))
        return Filter(supported, max_results)

    def to_dict(self) -> dict:
        result: dict = {}
        result["supported"] = from_union([from_bool, from_none], self.supported)
        result["maxResults"] = from_union([from_int, from_none], self.max_results)
        return result


@dataclass
class ServiceProviderConfigsResponse:
    authentication_schemes: Optional[List[AuthenticationScheme]] = None
    patch: Optional[ChangePassword] = None
    bulk: Optional[Bulk] = None
    filter: Optional[Filter] = None
    change_password: Optional[ChangePassword] = None
    sort: Optional[ChangePassword] = None
    etag: Optional[ChangePassword] = None
    xml_data_format: Optional[ChangePassword] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ServiceProviderConfigsResponse':
        assert isinstance(obj, dict)
        authentication_schemes = from_union([lambda x: from_list(AuthenticationScheme.from_dict, x), from_none], obj.get("authenticationSchemes"))
        patch = from_union([ChangePassword.from_dict, from_none], obj.get("patch"))
        bulk = from_union([Bulk.from_dict, from_none], obj.get("bulk"))
        filter = from_union([Filter.from_dict, from_none], obj.get("filter"))
        change_password = from_union([ChangePassword.from_dict, from_none], obj.get("changePassword"))
        sort = from_union([ChangePassword.from_dict, from_none], obj.get("sort"))
        etag = from_union([ChangePassword.from_dict, from_none], obj.get("etag"))
        xml_data_format = from_union([ChangePassword.from_dict, from_none], obj.get("xmlDataFormat"))
        return ServiceProviderConfigsResponse(authentication_schemes, patch, bulk, filter, change_password, sort, etag, xml_data_format)

    def to_dict(self) -> dict:
        result: dict = {}
        result["authenticationSchemes"] = from_union([lambda x: from_list(lambda x: to_class(AuthenticationScheme, x), x), from_none], self.authentication_schemes)
        result["patch"] = from_union([lambda x: to_class(ChangePassword, x), from_none], self.patch)
        result["bulk"] = from_union([lambda x: to_class(Bulk, x), from_none], self.bulk)
        result["filter"] = from_union([lambda x: to_class(Filter, x), from_none], self.filter)
        result["changePassword"] = from_union([lambda x: to_class(ChangePassword, x), from_none], self.change_password)
        result["sort"] = from_union([lambda x: to_class(ChangePassword, x), from_none], self.sort)
        result["etag"] = from_union([lambda x: to_class(ChangePassword, x), from_none], self.etag)
        result["xmlDataFormat"] = from_union([lambda x: to_class(ChangePassword, x), from_none], self.xml_data_format)
        return result


def service_provider_configs_response_from_dict(s: Any) -> ServiceProviderConfigsResponse:
    return ServiceProviderConfigsResponse.from_dict(s)


def service_provider_configs_response_to_dict(x: ServiceProviderConfigsResponse) -> Any:
    return to_class(ServiceProviderConfigsResponse, x)
