import numpy as np
import matplotlib.pyplot as plt

def fitness_function(x):
    return 1 - x**2

def binary_to_real(binary_str):
    return -5 + 10 * int(''.join(binary_str), 2) / (2**10 - 1)

def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    child1 = ''.join(parent1[:crossover_point]) + ''.join(parent2[crossover_point:])
    child2 = ''.join(parent2[:crossover_point]) + ''.join(parent1[crossover_point:])
    return child1, child2

def mutation(chromosome, mutation_rate):
    mutated_chromosome = ''
    for bit in chromosome:
        if np.random.rand() < mutation_rate:
            mutated_chromosome += '0' if bit == '1' else '1'
        else:
               mutated_chromosome += bit
    return mutated_chromosome

population_size = 10
chromosome_length = 10
population = [np.random.choice(['0', '1'], size=chromosome_length) for _ in range(population_size)]

num_generations = 100
best_fitnesses = []
average_fitnesses = []

for generation in range(num_generations):
    
    fitness_scores = [fitness_function(binary_to_real(chromosome)) for chromosome in population]
    best_fitness = max(fitness_scores)
    average_fitness = np.mean(fitness_scores)
    best_fitnesses.append(best_fitness)
    average_fitnesses.append(average_fitness)

    print(f"Generation {generation + 1}: Best Fitness = {best_fitness}, Average Fitness = {average_fitness}")

    
    fitness_scores = np.array(fitness_scores) + np.abs(np.min(fitness_scores)) + 0.01

    
    normalized_fitness = np.array(fitness_scores) / np.sum(fitness_scores)

    
    parent_indices = np.random.choice(range(population_size), size=2, p=normalized_fitness, replace=False)
    parent1 = population[parent_indices[0]]
    parent2 = population[parent_indices[1]]

    child1, child2 = crossover(parent1, parent2)

    child1 = mutation(child1, mutation_rate=0.01)
    child2 = mutation(child2, mutation_rate=0.01)

    
    worst_index1 = np.argmin(fitness_scores)
    population[worst_index1] = child1
    worst_index2 = np.argmin([fitness_function(binary_to_real(chromosome)) for chromosome in population])
    population[worst_index2] = child2

    print(f"Defined 10-bit chromosome: {population[worst_index1]}")


best_solution_index = np.argmax([fitness_function(binary_to_real(chromosome)) for chromosome in population])
best_solution = binary_to_real(population[best_solution_index])
print(f"The final value of x that maximizes f(x) is: {best_solution}")


plt.figure(figsize=(10, 6))
plt.plot(range(num_generations), best_fitnesses, label='Best Fitness')
plt.plot(range(num_generations), average_fitnesses, label='Average Fitness')
plt.xlabel('Generation')
plt.ylabel('Fitness')
plt.title('Genetic Algorithm for Maximizing f(x) = 1 - x^2')
plt.legend()
plt.grid(True)
plt.show()