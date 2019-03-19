from kanren import *


class KanrenBingRequest:
    def __init__(self, request_obj, input_1, input_2):
        self.request = request_obj(input_1, input_2)
        '''print('---')
        print('Request: ' + str(request_obj))
        print('input_1: ' + str(input_1))
        print('input_2: ' + str(input_2))'''
