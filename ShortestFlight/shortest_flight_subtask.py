import heapq as hq
from time import perf_counter


def find_shortest_flight_modified(flights, source, destination, friend_count):
    city_code_to_index = {}
    index = 0
    for flight in flights[:2]:
        for city in flight:
            if city not in city_code_to_index:
                city_code_to_index[city] = index
                index += 1

    if source not in city_code_to_index or destination not in city_code_to_index:
        return 0

    cities = len(city_code_to_index)
    adj_list = [[] for _ in range(cities)]

    for flight in flights:
        src_index = city_code_to_index[flight[0]]
        dest_index = city_code_to_index[flight[1]]
        capacity = int(flight[2])
        adj_list[src_index].append((dest_index, 1, capacity))

    pq = []
    src_index = city_code_to_index[source]
    dst_index = city_code_to_index[destination]

    hq.heappush(pq, (0, src_index, friend_count))

    while pq:
        cost, current, remaining_capacity = hq.heappop(pq)

        if current == dst_index:
            return cost

        for next_index, next_cost, next_capacity in adj_list[current]:
            if next_capacity >= remaining_capacity:
                hq.heappush(pq, (cost + next_cost, next_index, friend_count))

    return 0


if __name__ == '__main__':
    flight_list = [['SOF', 'MLE', 2], ['SOF', 'LON', 3], ['LON', 'MLE', 4]]

    source_city = 'SOF'
    dest_city = 'MLE'
    group_size = 3

    start = perf_counter()
    ans = find_shortest_flight_modified(flight_list, source_city, dest_city, group_size)
    end = perf_counter()

    print("Fastest time:", ans)
    print("Execution time (seconds):", end - start)