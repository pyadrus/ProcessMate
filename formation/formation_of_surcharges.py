import tkinter as tk
from tkinter import messagebox

from gui.gui import root
from formation.opening_additional_payments import opening_additional_payments, opening_additional_payments_1

payment_ids = ["124", "164", "109", "122", "112"]
payment_ids_1 = ["130", "410"]

dates_vars = [
    '012023', '022023', '032023', '042023', '052023', '062023', '072023', '082023', '092023', '102023', '112023', '122023',
    '012024', '022024', '032024', '042024', '052024', '062024', '072024', '082024', '092024', '102024', '112024', '122024',
    '012025', '022025', '032025', '042025', '052025', '062025', '072025', '082025', '092025', '102025', '112025', '122025',
]

def formation_of_surcharges_1():
    """Формирование доплат"""
    try:
        # Создание нового окна для чекбоксов
        window = tk.Toplevel(root)
        window.title("Выбор дат и доплат")
        window.geometry("500x600")  # Установка размера окна
        # Создаем словарь для хранения переменных чекбоксов
        checkboxes = {}
        # Фрейм для чекбоксов с датами
        dates_frame = tk.Frame(window)
        dates_frame.pack(anchor=tk.W, padx=10, pady=5)
        # Чекбоксы для дат
        tk.Label(dates_frame, text="Выберите даты:").pack(anchor=tk.W)

        # Разделение дат на две колонки

        # Создание трех колонок
        column1_frame = tk.Frame(dates_frame)
        column1_frame.pack(side=tk.LEFT, anchor=tk.W, padx=10)
        column2_frame = tk.Frame(dates_frame)
        column2_frame.pack(side=tk.LEFT, anchor=tk.W, padx=10)
        column3_frame = tk.Frame(dates_frame)
        column3_frame.pack(side=tk.LEFT, anchor=tk.W, padx=10)

        # Распределение дат по трем колонкам
        for i, date in enumerate(dates_vars):
            var = tk.BooleanVar()
            if i < len(dates_vars) // 3:  # Первая треть дат
                chk = tk.Checkbutton(column1_frame, text=f"Дата {date}", variable=var)
            elif i < (len(dates_vars) * 2) // 3:  # Вторая треть дат
                chk = tk.Checkbutton(column2_frame, text=f"Дата {date}", variable=var)
            else:  # Последняя треть дат
                chk = tk.Checkbutton(column3_frame, text=f"Дата {date}", variable=var)
            chk.pack(anchor='w')
            checkboxes[date] = var

        # Чекбоксы для доплат
        tk.Label(window, text="Выберите виды доплат:").pack(anchor=tk.W, padx=10, pady=5)

        for i in payment_ids_1:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(window, text=f"Доплата {i}", variable=var)
            chk.pack(anchor='w')
            checkboxes[i] = var

        # Обработчик кнопки "Готово"
        def on_done_action():
            # Получение выбранных дат
            selected_dates = [option for option, var in checkboxes.items() if var.get() and option in dates_vars]
            # Получение выбранных доплат
            selected_payments = [payment for payment, var in checkboxes.items() if
                                 var.get() and payment in payment_ids_1]

            if not selected_dates and not selected_payments:
                messagebox.showwarning("Предупреждение", "Выберите хотя бы один пункт!")
                return

            # Вывод результата в messagebox
            messagebox.showinfo("Результат",
                                f"Выбранные даты: {selected_dates}\nВыбранные доплаты: {selected_payments}")
            # Закрытие окна
            window.destroy()
            # Вызов функции с выбранными данными
            opening_additional_payments_1(dist_list=selected_payments, site_selection=selected_dates)

        # Обработчик кнопки "Назад"
        def on_back_action():
            window.destroy()

        # Кнопки "Готово" и "Назад"
        button_frame = tk.Frame(window)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Готово", command=on_done_action).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Назад", command=on_back_action).pack(side=tk.LEFT, padx=5)

    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")


def formation_of_surcharges():
    """Формирование доплат"""
    try:
        # Создание нового окна для чекбоксов
        window = tk.Toplevel(root)
        window.title("Выбор дат и доплат")
        window.geometry("500x600")  # Установка размера окна
        # Создаем словарь для хранения переменных чекбоксов
        checkboxes = {}
        # Фрейм для чекбоксов с датами
        dates_frame = tk.Frame(window)
        dates_frame.pack(anchor=tk.W, padx=10, pady=5)
        # Чекбоксы для дат
        tk.Label(dates_frame, text="Выберите даты:").pack(anchor=tk.W)

        # Разделение дат на две колонки

        # Создание трех колонок
        column1_frame = tk.Frame(dates_frame)
        column1_frame.pack(side=tk.LEFT, anchor=tk.W, padx=10)
        column2_frame = tk.Frame(dates_frame)
        column2_frame.pack(side=tk.LEFT, anchor=tk.W, padx=10)
        column3_frame = tk.Frame(dates_frame)
        column3_frame.pack(side=tk.LEFT, anchor=tk.W, padx=10)

        # Распределение дат по трем колонкам
        for i, date in enumerate(dates_vars):
            var = tk.BooleanVar()
            if i < len(dates_vars) // 3:  # Первая треть дат
                chk = tk.Checkbutton(column1_frame, text=f"Дата {date}", variable=var)
            elif i < (len(dates_vars) * 2) // 3:  # Вторая треть дат
                chk = tk.Checkbutton(column2_frame, text=f"Дата {date}", variable=var)
            else:  # Последняя треть дат
                chk = tk.Checkbutton(column3_frame, text=f"Дата {date}", variable=var)
            chk.pack(anchor='w')
            checkboxes[date] = var

        # Чекбоксы для доплат
        tk.Label(window, text="Выберите виды доплат:").pack(anchor=tk.W, padx=10, pady=5)

        for i in payment_ids:
            var = tk.BooleanVar()
            chk = tk.Checkbutton(window, text=f"Доплата {i}", variable=var)
            chk.pack(anchor='w')
            checkboxes[i] = var

        # Обработчик кнопки "Готово"
        def on_done_action():
            # Получение выбранных дат
            selected_dates = [option for option, var in checkboxes.items() if var.get() and option in dates_vars]
            # Получение выбранных доплат
            selected_payments = [payment for payment, var in checkboxes.items() if
                                 var.get() and payment in payment_ids]

            if not selected_dates and not selected_payments:
                messagebox.showwarning("Предупреждение", "Выберите хотя бы один пункт!")
                return

            # Вывод результата в messagebox
            messagebox.showinfo("Результат",
                                f"Выбранные даты: {selected_dates}\nВыбранные доплаты: {selected_payments}")
            # Закрытие окна
            window.destroy()
            # Вызов функции с выбранными данными
            opening_additional_payments(dist_list=selected_payments, site_selection=selected_dates)

        # Обработчик кнопки "Назад"
        def on_back_action():
            window.destroy()

        # Кнопки "Готово" и "Назад"
        button_frame = tk.Frame(window)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Готово", command=on_done_action).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Назад", command=on_back_action).pack(side=tk.LEFT, padx=5)

    except Exception as e:
        print(f"An error occurred: {e}")
        messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == '__main__':
    formation_of_surcharges()
    formation_of_surcharges_1()
