import time

from pywinauto.keyboard import send_keys

from launch_program import launch_program


def main(dist_list) -> None:
    """Запуск программы"""
    for dist in dist_list:
        print("Привет, мир!")
        launch_program()  # Запускаем программу, вводим пароль
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
    send_keys('{ENTER 2}', with_spaces=True, pause=0.1)
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
    site_selection = "112021"
    dataa = list(site_selection)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    dataaa = list(dist)
    for keys_pasa in dataaa:
        send_keys('{VK_NUMPAD' + keys_pasa + '}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)


if __name__ == "__main__":
    dist_list = ['110100', '110110', '110120', '110130', '110140', '110150', '110160', '110170', '110191', '110192',
                 '110193', '110200', '110211', '110220', '110230', '110240', '110250', '120110', '120210', '120220',
                 '120400', '120410', '120420', '120500', '120520', '120530', '120610', '120700', '120800', '120900',
                 '121000', '121010', '121020', '121030', '121040', '121050', '121060', '121070', '121100', '121110',
                 '121200', '121400', '121500', '121600', '121710', '121730', '121810', '121820', '121830', '121840',
                 '121850', '121860', '121870', '121940', '121950', '121960', '121972', '121970', '121971', '122100',
                 '122200', '122400', '130010', '130020', '130030', ]
    main(dist_list)
