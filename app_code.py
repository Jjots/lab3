import tkinter as tk
import time

root = tk.Tk()
root.title("Таймер-секундомер")
root.geometry("500x600+1000+10")

# Переменные для отслеживания состояния секундомера
running = False
start_time = 0
elapsed_time = 0

def update_timer():
    """Обновление времени на экране"""
    if running:
        global elapsed_time
        elapsed_time = time.time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        root.after(100, update_timer)

def start_timer():
    """Запуск секундомера"""
    global running, start_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time  # продолжаем с того места, где остановились
        update_timer()

def make_pause():
    """Пауза секундомера"""
    global running
    running = False

def make_reset():
    """Сброс секундомера"""
    global running, elapsed_time
    running = False
    elapsed_time = 0
    timer_label.config(text="00:00")

def start_countdown():
    """Запуск таймера с заданным временем"""
    try:
        minutes = int(entry_minutes.get())
        seconds = int(entry_seconds.get())
        total_seconds = minutes * 60 + seconds
        countdown(total_seconds)
    except ValueError:
        # Если введены некорректные данные
        label_error.config(text="Неверный ввод! Введите числа.")

def countdown(seconds_left):
    """Функция обратного отсчета времени"""
    if seconds_left >= 0:
        minutes, seconds = divmod(seconds_left, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        root.after(1000, countdown, seconds_left - 1)
    else:
        timer_label.config(text="00:00")
        label_error.config(text="Время вышло!")

# Создаем основной фрейм для окон
frame_timer = tk.Frame(root)
frame_timer.pack(pady=20)

frame_stopwatch = tk.Frame(root)
frame_stopwatch.pack(pady=20)

# Секундомер
label_1 = tk.Label(frame_stopwatch, text="Секундомер", font=('Arial', 15), padx=20)
label_1.pack()

timer_label = tk.Label(frame_stopwatch, text="00:00", font=('Arial', 30), padx=20, pady=70)
timer_label.pack()

frame1 = tk.Frame(frame_stopwatch)
frame1.pack(pady=10)

btn_start = tk.Button(frame1, text='Старт', command=start_timer)
btn_start.pack(side="left", padx=10)

btn_pause = tk.Button(frame1, text='Пауза', command=make_pause)
btn_pause.pack(side="left", padx=10)

btn_reset = tk.Button(frame1, text='Сброс', command=make_reset)
btn_reset.pack(side="left", padx=10)

# Таймер
label_2 = tk.Label(frame_timer, text="Введите значение для таймера (минуты и секунды):", font=('Arial', 10), pady=10)
label_2.pack()

frame2 = tk.Frame(frame_timer)
frame2.pack(pady=10)

entry_minutes = tk.Entry(frame2, width=5)
entry_minutes.pack(side="left", padx=5)

entry_seconds = tk.Entry(frame2, width=5)
entry_seconds.pack(side="left", padx=5)

btn_start_timer = tk.Button(frame2, text="Запустить таймер", command=start_countdown)
btn_start_timer.pack(side="left", padx=10)

label_error = tk.Label(frame_timer, text="", font=('Arial', 10), fg="red")
label_error.pack()

root.mainloop()


