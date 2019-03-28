from KanrenBing.KanrenBingRule import *
from kanren import *


class KanrenBing:
    def __init__(self, consult):
        self.consult = consult

        bing_facts = {}
        bing_rules = {}

        for f in self.consult.fact_data.facts:
            if f.get_fact()[0] not in bing_facts:
                bing_facts[f.get_fact()[0]] = Relation()
            facts(bing_facts[f.get_fact()[0]], (f.get_fact()[1], f.get_fact()[2]))

        for rule in self.consult.rule_data.rules:
            exist = True

            for f in rule.facts:
                if f not in bing_facts:
                    exist = False
                    KanrenBing.error_rule(rule.rule_name, f)
                    break

            if exist:
                if rule.rule_name not in bing_rules:
                    bing_rules[rule.rule_name] = KanrenBingRule(rule.get_return_var())
                    bing_rules[rule.rule_name].setup_rule(rule.facts, bing_facts)

        self.rules = bing_rules
        self.facts = bing_facts

    @staticmethod
    def normalize_result(result):
        if len(result) > 1:
            print('Results ' + str(len(result)) + ':')
            for re in result:
                print(re)
        else:
            print('Result: ' + str(result))

    @staticmethod
    def error_rule(rule_name, f):
        print('<>' * 3)
        print('The Rule ' + rule_name + '\'s fact: \'' + f + '\' dont exists')
