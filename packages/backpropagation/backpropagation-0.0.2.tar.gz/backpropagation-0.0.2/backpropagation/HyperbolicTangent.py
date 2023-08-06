import numpy as np

class HyperbolicTangent:
    def activate(self, x):
        numerator = np.exp(x) - np.exp(-x)
        denominator = np.exp(x) + np.exp(-x)
        return numerator / denominator
    
    def derivative(self, x):
        return 1 - (x * x)
