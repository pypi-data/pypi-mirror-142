import numpy as np
from backpropagation.Sigmoid import Sigmod

class Backpropagation:
    
    def __init__(self, neuralnet, epochs=2000, lr=0.1, activation_function=Sigmod()):
        self.neuralnet = neuralnet
        self.epochs = epochs
        self.lr = lr
        self.activation_function = activation_function

    def train(self, input, target):
        for i in range(self.epochs):
            hidden_layer = np.dot(input,self.neuralnet.hidden_weights)
            if self.neuralnet.bias:
                hidden_layer += self.neuralnet.hidden_bias_weights
            hidden_layer = self.activation_function.activate(hidden_layer)
            output_layer = np.dot(hidden_layer,self.neuralnet.output_weights)
            if self.neuralnet.bias:
                output_layer += self.neuralnet.output_bias_weights
            output_layer = self.activation_function.activate(output_layer)
            derivative_output = self.activation_function.derivative(output_layer)
            del_k = output_layer * derivative_output * (target - output_layer)
            sum_del_h = del_k.dot(self.neuralnet.output_weights.T)
            derivative_hidden = self.activation_function.derivative(hidden_layer)
            del_h = hidden_layer * derivative_hidden * sum_del_h
            self.neuralnet.output_weights += hidden_layer.T.dot(del_k) * self.lr
            self.neuralnet.hidden_weights += input.T.dot(del_h) * self.lr
        self.output = output_layer
        print(output_layer)
    def predict(self, input):
        pass