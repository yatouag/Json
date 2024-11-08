from tkinter import *
import requests as r
from tkinter import filedialog as fd
from tkinter import messagebox as mb

def load_file():
    try:
        file = fd.askopenfilename()
        if file:
            answer = r.post("https://file.io", files={"file": open(file, "rb")})
            print(answer)
            if answer.status_code == 200:
                link_file = (answer.json()["link"])
                e.insert(0, link_file)
            else:
                print("Ошибка")
    except Exception as exc:
        mb.showerror("Ошибка", f"Ошибка: {exc}")

window = Tk()
window.title("Обмен файлами")
window.geometry("300x150")

btn = Button(window, text="Загрузить файл", command=load_file)
btn.pack(pady=10)

e = Entry(window, font=("Arial, 14"))
e.pack(pady=10)





window.mainloop()