from http.client import responses

from config.api_config import APIURLS
from functional_APITest.functional_param import FunctionalParam
from request_response.request.gorest import GoRest
from util.common_util import commonUtility
from util.framework_utils import FrameworkUtils


def test_url():
    URL = FunctionalParam.get_base_end_point()
    print("URL",  URL)

    GET_USER = APIURLS.Get_User
    print("GET_USER", GET_USER)

    Ger_User_ID = APIURLS.get_user_userid("123456")
    print("Ger_User_ID", Ger_User_ID)

    headers = commonUtility.get_custom_header()
    print("headers", headers)

    random_email=commonUtility.get_unique_email()
    print("random_email", random_email)

    json_req = GoRest.Create_User
    print("json_req", json_req)

    response = FrameworkUtils.fire_api_custom("GET", request_url=GET_USER, headers=headers)
    print("response", response.json())




test_url()