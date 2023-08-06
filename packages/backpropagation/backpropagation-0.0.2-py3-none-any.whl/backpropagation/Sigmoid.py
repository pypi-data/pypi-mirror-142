import numpy as np

class Sigmoid:
    def activate(self, x):
        return 1/(1 + np.exp(-x))
    def derivative(self, x):
        return x * (1 - x)