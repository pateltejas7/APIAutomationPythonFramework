import json


class FunctionalParam:
    @staticmethod
    def get_base_end_point():
        with open("C:/Users/patel/PycharmProjects/APIAutomationPytest/config/endpoints.json") as json_file:
            properties = json.load(json_file)
            env= properties["enviroment"]["env"]
            return properties[env]["base_url"]

