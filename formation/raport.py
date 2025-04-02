from pywinauto.keyboard import send_keys

from launch_program import launch_program


def formation_of_reports():
    """Формирование рапортов"""
    # Запускаем программу, вводим пароль
    launch_program()  # Запускаем программу, вводим пароль
    site_selection = "130030"
    opening_formation_of_reports(site_selection)


def opening_formation_of_reports(site_selection) -> None:
    """Открытие функции штатная должность"""
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True, pause=1)
    send_keys('{UP}', with_spaces=True)
    data = list(site_selection)
    for keys_pas in data:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.5)
    send_keys('{ENTER 2}', with_spaces=True, pause=0.2)
    send_keys('{ENTER 2}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True, pause=0.1)


if __name__ == "__main__":
    formation_of_reports()
