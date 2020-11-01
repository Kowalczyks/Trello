import requests
from backend.helpers.logger import Logger


class RestApiHelper:

    @staticmethod
    def post_call(endpoint, payload=None, headers=None):
        """
        :param endpoint:
        :param payload:
        :param headers:
        :return:
        """
        if not headers:
            headers = {"Content-Type": "application/json"}
        Logger.LogInfo("making POST request to " + endpoint)
        response = requests.post(endpoint, payload, headers=headers)
        Logger.LogInfo(f"received response {response.text}")

        return response

    @staticmethod
    def get_call(endpoint, headers):
        """
        :param endpoint:
        :param headers:
        :return:
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        response = requests.get(endpoint, headers=headers)
        Logger.LogInfo(f"received response {response.text}")

        return response

    @staticmethod
    def delete_call(endpoint, headers):
        """
        :param endpoint:
        :param headers:
        :return:
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        Logger.LogInfo("making DEL request to " + endpoint)
        response = requests.delete(endpoint, headers=headers)
        Logger.LogInfo(f"received response {response.text}")

        return response

    @staticmethod
    def put_call(endpoint, headers):
        """
        :param endpoint:
        :param headers:
        :return:
        """
        if not headers:
            headers = {"Content-Type": "application/json"}

        Logger.LogInfo("making PUT request to " + endpoint)
        response = requests.put(endpoint, headers=headers)
        Logger.LogInfo(f"received response {response.text}")

        return response
