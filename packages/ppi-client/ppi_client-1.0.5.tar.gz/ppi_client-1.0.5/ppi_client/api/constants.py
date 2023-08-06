ACCOUNT_LOGIN = '1.0/Account/Login'
ACCOUNT_REFRESH_TOKEN = '1.0/Account/RefreshToken'
ACCOUNT_ACCOUNTS = '1.0/Account/Accounts'
ACCOUNT_BANK_ACCOUNTS = '1.0/Account/BankAccounts?accountNumber={0}'
ACCOUNT_AVAILABLE_BALANCE = '1.0/Account/AvailableBalance?accountNumber={0}'
ACCOUNT_BALANCE_POSITIONS = '1.0/Account/BalancesAndPositions?accountNumber={0}'
ACCOUNT_MOVEMENTS = '1.0/Account/Movements?accountNumber={0}'

CONFIGURATION_INSTRUMENT_TYPES = '1.0/Configuration/InstrumentTypes'
CONFIGURATION_MARKETS = '1.0/Configuration/Markets'
CONFIGURATION_SETTLEMENTS = '1.0/Configuration/Settlements'
CONFIGURATION_QUANTITY_TYPES = '1.0/Configuration/QuantityTypes'
CONFIGURATION_OPERATION_TERMS = '1.0/Configuration/OperationTerms'
CONFIGURATION_OPERATION_TYPES = '1.0/Configuration/OperationTypes'
CONFIGURATION_OPERATIONS = '1.0/Configuration/Operations'

MARKETDATA_SEARCH_INSTRUMENT = '1.0/MarketData/SearchInstrument'
MARKETDATA_SEARCH = '1.0/MarketData/Search'
MARKETDATA_CURRENT = '1.0/MarketData/Current'
MARKETDATA_BOOK = '1.0/MarketData/Book'
MARKETDATA_INTRADAY = '1.0/MarketData/Intraday'

ORDER_ORDERS = '1.0/Order/Orders?accountNumber={0}'
ORDER_DETAIL = '1.0/Order/Detail'
ORDER_BUDGET = '1.0/Order/Budget'
ORDER_CONFIRM = '1.0/Order/Confirm'
ORDER_CANCEL = '1.0/Order/Cancel'
ORDER_MASS_CANCEL = '1.0/Order/MassCancel?accountNumber={0}'

HTTP_STATUS = 'httpStatus'
HTTP_RESPONSE = 'httpResponse'
MIME_JSON = "application/json"
MIME_FORM = "application/x-www-form-urlencoded"