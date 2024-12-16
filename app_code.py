import tkinter as tk
import time

root = tk.Tk()
root.title("Таймер-секундомер")
root.geometry("500x600+1000+10")

def make_pause():
    pass

def make_reset():
    pass

def start_timer(duration):
    for remaining in range (duration, 0, -1):
        print(remaining, end)


label_1 = tk.Label(root, text="секундомер",
                   font=('Arial', 15),
                   padx=20)
label_1.pack()

frame1 = tk.Frame(root)
frame1.pack(pady=10)  

btn_pause = tk.Button(frame1, text='пауза',
                      command=make_pause)
btn_pause.pack(side="left", padx=10)

btn_reset = tk.Button(frame1, text='сброс',
                      command=make_reset)
btn_reset.pack(side="left", padx=10)

label_2 = tk.Label(root, text="таймер",
                   font=('Arial', 15),
                   padx=20,
                   pady=150)
label_2.pack()




root.mainloop()
