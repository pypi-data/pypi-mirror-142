# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = resources_removed_event_from_dict(json.loads(json_string))

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


@dataclass
class Grant:
    type: Optional[str] = None
    resource_id: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Grant':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        resource_id = from_union([from_str, from_none], obj.get("resource_id"))
        return Grant(type, resource_id)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["resource_id"] = from_union([from_str, from_none], self.resource_id)
        return result


@dataclass
class ResourceResource:
    type: Optional[str] = None
    grant: Optional[Grant] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceResource':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        grant = from_union([Grant.from_dict, from_none], obj.get("grant"))
        return ResourceResource(type, grant)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["grant"] = from_union([lambda x: to_class(Grant, x), from_none], self.grant)
        return result


@dataclass
class ResourceElement:
    resource: Optional[ResourceResource] = None
    scopes: Optional[List[str]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResourceElement':
        assert isinstance(obj, dict)
        resource = from_union([ResourceResource.from_dict, from_none], obj.get("resource"))
        scopes = from_union([lambda x: from_list(from_str, x), from_none], obj.get("scopes"))
        return ResourceElement(resource, scopes)

    def to_dict(self) -> dict:
        result: dict = {}
        result["resource"] = from_union([lambda x: to_class(ResourceResource, x), from_none], self.resource)
        result["scopes"] = from_union([lambda x: from_list(from_str, x), from_none], self.scopes)
        return result


@dataclass
class ResourcesRemovedEvent:
    type: Optional[str] = None
    resources: Optional[List[ResourceElement]] = None

    @staticmethod
    def from_dict(obj: Any) -> 'ResourcesRemovedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        resources = from_union([lambda x: from_list(ResourceElement.from_dict, x), from_none], obj.get("resources"))
        return ResourcesRemovedEvent(type, resources)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["resources"] = from_union([lambda x: from_list(lambda x: to_class(ResourceElement, x), x), from_none], self.resources)
        return result


def resources_removed_event_from_dict(s: Any) -> ResourcesRemovedEvent:
    return ResourcesRemovedEvent.from_dict(s)


def resources_removed_event_to_dict(x: ResourcesRemovedEvent) -> Any:
    return to_class(ResourcesRemovedEvent, x)
