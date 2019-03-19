from KanrenBing.KanrenBingRequest import *
from kanren import *


class KanrenBingRule:
    def __init__(self, request_obj):
        self.request_obj_name = str(request_obj)
        self.request_obj = var(self.request_obj_name)

        self.bing_function = ()
        self.rule_requests = []

    def setup_rule(self, rule_facts, bing_facts):
        for f in rule_facts:
            self.create_kanren_request(f, rule_facts[f], bing_facts)

    def create_kanren_request(self, fact_name, inputs_name, bing_facts):
        self.rule_requests.append(KanrenBingRequest(bing_facts[fact_name], self.get_new_var(inputs_name[0]), self.get_new_var(inputs_name[1])))

    def get_request_command(self):
        c = self.rule_requests[0]

        if len(self.rule_requests) > 1:
            for i in range(len(self.rule_requests) - 1):
                c = conde((c.request, self.rule_requests[i + 1].request))

        return c

    def second_fact_setup(self, fact_name, inputs_name, bing_facts):
        self.bing_function = conde((self.bing_function, fact_name))

    def get_first_function(self, first):
        if first:
            return lambda f_fact_name, f_inputs_name, f_bing_facts: self.create_kanren_request(f_fact_name, f_inputs_name, f_bing_facts)
        else:
            return lambda f_fact_name, f_inputs_name, f_bing_facts: self.second_fact_setup(f_fact_name, f_inputs_name, f_bing_facts)

    def get_new_var(self, token):
        if str(token) != str(self.request_obj_name):
            return var(token)

        return self.request_obj
