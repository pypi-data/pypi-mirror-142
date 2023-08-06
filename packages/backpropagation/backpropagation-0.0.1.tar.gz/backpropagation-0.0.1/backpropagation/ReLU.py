class ReLU:
    def activate(self, x):
        return x * (x > 0)
    def derivative(self, x):
        return 1. * (x > 0) 