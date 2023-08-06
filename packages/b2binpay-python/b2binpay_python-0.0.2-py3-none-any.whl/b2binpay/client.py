import datetime
import json
from typing import Dict, Optional, List

import aiohttp
import asyncio
import requests
import hashlib
import hmac
from uuid import uuid4
from loguru import logger

from .exeptions import B2BAPIException, B2BRequestException

TEST_MODE = True


def convert_dt_to_datetime(dt) -> datetime.datetime:
    dt = dt.replace("T", " ").replace("Z", " ").split('.')[0]
    return datetime.datetime.strptime(dt, '%Y-%m-%d %H:%M:%S')


class BaseClient:
    API_URL = "https://api.b2binpay.com"
    TEST_API_URL = "https://api-sandbox.b2binpay.com"

    def __init__(
            self, api_key: Optional[str] = None, api_secret: Optional[str] = None
    ):
        """B2BinPay API Client constructor

        :param api_key: Api Key
        :type api_key: str.
        :param api_secret: Api Secret
        :type api_secret: str.
        """
        self._API_KEY = api_key
        self._API_SECRET = api_secret
        self.session = self._init_session()

    def _get_data_connection(self, headers):
        url = self._create_api_uri("token/")

        # Request basic information
        data = {
            "data": {
                "type": "auth-token",
                "attributes": {
                    "login": self._API_KEY,
                    "password": self._API_SECRET,
                },
            },
        }
        data = requests.post(url, headers=headers, json=data)
        data = data.json()

        if not data["data"]:
            raise Exception("Connection data invalid")

        self._is_connected = True
        self._access_token = data["data"]["attributes"]["access"]
        self._refresh_token = data["data"]["attributes"]["refresh"]
        self._access_expired_at = data["data"]["attributes"]["access_expired_at"]
        self._refresh_expired_at = data["data"]["attributes"]["refresh_expired_at"]
        self._is_2fa_confirmed = data["data"]["attributes"]["is_2fa_confirmed"]
        self._meta = data["meta"]
        self._message = data["meta"]["time"] + data["data"]["attributes"]["refresh"]
        self._response_sign = data["meta"]["sign"]
        self._crypted = hashlib.sha256(self._API_KEY.encode() + self._API_SECRET.encode()).hexdigest().encode()
        self._calculated_sign = hmac.new(self._message.encode(), self._crypted, hashlib.sha256).hexdigest()

        return data

    def _validate_connection(self, expired_at):
        dt_now = datetime.datetime.now()
        expired_at = convert_dt_to_datetime(expired_at)
        if dt_now > expired_at:
            logger.error('Connection not valid')
            return False
        return True

    def _init_session(self):
        raise NotImplementedError

    def _create_api_uri(self, path: str) -> str:
        url = self.API_URL if not TEST_MODE else self.TEST_API_URL
        return url + "/" + path


