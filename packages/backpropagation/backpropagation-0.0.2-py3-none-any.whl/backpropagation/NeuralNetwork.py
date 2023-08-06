import numpy as np

class NeuralNetwork:

    def __init__(self,input,hidden,output):
        self.input = input
        self.hidden = hidden
        self.output = output
    
    def initalize_weights(self, bias=False):
        self.hidden_weights=np.random.uniform(size=(self.input,self.hidden))
        self.output_weights=np.random.uniform(size=(self.hidden,self.output))
        self.bias = False
        if bias:
            self.hidden_bias_weights=np.random.uniform(size=(1,self.hidden))
            self.output_bias_weights=np.random.uniform(size=(1,self.output))
            self.bias = True
        
