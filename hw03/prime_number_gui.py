import tkinter as tk
from tkinter import simpledialog
from lec01.prime_number import is_prime
ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger("User","Enter a number:"))

if is_prime(USER_INT):
    print(f"{USER_INT} is a prime number")
else:
    print(f"{USER_INT} is not a prime number")
