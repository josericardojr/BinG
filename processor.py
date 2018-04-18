from kanren import Relation, facts, var, run
from Loader import *
from LoadedXML import *

diffLowerFactor = Relation()
diffRiseFactor = Relation()
minRiseHappenings = Relation()

#infos retiradas do xml

#numero de hits em ordem de tipo de inimigo
hits = range(4);
#numero de usos de ataque em ordem de tipo de inimigo
happenings = range(4);

#BASEAR EM TEMPO

#infos estabelecidas aqui
facts(diffLowerFactor, ("enemy1", "0.5"),
    ("enemy2", "0.4"),
    ("enemy3", "0.3"),
    ("enemy4", "0.3"))

facts(diffRiseFactor, ("enemy1", "0.5"),
    ("enemy2", "0.4"),
    ("enemy3", "0.3"),
    ("enemy4", "0.3"))

facts(minRiseHappenings, ("enemy1", "3"),
    ("enemy2", "4"),
    ("enemy3", "10"),
    ("enemy4", "10"))

def getXMLInfo():
    xml = LoadedXML(fullpath('Lucas_5.xml', 'XML'))
    vertexs = xml.vertexs()

    for v in vertexs:
        #if(v.label() == "Attacking (Enemy)"):
        #    print('id: {0}\ntype: {1}\nlabel: {2}\ndate: {3}'.format(v.id(), v.type(), v.label(), v.date()))
        atr = v.attributes()
        aux = 0
        if(v.label() == "Being Hit(Player)"):
            if(v.attributes()[3].value() == "Straight"):
                hits[0] += 1
            if(v.attributes()[3].value() == "Chaser"):
                hits[1] += 1
            if(v.attributes()[3].value() == "Round"):
                hits[2] += 1
            if(v.attributes()[3].value() == "Irregular"):
                hits[3] += 1

        if(v.label() == "Attacking (Enemy)"):
            if(v.attributes()[6].value() == "Enemy_Straight"):
                happenings[0] += 1
            if(v.attributes()[6].value() == "Enemy_Chaser"):
                happenings[1] += 1
            if(v.attributes()[6].value() == "Enemy_Round"):
                happenings[2] += 1
            if(v.attributes()[6].value() == "Enemy_Irregular"):
                happenings[3] += 1

        for a in atr:
            aux = aux + 1
               # print('attributes{0} name: {1} value: {2}'.format(aux, a.name(), a.value()))
        #print('_' * 10)


for s in sys.argv:
    increaseDifficulty('UNITY: arguments {0};'.format(s))
    decreaseDifficulty('UNITY: arguments {0};'.format(s))
    
def increaseDifficulty (factor):
    x = var()
    y = var()
    if(happenings[factor] > 0):
        if(hits[factor] / happenings[factor] >= run(1, x, (diffRiseFactor, x, "enemy" + factor)) and
           happenings[factor] >= run(1, y, (minRiseHappenings, y, "enemy" + factor))):
            print("true_increase")
        else:
            print("false_increase")

def decreaseDifficulty (factor):
    x = var()
    y = var()
    if(happenings[factor] > 0):
        if(hits[factor] / happenings[factor] <= run(1, x, (diffLowerFactor, x, "enemy" + factor)) and
           happenings[factor] >= run(1, y, (minRiseHappenings, y, "enemy" + factor))):
            print("true_decrease")
        else:
            print("false_decrease")



