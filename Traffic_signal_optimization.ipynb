import random
# 1. Initialize Parameters
POP_SIZE = 30
GENE_LENGTH = 4
MIN_GREEN = 10
MAX_GREEN = 60
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.05
GENERATIONS = 100
CYCLE_LENGTH = 120

# Vehicles arriving per minute on four roads
TRAFFIC_FLOW = [18, 12, 22, 15]


# 2. Create a Chromosome
# Each gene represents the green time for one road
def create_chromosome():
    while True:
        chromosome = [
            random.randint(MIN_GREEN, MAX_GREEN)
            for _ in range(GENE_LENGTH)
        ]

        if sum(chromosome) == CYCLE_LENGTH:
            return chromosome


# 3. Create Initial Population
def create_population():
    return [create_chromosome() for _ in range(POP_SIZE)]


# 4. Calculate Total Waiting Cost
def waiting_cost(chromosome):
    total = 0

    for i in range(GENE_LENGTH):
        green_time = chromosome[i]
        red_time = CYCLE_LENGTH - green_time

        total += TRAFFIC_FLOW[i] * (red_time ** 2) / 2

    return total


# 5. Fitness Function
# Lower waiting cost means higher fitness
def fitness_function(chromosome):
    return -waiting_cost(chromosome)


# 6. Tournament Selection
def selection(population):
    i, j = random.sample(range(len(population)), 2)

    if fitness_function(population[i]) > fitness_function(population[j]):
        return population[i][:]

    return population[j][:]


# 7. Repair Chromosome
# Ensure green times are within limits and sum to 120
def repair(chromosome):
    chromosome = [
        max(MIN_GREEN, min(MAX_GREEN, int(x)))
        for x in chromosome
    ]

    difference = CYCLE_LENGTH - sum(chromosome)

    while difference != 0:
        if difference > 0:
            choices = [
                i for i in range(GENE_LENGTH)
                if chromosome[i] < MAX_GREEN
            ]

            if not choices:
                break

            i = random.choice(choices)
            change = min(difference, MAX_GREEN - chromosome[i])
            chromosome[i] += change
            difference -= change

        else:
            choices = [
                i for i in range(GENE_LENGTH)
                if chromosome[i] > MIN_GREEN
            ]

            if not choices:
                break

            i = random.choice(choices)
            change = min(-difference, chromosome[i] - MIN_GREEN)
            chromosome[i] -= change
            difference += change

    return chromosome


# 8. Single-Point Crossover
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, GENE_LENGTH - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

        return repair(child1), repair(child2)

    return parent1[:], parent2[:]


# 9. Mutation
def mutate(chromosome):
    chromosome = chromosome[:]

    for i in range(GENE_LENGTH):
        if random.random() < MUTATION_RATE:
            chromosome[i] += random.choice([-5, -3, 3, 5])

    return repair(chromosome)


# 10. Main Genetic Algorithm
def genetic_algorithm():
    population = create_population()

    best_solution = min(population, key=waiting_cost)[:]
    best_cost = waiting_cost(best_solution)

    for generation in range(GENERATIONS):

        # Evaluate and sort population
        population.sort(key=fitness_function, reverse=True)

        # Elitism: preserve the best individual
        next_population = [population[0][:]]

        # Selection, crossover and mutation
        while len(next_population) < POP_SIZE:
            parent1 = selection(population)
            parent2 = selection(population)

            child1, child2 = crossover(parent1, parent2)

            next_population.append(mutate(child1))

            if len(next_population) < POP_SIZE:
                next_population.append(mutate(child2))

        population = next_population

        # Update the best solution
        current_best = min(population, key=waiting_cost)
        current_cost = waiting_cost(current_best)

        if current_cost < best_cost:
            best_solution = current_best[:]
            best_cost = current_cost

        if (generation + 1) % 10 == 0:
            print(
                f"Generation {generation + 1}: "
                f"Best Waiting Cost = {best_cost:.2f}"
            )

    # 11. Display Results
    roads = [
        "North-South Road 1",
        "East-West Road 1",
        "North-South Road 2",
        "East-West Road 2"
    ]

    print("\nOPTIMIZED TRAFFIC SIGNAL TIMINGS")

    for road, green_time in zip(roads, best_solution):
        print(f"{road}: {green_time} seconds")

    print("\nTotal Cycle Length:", sum(best_solution), "seconds")
    print("Minimum Estimated Waiting Cost:", round(best_cost, 2))

    return best_solution


# 12. Execute
if __name__ == "__main__":
    random.seed(42)
    genetic_algorithm()
