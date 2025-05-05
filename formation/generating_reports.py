import time

from pywinauto.keyboard import send_keys

from launch_program import launch_program

password = '21012'  # Пароль от программы


def main() -> None:
    """Запуск программы"""
    launch_program()  # Запускаем программу, вводим пароль
    opening_formation_of_reports()  # Включение табеля с вводом месяца
    time.sleep(1)


def opening_formation_of_reports() -> None:
    """Открытие функции штатная должность"""
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    for _ in range(3):
        send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    for _ in range(11):
        send_keys('{DOWN}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    time.sleep(1)
    for _ in range(3):
        send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True, pause=15)
    send_keys('{ENTER 2}', with_spaces=True)


if __name__ == "__main__":
    main()
