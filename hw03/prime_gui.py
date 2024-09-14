import tkinter as tk
from tkinter import simpledialog
from hw02.prime_number import is_prime

ROOT = tk.Tk()

ROOT.withdraw()

USER_INP =int(simpledialog.askinteger(title="범위의 소수 구하기",prompt="숫자를 입력하시오."))

primes = []
for i in range(2,USER_INP):
    if is_prime(i):
        primes.append(i)

print(f"1부터 {USER_INP}까지의 수 중 소수는 {primes}입니다.")
