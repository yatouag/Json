from tkinter import *
import requests as r
from tkinter import filedialog as fd
from tkinter import messagebox as mb
import pyperclip
import os
import  json


def save_file(path_file, link_file, name_file):
    history = []
    if os.path.exists("History.json"):
        with open("History.json", "r", encoding="utf-8") as f:
            history = json.load(f)

    history.append({"path_file": path_file, "name_file": name_file, "link_file": link_file})

    with open("History.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)



def load_file():
    try:
        file = fd.askopenfilename()
        if file:
            answer = r.post("https://file.io", files={"file": open(file, "rb")})
            print(answer)
            if answer.status_code == 200:
                link_file = answer.json()["link"]
                name_file = answer.json()["name"]
                e.delete(0, END)
                e.insert(0, link_file)
                pyperclip.copy(link_file)
                save_file(file, link_file, name_file)
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