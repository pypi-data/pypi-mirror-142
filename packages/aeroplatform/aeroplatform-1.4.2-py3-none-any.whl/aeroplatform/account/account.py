import requests
import os
import json
import logging
import boto3

from hashlib import sha256
from pathlib import Path
from enum import Enum, unique
from ..utils import ROOT_DIR

logger = logging.getLogger(__name__)


@unique
class ComputeStatus(Enum):
    NO_VALUE = 0
    INIT = 1
    CREATING = 2
    CREATED = 3
    FAILED = 4


class UserNotFound(Exception):
    ...


class IncorrectPassword(Exception):
    ...

class FreeTrialEnded(Exception):
    ...

class ProvisionError(Exception):

    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code


class Account:

    JSON_CONFIG = json.load(open(os.path.join(ROOT_DIR, "config.json"), "r"))
    BASE_URL = JSON_CONFIG['BASE_API_URL']
    CLIENT_ID = JSON_CONFIG['USER_POOL_CLIENT_ID']
    PROVISION_URL = f"{BASE_URL}/compute/config"

    def __init__(self, email: str, password: str):

        self._email = email
        self._password = password
        self._auth_token = None
        self._id_token = None
        self._user_home = str(Path.home())

    def login(self):

        cognito = boto3.client('cognito-idp', region_name='eu-west-1')

        try:
            logger.debug("Account::login()")
            response = cognito.initiate_auth(
                AuthFlow="USER_PASSWORD_AUTH",
                AuthParameters={
                    "USERNAME": self._email,
                    "PASSWORD": self._password
                },
                ClientId=self.CLIENT_ID
            )

        except cognito.exceptions.UserNotFoundException:
            logger.debug('User Not Found')
            raise UserNotFound
        except cognito.exceptions.NotAuthorizedException as e:
            if 'User is disabled' in str(e):
                raise FreeTrialEnded
            logger.debug('Incorrect Password')
            raise IncorrectPassword
        except Exception as e:
            logger.debug('Client Error: {e}')
            raise

        logger.debug(f'initiate_auth RESPONSE: {response}')

        if 'AuthenticationResult' not in response:
            raise Exception("Error logging in")

        logger.debug(
            f"Auth Token: {response['AuthenticationResult']['AccessToken']}")

        self._auth_token = response['AuthenticationResult']['AccessToken']
        self._refresh_token = response['AuthenticationResult']['RefreshToken']

    def provision(self, is_first_provision: bool) -> ComputeStatus:

        data = dict(
            company="solo",
            project="default"
        )

        logger.debug(f"Account::provision(): {data}")

        r = requests.post(self.PROVISION_URL,
                          json=data,
                          headers={
                              "x-api-key": self._auth_token
                          }
                          )

        logger.debug(f'Provision Status Code: {r.status_code}')

        if r.status_code == 202:
            return ComputeStatus.INIT
        elif r.status_code == 207:
            return ComputeStatus.CREATING
        elif r.status_code != 200:
            logger.debug(r.text)
            raise ProvisionError(r.text, r.status_code)

        response_data = r.json()

        if is_first_provision:
            self.login()

        response_data['config']['AERO_REFRESH_TOKEN'] = self._refresh_token
        response_data['config']['USER_POOL_CLIENT_ID'] = self.CLIENT_ID

        # Create Metaflow directory
        if not os.path.exists(f"{self._user_home}/.metaflowconfig"):
            os.mkdir(f"{self._user_home}/.metaflowconfig")

        with open(f"{self._user_home}/.metaflowconfig/config.json", 'w', encoding='utf-8') as f:
            json.dump(response_data['config'], f, ensure_ascii=False, indent=4)

        return ComputeStatus.CREATED

    @staticmethod
    def _hash(password):

        return sha256(password.strip()).hexdigest()
