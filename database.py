
import requests
from datetime import datetime


class NSE_SESSION:
    def __init__(self):
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
            'accept-language': 'en,gu;q=0.9,hi;q=0.8',
            'accept-encoding': 'gzip, deflate, br'}
        self.cook_url = "https://www.nseindia.com/option-chain"
        self.session = requests.Session()
        self.cookies = self.session.get(self.cook_url, headers=self.headers , timeout = 5).cookies

    def GetExpiry(self,indices):
        url = f'https://www.nseindia.com/api/option-chain-indices?symbol={indices}'
        input_format = "%d-%b-%Y"
        output_format = "%d%b%y"
        try:
            response = self.session.get(url,headers=self.headers, timeout=5, cookies=self.cookies)
            if response.status_code == 200:
                records = response.json()['records']
                format_exp = [datetime.strptime(date, input_format).strftime(output_format).upper() for date in
                              records['expiryDates']]
                return format_exp
            else:
                return []

        except Exception as ex:
            print('Error: {}'.format(ex))
