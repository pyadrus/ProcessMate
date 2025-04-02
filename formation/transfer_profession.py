import os

from pywinauto.keyboard import send_keys

from launch_program import launch_program


def opening_of_the_full_time_position_function(site_selection) -> None:
    """Открытие функции штатная должность"""
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{VK_LEFT}', with_spaces=True)
    send_keys('{VK_F1}', with_spaces=True)
    data = list(site_selection)
    for keys_pas in data:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{VK_RIGHT}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)


def transfer_prof() -> None:
    """Перевод на другой участок или на другую профессию ГУП ДНР "Шахта им. А.Ф. Засядько" """
    os.system("mode con cols=80 lines=60")
    print("[1] - 110100 Руководство\n",
          "[2] - 110120 Производ.служба\n",
          "[3] - 110130 Техн.служба\n",
          "[4] - 110140 СОТ и ТБ\n",
          "[5] - 110150 Маркшейдерская служба\n",
          "[6] - 110170 ЭМС\n",
          "[7] - 110191 ПЭО\n",
          "[8] - 110192 ООТиЗП\n",
          "[9] - 110193 Финансовый сектор\n",
          "[10] - 110200 Бухгалтерия\n",
          "[11] - 110211 Сектор договорной работы\n",
          "[12] - 110220 Сектор МТС\n",
          "[13] - 110230 ОК\n",
          "[14] - 110240 Сектор по социальным вопросам\n",
          "[18] - 120400 Уч.ШТ\n",
          "[21] - 120450 УКТ\n",
          "[22] - 120500 Уч.РВР\n",
          "[23] - 120520 Уч.РВР №2\n",
          "[25] - 120610 Уч.МДГО № 1\n",
          "[26] - 120700 ВТБ\n",
          "[29] - 121000 Водоотлив\n",
          "[30] - 121010 Стац.оборуд.№1\n",
          "[31] - 121020 Стац.оборуд №2\n",
          "[32] - 121030 Электроцех\n",
          "[33] - 121040 РЗО\n",
          "[34] - 121050 ОМК\n",
          "[35] - 121060 РВВ\n",
          "[36] - 121070 Котельная\n",
          "[37] - 121100 Отдел технич-го контроля угля\n",
          "[38] - 121110 Участок АСУиТП\n",
          "[40] - 121400 АБК\n",
          "[41] - 121500 Здравпункт\n",
          "[42] - 121600 Охрана\n",
          "[43] - 121710 Автотранспортный участок\n",
          "[44] - 121730 УФПО\n",
          "[45] - 121810 ИТР ОФ\n",
          "[46] - 121820 ОП ОФ\n",
          "[47] - 121830 Электроцех ОФ\n",
          "[48] - 121840 Монтажно-демонтажная группа ОФ\n",
          "[49] - 121850 Ремонтная группа ОФ\n",
          "[50] - 121860 Углехимическая лаборатория ОФ\n",
          "[51] - 121870 АБК ОФ\n",
          "[52] - 121930 Склад №1\n",
          "[53] - 121950 Склад №2\n",
          "[54] - 121960 Склад строительных материалов\n",
          "[55] - 121970 Угольной склад\n",
          "[56] - 121971 Лесной склад\n",
          "[57] - 121972 Склад №4\n",
          "[58] - 122100 КГЭС\n",
          "[59] - 122200 Уч.по изг и рем.\n",
          "[60] - 122400 УСМР\n",
          "[61] - 130010 Общежитие №1\n",
          "[62] - 130020 Гостиница 'Олимп'\n",
          "[63] - 130030 ПТК 'Донецкий'")
    user_input = input("Введите номер: ")
    if user_input == "1":
        launch_program()
        site_selection = "110100"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "2":

        launch_program()
        site_selection = "110120"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "3":
        launch_program()
        site_selection = "110130"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "4":
        launch_program()
        site_selection = "110140"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "5":
        launch_program()
        site_selection = "110150"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "6":
        launch_program()
        site_selection = "110170"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "7":
        launch_program()
        site_selection = "110191"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "8":
        launch_program()
        site_selection = "110192"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "9":
        launch_program()
        site_selection = "110193"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "10":
        launch_program()
        site_selection = "110200"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "11":
        launch_program()
        site_selection = "110211"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "12":
        launch_program()
        site_selection = "110220"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "13":
        launch_program()
        site_selection = "110230"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "14":
        launch_program()
        site_selection = "110240"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "18":
        launch_program()
        site_selection = "120400"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "21":
        launch_program()
        site_selection = "120450"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "22":
        launch_program()
        site_selection = "120500"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "23":
        launch_program()
        site_selection = "120520"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "25":
        launch_program()
        site_selection = "120610"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "26":
        launch_program()
        site_selection = "120700"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "29":
        launch_program()
        site_selection = "121000"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "30":
        launch_program()
        site_selection = "121010"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "31":
        launch_program()
        site_selection = "121020"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "32":
        launch_program()
        site_selection = "121030"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "33":
        launch_program()
        site_selection = "121040"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "34":
        launch_program()
        site_selection = "121050"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "35":
        launch_program()
        site_selection = "121060"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "36":
        launch_program()
        site_selection = "121070"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "37":
        launch_program()
        site_selection = "121100"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "38":
        launch_program()
        site_selection = "121110"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "40":
        launch_program()
        site_selection = "121400"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "41":
        launch_program()
        site_selection = "121500"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "42":
        launch_program()
        site_selection = "121600"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "43":
        launch_program()
        site_selection = "121710"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "44":
        launch_program()
        site_selection = "121730"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "45":
        launch_program()
        site_selection = "121810"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "46":
        launch_program()
        site_selection = "121820"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "47":
        launch_program()
        site_selection = "121830"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "48":
        launch_program()
        site_selection = "121840"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "49":
        launch_program()
        site_selection = "121850"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "50":
        launch_program()
        site_selection = "121860"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "51":
        launch_program()
        site_selection = "121870"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "52":
        launch_program()
        site_selection = "121930"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "53":
        launch_program()
        site_selection = "121950"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "54":
        launch_program()
        site_selection = "121960"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "55":
        launch_program()
        site_selection = "121970"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "56":
        launch_program()
        site_selection = "121971"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "57":
        launch_program()
        site_selection = "121972"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "58":
        launch_program()
        site_selection = "122100"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "59":
        launch_program()
        site_selection = "122200"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "60":
        launch_program()
        site_selection = "122400"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "61":
        launch_program()
        site_selection = "130010"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "62":
        launch_program()
        site_selection = "130020"
        opening_of_the_full_time_position_function(site_selection)
    elif user_input == "63":
        launch_program()
        site_selection = "130030"
        opening_of_the_full_time_position_function(site_selection)


if __name__ == "__main__":
    transfer_prof()
