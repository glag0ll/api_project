import requests

class HttpMethods:
    headers = {'Content-Type': 'application/json'}
    cookies = ''

    @classmethod
    def get(cls, url, body):
        return requests.get(url, json=body, headers=cls.headers, cookies=cls.cookies)

    @classmethod
    def post(cls, url, body):
        return requests.post(url, json=body, headers=cls.headers, cookies=cls.cookies)

    @classmethod
    def put(cls, url, body):
        return requests.put(url, json=body, headers=cls.headers, cookies=cls.cookies)

    @classmethod
    def delete(cls, url, body):
        return requests.delete(url, json=body, headers=cls.headers, cookies=cls.cookies)