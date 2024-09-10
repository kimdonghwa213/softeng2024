import tkinter as tk
from tkinter import simpledialog
from lec01.odd_even import is_even

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = int(simpledialog.askstring("Odd Even Test", "Enter number of odd even test"))

if is_even(USER_INP):
    print(f"{USER_INP} is an even number")
else:
    print(f"{USER_INP} is an odd number")
