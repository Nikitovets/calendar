import tkinter as tk
from tkinter import messagebox
from datetime import datetime

#Список для збереження подій
events = []

def add_event():
    title = title_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    if not title or not date or not time:
        messagebox.showwarning("Помилка", "Заповніть усі поля!")
        return

    try:
        datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
    except ValueError:
        messagebox.showerror("Невірний формат", "Використовуйте формат дати YYYY-MM-DD та часу HH:MM.")
        return

    event = f"{date} {time} - {title}"
    events.append(event)
    update_event_list()
    clear_entries()

def update_event_list():
    event_list.delete(0, tk.END)
    for event in sorted(events):
        event_list.insert(tk.END, event)

def clear_entries():
    title_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

#--- Графічний інтерфейс ---
root = tk.Tk()
root.title("Планувальник подій")

tk.Label(root, text="Назва події:").grid(row=0, column=0, sticky="e")
title_entry = tk.Entry(root, width=30)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Дата (YYYY-MM-DD):").grid(row=1, column=0, sticky="e")
date_entry = tk.Entry(root, width=30)
date_entry.grid(row=1, column=1)

tk.Label(root, text="Час (HH:MM):").grid(row=2, column=0, sticky="e")
time_entry = tk.Entry(root, width=30)
time_entry.grid(row=2, column=1)

add_button = tk.Button(root, text="Додати подію", command=add_event)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

event_list = tk.Listbox(root, width=50)
event_list.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
#17 апреля 2025 г.
