from kanren import *


class KanrenBing:
    def __init__(self, consult):
        self.consult = consult

        bingFacts = {}
        last_fact = ''
        for f in self.consult.fact_data.facts:
            if f.get_facts()[0] not in bingFacts:
                last_fact = f.get_facts()[0]
                bingFacts[f.get_facts()[0]] = Relation()
            facts(bingFacts[f.get_facts()[0]], (f.get_facts()[1], f.get_facts()[2]))


        x = var()
        y = var()
        z = var()

        print("Last_fact: " + last_fact)
        bFacts = bingFacts[last_fact]

        quest1 = (bFacts(x, "stu"))
        quest2 = (bFacts(x, "prog"))
        c = conde((quest1, quest2))

        result = (run(0, x, bFacts(x, "Enemy_Round")))

        for r in result:
            print(r)
