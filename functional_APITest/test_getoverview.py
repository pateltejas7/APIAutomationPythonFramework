import allure

from util.framework_utils import FrameworkUtils

@allure.suite("Test Getoverview")
@allure.title("Getoverview API Test")
def test_get_overview():
  #  get_overview = FunctionalParam.get_base_end_point()
  #  print(get_overview)

    response, pretty_response = FrameworkUtils.fire_api_custom(request_method = "GET",
                                              request_url= "/crm-x-orders/api/v1/TLBILMBRINFOGETOVERVIEW",
                                              request_param={"memberNumber": "130373030806"},
                                              request_json=None,
                                              headers=None,
                                              expected_status_code=200
                                                )
    print(pretty_response)
    assert response.json()["resultSet2"][0]["memberName"] == "MICHAEL GORMAN"