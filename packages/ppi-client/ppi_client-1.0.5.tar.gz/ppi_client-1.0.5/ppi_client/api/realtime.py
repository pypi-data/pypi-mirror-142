import asyncio

from ppi_client.models.instrument import Instrument
from ppi_client.ppi_api_client import PPIClient


class RealtimeApi(object):
    __api_client: PPIClient
    __ws_loop: None

    def __init__(self, api_client):
        self.__api_client = api_client

    def connect_to_market_data(self, connect_handler, disconnect_handler, marketdata_handler):
        """Initialize the Websocket Client to realtime and register handlers.
                :param connect_handler: Callback for on connect event
                :type connect_handler: callable
                :param disconnect_handler: Callback for on disconnect event
                :type disconnect_handler: callable
                :param marketdata_handler: Callback for market data event
                :type marketdata_handler: callable
                """
        self.__ws_loop = asyncio.new_event_loop()
        self.__ws_loop.run_until_complete(self.__api_client.connect_to_websocket(connect_handler, disconnect_handler, marketdata_handler))
        self.__ws_loop.run_forever()

    def subscribe_to_element(self, instrument: Instrument):
        """Subscribe to an instrument's updates. marketdata_handler callback is called on every market data update.
        :param instrument: Parameters for the subscription: ticker: str, type: str, settlement: str
        :type instrument: Instrument
        """
        self.__api_client.ws_connection.send("MarketDataSubscribe", [instrument])


