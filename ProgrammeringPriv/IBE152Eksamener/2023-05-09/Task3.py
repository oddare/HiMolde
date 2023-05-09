def flightList(cities: list, direct_flights: list, city: str) -> list:
    connections = []
    index = -1

    for n in cities:
        if n == city:
            index = cities.index(n)

    if index != -1:
        for n in range(len(direct_flights[index])):
            if direct_flights[index][n] == 1 and cities[n] != city :
                connections += [cities[n]]

    return connections




cities = ["Seattle", "Denver", "New York", "Chicago"]
direct_flights = [

    [1, 0, 1, 1], # Seattle

    [0, 1, 1, 0], # Denver

    [1, 1, 1, 1], # New York

    [0, 0, 1, 1] # Chicago

]
print(flightList(cities, direct_flights, 'Seattle'))