import tkinter as tk
from tkinter import simpledialog
from lec01.odd_even import is_even

def is_odd(n):
    if n % 2 == 1:
        return n

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = int(simpledialog.askstring("홀짝테스트", "숫자를 입력하시오"))

if is_even(USER_INP):
    print(f"{USER_INP} 은(는) 짝수입니다.")
elif is_odd(USER_INP):
    print(f"{USER_INP} 은(는) 홀수입니다.")
else:
    print(f"{USER_INP} is 0")
