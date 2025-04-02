from pywinauto.keyboard import send_keys

from launch_program import launch_program


def formation_the_payroll():
    """Формирование списочного состава"""
    launch_program() # Ввод пароля для программы

    send_keys('{VK_RIGHT}', with_spaces=True, pause=0.1)
    send_keys('{ENTER 2}', with_spaces=True, pause=14)
    send_keys('{ENTER 2}', with_spaces=True, pause=5)
    send_keys('{VK_F5}', with_spaces=True, pause=2)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=1)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=1)
    send_keys('{VK_RIGHT}', with_spaces=True, pause=1)
    send_keys('{ENTER}', with_spaces=True, pause=1) # Если ENTER 2, то как будто срабатывает 2 нажатие если ENTER работает как одно
    send_keys('{PGUP}', with_spaces=True, pause=1)
    for _ in range(13):
        send_keys('{INSERT}', with_spaces=True, pause=0.1)
    send_keys('{ENTER}',  with_spaces=True)  # Если ENTER 2, то как будто срабатывает 2 нажатие если ENTER работает как одно

if __name__ == '__main__':
    formation_the_payroll()