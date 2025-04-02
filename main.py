import tkinter as tk

from loguru import logger

from formation.formation_of_reports import formation_of_reports
from formation.formation_of_surcharges import formation_of_surcharges, formation_of_surcharges_1
from formation.formation_the_payroll import formation_the_payroll
from formation.summary_by_types_and_categories import summary_by_types_and_categories
from formation.tabel_21012 import tabel
from formation.transfer_profession import transfer_prof
from gui.gui import root
from launch_program import launch_program

dist_list = ['110100', '110110', '110120', '110130', '110140', '110150', '110170', '110191', '110192', '110193',
             '110200', '110211', '110220', '110230', '110240', '120110', '120210', '120220', '120400', '120410',
             '120420', '120450', '120500', '120520', '120530', '120610', '120700', '120800', '120900', '121000',
             '121010', '121020', '121030', '121040', '121050', '121060', '121070', '121100', '121110', '121200',
             '121400', '121500', '121600', '121710', '121730', '121810', '121820', '121830', '121840', '121850',
             '121860', '121870', '121930', '121950', '121960', '121972', '121970', '121971', '122100', '122200',
             '122400', '130010', '130020', '130030', '110194', ]


# Основное меню программы на основе Tkinter

def main():
    root.title("Basic elevated buttons")
    root.geometry("500x350")  # Ширина и высота окна 500 ширина и 350 высота
    root.resizable(False, False)

    def opening_of_the_payroll() -> None:
        """Открытие списочного состава"""
        root.destroy()
        formation_the_payroll()

    def exit_and_run_transfer_prof():
        """КШД"""
        root.destroy()
        transfer_prof()

    def summary_by_types_and_categories_gui():
        """BZ 14"""
        root.destroy()
        summary_by_types_and_categories()

    def formation_of_reports_gui():
        """Формирование рапортов"""
        root.destroy()
        formation_of_reports(dist_list)

    def tabel_gui():
        """Формирование табеля"""
        root.destroy()
        tabel(dist_list)

    def launch_program_gui():
        """Открытие программы"""
        root.destroy()
        launch_program()

    # Формирование доплат
    def opening_additional_payments_gui():
        """Доплаты: 124, 164"""
        formation_of_surcharges()

    def opening_additional_payments_1_gui():
        """Доплаты: 130, 140"""
        formation_of_surcharges_1()

    # Создаем кнопки с аналогичными размерами и функциями
    buttons = [
        ("Жаровые", None),
        ("КШД", exit_and_run_transfer_prof),
        ("BZ 14", summary_by_types_and_categories_gui),
        ("Формирование рапортов", formation_of_reports_gui),
        ("Формирование табеля", tabel_gui),
        ("Доплаты", opening_additional_payments_gui),
        ("Доплаты 130, 410", opening_additional_payments_1_gui),
        ("Формирование списочного состава", opening_of_the_payroll),
        ("Запустить программу", launch_program_gui),
    ]

    for text, command in buttons:
        btn = tk.Button(root, text=text, width=50, height=1, command=command)
        btn.pack(pady=5)

    root.mainloop()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.exception(e)
