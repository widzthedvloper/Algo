from sys import stdin


def min_refills(distance, tank, stops):
    if distance == 0 or tank == 0 or len(stops) == 0:
        return -1
    # write your code here  
    my_reserve = tank
    refill = 0
    for idx, station in enumerate(stops):
        next_stop = 0
        if idx + 1 < len(stops):
            next_stop = stops[idx + 1]
        else:
            next_stop = distance
        
        my_distance = next_stop - station
        my_reserve -= my_distance 
        if (my_reserve + tank) < my_distance:
            return -1 
        if my_distance > my_reserve:
            refill += 1
            my_reserve += tank
    return refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))

# print(min_refills(950, 400, [200,375, 550, 750]))
