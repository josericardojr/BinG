from kanren import *


class KanrenBingRequest:
    def __init__(self, f, input_1, input_2):
        self.fact = f
        self.input_1 = input_1
        self.input_2 = input_2

    def get_request(self, inputs):
        input_1 = self.input_1
        input_2 = self.input_2

        for inp in inputs:
            if str(inp) == input_1:
                input_1 = inputs[inp]
            if str(inp) == input_2:
                input_2 = inputs[inp]

        return self.fact(input_1, input_2)
