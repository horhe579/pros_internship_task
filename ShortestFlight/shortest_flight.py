from heapq import heappush, heappop
from time import perf_counter


def find_shortest_flight(flights, source, destination):

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
        if len(flight) != 2:
            raise Exception("Flight must contain 2 elements: source and destination")
        if type(flight[0]) is not str or type(flight[1]) is not str:
            raise Exception("City code must be a string")
        for city in flight:
            if city not in city_code_to_index:
                city_code_to_index[city] = index
                index += 1

    # Check if the source and destination cities are in the city code dictionary
    # if not the function returns 0

    if source not in city_code_to_index or destination not in city_code_to_index:
        return 0

    # Number of cities
    cities = len(city_code_to_index)
    # Adjacency list for each city index
    adj_list = [[] for _ in range(cities)]

    # Populate the adjacency list
    for flight in flights:
        src_index = city_code_to_index[flight[0]]
        dest_index = city_code_to_index[flight[1]]
        adj_list[src_index].append((dest_index, 1))  # Cost is assumed to be 1 as per the original example

    # Implementing Priority Queue
    pq = []
    src_index = city_code_to_index[source]
    dst_index = city_code_to_index[destination]

    # Start with the source city
    heappush(pq, (0, src_index))

    # Dijkstra's algorithm for finding the shortest path between the nodes(cities)
    while pq:
        cost, current = heappop(pq)

        if current == dst_index:
            return cost

        for next_index, next_cost in adj_list[current]:
            heappush(pq, (cost + next_cost, next_index))

    # If no routes exist, return 0
    return 0


if __name__ == '__main__':
    flight_list = [['SOF', 'IST'], ['IST', 'CMB'], ['CMB', 'MLE']]

    source_city = 'SOF'
    dest_city = 'MLE'

    start = perf_counter()
    ans = find_shortest_flight(flight_list, source_city, dest_city)
    end = perf_counter()

    print("Fastest time:", ans)
    print("Execution time (seconds):", end - start)