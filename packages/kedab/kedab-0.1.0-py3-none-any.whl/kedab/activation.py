from enum import Enum
import numpy as np


class Activation(Enum):
    RELU = 0
    TANH = 1
    SIGMOID = 2
    LINEAR = 3

    @classmethod
    def sigmoid(self, z):
        return 1 / (1 + np.e ** -z)

    @classmethod
    def d_sigmoid(self, z):
        return np.divide(np.exp(-z), np.power(1 + np.exp(-z), 2))

    @classmethod
    def tanh(self, z):
        return np.tanh(z)

    @classmethod
    def d_tanh(self, z):
        return 1 - (np.tanh(z) ** 2)

    @classmethod
    def relu(self, z):
        return max(0.0, z)

    @classmethod
    def d_relu(self, z):
        if z < 0:
            return 0
        elif z == 0:
            raise Exception("RELU is undefined at z=0")
        else:
            return 1


def activate(activation, z):
    match activation:
        case Activation.RELU:
            return activation.relu(z)
        case Activation.TANH:
            return activation.tanh(z)
        case Activation.SIGMOID:
            return activation.sigmoid(z)
        case Activation.LINEAR:
            return z


def d_activate(activation, z):
    match activation:
        case Activation.RELU:
            return activation.d_relu(z)
        case Activation.TANH:
            return activation.d_tanh(z)
        case Activation.SIGMOID:
            return activation.d_sigmoid(z)
        case Activation.LINEAR:
            return z
