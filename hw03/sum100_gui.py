import tkinter as tk
from tkinter import simpledialog
from hw02.odd_even import is_even

ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger(title="짝수의 합 구하기",prompt="숫자를 입력하시오"))

total = 0

for i in range(1, USER_INT+1):
    if is_even(i):
        total += i
print(f"1부터 {USER_INT}까지 짝수의 합은 {total}입니다.")

even_sum = [i for i in range(1, USER_INT+1) if i % 2 == 0]
print(even_sum)
