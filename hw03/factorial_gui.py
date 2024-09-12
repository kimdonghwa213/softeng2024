import tkinter as tk
from tkinter import simpledialog
from lec01.factorial import factorial

ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger("User","Enter a number:"))

print(f"{USER_INT}! = {factorial(USER_INT)} 입니다.")
