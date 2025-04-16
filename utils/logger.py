import datetime
import os
from requests import Response

class Logger:

    log_dir = 'СЮДА НУЖНО ВСТАВИТЬ ПУТЬ ДО ПАПКИ logs'
    file_name = f'log_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log'
    file_path = os.path.join(log_dir, file_name)

    @classmethod
    def _ensure_log_dir_exists(cls):
        """создает директорию для логов, если её нет"""
        os.makedirs(cls.log_dir, exist_ok=True)

    @classmethod
    def write_log_to_file(cls, data: str):
        try:
            cls._ensure_log_dir_exists()
            with open(cls.file_path, 'a', encoding='utf-8') as logger_file:
                logger_file.write(data)
        except Exception as e:
            print(f"❗ ошибка записи в лог: {e}")

    @classmethod
    def add_request(cls, url: str, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        data_to_add = (
            "\n-----\n"
            f"тест: {test_name}\n"
            f"время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"метод: {method}\n"
            f"URL: {url}\n\n"
        )

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_response(cls, result: Response):

        if not isinstance(result, Response):
            error_msg = f"ошибка: ожидается Response, получен {type(result)}"
            print(error_msg)
            cls.write_log_to_file(error_msg)
            return

        try:
            cookies = dict(result.cookies)
            headers_as_dict = dict(result.headers)

            data_to_add = (
                f"код ответа: {result.status_code}\n"
                f"текст ответа: {result.text}\n"
                f"заголовки: {headers_as_dict}\n"
                f"cookies: {cookies}\n"
                "-----\n\n"
            )

            cls.write_log_to_file(data_to_add)
        except AttributeError as e:
            error_msg = f"ошибка обработки ответа: {e}"
            print(error_msg)
            cls.write_log_to_file(error_msg)