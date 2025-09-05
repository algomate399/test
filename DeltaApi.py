import hashlib
import hmac
import requests
import time


def run():
    # Replace with your Webshare proxy credentials
    proxy_host="23.95.150.145"
    proxy_port="6114"  # or the port given to you
    proxy_user="cqgwbldr"
    proxy_pass="vnidqmrkz75j"

    proxies={
        "http" : f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}" ,
        "https" : f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}" ,
    }

    base_url = 'https://cdn-ind.testnet.deltaex.org'
    api_key = 'wzCBXaa6qlCvfQybJ3LqRd1dMKd8bU'
    api_secret = 'VKHQAlhbt9Ven8vHSUGr34EOlUZJ57wIGckRqtZIbTlc4drDZzNQ1OvIQT2N'

    def generate_signature(secret, message):
        message = bytes(message, 'utf-8')
        secret = bytes(secret, 'utf-8')
        hash = hmac.new(secret, message, hashlib.sha256)
        return hash.hexdigest()

    # Get open orders
    method = 'GET'
    timestamp = str(int(time.time()))
    path = '/v2/orders'
    url = f'{base_url}{path}'
    query_string = '?product_id=1&state=open'
    payload = ''
    signature_data = method + timestamp + path + query_string + payload
    signature = generate_signature(api_secret, signature_data)

    req_headers = {
      'api-key': api_key,
      'timestamp': timestamp,
      'signature': signature,
      'User-Agent': 'python-rest-client',
      'Content-Type': 'application/json'
    }

    query = {"product_id": 1, "state": 'open'}

    response = requests.request(
        method, url, data=payload, params=query, timeout=(3, 27), headers=req_headers , proxies = proxies
    )

    # Place new order
    method = 'GET'
    timestamp = str(int(time.time()))
    path = '/v2/orders/history'
    url = f'{base_url}{path}'
    query_string = ''
    payload = ""
    signature_data = method + timestamp + path + query_string + payload
    signature = generate_signature(api_secret, signature_data)

    req_headers = {
      'api-key': api_key,
      'timestamp': timestamp,
      'signature': signature,
      'User-Agent': 'rest-client',
      'Content-Type': 'application/json'
    }

    response = requests.request(
        method, url, data=payload, params={}, timeout=(8, 27), headers=req_headers , proxies = proxies )

    print(response.json())

