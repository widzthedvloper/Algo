def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibo_number(n):
    arr = [None for i in range(n + 1)]
    if n <= 1:
        return n
    arr[0] = 0
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i -1] + arr[i - 2]

    return arr[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibo_number(input_n))
