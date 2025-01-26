#SIYAVASH
#وارد کردن کتابخونه ها 
#massagebox for error , simpledilog for input
import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

#ذخیره سازی اطلاعات
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "tasks.json")
#رنگا
#انگار که کلاس رنگا با رابط گرافیکی نمیخونه
class color:
    Ghermez= '\033[91m'
    Abi='\x1b[94m'
    Banafsh='\033[95m'
    Sabz='x1b[92m'
    END='\033[0m'
class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TO DO LIST")
        self.tasks = self.load_tasks()
        self.listbox = tk.Listbox(root, width=50, height=15)
        self.listbox.pack(pady=10)
        # دکمه‌ها
        btn_frame = tk.Frame(root)
        btn_frame.pack()
        tk.Button(btn_frame, text="افزودن", command=self.add_task).grid(row=0, column=0)
        tk.Button(btn_frame, text="ویرایش", command=self.edit_task).grid(row=0, column=1)
        tk.Button(btn_frame, text="انجام", command=self.mark_done).grid(row=0, column=2)
        tk.Button(btn_frame, text="حذف", command=self.delete_task).grid(row=0, column=3)

        self.load_listbox()

    def load_tasks(self):
        """بارگذاری کارها از فایل JSON"""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        return []

    def save_tasks(self):
        """ذخیره کارها در فایل JSON"""
        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(self.tasks, file, ensure_ascii=False, indent=4)

    def load_listbox(self):
        """بارگذاری داده‌ها در لیست‌باکس"""
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✅" if task["done"] else "⬜"
            self.listbox.insert(tk.END, f"{status} {task['title']}")

    def add_task(self):
        """افزودن کار جدید"""
        title = simpledialog.askstring("افزودن کار", "عنوان کار:")
        if title:
            self.tasks.append({"title": title, "done": False})
            self.save_tasks()
            self.load_listbox()

    def edit_task(self):
        """ویرایش کار انتخاب شده"""
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("خطا", "لطفاً یک کار را انتخاب کنید!")
            return

        index = selected_index[0]
        new_title = simpledialog.askstring("ویرایش کار", "عنوان جدید:", initialvalue=self.tasks[index]["title"])
        if new_title:
            self.tasks[index]["title"] = new_title
            self.save_tasks()
            self.load_listbox()

    def mark_done(self):
        """علامت‌گذاری کار به عنوان انجام‌شده"""
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("خطا", "لطفاً یک کار را انتخاب کنید!")
            return

        index = selected_index[0]
        self.tasks[index]["done"] = not self.tasks[index]["done"]
        self.save_tasks()
        self.load_listbox()

    def delete_task(self):
        """حذف کار انتخاب شده"""
        selected_index = self.listbox.curselection()
        if not selected_index:
            messagebox.showwarning("خطا", "لطفاً یک کار را انتخاب کنید!")
            return

        index = selected_index[0]
        del self.tasks[index]
        self.save_tasks()
        self.load_listbox()

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
#SIYAVASH