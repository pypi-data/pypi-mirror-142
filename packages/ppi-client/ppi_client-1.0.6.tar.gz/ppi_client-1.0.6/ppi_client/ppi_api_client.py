from ppi_client.api.constants import MIME_JSON, ACCOUNT_REFRESH_TOKEN, ACCOUNT_LOGIN
from ppi_client.ppi_restclient import RestClient


class PPIClient(object):
    __access_data = None
    __rest_client = None
    ws_connection = None
    token = None
    refreshToken = None
    refreshedCant = 0
    __client_id = None
    __client_secret = None
    __on_connect_handler = None
    __on_disconnect_handler = None
    __on_marketdata_handler = None
    __on_error_handler = None

    def __init__(self, version, sandbox):
        if sandbox:
            self.__client_key = 'ppPYTHONDev'
            self.__authorized_client = 'API-PYTHON'
        else:
            self.__client_key = 'pp19CliApp12'
            self.__authorized_client = 'API-CLI'

        self.__rest_client = RestClient(version, sandbox)
        self.__rest_client.client_key = self.__client_key
        self.__rest_client.authorized_client = self.__authorized_client


        self.ws_connection = None
        self.__ws_isconnected = False

    def get_rest_client(self):
        return self.__rest_client

    def get(self, uri, params=None, data=None, content_type=MIME_JSON):
        auth_headers = {'AuthorizedClient': self.__authorized_client, 'ClientKey': self.__client_key}
        if self.token is not None:
            auth_headers.update({'Authorization': 'Bearer ' + self.token})
        res = self.__rest_client.get(uri, params, auth_headers, data, content_type)

        if res.httpStatus == 401 and self.refreshToken is not None and self.refreshedCant < 5:
            try:
                self.renew_token()
                auth_headers.update({'Authorization': 'Bearer ' + self.token})
                return self.get(uri=uri, params=params, data=data)
            except Exception as e:
                print(e)
        if res.httpStatus != 200:
            raise Exception(res.response)

        return res.response

    def post(self, uri, data=None, params=None, content_type=MIME_JSON):
        auth_headers = {'AuthorizedClient': self.__authorized_client, 'ClientKey': self.__client_key}
        if self.token is not None:
            auth_headers.update({'Authorization': 'Bearer ' + self.token})

        res = self.__rest_client.post(uri, data, params, auth_headers, content_type)
        if res.httpStatus == 401 and self.refreshToken is not None and self.refreshedCant < 5:
            try:
                self.renew_token()
                auth_headers.update({'Authorization': 'Bearer ' + self.token})
                return self.post(uri=uri, params=params, data=data)
            except Exception as e:
                print(e)

        if res.httpStatus != 200:
            raise Exception(res.response)

        return res.response

    def put(self, uri, data=None, params=None, content_type=MIME_JSON):
        auth_headers = {'AuthorizedClient': self.__authorized_client, 'ClientKey': self.__client_key}
        if self.token is not None:
            auth_headers.update({'Authorization': 'Bearer ' + self.token})

        res = self.__rest_client.put(uri, data, params, auth_headers, content_type)

        if res.httpStatus == 401 and self.refreshToken is not None and self.refreshedCant < 5:
            try:
                self.renew_token()
                auth_headers.update({'Authorization': 'Bearer ' + self.token})
                return self.put(uri=uri, params=params, data=data)
            except Exception as e:
                print(e)

        if res.httpStatus != 200:
            raise Exception(res.response)

        return res.response

    def delete(self, uri, data=None, params=None, content_type=MIME_JSON):
        auth_headers = {'AuthorizedClient': self.__authorized_client, 'ClientKey': self.__client_key}
        if self.token is not None:
            auth_headers.update({'Authorization': 'Bearer ' + self.token})

        res = self.__rest_client.delete(uri, data, params, auth_headers, content_type)

        if res.httpStatus == 401 and self.refreshToken is not None and self.refreshedCant < 5:
            try:
                self.renew_token()
                auth_headers.update({'Authorization': 'Bearer ' + self.token})
                return self.delete(uri=uri, params=params, data=data)
            except Exception as e:
                print(e)

        if res.httpStatus != 200:
            raise Exception(res.response)

        return res.response

    async def connect_to_websocket(self, onconnect_handler=None, ondisconnect_handler=None, marketdata_handler=None):
        self.__on_connect_handler = onconnect_handler
        self.__on_disconnect_handler = ondisconnect_handler
        self.__on_marketdata_handler = marketdata_handler

        if self.ws_connection and self.__ws_isconnected:
            return self.ws_connection
        else:
            conn = await self.__rest_client.connect_to_websocket()
            self.ws_connection = conn

            def on_open():
                self.__ws_isconnected = True
                self.__on_connect_handler()

            def on_marketdata(msj):
                self.__on_marketdata_handler(msj[0])

            def on_close(msg):
                lambda: print("connection closed" + msg)
                self.__ws_isconnected = False
                self.__on_disconnect_handler()

            def on_scheduled_disconnection(msg):
                print("connection closed by server")
                conn.stop()
                on_close(msg)

            def on_error():
                lambda data: print(f"An exception was thrown closed: {data.error}")

            conn.on_open(on_open)
            conn.on_close(on_close)
            conn.on("marketdata", on_marketdata)
            conn.on("scheduled-disconnection", on_scheduled_disconnection)
            conn.on_error(on_error)

            conn.start()
            return conn

    def renew_token(self):
        self.refreshedCant = self.refreshedCant + 1
        auth_headers = {'AuthorizedClient': self.__authorized_client, 'ClientKey': self.__client_key}
        auth_headers.update({'Authorization': 'Bearer ' + self.token})
        body = {
            "refreshToken": self.refreshToken
        }
        res = self.__rest_client.post(ACCOUNT_REFRESH_TOKEN, body, None, auth_headers, MIME_JSON)
        if res.httpStatus == 200:
            self.token = res.response['accessToken']
            self.refreshToken = res.response['refreshToken']
        elif self.refreshedCant == 5:
            if bool(self.__rest_client.login_ws()):
                self.token = self.__rest_client.token_ws
                self.refreshToken = self.__rest_client.refresh_token_ws
                self.refreshedCant == 0
