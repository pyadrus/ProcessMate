import time

from loguru import logger
from pywinauto.application import Application
from pywinauto.keyboard import send_keys

program_path = 'esctermpro.exe 172.25.0.115 23'  # Запуск программы
password = '21013'  # Пароль от программы21012


def launch_program() -> None:
    """Запуск программы и ввод пароля"""
    logger.info('Запуск программы')

    Application().start(program_path)
    time.sleep(3)
    data = list(password)
    for keys_pas in data:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)


if __name__ == '__main__':
    launch_program()
