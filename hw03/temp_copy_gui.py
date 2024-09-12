import tkinter as tk
from tkinter import simpledialog
from lec01.temp_copy import f2c
ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger("User","Enter a number:"))

temp_c = f2c(USER_INT)

print(f"{USER_INT}F => {temp_c:.1f}C")
