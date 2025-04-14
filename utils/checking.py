"""методы для проверки запросов"""
import json


class Checking():

    """метод для проверки статус-кода"""
    @staticmethod
    def check_status_code(response, status_code):
        assert response.status_code == status_code

        if response.status_code == status_code:
            print(f'успешно! статус код: {str(response.status_code)}')
        else:
            print(f'неудача. статус код: {str(response.status_code)}')

    """метод для проверки наличия обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_token(response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('все поля присутствуют')

    """метод для проверки значений обязательных полей в ответе запроса"""
    @staticmethod
    def check_json_value(response, expected_value, field_name):
        check = response.json()
        check_info = check.get(expected_value)
        assert field_name in check_info
        print(f'{field_name} верен')


