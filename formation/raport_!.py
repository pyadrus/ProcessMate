import pywinauto
from pywinauto.keyboard import send_keys, KeySequenceError

from launch_program import launch_program


def opening_of_the_full_time_position_function(site_selection) -> None:
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
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{UP}', with_spaces=True)
    data = list(site_selection)
    for keys_pas in data:
        send_keys('{VK_NUMPAD' + keys_pas + '}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{ENTER 2}', with_spaces=True, pause=15)
    # Connect to Excel and save the file
    try:
        app = pywinauto.application.Application().connect(title_re='.*Excel.*')
    except pywinauto.application.ProcessNotFoundError:
        print("Excel is not running")
        return
    window = app.window(title_re='.*Excel.*')
    window.set_focus()
    try:
        send_keys('{DOWN}', with_spaces=True)
        window.type_keys('^s')
        window.type_keys('^s')

    except KeySequenceError:
        print("Could not save the file")
        return


def main():
    launch_program()  # Запускаем программу, вводим пароль
    site_selection = "110100"
    opening_of_the_full_time_position_function(site_selection)


if __name__ == '__main__':
    main()
