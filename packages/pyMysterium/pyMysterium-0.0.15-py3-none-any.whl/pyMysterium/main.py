import io
import requests
import json
from .endpoints import EndPoints
from .errors import *
from .models import Proposals
import base64
import subprocess


class Mysterium:
    """Base class for Mysterium-API
    Initiallise the class
    ```python
    myst = Mysterium()
    ```
    ## Accepts the following arguements
    No. | Arguement | Description
    --- | --- | ---
    1. | `protocol` | Either `http` or `https`
    """

    def __init__(self, protocol: str = "http", hostname: str = "localhost", port: int = 4050, slug: str = "", get_identity: bool = True) -> None:
        self.base_url = f"{protocol}://{hostname}:{port}/{slug}/"
        self.urls = EndPoints(self.base_url)
        self.http_timeout = 10
        self.current_identity = self.get_current_identity() if get_identity else None
        self.channel_id = self.get_current_identity_details().get(
            "channel_address") if get_identity else None

    def __execute(self, command: str):
        return subprocess.Popen(command.split(), stdout=subprocess.PIPE).communicate()

    def get_access_list(self) -> str:
        response = requests.get(self.urls.access_policies)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_connection_status(self) -> str:
        """Returns current connection status"""
        response = requests.get(self.urls.connection)
        if response.status_code == 200:
            return json.loads(response.content).get("status")
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_current_identity(self, passphrase: str = '', id: str = None) -> str:
        """Returns current identity
`passphrase` is the password used to unlock identity
**Note** leave it as default."""
        data = {
            "id": id,
            "passphrase": passphrase
        }
        response = requests.put(self.urls.current_identity, json=data)
        if response.status_code == 200:
            self.current_identity = json.loads(response.content)["id"]
            return self.current_identity
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 422:
            raise ParameterValidationError(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_identities(self) -> dict:
        """Returns a dictionary with identities"""
        response = requests.get(self.urls.identities)
        if response.status_code == 200:
            return json.loads(response.content).get("identities")
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def create_new_identity(self, passphrase: str = '') -> str:
        """Creates a new identity and `passphrase` is the password used to unlock the identity
**Note: leave it default"""
        data = {
            "passphrase": passphrase
        }
        response = requests.post(self.urls.identities, json=data)
        if response.status_code == 200:
            return json.loads(response.content)["id"]
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 422:
            raise ParameterValidationError(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_current_identity_details(self) -> dict:
        data = {
            "id": self.current_identity
        }
        response = requests.get(self.urls.get_identity.format(**data))
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_beneficiary_address(self) -> str:
        data = {
            "id": self.current_identity
        }
        response = requests.get(self.urls.beneficiary_address.format(**data))
        if response.status_code == 200:
            return json.loads(response.content)["beneficiary"]
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def register_current_identity(self, beneficiary: str = None, referral_token: str = None, stake: int = None) -> int:
        """Registers current identity"""
        registration_status = self.registration_status()
        if registration_status == "InProgress":
            raise RegistrationAlreadyInProgressError(
                f"Registration already in progress. Top-up your node {self.current_identity} to continue.")

        json_data = {
            "beneficiary": beneficiary,
            "referral_token": referral_token,
            "stake": stake
        }
        data = {
            "id": self.current_identity
        }
        response = requests.post(
            self.urls.register_identity.format(**data), json=json_data)
        if response.status_code == 200:
            return response.status_code
        if response.status_code == 202:
            return response.status_code
        elif response.status_code == 409:
            raise RegistrationAlreadyInProgressError(
                json.loads(response.content))
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 500:
            if "in progress" in response.content.decode():
                raise RegistrationAlreadyInProgressError(
                    json.loads(response.content))
            raise InternalServerError(json.loads(response.content))

    def registration_status(self):
        """Returns registration status"""
        data = {
            "id": self.current_identity
        }
        response = requests.get(self.urls.registration_status.format(**data))
        if response.status_code == 200:
            return json.loads(response.content)["status"]
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def is_identity_registered(self):
        data = {
            "id": self.current_identity
        }
        response = requests.get(self.urls.registration_status.format(**data))
        if response.status_code == 200:
            return json.loads(response.content)["registered"]
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def import_identity(self, current_passphrase: str, backed_up_data: dict, new_passphrase: str = "", set_default: bool = True) -> str:
        """Function to import an exported identity
        `current_passphrase` is the password used to encrypt the export
        `backed_up_data` is the json formatted exported data
        `new_passphrase` is the password used to unlock identity after importing
        `set_default` when `True` the imported identity is set as default"""
        data = {
            "current_passphrase": current_passphrase,
            "data": base64.b64encode(json.dumps(backed_up_data).encode()).decode(),
            "new_passphrase": new_passphrase,
            "set_default": set_default
        }
        response = requests.post(self.urls.import_identity, json=data)
        if response.status_code == 200:
            return json.loads(response.content)["id"]
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))
        else:
            raise MystAPIError(f'Error Code:{response.status_code}\n{response.content.decode()}')

    def export_current_identity(self, passphrase: str = ''):
        """Exports current identity"""
        if len(passphrase) < 8:
            raise MinimumPassphraseLengthError(
                f'Length of export passphrase must be atleast 8 characters')
        exported_file_name = "/tmp/myst-export.json"
        result = self.__execute(
            f'myst cli --agreed-terms-and-conditions identities export {self.current_identity} {passphrase} {exported_file_name}')
        try:
            return json.load(io.open(exported_file_name, 'r', encoding='utf-8'))
        except:
            raise ExportError(f'Failed to export current identity:\n{result}')

    def get_all_orderes(self) -> list:
        data = {
            "id": self.current_identity
        }
        response = requests.get(self.urls.get_all_orders.format(**data))
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))
        else:
            return response

    # TODO: Change function
    # def create_new_order(self, gateway: str = 'coingate', country: str = "US", myst_amount: float = 0, pay_currency: str = "LTC") -> dict:
    #     minimum_amount = self.payment_order_options()["minimum"]
    #     if myst_amount <= minimum_amount:
    #         raise MinimumAmountError(
    #             f"Amount must be greater than {minimum_amount}")
    #     data = {
    #         'id': self.current_identity,
    #         'gw': gateway
    #     }
    #     json_data = {
    #         'country': country,
    #         'gateway_caller_data': {},
    #         'myst_amount': myst_amount,
    #         'pay_currency': pay_currency
    #     }

    def create_new_order(self, lightning_network: bool = False, myst_amount: float = 0, pay_currency: str = "LTC") -> dict:
        minimum_amount = self.payment_order_options()[
            0]['order_options']['minimum']
        if myst_amount <= minimum_amount:
            raise MinimumAmountError(
                f"Amount must be greater than {minimum_amount}")
        data = {
            "id": self.current_identity
        }
        json_data = {
            "lightning_network": lightning_network,
            "myst_amount": myst_amount,
            "pay_currency": pay_currency
        }
        response = requests.post(
            self.urls.create_order.format(**data), json=json_data)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_order_info(self, order_id: int):
        data = {
            "id": self.current_identity,
            "order_id": order_id
        }
        response = requests.get(self.urls.get_order_info.format(**data))
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def payment_order_options(self):
        response = requests.get(self.urls.payment_gateway_config)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def payment_order_currencies(self):
        response = requests.get(self.urls.payment_order_currencies)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def host_location_info(self):
        response = requests.get(self.urls.host_location)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))
        elif response.status_code == 503:
            raise ServiceUnavailableError(json.loads(response.content))

    def proposals(self, service_type: str = "wireguard", country: str = None, ip_type: str = None, price_hour_max: float = None, price_gib_max: float = None):
        filter_data = {
            "service_type": service_type,
            "location_country": country,
            "ip_type": ip_type,
            "price_hour_max": price_hour_max,
            "price_gib_max": price_gib_max,
        }
        response = requests.get(self.urls.proposals, params=filter_data)
        if response.status_code == 200:
            return Proposals(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def proposals_per_country(self):
        response = requests.get(self.urls.countries)
        if response.status_code == 200:
            return json.loads(response.content)
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))
        else:
            raise MystAPIError(
                f'Unable to retrive proposals per country: {response.content.decode()}')

    def agree_terms(self, agreed: bool = True) -> bool:
        response = requests.get(self.urls.terms)
        if response.status_code == 200:
            terms = json.loads(response.content)
            if (terms["current_version"] > terms["agreed_version"]) or (not terms["agreed_consumer"]):
                data = {
                    "agreed_consumer": True,
                    "agreed_provider": False,
                    "agreed_version": terms["current_version"]
                }
                response = requests.post(self.urls.terms, json=data)
                if response.status_code == 200:
                    return True
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_balance(self) -> float:
        response = requests.put(
            self.urls.balance.format(id=self.current_identity))
        if response.status_code == 200:
            return (json.loads(response.content)['Balance'])/10**18
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))

    def get_int_balance(self) -> int:
        response = requests.put(
            self.urls.balance.format(id=self.current_identity))
        if response.status_code == 200:
            return (json.loads(response.content)['Balance'])
        elif response.status_code == 400:
            raise BadRequestError(json.loads(response.content))
        elif response.status_code == 500:
            raise InternalServerError(json.loads(response.content))
