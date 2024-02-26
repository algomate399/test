
import requests
from datetime import datetime


class NSE_Session:
    def __init__(self, symbol,timeout=5):
        self.__url = "https://www.nseindia.com/api/option-chain-indices?symbol={}".format(symbol)
        self.__session = requests.sessions.Session()
        self.__session.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
            "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5"}
        self.__timeout = timeout
        self.__session.get("https://www.nseindia.com/option-chain", timeout=self.__timeout)

    def get_expiry(self):
        input_format = "%d-%b-%Y"
        output_format = "%d%b%y"
        try:
            response = self.__session.get(url=self.__url, timeout=self.__timeout)
            if response.status_code == 200:
                records = response.json()['records']
                format_exp = [datetime.strptime(date, input_format).strftime(output_format).upper() for date in
                              records['expiryDates']]
                return format_exp
            else:
                return []

        except Exception as ex:
            print('Error: {}'.format(ex))
            self.__session.get("https://www.nseindia.com/option-chain", timeout=self.__timeout)



