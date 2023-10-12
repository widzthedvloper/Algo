import sys
sys.set_int_max_str_digits(0)

def fibonacci_last_digit(n):     
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(2, n + 1):
        previous, current = current, previous + current

    
    return current % 10

def fibo_last_digit(n):
    if n <= 9:
        return n
    
    return n % 10


if __name__ == '__main__':
    n = int(input())
    print(fibonacci_last_digit(n))
