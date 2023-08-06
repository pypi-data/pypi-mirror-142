# Backpropagation
This module contains the implementation of the backpropagation algorithm

# Usage
```python
    from backpropagation.NeuralNetwork import NeuralNetwork

    from backpropagation.Backpropagation import Backpropagation
    from backpropagation.HyperbolicTangent import HyperbolicTangent
    from backpropagation.ReLU import ReLU
    from backpropagation.Sigmoid import Sigmoid

    nn = NeuralNetwork(input_units, hidden_units, output_units)
    nn.initalize_weights(bais -> boolean)

    bp = Backpropagation(NeuralNetwork, epochs, learning_rate, activation_fuction)
    bp.train(input, target)
    bp.predict(input, actual_output)
```