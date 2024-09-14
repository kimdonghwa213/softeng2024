import tkinter as tk
from tkinter import simpledialog
from hw02.factorial import factorial

ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger(title="팩토리얼 구하기",prompt="숫자를 입력하시오."))

print(f"{USER_INT}! = {factorial(USER_INT)} 입니다.")
