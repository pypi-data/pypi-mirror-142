# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = groups_response_from_dict(json.loads(json_string))

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
class Errors:
    description: Optional[str] = None
    code: Optional[int] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Errors':
        assert isinstance(obj, dict)
        description = from_union([from_str, from_none], obj.get("description"))
        code = from_union([from_int, from_none], obj.get("code"))
        return Errors(description, code)

    def to_dict(self) -> dict:
        result: dict = {}
        result["description"] = from_union([from_str, from_none], self.description)
        result["code"] = from_union([from_int, from_none], self.code)
        return result


@dataclass
class Member:
    value: Optional[str] = None
    display: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Member':
        assert isinstance(obj, dict)
        value = from_union([from_str, from_none], obj.get("value"))
        display = from_union([from_str, from_none], obj.get("display"))
        return Member(value, display)

    def to_dict(self) -> dict:
        result: dict = {}
        result["value"] = from_union([from_str, from_none], self.value)
        result["display"] = from_union([from_str, from_none], self.display)
        return result


@dataclass
class Meta:
    created: Optional[str] = None
    location: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Meta':
        assert isinstance(obj, dict)
        created = from_union([from_str, from_none], obj.get("created"))
        location = from_union([from_str, from_none], obj.get("location"))
        return Meta(created, location)

    def to_dict(self) -> dict:
        result: dict = {}
        result["created"] = from_union([from_str, from_none], self.created)
        result["location"] = from_union([from_str, from_none], self.location)
        return result


@dataclass
class Resource:
    schemas: Optional[List[str]] = None
    id: Optional[str] = None
    display_name: Optional[str] = None
    members: Optional[List[Member]] = None
    meta: Optional[Meta] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Resource':
        assert isinstance(obj, dict)
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        id = from_union([from_str, from_none], obj.get("id"))
        display_name = from_union([from_str, from_none], obj.get("displayName"))
        members = from_union([lambda x: from_list(Member.from_dict, x), from_none], obj.get("members"))
        meta = from_union([Meta.from_dict, from_none], obj.get("meta"))
        return Resource(schemas, id, display_name, members, meta)

    def to_dict(self) -> dict:
        result: dict = {}
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["id"] = from_union([from_str, from_none], self.id)
        result["displayName"] = from_union([from_str, from_none], self.display_name)
        result["members"] = from_union([lambda x: from_list(lambda x: to_class(Member, x), x), from_none], self.members)
        result["meta"] = from_union([lambda x: to_class(Meta, x), from_none], self.meta)
        return result


@dataclass
class GroupsResponse:
    total_results: Optional[int] = None
    items_per_page: Optional[int] = None
    start_index: Optional[int] = None
    schemas: Optional[List[str]] = None
    resources: Optional[List[Resource]] = None
    errors: Optional[Errors] = None

    @staticmethod
    def from_dict(obj: Any) -> 'GroupsResponse':
        assert isinstance(obj, dict)
        total_results = from_union([from_int, from_none], obj.get("totalResults"))
        items_per_page = from_union([from_int, from_none], obj.get("itemsPerPage"))
        start_index = from_union([from_int, from_none], obj.get("startIndex"))
        schemas = from_union([lambda x: from_list(from_str, x), from_none], obj.get("schemas"))
        resources = from_union([lambda x: from_list(Resource.from_dict, x), from_none], obj.get("Resources"))
        errors = from_union([Errors.from_dict, from_none], obj.get("Errors"))
        return GroupsResponse(total_results, items_per_page, start_index, schemas, resources, errors)

    def to_dict(self) -> dict:
        result: dict = {}
        result["totalResults"] = from_union([from_int, from_none], self.total_results)
        result["itemsPerPage"] = from_union([from_int, from_none], self.items_per_page)
        result["startIndex"] = from_union([from_int, from_none], self.start_index)
        result["schemas"] = from_union([lambda x: from_list(from_str, x), from_none], self.schemas)
        result["Resources"] = from_union([lambda x: from_list(lambda x: to_class(Resource, x), x), from_none], self.resources)
        result["Errors"] = from_union([lambda x: to_class(Errors, x), from_none], self.errors)
        return result


def groups_response_from_dict(s: Any) -> GroupsResponse:
    return GroupsResponse.from_dict(s)


def groups_response_to_dict(x: GroupsResponse) -> Any:
    return to_class(GroupsResponse, x)
