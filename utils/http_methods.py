import requests

from utils.logger import Logger


class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookies = ''

    @classmethod
    def get(cls, url):
        Logger.add_request(url, method='GET')
        result = requests.get(url, headers=cls.headers, cookies=cls.cookies)
        Logger.add_response(result)
        return result

    @classmethod
    def post(cls, url, body):
        Logger.add_request(url, method='POST')
        result = requests.post(url, json=body, headers=cls.headers, cookies=cls.cookies)
        Logger.add_response(result)
        return result

    @classmethod
    def put(cls, url, body):
        Logger.add_request(url, method='PUT')
        result = requests.put(url, json=body, headers=cls.headers, cookies=cls.cookies)
        Logger.add_response(result)
        return result

    @classmethod
    def delete(cls, url, body):
        Logger.add_request(url, method='DELETE')
        result = requests.delete(url, json=body, headers=cls.headers, cookies=cls.cookies)
        Logger.add_response(result)
        return result
