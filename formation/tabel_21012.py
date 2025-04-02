import time

from pywinauto.keyboard import send_keys

from launch_program import launch_program


def tabel(dist_list) -> None:
    """Запуск программы"""
    for dist in dist_list:
        print("Привет, мир!")
        launch_program()  # Ввод пароля для программы
        opening_formation_of_reports(dist)  # Включение табеля с вводом месяца
        time.sleep(1)


def opening_formation_of_reports(dist) -> None:
    """Открытие функции штатная должность"""
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
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
    send_keys('{ENTER 2}', with_spaces=True, pause=1)
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
    send_keys('{ENTER 2}', with_spaces=True, pause=0.1)
    send_keys('{UP}', with_spaces=True, pause=0.1)
    site_selection = "112022"
    dataa = list(site_selection)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)

    dataaa = list(dist)
    for keys_pasa in dataaa:
        send_keys('{VK_NUMPAD' + keys_pasa + '}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
