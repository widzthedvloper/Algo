import random

def lcm(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    assert False

def my_gcd(a, b):

    if b == 0:
        return a
    else:
      return my_gcd(b, a % b)

def my_lcm(a, b):
    result = (a * b) // my_gcd(a, b)
    return result
    
    
def stress_test():
    print("computing.....")
    while True:
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        if lcm(a, b) != my_lcm(a, b):
            print(a, b, "Divergence here!!!!")
            print(lcm(a, b), my_lcm(a, b))
            break
        
        print(a, b)


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(my_lcm(a, b))
    # stress_test()

