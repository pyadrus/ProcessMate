from pywinauto.keyboard import send_keys

from launch_program import launch_program


def formation_of_reports(dist_list):
    """Формирование рапортов"""
    for dist in dist_list:
        print("Формирование рапортов!")
        launch_program()  # Запускаем программу, вводим пароль
        opening_formation_of_reports(dist)


def opening_formation_of_reports(dist) -> None:
    """Открытие функции Формирование рапортов"""
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
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True, pause=1)
    send_keys('{UP}', with_spaces=True, pause=0.1)
    send_keys('{DOWN}', with_spaces=True)

    site_selection = "022025"  # Дата формирования рапорта
    dataa = list(site_selection)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.3)
    send_keys('{ESC}', with_spaces=True, pause=0.2)
    send_keys('{UP}', with_spaces=True)

    dataaa = list(dist)
    for keys_pasa in dataaa:
        send_keys('{VK_NUMPAD' + keys_pasa + '}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True, pause=1)
    send_keys('{ENTER 2}', with_spaces=True)
