from KanrenBing.KanrenBingRequest import *
from kanren import *


class KanrenBingRule:
    def __init__(self, request_obj):
        self.request_obj_name = str(request_obj)
        self.request_obj = var(self.request_obj_name)

        self.bing_function = ()
        self.rule_requests = []

    def run(self, inputs):
        return run(0, self.request_obj, self.get_request_command(inputs))

    def get_request_command(self, inputs):
        c = self.rule_requests[0].get_request(inputs)

        if len(self.rule_requests) > 1:
            for i in range(len(self.rule_requests) - 1):
                c = conde((c, self.rule_requests[i + 1].get_request(inputs)))

        return c

    def setup_rule(self, rule, bing_facts):
        for f in rule.facts:
            self.create_kanren_request(rule.inputs, bing_facts[f], rule.facts[f])

    def create_kanren_request(self, rule_inputs, bing_fact, rule_facts_inputs_names):
        self.rule_requests.append(
            KanrenBingRequest(bing_fact,
                              self.get_new_var(rule_facts_inputs_names[0], rule_inputs),
                              self.get_new_var(rule_facts_inputs_names[1], rule_inputs)))

    def get_new_var(self, token, rule_inputs):

        if token in rule_inputs:
            return token

        if str(token) != str(self.request_obj_name):
            return var(token)

        return self.request_obj
