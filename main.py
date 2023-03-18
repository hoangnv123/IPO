import math
import random

data_base = [[1, 3, 2], [1, 4, 3], [1, 5, 6], [1, 6, 5], [1, 7, 6], [1, 8, 7], [1, 9, 8], [2, 3, 1], [2, 5, 3],
             [2, 7, 5]]


def active_func(x):
    return (math.exp(2*x) - 1) / (math.exp(2*x) + 1)


def resolve_quadratic_equation(a: int, b: int, c: int):
    delta = b**2 - 4*a*c
    if delta < 0:
        return [0, 0]
    else:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        return [x1, x2]


class Neural:
    def __init__(self, id, input_data, bias, active_function):
        self.id = id
        self.bias = bias
        self.active_function = active_function
        self.input_data = input_data

    def get_output(self):
        return self.active_function(self.input_data + self.bias)


class Edge:
    def __init__(self, left, right, weight):
        self.left = left
        self.right = right
        self.weight = weight


class Neural_Network:
    list_neural = [[Neural(i + 1, 0, 0, active_func) for i in range(3)],
                   [Neural(i + 1, 0, 0, active_func) for i in range(3, 6)],
                   [Neural(i + 1, 0, 0, active_func) for i in range(6, 8)],
                   [Neural(i + 1, 0, 0, active_func) for i in range(8, 10)],
                   [Neural(i + 1, 0, 0, active_func) for i in range(10, 12)]]

    list_edges = [[Edge(1, 4, random.random()), Edge(2, 5, random.random()), Edge(3, 6, random.random())],
                  [Edge(4, 7, random.random()), Edge(4, 8, random.random()), Edge(5, 7, random.random()), Edge(6, 8, random.random())],
                  [Edge(7, 9, random.random()), Edge(7, 10, random.random()), Edge(8, 10, random.random())],
                  [Edge(9, 11, random.random()), Edge(10, 12, random.random())]]

    def __init__(self, input_parameters):
        self.input_parameters = input_parameters
        self.list_neural[0][0].input_data = input_parameters[0]
        self.list_neural[0][1].input_data = input_parameters[1]
        self.list_neural[0][2].input_data = input_parameters[2]

        for i in range(1, len(self.list_neural)):
            for j in self.list_neural[i]:
                edges_to_this_neural = []
                for k in self.list_edges[i - 1]:
                    if k.right == j.id:
                        edges_to_this_neural.append(k)

                neural_to_this_neural = []
                for y in edges_to_this_neural:
                    for x in self.list_neural[i - 1]:
                        if x.id == y.left:
                            neural_to_this_neural.append(x)

                for k in range(len(neural_to_this_neural)):
                    j.input_data += neural_to_this_neural[k].get_output() * edges_to_this_neural[k].weight


    def get_output(self):
        return [self.list_neural[-1][0].get_output(), self.list_neural[-1][1].get_output()]


print(Neural_Network([1, 2, 3]).get_output())



