from heapq import heappush, heappop
from time import perf_counter


def find_shortest_flight_modified(flights, source, destination, friend_count):
    # Check if arguments are valid
    if not flights:
        raise Exception("Flights not given")
    if type(flights) is not list:
        raise Exception("Flights must be a list")
    if not source:
        raise Exception("Source not given")
    if type(source) is not str:
        raise Exception("Source city code must be a string")
    if not destination:
        raise Exception("Destination not given")
    if type(destination) is not str:
        raise Exception("Destination city code must be a string")
    if friend_count and type(friend_count) is int and friend_count < 1:
        raise Exception("Group size must be a positive integer")

    city_code_to_index = {}
    index = 0
    for flight in flights:
        if len(flight) != 3:
            raise Exception("Flight must contain 3 elements: source, destination, and capacity")
        if type(flight[0]) is not str or type(flight[1]) is not str:
            raise Exception("City code must be a string")
        if type(flight[2]) is not int:
            raise Exception("Capacity must be an integer")
        for city in flight[:2]:
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

    heappush(pq, (0, src_index, friend_count))

    while pq:
        cost, current, remaining_capacity = heappop(pq)

        if current == dst_index:
            return cost

        for next_index, next_cost, next_capacity in adj_list[current]:
            if next_capacity >= remaining_capacity:
                heappush(pq, (cost + next_cost, next_index, friend_count))

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
