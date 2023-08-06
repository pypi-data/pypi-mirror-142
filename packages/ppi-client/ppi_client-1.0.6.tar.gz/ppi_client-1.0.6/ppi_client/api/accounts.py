from ppi_client.api.constants import ACCOUNT_LOGIN, ACCOUNT_REFRESH_TOKEN, ACCOUNT_ACCOUNTS, ACCOUNT_BANK_ACCOUNTS, \
     ACCOUNT_AVAILABLE_BALANCE, ACCOUNT_BALANCE_POSITIONS, ACCOUNT_MOVEMENTS
from ppi_client.ppi_api_client import PPIClient
from ppi_client.models.account_movements import AccountMovements


class AccountsApi(object):
    __api_client: PPIClient

    def __init__(self, api_client):
        self.__api_client = api_client

    def login(self, client_id: str, client_secret: str):
        """Tries to log in with the given credentials. Returns a session token which is needed to use the API.

        :param client_id: Client id
        :type client_id: str
        :param client_secret: Client secret
        :type client_secret: str
        :rtype: authorization payload, including access_token, refresh_token and expiration date.
        """
        login = {
            "user": client_id,
            "password": client_secret
        }
        res = self.__api_client.post(ACCOUNT_LOGIN, data=login)
        self.__api_client.token = res['accessToken']
        self.__api_client.refreshToken = res['refreshToken']
        self.__api_client.refreshedCant = 0
        self.__api_client.get_rest_client().client_id = client_id
        self.__api_client.get_rest_client().client_secret = client_secret

        return res

    def get_accounts(self):
        """Retrieves all the available accounts and their officer for the current session.

        :rtype: list of accounts
        """
        return self.__api_client.get(ACCOUNT_ACCOUNTS, None)

    def get_bank_accounts(self, account_number: str):
        """Retrieves all the available bank accounts for the given account.

        :param account_number: Account number to retrieve bank accounts
        :type account_number: str
        :rtype: list of bank accounts
        """
        return self.__api_client.get(ACCOUNT_BANK_ACCOUNTS.format(account_number))

    def get_available_balance(self, account_number: str):
        """Retrieves cash balance available for trading for the given account.

        :param account_number: Account number to retrieve availability
        :type account_number: str
        :rtype: List of availability
        """
        return self.__api_client.get(ACCOUNT_AVAILABLE_BALANCE.format(account_number))

    def get_balance_and_positions(self, account_number: str):
        """Retrieves account balance and positions for the given account.

        :param account_number: Account number to retrieve balance and position
        :type account_number: Grouped availability and grouped instruments
        """
        return self.__api_client.get(ACCOUNT_BALANCE_POSITIONS.format(account_number))

    def get_movements(self, parameters: AccountMovements):
        """Retrieves movements for the given account between the specified dates.

        :param parameters: Parameters for the report: account_number: str, from_date: datetime, to_date: datetime, ticker: str
        :type parameters: AccountMovements
        :rtype: List of movements
        """
        params = {
            'dateFrom': parameters.from_date,
            'dateTo': parameters.to_date,
            'ticker': parameters.ticker
            }
        return self.__api_client.get(ACCOUNT_MOVEMENTS.format(parameters.account_number), params=params)
