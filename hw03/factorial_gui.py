import tkinter as tk
from tkinter import simpledialog
from lec01.factorial import factorial

ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger("팩토리얼 구하기","숫자를 입력하시오."))

print(f"{USER_INT}! = {factorial(USER_INT)} 입니다.")
