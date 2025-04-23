import json
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


def get_data_from_json():
    with open('data/tab_2024.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


dist_list = get_data_from_json()


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
