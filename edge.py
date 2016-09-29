
from outNode import OutNode

class Edge:
    def __init__(self, out_value, weight):

        self.learning_rate = 0.5
        self.weight = weight
        out = OutNode(out_value)


    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_learning(self):
        return self.learning_rate