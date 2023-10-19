from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    cap = capacity
    # write your code here
    values_per_weights = {}
    values_per_weights_arr = []
    for i in range(len(weights)):
        val_per_weight = values[i] / weights[i]
        values_per_weights_arr.append(val_per_weight)
        values_per_weights[val_per_weight] = [values[i], weights[i]]

    values_per_weights_arr.sort()

    for val_per_w in values_per_weights_arr:
        val, wei = values_per_weights[val_per_w]
        if wei <= cap and cap < 0:
            value += wei * val_per_w
            cap -= val
        elif wei > cap:
            value += cap * val_per_w
            cap = 0

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
