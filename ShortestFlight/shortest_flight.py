from heapq import heappop, heappush
from time import perf_counter


def find_shortest_flight(flights, source, destination, friend_count=None):

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

    # A dictionary to map city codes to indices
    city_code_to_index = {}
    index = 0
    for flight in flights:
        # Check if the flight list is valid
        if friend_count and type(friend_count) is int:
            if len(flight) != 3:
                raise Exception("Flight must contain 3 elements: source, destination, and capacity")
            if type(flight[0]) is not str or type(flight[1]) is not str:
                raise Exception("City code must be a string")
            if type(flight[2]) is not int:
                raise Exception("Capacity must be an integer")
        elif not friend_count:
            if len(flight) != 2:
                raise Exception("Flight must contain 2 elements: source and destination")
            if type(flight[0]) is not str or type(flight[1]) is not str:
                raise Exception("City code must be a string")
        else:
            raise Exception("Friend count cannot be less than 1")
        for city in flight[:2]:
            if city not in city_code_to_index:
                city_code_to_index[city] = index
                index += 1

    # Check if the source and destination cities are in the city code dictionary
    # if not the function returns 0

    if source not in city_code_to_index or destination not in city_code_to_index:
        return 0

    # Number of cities
    cities = len(city_code_to_index)
    adj_list = [[] for _ in range(cities)]

    # Populate the adjacency list
    for flight in flights:
        src_index = city_code_to_index[flight[0]]
        dest_index = city_code_to_index[flight[1]]
        # If the flight has a listed capacity we use it
        # otherwise we assume it is the group size
        capacity = None
        if len(flight) == 3:
            capacity = int(flight[2])
        # else:
        #     capacity = friend_count

        adj_list[src_index].append((dest_index, 1, capacity))

    # Implementing Priority Queue
    pq = []
    src_index = city_code_to_index[source]
    dst_index = city_code_to_index[destination]

    # Start with the source city
    heappush(pq, (0, src_index, friend_count))

    # Dijkstra's algorithm for finding the shortest path between the nodes(cities)
    while pq:
        cost, current, remaining_capacity = heappop(pq)

        if current == dst_index:
            return cost

        for next_index, next_cost, next_capacity in adj_list[current]:
            if capacity:
                if next_capacity >= remaining_capacity:
                    heappush(pq, (cost + next_cost, next_index, friend_count))
            else:
                heappush(pq, (cost + next_cost, next_index))

    # If no routes exist, return 0
    return 0


if __name__ == '__main__':
    flight_list = [['SOF', 'MLE', 2], ['SOF', 'LON', 3], ['LON', 'MLE', 4]]

    source_city = 'SOF'
    dest_city = 'MLE'
    group_size = 3

    start = perf_counter()
    try:
        ans = find_shortest_flight(flight_list, source_city, dest_city, group_size)
        print("Fastest time:", ans)
    except Exception as e:
        print(e)
    end = perf_counter()

    print("Execution time (seconds):", end - start)
