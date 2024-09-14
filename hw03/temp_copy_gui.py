import tkinter as tk
from tkinter import simpledialog
from hw02.temp_copy import f2c

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP =int(simpledialog.askinteger(title="온도단위 변환기",prompt="변환시킬 화씨 온도를 입력하시오"))

temp_c = f2c(USER_INP)

print(f"{USER_INP}F => {temp_c:.1f}C")
