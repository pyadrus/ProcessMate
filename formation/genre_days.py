from pywinauto.keyboard import send_keys

from launch_program import launch_program


def opening_of_the_full_time_position_function() -> None:
    """Открытие функции штатная должность"""
    send_keys('{DOWN}', with_spaces=True)
    # send_keys('{DOWN}', with_spaces=True)
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
    send_keys('{ENTER 2}', with_spaces=True)
    send_keys('{DOWN}', with_spaces=True)


def main() -> None:
    """Перевод на другой участок или на другую профессию ГУП ДНР "Шахта им. А.Ф. Засядько" """
    launch_program()  # Запускаем программу, вводим пароль
    opening_of_the_full_time_position_function()


if __name__ == "__main__":
    main()
