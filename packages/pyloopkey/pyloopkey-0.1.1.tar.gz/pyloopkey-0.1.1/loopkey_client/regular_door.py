"""DoorAPI class to handle door in regular integration."""
from typing import Optional

import requests

from loopkey_client.client import Client
from loopkey_client.loopkey_api import LoopkeyAPI
import loopkey_client.const as co
import loopkey_client.exceptions as ex


class DoorAPI(LoopkeyAPI):

    base_url = co.API_REGULAR_DOOR

    def __init__(self, client: Client, door_id: Optional[int] = None):
        """
        Init for Site.
        :param client: Client for authentication.
        :param door_id: Door id.
        """
        self._id = door_id
        super().__init__(client)

    def list_online_doors(self) -> requests.Response:
        """
        Set loopkey availability.
        :return: Response object from requests library with Door state json.
        """
        return self._call_action(requests.get, "online")

    def send_command(
            self,
            command: str,
            **kwargs,
    ) -> requests.Response:
        """
        Send remote command to smartlock.
        :param command: Command can be unlock, schedule_start, schedule_stop, schedule_check,
        custom, restart, update_time and update_timezone.
        :param kwargs: kwargs can contain start, duration and customCommand.
        :return: Response object from requests library with Door command json
        """
        data_dict = {"id": self._id}
        data_dict.update(kwargs)
        return self._call_action(requests.post, f"send/{command}", data=data_dict)

    def check_battery(self,) -> requests.Response:
        """
        Check battery of smartlock.
        :return: Response object from requests library with Door battery json.
        """
        return self._call_action(requests.post, "send/read_battery", data={"id": self._id})

    def list_events(self, action: str) -> requests.Response:
        """
        List events for a door.
        :param action: Action to consider, can be set or unset.
        :return: Response object from requests library with Door events json.
        """
        if action not in co.Actions.__members__.__str__():
            raise ex.NotSupportedError(action)
        params = {
            co.DOOR_ID: self._id,
            "eventKind": "access,management",
            "limit": co.BUFFER
        }
        return self._call_action(requests.get, url=co.API_GET_EVENTS, params=params)

    def set_usercode(
            self,
            passcode: str,
            name: str,
            surname: str,
    ) -> requests.Response:
        """
        Attempt to set a code based on given action.
        :param passcode: Passcode to consider.
        :param name: Name to consider.
        :param surname: Surname to consider.
        :return: Response object from requests library with Door passcode json.
        """
        data_dict = {
            co.DOOR_ID: self._id,
            co.GATEWAY: True,
            co.PASSCODE: passcode,
            co.NAME: name,
            co.SURNAME: surname,
        }
        response = self._call_action(
            requests.post,
            url=co.API_SET_PASSCODE,
            data=data_dict,
        )
        if response.status_code not in (404, 409, 200):
            raise ex.OperationError(
                co.Actions.SET.value, response.json().get("errorDescription"), response.status_code
            )
        return response

    def unset_usercode(self, passcode: str) -> requests.Response:
        """
        Attempt to unset a code based on given action.
        :param passcode: Passcode to consider.
        :return: Response object from requests library with Door passcode json.
        """
        data_dict = {
            co.DOOR_ID: self._id,
            co.GATEWAY: True,
            co.PERMISSION_TYPE: "passcode",
            co.VALUE: passcode
        }
        response = self._call_action(
            requests.post,
            url=co.API_REMOVE_PASSCODE,
            data=data_dict,
        )
        if response.status_code not in (404, 409, 200):
            raise ex.OperationError(
                co.Actions.UNSET.value, response.json().get("errorDescription"), response.status_code
            )
        return response
