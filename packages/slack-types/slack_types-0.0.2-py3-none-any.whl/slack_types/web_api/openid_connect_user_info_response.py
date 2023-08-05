# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = openid_connect_user_info_response_from_dict(json.loads(json_string))

from dataclasses import dataclass
from typing import Optional, Any, TypeVar, Type, cast


T = TypeVar("T")


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
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


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class OpenidConnectUserInfoResponse:
    ok: Optional[bool] = None
    warning: Optional[str] = None
    error: Optional[str] = None
    needed: Optional[str] = None
    provided: Optional[str] = None
    sub: Optional[str] = None
    https_slack_com_user_id: Optional[str] = None
    https_slack_com_team_id: Optional[str] = None
    https_slack_com_enterprise_id: Optional[str] = None
    email: Optional[str] = None
    email_verified: Optional[bool] = None
    date_email_verified: Optional[int] = None
    name: Optional[str] = None
    picture: Optional[str] = None
    given_name: Optional[str] = None
    family_name: Optional[str] = None
    locale: Optional[str] = None
    https_slack_com_team_name: Optional[str] = None
    https_slack_com_team_domain: Optional[str] = None
    https_slack_com_enterprise_name: Optional[str] = None
    https_slack_com_enterprise_domain: Optional[str] = None
    https_slack_com_user_image_24: Optional[str] = None
    https_slack_com_user_image_32: Optional[str] = None
    https_slack_com_user_image_48: Optional[str] = None
    https_slack_com_user_image_72: Optional[str] = None
    https_slack_com_user_image_192: Optional[str] = None
    https_slack_com_user_image_512: Optional[str] = None
    https_slack_com_user_image_1024: Optional[str] = None
    https_slack_com_team_image_34: Optional[str] = None
    https_slack_com_team_image_44: Optional[str] = None
    https_slack_com_team_image_68: Optional[str] = None
    https_slack_com_team_image_88: Optional[str] = None
    https_slack_com_team_image_102: Optional[str] = None
    https_slack_com_team_image_132: Optional[str] = None
    https_slack_com_team_image_230: Optional[str] = None

    @staticmethod
    def from_dict(obj: Any) -> 'OpenidConnectUserInfoResponse':
        assert isinstance(obj, dict)
        ok = from_union([from_bool, from_none], obj.get("ok"))
        warning = from_union([from_str, from_none], obj.get("warning"))
        error = from_union([from_str, from_none], obj.get("error"))
        needed = from_union([from_str, from_none], obj.get("needed"))
        provided = from_union([from_str, from_none], obj.get("provided"))
        sub = from_union([from_str, from_none], obj.get("sub"))
        https_slack_com_user_id = from_union([from_str, from_none], obj.get("https://slack.com/user_id"))
        https_slack_com_team_id = from_union([from_str, from_none], obj.get("https://slack.com/team_id"))
        https_slack_com_enterprise_id = from_union([from_str, from_none], obj.get("https://slack.com/enterprise_id"))
        email = from_union([from_str, from_none], obj.get("email"))
        email_verified = from_union([from_bool, from_none], obj.get("email_verified"))
        date_email_verified = from_union([from_int, from_none], obj.get("date_email_verified"))
        name = from_union([from_str, from_none], obj.get("name"))
        picture = from_union([from_str, from_none], obj.get("picture"))
        given_name = from_union([from_str, from_none], obj.get("given_name"))
        family_name = from_union([from_str, from_none], obj.get("family_name"))
        locale = from_union([from_str, from_none], obj.get("locale"))
        https_slack_com_team_name = from_union([from_str, from_none], obj.get("https://slack.com/team_name"))
        https_slack_com_team_domain = from_union([from_str, from_none], obj.get("https://slack.com/team_domain"))
        https_slack_com_enterprise_name = from_union([from_str, from_none], obj.get("https://slack.com/enterprise_name"))
        https_slack_com_enterprise_domain = from_union([from_str, from_none], obj.get("https://slack.com/enterprise_domain"))
        https_slack_com_user_image_24 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_24"))
        https_slack_com_user_image_32 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_32"))
        https_slack_com_user_image_48 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_48"))
        https_slack_com_user_image_72 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_72"))
        https_slack_com_user_image_192 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_192"))
        https_slack_com_user_image_512 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_512"))
        https_slack_com_user_image_1024 = from_union([from_str, from_none], obj.get("https://slack.com/user_image_1024"))
        https_slack_com_team_image_34 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_34"))
        https_slack_com_team_image_44 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_44"))
        https_slack_com_team_image_68 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_68"))
        https_slack_com_team_image_88 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_88"))
        https_slack_com_team_image_102 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_102"))
        https_slack_com_team_image_132 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_132"))
        https_slack_com_team_image_230 = from_union([from_str, from_none], obj.get("https://slack.com/team_image_230"))
        return OpenidConnectUserInfoResponse(ok, warning, error, needed, provided, sub, https_slack_com_user_id, https_slack_com_team_id, https_slack_com_enterprise_id, email, email_verified, date_email_verified, name, picture, given_name, family_name, locale, https_slack_com_team_name, https_slack_com_team_domain, https_slack_com_enterprise_name, https_slack_com_enterprise_domain, https_slack_com_user_image_24, https_slack_com_user_image_32, https_slack_com_user_image_48, https_slack_com_user_image_72, https_slack_com_user_image_192, https_slack_com_user_image_512, https_slack_com_user_image_1024, https_slack_com_team_image_34, https_slack_com_team_image_44, https_slack_com_team_image_68, https_slack_com_team_image_88, https_slack_com_team_image_102, https_slack_com_team_image_132, https_slack_com_team_image_230)

    def to_dict(self) -> dict:
        result: dict = {}
        result["ok"] = from_union([from_bool, from_none], self.ok)
        result["warning"] = from_union([from_str, from_none], self.warning)
        result["error"] = from_union([from_str, from_none], self.error)
        result["needed"] = from_union([from_str, from_none], self.needed)
        result["provided"] = from_union([from_str, from_none], self.provided)
        result["sub"] = from_union([from_str, from_none], self.sub)
        result["https://slack.com/user_id"] = from_union([from_str, from_none], self.https_slack_com_user_id)
        result["https://slack.com/team_id"] = from_union([from_str, from_none], self.https_slack_com_team_id)
        result["https://slack.com/enterprise_id"] = from_union([from_str, from_none], self.https_slack_com_enterprise_id)
        result["email"] = from_union([from_str, from_none], self.email)
        result["email_verified"] = from_union([from_bool, from_none], self.email_verified)
        result["date_email_verified"] = from_union([from_int, from_none], self.date_email_verified)
        result["name"] = from_union([from_str, from_none], self.name)
        result["picture"] = from_union([from_str, from_none], self.picture)
        result["given_name"] = from_union([from_str, from_none], self.given_name)
        result["family_name"] = from_union([from_str, from_none], self.family_name)
        result["locale"] = from_union([from_str, from_none], self.locale)
        result["https://slack.com/team_name"] = from_union([from_str, from_none], self.https_slack_com_team_name)
        result["https://slack.com/team_domain"] = from_union([from_str, from_none], self.https_slack_com_team_domain)
        result["https://slack.com/enterprise_name"] = from_union([from_str, from_none], self.https_slack_com_enterprise_name)
        result["https://slack.com/enterprise_domain"] = from_union([from_str, from_none], self.https_slack_com_enterprise_domain)
        result["https://slack.com/user_image_24"] = from_union([from_str, from_none], self.https_slack_com_user_image_24)
        result["https://slack.com/user_image_32"] = from_union([from_str, from_none], self.https_slack_com_user_image_32)
        result["https://slack.com/user_image_48"] = from_union([from_str, from_none], self.https_slack_com_user_image_48)
        result["https://slack.com/user_image_72"] = from_union([from_str, from_none], self.https_slack_com_user_image_72)
        result["https://slack.com/user_image_192"] = from_union([from_str, from_none], self.https_slack_com_user_image_192)
        result["https://slack.com/user_image_512"] = from_union([from_str, from_none], self.https_slack_com_user_image_512)
        result["https://slack.com/user_image_1024"] = from_union([from_str, from_none], self.https_slack_com_user_image_1024)
        result["https://slack.com/team_image_34"] = from_union([from_str, from_none], self.https_slack_com_team_image_34)
        result["https://slack.com/team_image_44"] = from_union([from_str, from_none], self.https_slack_com_team_image_44)
        result["https://slack.com/team_image_68"] = from_union([from_str, from_none], self.https_slack_com_team_image_68)
        result["https://slack.com/team_image_88"] = from_union([from_str, from_none], self.https_slack_com_team_image_88)
        result["https://slack.com/team_image_102"] = from_union([from_str, from_none], self.https_slack_com_team_image_102)
        result["https://slack.com/team_image_132"] = from_union([from_str, from_none], self.https_slack_com_team_image_132)
        result["https://slack.com/team_image_230"] = from_union([from_str, from_none], self.https_slack_com_team_image_230)
        return result


def openid_connect_user_info_response_from_dict(s: Any) -> OpenidConnectUserInfoResponse:
    return OpenidConnectUserInfoResponse.from_dict(s)


def openid_connect_user_info_response_to_dict(x: OpenidConnectUserInfoResponse) -> Any:
    return to_class(OpenidConnectUserInfoResponse, x)
