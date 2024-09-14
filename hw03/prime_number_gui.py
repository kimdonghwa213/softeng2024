import tkinter as tk
from tkinter import simpledialog
from hw02.prime_number import is_prime

ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger(title="소수 구하기",prompt="숫자를 입력하시오."))

if is_prime(USER_INT):
    print(f"{USER_INT} 은(는) 소수입니다.")
else:
    print(f"{USER_INT} 은(는) 소수가 아닙니다.")
