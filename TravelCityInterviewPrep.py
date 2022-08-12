def solution(fuel_arr, dist_arr):
    n = len(fuel_arr)
    trips = dict()
    for i in range(n):
        trips[(i, i, i)] = fuel_arr[i]
    max_towns = 1
    for _ in range(n):
        new_trips = dict()
        for k, cur_fuel in trips.items():
            start, end, cur_town = k
            if start - 1 >= 0 and abs(dist_arr[cur_town] - dist_arr[start - 1]) <= cur_fuel:
                new_start = start - 1
                new_fuel = cur_fuel - abs(dist_arr[cur_town] - dist_arr[start - 1]) + fuel_arr[new_start]
                new_key = (new_start, end, new_start)
                if new_key not in new_trips:
                    max_towns = max(max_towns, end - new_start + 1)
                    new_trips[new_key] = new_fuel
                else:
                    new_trips[new_key] = max(new_trips[new_key], new_fuel)
            if end + 1 < n and abs(dist_arr[end + 1] - dist_arr[cur_town]) <= cur_fuel:
                new_end = end + 1
                new_key = (start, new_end, new_end)
                new_fuel = cur_fuel - abs(dist_arr[new_end] - dist_arr[cur_town]) + fuel_arr[new_end]
                if new_key not in new_trips:
                    max_towns = max(max_towns, new_end - start + 1)
                    new_trips[new_key] = new_fuel
                else:
                    new_trips[new_key] = max(new_trips[new_key], new_fuel)
        trips = new_trips
    return max_towns


solution([4, 1, 4, 3, 3], [8, 10, 11, 13, 100])
