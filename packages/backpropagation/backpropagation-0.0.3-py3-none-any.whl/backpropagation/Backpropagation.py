import numpy as np
from backpropagation.Sigmoid import Sigmoid

class Backpropagation:
    
    def __init__(self, neuralnet, epochs=2000, lr=0.1, activation_function=Sigmoid()):
        self.neuralnet = neuralnet
        self.epochs = epochs
        self.lr = lr
        self.activation_function = activation_function
    
    def feedForward(self, input):

        hidden_layer = np.dot(input,self.neuralnet.hidden_weights)
        if self.neuralnet.bias:
            hidden_layer += self.neuralnet.hidden_bias_weights
        hidden_layer = self.activation_function.activate(hidden_layer)
        
        output_layer = np.dot(hidden_layer,self.neuralnet.output_weights)
        if self.neuralnet.bias:
            output_layer += self.neuralnet.output_bias_weights
        output_layer = self.activation_function.activate(output_layer)
        return hidden_layer, output_layer

    def train(self, input, target):
        for _ in range(self.epochs):
            # Feed Forward
            hidden_layer, output_layer = self.feedForward(input)

            #Error term for each output unit k
            derivative_output = self.activation_function.derivative(output_layer)
            del_k = output_layer * derivative_output * (target - output_layer)

            # Error term for each hidden unit h
            sum_del_h = del_k.dot(self.neuralnet.output_weights.T)
            derivative_hidden = self.activation_function.derivative(hidden_layer)
            del_h = hidden_layer * derivative_hidden * sum_del_h

            # Weight Update
            self.neuralnet.output_weights += hidden_layer.T.dot(del_k) * self.lr
            self.neuralnet.hidden_weights += input.T.dot(del_h) * self.lr
    
    def predict(self, input, actual_output):
        hidden_layer, output_layer = self.feedForward(input)
        for i in range(len(input)):
            print(f"For input {input[i]} the predicted output is {output_layer[i][0]} and the actual output is {actual_output[i][0]}")
