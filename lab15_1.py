
import tkinter as tk

window = tk.Tk()

window.title("Лабораторна робота №15")
window.geometry("600x350")
window.configure(bg="blue")

text_box = tk.Text(
    window,
    width=65,
    height=17,
    font=("Arial", 11)
)

text_box.place(x=15, y=15)

with open("text.txt", "r", encoding="utf-8") as file:
    content = file.read()

text_box.insert("1.0", content)

window.mainloop()