class AsyncClient(BaseClient):

    def __init__(
            self, api_key: Optional[str] = None, api_secret: Optional[str] = None, loop=None
    ):
        self.loop = loop or asyncio.get_event_loop()
        super().__init__(api_key, api_secret)

    @classmethod
    async def create(
            cls, api_key: Optional[str] = None, api_secret: Optional[str] = None):

        self = cls(api_key, api_secret)

        return self

    def _init_session(self) -> aiohttp.ClientSession:

        headers = {
            "content-type": "application/vnd.api+json"
        }

        self._get_data_connection(headers)

        headers["authorization"] = f"Bearer {self._access_token}"
        headers["idempotency-key"] = f"{str(uuid4())}"

        session = aiohttp.ClientSession(
            loop=self.loop,
            headers=headers
        )

        return session

    async def refresh(self):

        url = self._create_api_uri("token/refresh/")

        headers = {
            "content-type": "application/vnd.api+json"
        }

        data = {
            "data": {
                "type": "auth-token",
                "attributes": {
                    'refresh': f"{self._refresh_token}",
                },
            },
        }
        data = requests.post(url, headers=headers, json=data)
        data = data.json()

        self._access_token = data["data"]["attributes"]["access"]
        self._refresh_token = data["data"]["attributes"]["refresh"]
        self._access_expired_at = data["data"]["attributes"]["access_expired_at"]
        self._refresh_expired_at = data["data"]["attributes"]["refresh_expired_at"]
        self._is_2fa_confirmed = data["data"]["attributes"]["is_2fa_confirmed"]

        return self._refresh_token

    async def close_connection(self):
        if self.session:
            assert self.session
            await self.session.close()

    async def _request(self, method, uri: str, data: dict):
        logger.info(f"Try to make {method} request to url: {uri} with data={data}")

        # validate connaction
        # if not self._validate_connection(self._access_expired_at):
        #     self.session = self._init_session()

        # Convert data if special methods called
        for i in ['payout', 'deposit']:
            if i in uri:
                data = json.dumps(data)

        try:
            if method == 'post':
                async with self.session.post(uri, data=data) as resp:
                    return await self._handle_response(resp)
            elif method == 'get':
                async with self.session.get(uri, data=data) as resp:
                    return await self._handle_response(resp)
        except Exception as e:
            logger.exception(e)

    async def _handle_response(self, response: aiohttp.ClientResponse):
        if not str(response.status).startswith("2"):
            await self.close_connection()
            raise B2BAPIException(response, response.status, await response.text())
        try:
            text = await response.text()
            logger.info(f"Successfull! response: {text}\n\n")
            return await response.json()
        except ValueError:
            txt = await response.text()
            await self.close_connection()
            raise B2BRequestException(f"Invalid Response: {txt}")

    async def _request_api(self, method, path, **kwargs):
        uri = self._create_api_uri(path)
        return await self._request(method, uri, kwargs)

    async def _get(self, path, **kwargs) -> Dict:
        return await self._request_api("get", path, **kwargs)

    async def _post(self, path, **kwargs) -> Dict:
        return await self._request_api("post", path, **kwargs)

    # Endpoints
    async def get_wallets(self) -> List:
        return await self._get(f"wallet")

    async def get_wallet(self, wallet_id: str = None) -> Dict:
        return await self._get(f"wallet/{wallet_id}")

    async def get_currencies(self) -> List:
        return await self._get(f"currency")

    async def get_currency(self, currency_id: str) -> Dict:
        return await self._get(f"currency/{currency_id}")

    async def get_transfers(self) -> List:
        return await self._get(f"transfer")

    async def get_transfer(self, transfer_id: str) -> Dict:
        """
        Transfer_id can be str of transfer id or filter string
        exapmle: ?%5Bop_type%5D=2&filter%5Bop_id%5D=100
        """
        return await self._get(f"transfer/{transfer_id}")

    async def get_rates(self, filter_str) -> List:
        """
        :param filter_str: example: filter[left]=BTC
        """
        if 'filter' not in filter_str:
            await self.close_connection()
            raise Exception('Incorrect filter format. Example: "filter[left]=BTC"')

        return await self._get(f"rates/?{filter_str}")

    async def get_deposit(self, deposit_id) -> List:
        return await self._get(f"deposit/{deposit_id}")

    async def get_deposits(self) -> Dict:
        return await self._get(f"deposit")

    async def create_deposit(self,
                             wallet_id,
                             label="",
                             tracking_id=""
                             ,
                             callbback_url="",
                             confirmations_needed=1
                             ):

        data = {
            "type": "deposit",
            "attributes": {
                "label": label,
                "tracking_id": tracking_id,
                "confirmations_needed": confirmations_needed,
                "callback_url": callbback_url,
            },
            "relationships": {
                "wallet": {
                    "data": {
                        "type": "wallet",
                        "id": wallet_id,
                    },
                },
            },
        }
        return await self._post("deposit", data=data)

    async def get_invoice(self, invoice_id=None):
        return await self._get(f"deposit/{invoice_id}")

    async def create_invoice(self,
                             wallet_id,
                             label="",
                             tracking_id="",
                             callbback_url="",
                             confirmations_needed=1,
                             currency_id="",
                             ):

        data = {
            "type": "deposit",
            "attributes": {
                "label": label,
                "tracking_id": tracking_id,
                "confirmations_needed": confirmations_needed,
                "callback_url": callbback_url
            },
            "relationships": {
                "currency": {
                    "data": {
                        "type": "currency",
                        "id": currency_id
                    }
                },
                "wallet": {
                    "data": {
                        "type": "wallet",
                        "id": wallet_id
                    }
                }
            }
        }

        return await self._post("deposit", data=data)

    async def get_payout(self, payout_id=None):
        return await self._get(f"payout/{payout_id}")

    async def create_payout(self,
                            wallet_id,
                            label="",
                            tracking_id="",
                            address="",
                            amount=0,
                            fee_amount=0,
                            callbback_url="",
                            confirmations_needed=1,
                            currency_id="",
                            ):

        if fee_amount in [0, "low", "medium", "high"]:
            fee_amount = "medium" if fee_amount == 0 else fee_amount

            resp = await self.payout_fee(wallet_id, address, amount, currency_id)
            fee_amount = resp.get("data") \
                .get("attributes") \
                .get("fee") \
                .get(fee_amount)

        data = {
            'type': 'payout',
            'attributes': {
                'amount': amount,
                'address': address,
                'fee_amount': fee_amount,
                "label": label,
                'tracking_id': tracking_id,
                'confirmations_needed': confirmations_needed,
                'callback_url': callbback_url,
            },
            'relationships': {
                'wallet': {
                    'data': {
                        'type': 'wallet',
                        'id': wallet_id,
                    },
                },
                'currency': {
                    'data': {
                        'type': 'currency',
                        'id': currency_id,
                    },
                },
            },
        }

        return await self._post("payout", data=data)

    async def payout_fee(self, wallet_id, address, amount, currency_id):

        data = {
            'type': 'payout-calculation',
            'attributes': {
                'amount': amount,
                'to_address': address,
            },
            'relationships': {
                'wallet': {
                    'data': {
                        'type': 'wallet',
                        'id': wallet_id,
                    }
                },
                'currency': {
                    'data': {
                        'type': 'currency',
                        'id': currency_id,
                    },
                },
            },
        }
        return await self._post(f"payout/calculate", data=data)
