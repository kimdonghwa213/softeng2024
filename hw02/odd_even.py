def is_even(n):
    if n % 2 == 0:
        return n

def main():
    n = 10
    if n % 2 == 0:
        print(f"{n}은 짝수입니다.")
    else:
        print(f"{n}은 홀수입니다.")

if __name__ == '__main__':
    main()
