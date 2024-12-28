import tkinter as tk
from tkinter import messagebox

# Установим фиксированный курс доллара, например, 1 единица вашей валюты = 400 тенге
EXCHANGE_RATE = 400  # Пример: курс 1 тенге = 400 долларов США (здесь используйте свой курс)

# Функция для конвертации
def convert_to_usd():
    try:
        amount = float(entry_amount.get())  # Получаем введенную сумму
        usd_amount = amount / EXCHANGE_RATE  # Конвертируем в доллары
        label_result.config(text=f"Сумма в долларах США: {usd_amount:.2f} $")  # Выводим результат
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное число!")

# Создаем окно с графическим интерфейсом
window = tk.Tk()
window.title("Конвертер валют")

# Метка для ввода суммы
label_amount = tk.Label(window, text="Введите сумму в вашей валюте:")
label_amount.pack()

# Поле для ввода суммы
entry_amount = tk.Entry(window)
entry_amount.pack()

# Кнопка для конвертации
button_convert = tk.Button(window, text="Конвертировать", command=convert_to_usd)
button_convert.pack()

# Метка для отображения результата
label_result = tk.Label(window, text="Сумма в долларах США:")
label_result.pack()

# Запуск интерфейса
window.mainloop()
