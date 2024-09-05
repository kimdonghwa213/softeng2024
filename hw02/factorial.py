def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    n =5
    print(factorial(n))

if __name__ == '__main__':
    main()
