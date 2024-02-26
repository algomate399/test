
import requests
from datetime import datetime

def get_expiry(indices):
    input_format = "%d-%b-%Y"
    output_format = "%d%b%y"
    url = f'https://www.nseindia.com/api/option-chain-indices?symbol={indices}'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
        "Connection": "keep-alive"
    }
    response = requests.get(url, headers=headers)
    print('resp',response)
    if response.status_code == 200:
        records = response.json()['records']
        format_exp = [datetime.strptime(date, input_format).strftime(output_format).upper() for date in records['expiryDates']]
        return format_exp
    else:
        return []  # or handle the error in an appropriate way
