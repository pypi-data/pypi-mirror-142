"""
Simple Neural Network with 1 input layer, 2-node hidden layer and 1 output layer
4 weight parameters, no biases.
"""

import numpy as np


class neural_network:
    def __init__(self, t, data, std=1):
        self.t = np.array(t)
        self.data = np.array(data)
        self.std = std

    def predictions(self, theta):
        n11 = np.tanh(self.t)  # Layer 1
        n21 = np.tanh(theta[0] * n11)
        n22 = np.tanh(theta[1] * n11)
        n31 = np.tanh(theta[2] * n21 + theta[3] * n22)
        return n31

    def residuals(self, theta):
        if all(0 < theta) and all(theta < 20):
            return (self.predictions(theta) - self.data) / self.std
        else:
            return np.repeat(np.inf, len(self.data))

    def cost(self, theta):
        return np.sum(self.residuals(theta) ** 2) / 2
