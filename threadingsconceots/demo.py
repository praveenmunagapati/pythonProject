
import time
import random
from datetime import timedelta
start_time = time.monotonic()
#print(random.randrange(1000))
listrandomints = [random.randrange(1000000) for i in range(1000000) ]
listrandomints = sorted(listrandomints)
#print(listrandomints)
end_time = time.monotonic()
print(timedelta(seconds=end_time - start_time))

import timeit

# print addition of first 1 million numbers
def addition():
    print('Addition:', sum(range(100000)))

# run same code 5 times to get measurable data
n = 5

# calculate total execution time
result = timeit.timeit(stmt='addition()', globals=globals(), number=n)

# calculate the execution time
# get the average execution time
print(f"Execution time is {result / n} seconds")


import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        for pattern in patterns:
            pattern = np.array(pattern).reshape((self.size, 1))
            self.weights += np.dot(pattern, pattern.T)
            np.fill_diagonal(self.weights, 0)

    def recall(self, pattern, max_iterations=100):
        pattern = np.array(pattern).reshape((self.size, 1))
        for _ in range(max_iterations):
            energy = -0.5 * np.dot(pattern.T, np.dot(self.weights, pattern))
            new_pattern = np.sign(np.dot(self.weights, pattern))
            if np.array_equal(pattern, new_pattern):
                return new_pattern.flatten()
            pattern = new_pattern
        print("Max iterations reached. Convergence not achieved.")
        return pattern.flatten()

# Example usage
if __name__ == "__main__":
    # Create a Hopfield Network with 5 neurons
    hopfield_net = HopfieldNetwork(5)

    # Define some patterns to train the network
    patterns = [[1, 1, -1, -1, 1],
                [-1, 1, -1, 1, -1],
                [-1, -1, 1, -1, -1]]

    # Train the network with the defined patterns
    hopfield_net.train(patterns)

    # Test recall with a corrupted version of a pattern
    test_pattern = [1, 1, 1, -1, -1]
    recalled_pattern = hopfield_net.recall(test_pattern)
    print("Recalled Pattern:", recalled_pattern)

import numpy as np
import matplotlib.pyplot as plt

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((size, size))

    def train(self, patterns):
        for pattern in patterns:
            pattern = np.array(pattern).reshape((self.size, 1))
            self.weights += np.dot(pattern, pattern.T)
            np.fill_diagonal(self.weights, 0)

    def recall(self, pattern, max_iterations=100):
        pattern = np.array(pattern).reshape((self.size, 1))
        for _ in range(max_iterations):
            energy = -0.5 * np.dot(pattern.T, np.dot(self.weights, pattern))
            new_pattern = np.sign(np.dot(self.weights, pattern))
            if np.array_equal(pattern, new_pattern):
                return new_pattern.flatten()
            pattern = new_pattern
        print("Max iterations reached. Convergence not achieved.")
        return pattern.flatten()

def plot_patterns(patterns, titles):
    num_patterns = len(patterns)
    fig, axes = plt.subplots(1, num_patterns, figsize=(4*num_patterns, 4))
    for i, pattern in enumerate(patterns):
        pattern = np.array(pattern).reshape((3, 3))
        axes[i].imshow(pattern, cmap='binary', interpolation='nearest')
        axes[i].set_title(titles[i])
        axes[i].set_xticks([])
        axes[i].set_yticks([])
    plt.show()

# Generate random binary patterns
def generate_random_patterns(num_patterns, size):
    patterns = []
    for _ in range(num_patterns):
        pattern = np.random.choice([-1, 1], size)
        patterns.append(pattern)
    return patterns

# Example usage
if __name__ == "__main__":
    # Create a Hopfield Network with 9 neurons
    hopfield_net = HopfieldNetwork(9)

    # Generate and train the network with random binary patterns
    num_patterns = 3
    patterns = generate_random_patterns(num_patterns, 9)
    hopfield_net.train(patterns)

    # Test recall with a corrupted version of a random pattern
    test_pattern_index = np.random.randint(num_patterns)
    test_pattern = patterns[test_pattern_index]
    recalled_pattern = hopfield_net.recall(test_pattern)

    # Plot original pattern and recalled pattern
    plot_patterns([test_pattern, recalled_pattern], ["Original Pattern", "Recalled Pattern"])
