from kanren import *


class KanrenBingRequest:
    def __init__(self, request_obj, input_1, input_2):
        self.request = request_obj(input_1, input_2)
