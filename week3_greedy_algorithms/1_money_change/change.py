def change(money):
    # write your code here
    sum = money
    numbre_of_ten = sum // 10
    sum = sum - numbre_of_ten * 10
    number_of_five = sum // 5
    sum = sum - number_of_five * 5
    number_of_one = sum // 1
    return numbre_of_ten + number_of_five + number_of_one


if __name__ == '__main__':
    m = int(input())
    print(change(m))
