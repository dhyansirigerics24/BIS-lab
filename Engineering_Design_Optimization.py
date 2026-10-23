import random
import math

# 1. Start

# 2. Define the objective function
# x[0] = radius, x[1] = length

def fitness_function(x):
    r = x[0]
    L = x[1]

    # Surface area of a closed cylindrical vessel
    cost = 2 * math.pi * r * L + 2 * math.pi * r * r

    # Required volume
    volume = math.pi * r * r * L
    required_volume = 1000

    # Penalty for violating the volume constraint
    penalty = 1000 * max(0, required_volume - volume) ** 2

    # PSO maximizes fitness, so return negative cost
    return -(cost + penalty)


# 3. Initialize parameters
NUM_PARTICLES = 30
BOUNDS = [(1, 10), (1, 100)]
INERTIA = 0.7
C1 = 1.5
C2 = 1.5
ITERATIONS = 100


# 4. Initialize particles with random positions and velocities
def initialize_particles():
    positions = []
    velocities = []

    for i in range(NUM_PARTICLES):
        position = [
            random.uniform(BOUNDS[0][0], BOUNDS[0][1]),
            random.uniform(BOUNDS[1][0], BOUNDS[1][1])
        ]

        velocity = [
            random.uniform(-1, 1),
            random.uniform(-1, 1)
        ]

        positions.append(position)
        velocities.append(velocity)

    return positions, velocities


# 5. Evaluate fitness
# 6. Set Pbest and Gbest
def particle_swarm_optimization():
    positions, velocities = initialize_particles()

    pbest_positions = [p[:] for p in positions]
    pbest_fitness = [fitness_function(p) for p in positions]

    best_index = pbest_fitness.index(max(pbest_fitness))
    gbest_position = pbest_positions[best_index][:]
    gbest_fitness = pbest_fitness[best_index]

    # 7–10. Main PSO loop
    for iteration in range(ITERATIONS):
        for i in range(NUM_PARTICLES):
            for d in range(2):
                r1 = random.random()
                r2 = random.random()

                # 7. Update velocity
                velocities[i][d] = (
                    INERTIA * velocities[i][d]
                    + C1 * r1 *
                    (pbest_positions[i][d] - positions[i][d])
                    + C2 * r2 *
                    (gbest_position[d] - positions[i][d])
                )

                # 8. Update position
                positions[i][d] += velocities[i][d]

                # Keep position within bounds
                positions[i][d] = max(
                    BOUNDS[d][0],
                    min(BOUNDS[d][1], positions[i][d])
                )

            # 9. Evaluate new fitness
            current_fitness = fitness_function(positions[i])

            # Update Pbest
            if current_fitness > pbest_fitness[i]:
                pbest_fitness[i] = current_fitness
                pbest_positions[i] = positions[i][:]

            # Update Gbest
            if current_fitness > gbest_fitness:
                gbest_fitness = current_fitness
                gbest_position = positions[i][:]

        # Display output only at multiples of 10
        if (iteration + 1) % 10 == 0:
            print(
                f"Iteration {iteration + 1}: "
                f"Best Cost = {-gbest_fitness:.2f}"
            )

    # 11. Display best solution
    radius = gbest_position[0]
    length = gbest_position[1]
    volume = math.pi * radius**2 * length
    cost = 2 * math.pi * radius * length + 2 * math.pi * radius**2

    print("\nOptimal Engineering Design")
    print(f"Radius       = {radius:.4f}")
    print(f"Length       = {length:.4f}")
    print(f"Volume       = {volume:.4f}")
    print(f"Surface Area = {cost:.4f}")
    print(f"Fitness      = {gbest_fitness:.4f}")


# 12. Stop
if __name__ == "__main__":
    particle_swarm_optimization()
