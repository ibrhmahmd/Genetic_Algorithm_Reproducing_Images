import numpy
import imageio
import gari
import pygad
import matplotlib.pyplot
import matplotlib.pyplot as plt

# Reading target image
target_im = imageio.imread("PATH")
target_im = numpy.asarray(target_im / 255, dtype=float)

target_chromosome = gari.img2chromosome(target_im)


def fitness_fun(ga_instance, solution, solution_idx):
    # Calculate fitness using a solution and solution_idx
    target_chromosome = gari.img2chromosome(target_im)
    fitness = numpy.sum(numpy.abs(target_chromosome - solution))

    # Negating the fitness value to make it increasing rather than decreasing.
    fitness = numpy.sum(target_chromosome) - fitness
    return fitness


# Define the callback function
def custom_callback(ga_instance):
    print("Generation = {gen}".format(gen=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))

    if ga_instance.generations_completed % 500 == 0:
        matplotlib.pyplot.imsave('solution_' + str(ga_instance.generations_completed) + '.png',
                                 gari.chromosome2img(ga_instance.best_solution()[0], target_im.shape))


# Initialize the GA instance without passing the callback_generation argument
ga_instance = pygad.GA(num_generations=1000,
                       num_parents_mating=10,
                       fitness_func=fitness_fun,
                       sol_per_pop=20,
                       num_genes=target_im.size,
                       init_range_low=0.0,
                       init_range_high=1.0,
                       mutation_percent_genes=0.01,
                       mutation_type="random",
                       mutation_by_replacement=True,
                       random_mutation_min_val=0.0,
                       random_mutation_max_val=1.0,
                       on_generation=custom_callback)  # Assign the custom callback to on_generation

# Run the GA
ga_instance.run()
#
# # Collect fitness values over generations
# fitness_values = ga_instance.best_solution_generation
#
# # Plot fitness values
#
# plt.plot(fitness_values)
# plt.xlabel('Generation')
# plt.ylabel('Fitness Value')
# plt.title('Fitness Value Over Generations')
# plt.show()

# After the generations complete, some plots are showed that summarize how the outputs/fitenss values evolve over
# generations.

# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

if ga_instance.best_solution_generation != -1:
    print("Best fitness value reached after {best_solution_generation} generations.".format(
        best_solution_generation=ga_instance.best_solution_generation))

result = gari.chromosome2img(solution, target_im.shape)
matplotlib.pyplot.imshow(result)
matplotlib.pyplot.title("PyGAD & GARI for Reproducing Images")
matplotlib.pyplot.show()
