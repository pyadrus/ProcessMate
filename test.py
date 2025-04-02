import tkinter as tk


def on_submit():
    selected_options = [option for option, var in checkboxes.items() if var.get()]
    print("Выбранные чекбоксы:", selected_options)

# Создаем основное окно
root = tk.Tk()
root.title("Чекбоксы")

# Создаем словарь для хранения переменных чекбоксов
checkboxes = {}

dates_vars = ['012024', '022024', '032024', '042024', '052024', '062024', '072024', '082024', '092024', '102024','112024', '122024']
# Создаем 12 чекбоксов
for i in dates_vars:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(root, text=f"Опция {i}", variable=var)
    chk.pack(anchor='w')
    checkboxes[i] = var

# Создаем кнопку "Готово"
submit_button = tk.Button(root, text="Готово", command=on_submit)
submit_button.pack(pady=10)

# Запускаем главный цикл обработки событий
root.mainloop()