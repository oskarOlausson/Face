
from outNode import OutNode
from constants import Constants

class Edge:
    def __init__(self, out_value, weight, constants):
        self.learning_rate = constants.get_learning_rate()
        self.weight = weight
        self.out = OutNode(out_value)

    def get_weight(self):
        return self.weight

    def calculate_weight(self, input, facit):
        weight = (self.out.get_value() - facit) * self.out.get_value() * (1 - self.out.get_value()) * input
        self.weight -= (weight * self.learning_rate)

    def get_learning(self):
        return self.learning_rate