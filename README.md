# Genetic_Algorithm_Reproducing_Images



# Image Reproduction Using Genetic Algorithm

This project demonstrates the use of a genetic algorithm (GA) to reproduce an image. The implementation utilizes the `pygad` library for the genetic algorithm, the `gari` library for image-to-chromosome conversion, and `matplotlib` for visualization. The aim is to generate an image that closely resembles a target image through evolutionary processes.

## Project Overview

The project involves the following steps:

1. **Reading and Normalizing the Target Image**: The target image is read from a file and normalized to have pixel values between 0 and 1.
2. **Chromosome Representation**: The image is converted into a chromosome representation for the genetic algorithm.
3. **Fitness Function**: A fitness function evaluates each solution (image) based on its similarity to the target image.
4. **Genetic Algorithm Configuration**: The GA is configured with specific parameters, such as the number of generations, number of parents mating, mutation rates, etc.
5. **Custom Callback Function**: A callback function saves the best solution image at intervals and prints the generation number and fitness value.
6. **Running the GA**: The GA is executed, evolving the population over generations to find the best solution.
7. **Visualization**: The best solution is converted back to an image and displayed. A plot summarizing the fitness values over generations is also generated.

## Requirements

- Python 3.x
- numpy
- imageio
- gari
- pygad
- matplotlib

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/image-reproduction-ga.git
   cd image-reproduction-ga
   ```

2. Install the required libraries:
   ```bash
   pip install numpy imageio gari pygad matplotlib
   ```

## Usage

1. Place your target image in the specified path.
2. Modify the image path in the code if necessary:
   ```python
   target_im = imageio.imread("path_to_your_image.jpg")
   ```
3. Run the Jupyter notebook or the Python script to start the genetic algorithm:
   ```bash
   jupyter notebook image_reproduction_ga.ipynb
   ```
   or
   ```bash
   python image_reproduction_ga.py
   ```

## Files

- `image_reproduction_ga.ipynb`: Jupyter notebook with a detailed explanation and implementation of the project.
- `image_reproduction_ga.py`: Python script for the project.
- `README.md`: This file.

## Example

An example target image and the resulting images at different generations will be saved in the working directory. The fitness values over generations will be plotted to show the progress of the GA.

## License

This project is licensed under the MIT License.

## Acknowledgments

- The `pygad` library for providing an easy-to-use framework for genetic algorithms.
- The `gari` library for facilitating image-to-chromosome conversions.
- The `matplotlib` library for visualization.

---

Feel free to open issues or pull requests if you have any suggestions or improvements!
