from loguru import logger
from pywinauto.keyboard import send_keys

from launch_program import launch_program


def opening_additional_payments_1(dist_list, site_selection) -> None:
    """
    Формирование доплат
    :param dist_list: список кодов доплат
    :param site_selection: список кодов сайтов
    return: NONE
    """
    logger.info("Формирование доплат!")
    for dist in dist_list:
        logger.info(f"Код доплаты: {dist}")
        for site in site_selection:
            logger.info(f"Дата расчетного периода: {site}")
            launch_program()  # Запускаем программу, вводим пароль
            opening_formation_of_reports_1(dist, site)
    logger.info("Формирование доплат завершено!")


def opening_formation_of_reports_1(dist, site_selection) -> None:
    """Открытие функции Формирование доплат"""
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.2)
    for _ in range(18):  # 18 - количество нажатий на клавишу вниз для выбора пункта меню
        send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{ENTER 2}', with_spaces=True, pause=2)

    dataa = list(site_selection)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.4)

    dataa = list(site_selection)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.4)

    dataa = list(dist)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.4)

    send_keys('{ENTER 2}', with_spaces=True)


def opening_additional_payments(dist_list, site_selection) -> None:
    """
    Формирование доплат
    :param dist_list: список кодов доплат
    :param site_selection: список кодов сайтов
    return: NONE
    """
    logger.info("Формирование доплат!")
    for dist in dist_list:
        logger.info(f"Код доплаты: {dist}")
        for site in site_selection:
            logger.info(f"Дата расчетного периода: {site}")
            launch_program()  # Запускаем программу, вводим пароль
            opening_formation_of_reports(dist, site)
    logger.info("Формирование доплат завершено!")


def opening_formation_of_reports(dist, site_selection) -> None:
    """Открытие функции Формирование доплат"""
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.2)
    for _ in range(14):  # 14 - количество нажатий на клавишу вниз для выбора пункта меню
        send_keys('{DOWN}', with_spaces=True, pause=0.2)
    send_keys('{ENTER 2}', with_spaces=True, pause=2)

    dataa = list(site_selection)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.4)

    dataa = list(dist)
    for keys_pas in dataa:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True, pause=0.4)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True, pause=2)
    send_keys('{ENTER 2}', with_spaces=True, pause=40)
