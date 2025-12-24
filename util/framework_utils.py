import json

import pytest
import requests

from config.api_config import Base_URL

class FrameworkUtils:
    @staticmethod
    def fire_api_custom(request_method = "GET",
                                    request_url= None,
                                    request_param=None,
                                    request_json= None,
                                    headers= None,
                        expected_status_code= 200,
                         ):

        full_url= Base_URL + request_url

        common_headers = {
            "clientapplication": "PEGA_CRM",
            "sourceenvironment": "GOLDNNE",
            "apiKey": "lMgkZhcqAkT6B5OLJj6m1MWdR4mYbFBW",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        if headers:
            common_headers.update(headers)

        response = requests.request(method=request_method,
                                    url = full_url,
                                    params=request_param,
                                    json= request_json,
                                    headers= common_headers,
                                    )
      #  try:
      #      assert  response.status_code == expected_status_code, f"API call failed expected {expected_status_code} but got {response.status_code}"
      #      return response.json()
       # except:
       #     pytest.fail(f"API call failed expected {expected_status_code} but got {response.status_code}")

        try:
            formatted_response = json.dumps(response.json(), indent=4)
        except ValueError:
            formatted_response = response.text

        if response.status_code != expected_status_code:
            pytest.fail(
                f"API call failed\n"
                f"URL: {response.request.url}\n"
                f"Expected: {expected_status_code}\n"
                f"Actual: {response.status_code}\n"
                f"Response:\n{formatted_response}"

            )

        return response, formatted_response