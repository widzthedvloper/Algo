def gcd(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd

def my_gcd(a, b):
    numerator = a
    denominator = b

    result = numerator % denominator

    if result == 0:
        return denominator
    else:
      return my_gcd(denominator, result)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(my_gcd(a, b))
