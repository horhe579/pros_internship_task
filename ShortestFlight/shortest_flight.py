import heapq as hq
from time import perf_counter


def find_shortest_flight(flights, source, destination):
    # A dictionary to map city codes to indices
    city_code_to_index = {}
    index = 0
    for flight in flights:
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
    hq.heappush(pq, (0, src_index))

    # Dijkstra's algorithm for finding the shortest path between the nodes(cities)
    while pq:
        cost, current = hq.heappop(pq)

        if current == dst_index:
            return cost

        for next_index, next_cost in adj_list[current]:
            hq.heappush(pq, (cost + next_cost, next_index))

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