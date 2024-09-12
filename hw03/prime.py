import tkinter as tk
from tkinter import simpledialog
from lec01.prime_number import is_prime

ROOT = tk.Tk()

ROOT.withdraw()

USER_INT =int(simpledialog.askinteger("User","Enter a number:"))

primes = []
for i in range(2,USER_INT):
    if is_prime(i):
        primes.append(i)

print(f"{USER_INT}까지의 수 중 소수는 {primes}입니다.")
