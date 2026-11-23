
import tkinter as tk
from tkinter import messagebox


def solve():
    try:
        a = [[float(entries[i][j].get()) for j in range(4)]
             for i in range(3)]

        for i in range(3):
            if a[i][i] == 0:
                for k in range(i + 1, 3):
                    if a[k][i] != 0:
                        a[i], a[k] = a[k], a[i]
                        break

        for i in range(3):
            if a[i][i] == 0:
                raise ValueError("Система не має єдиного розв'язку")

            pivot = a[i][i]

            for j in range(4):
                a[i][j] /= pivot

            for k in range(3):
                if k != i:
                    factor = a[k][i]
                    for j in range(4):
                        a[k][j] -= factor * a[i][j]

        x, y, z = [a[i][3] for i in range(3)]

        result.delete("1.0", tk.END)
        result.insert(
            tk.END,
            f"Результат розв'язання:\n\n"
            f"x = {x:.4f}\n"
            f"y = {y:.4f}\n"
            f"z = {z:.4f}"
        )

    except ValueError as error:
        messagebox.showerror("Помилка", str(error))
    except ZeroDivisionError:
        messagebox.showerror("Помилка", "Неможливо розв'язати систему")


window = tk.Tk()
window.title("Розв'язання системи рівнянь")
window.geometry("500x400")
window.configure(bg="lightblue")

title = tk.Label(
    window,
    text="Система трьох лінійних рівнянь",
    font=("Arial", 14, "bold"),
    bg="lightblue"
)
title.pack(pady=10)

frame = tk.Frame(window, bg="lightblue")
frame.pack()

entries = []

for i in range(3):
    row = []

    for j in range(4):
        entry = tk.Entry(frame, width=8, justify="center")
        entry.grid(row=i, column=j, padx=5, pady=5)
        row.append(entry)

    entries.append(row)

    tk.Label(
        frame,
        text=f"Рівняння {i + 1}",
        bg="lightblue"
    ).grid(row=i, column=4, padx=5)

button = tk.Button(
    window,
    text="Розв'язати",
    command=solve,
    bg="blue",
    fg="white",
    width=20
)
button.pack(pady=15)

result = tk.Text(window, width=40, height=6)
result.pack(pady=5)

window.mainloop()

