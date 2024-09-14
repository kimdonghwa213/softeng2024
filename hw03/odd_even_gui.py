import tkinter as tk
from tkinter import simpledialog
from hw02.odd_even import is_even

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP = int(simpledialog.askstring(title="홀짝테스트", prompt="숫자를 입력하시오"))

if is_even(USER_INP):
    print(f"{USER_INP} 은(는) 짝수입니다.")
else:
    print(f"{USER_INP} 은(는) 홀수입니다.")
