# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = bot_changed_event_from_dict(json.loads(json_string))

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
class Icons:
    image_36: Optional[str] = None
    image_48: Optional[str] = None
    image_72: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Icons':
        assert isinstance(obj, dict)
        image_36 = from_union([from_str, from_none], obj.get("image_36"))
        image_48 = from_union([from_str, from_none], obj.get("image_48"))
        image_72 = from_union([from_str, from_none], obj.get("image_72"))
        return Icons(image_36, image_48, image_72)

    def to_dict(self) -> dict:
        result: dict = {}
        result["image_36"] = from_union([from_str, from_none], self.image_36)
        result["image_48"] = from_union([from_str, from_none], self.image_48)
        result["image_72"] = from_union([from_str, from_none], self.image_72)
        return result


@dataclass
class Bot:
    id: Optional[str] = None
    app_id: Optional[str] = None
    name: Optional[str] = None
    icons: Optional[Icons] = None

    @staticmethod
    def from_dict(obj: Any) -> 'Bot':
        assert isinstance(obj, dict)
        id = from_union([from_str, from_none], obj.get("id"))
        app_id = from_union([from_str, from_none], obj.get("app_id"))
        name = from_union([from_str, from_none], obj.get("name"))
        icons = from_union([Icons.from_dict, from_none], obj.get("icons"))
        return Bot(id, app_id, name, icons)

    def to_dict(self) -> dict:
        result: dict = {}
        result["id"] = from_union([from_str, from_none], self.id)
        result["app_id"] = from_union([from_str, from_none], self.app_id)
        result["name"] = from_union([from_str, from_none], self.name)
        result["icons"] = from_union([lambda x: to_class(Icons, x), from_none], self.icons)
        return result


@dataclass
class BotChangedEvent:
    type: Optional[str] = None
    bot: Optional[Bot] = None

    @staticmethod
    def from_dict(obj: Any) -> 'BotChangedEvent':
        assert isinstance(obj, dict)
        type = from_union([from_str, from_none], obj.get("type"))
        bot = from_union([Bot.from_dict, from_none], obj.get("bot"))
        return BotChangedEvent(type, bot)

    def to_dict(self) -> dict:
        result: dict = {}
        result["type"] = from_union([from_str, from_none], self.type)
        result["bot"] = from_union([lambda x: to_class(Bot, x), from_none], self.bot)
        return result


def bot_changed_event_from_dict(s: Any) -> BotChangedEvent:
    return BotChangedEvent.from_dict(s)


def bot_changed_event_to_dict(x: BotChangedEvent) -> Any:
    return to_class(BotChangedEvent, x)
