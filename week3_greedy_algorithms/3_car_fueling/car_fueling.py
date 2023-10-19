from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    refill_amount = 0
    tank_miles = tank
    new_stops = stops.append(distance - (len(stops) - 1))
    for i in range(len(new_stops) - 2):
        next_stop_distance = new_stops[i + 1]
        tank_miles -= new_stops[1]

        if tank_miles < next_stop_distance:
            if tank_miles + tank > next_stop_distance:
                return -1
            refill_amount += 1
        


    return refill_amount


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
