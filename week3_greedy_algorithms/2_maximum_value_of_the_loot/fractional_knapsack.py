from sys import stdin

def sort_by_fraction(value_pair):
    weight, value = value_pair
    return weight / value

def optimal_value(capacity, weights, values):
    acc_capacity = capacity
    result = 0
    zip_weights_values = list(zip(weights, values))
    zip_weights_values.sort(key=sort_by_fraction, reverse=True)
    for value in zip_weights_values:
        W, V = value
        quantity = min(acc_capacity, V)
        if acc_capacity <= 0:
            return result
        acc_capacity -= quantity
        result += W * (quantity/V)
    return result


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

# print(optimal_value(50, [60,100,120], [20,50,30]))
