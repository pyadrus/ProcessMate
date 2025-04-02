import time

from pywinauto.keyboard import send_keys

from launch_program import launch_program


def summary_by_types_and_categories():
    """Открытие формы BZ 14"""
    launch_program()  # Ввод пароля для программы
    opening_formation_of_reports()  # Включение табеля с вводом месяца
    time.sleep(1)


def opening_formation_of_reports() -> None:
    """Открытие функции штатная должность"""
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True, pause=1)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True, pause=1)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True, pause=30)
    send_keys('{ENTER 2}', with_spaces=True)


if __name__ == "__main__":
    summary_by_types_and_categories()
