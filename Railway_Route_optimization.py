
import math
import random

# STEP 1: Define railway stations and coordinates
cities = {
    "Bangalore": (12.9716, 77.5946),
    "Chennai": (13.0827, 80.2707),
    "Hyderabad": (17.3850, 78.4867),
    "Mumbai": (19.0760, 72.8777),
    "Pune": (18.5204, 73.8567),
    "Delhi": (28.6139, 77.2090)
}

city_names = list(cities.keys())
n = len(city_names)

# STEP 2: Initialize ACO parameters
num_ants = 20
alpha = 1
beta = 5
rho = 0.5
Q = 100
iterations = 100

# STEP 3: Calculate distance using Haversine formula
def calculate_distance(city1, city2):

    lat1, lon1 = cities[city1]
    lat2, lon2 = cities[city2]

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1) * math.cos(lat2) *
         math.sin(dlon / 2) ** 2)

    distance = 6371 * 2 * math.asin(math.sqrt(a))

    return distance


# Create distance matrix
distance = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        distance[i][j] = calculate_distance(
            city_names[i], city_names[j]
        )


# STEP 4: Initialize pheromone values
pheromone = [[1.0] * n for _ in range(n)]

# Store the best route
best_route = None
best_distance = float('inf')


# STEP 5: ACO iterations
for iteration in range(iterations):

    all_routes = []

    # Each ant constructs a railway route
    for ant in range(num_ants):

        start = random.randint(0, n - 1)

        route = [start]

        unvisited = list(range(n))
        unvisited.remove(start)

        # Visit all remaining stations
        while unvisited:

            current = route[-1]

            probabilities = []

            for city in unvisited:

                pheromone_value = (
                    pheromone[current][city] ** alpha
                )

                heuristic_value = (
                    (1 / distance[current][city]) ** beta
                )

                probability = (
                    pheromone_value * heuristic_value
                )

                probabilities.append(probability)

            # Calculate selection probabilities
            total = sum(probabilities)

            probabilities = [
                p / total for p in probabilities
            ]

            # Select next station
            next_city = random.choices(
                unvisited,
                weights=probabilities,
                k=1
            )[0]

            route.append(next_city)
            unvisited.remove(next_city)

        # Calculate total route distance
        total_distance = 0

        for i in range(n - 1):
            total_distance += distance[
                route[i]
            ][
                route[i + 1]
            ]

        # Return to starting station
        total_distance += distance[route[-1]][route[0]]

        all_routes.append((route, total_distance))

        # Update global best route
        if total_distance < best_distance:

            best_distance = total_distance
            best_route = route.copy()

    # STEP 6: Evaporate pheromones
    for i in range(n):
        for j in range(n):

            pheromone[i][j] *= (1 - rho)

    # STEP 7: Deposit pheromones
    for route, route_distance in all_routes:

        deposit = Q / route_distance

        for i in range(n):

            city1 = route[i]
            city2 = route[(i + 1) % n]

            pheromone[city1][city2] += deposit
            pheromone[city2][city1] += deposit


# STEP 8: Display best railway route
print("\n===== RAILWAY ROUTE OPTIMIZATION =====")

print("\nBest Railway Route:")

for city in best_route:
    print(city, end=" -> ")

print(best_route[0])

print("\n\nMinimum Total Distance:",
      round(best_distance, 2), "km")

print("\nOptimization Completed!")
