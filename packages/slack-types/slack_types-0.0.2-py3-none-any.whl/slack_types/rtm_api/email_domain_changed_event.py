# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = email_domain_changed_event_from_dict(json.loads(json_string))

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


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class EmailDomainChangedEvent:
    type: Optional[str] = None
    email_domain: Optional[str] = None
    event_ts: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'EmailDomainChangedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        email_domain = from_union([from_str, from_none], obj.get("email_domain"))
        event_ts = from_union([from_str, from_none], obj.get("event_ts"))
        return EmailDomainChangedEvent(type, email_domain, event_ts)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["email_domain"] = from_union([from_str, from_none], self.email_domain)
        result["event_ts"] = from_union([from_str, from_none], self.event_ts)
        return result


def email_domain_changed_event_from_dict(s: Any) -> EmailDomainChangedEvent:
    return EmailDomainChangedEvent.from_dict(s)


def email_domain_changed_event_to_dict(x: EmailDomainChangedEvent) -> Any:
    return to_class(EmailDomainChangedEvent, x)
