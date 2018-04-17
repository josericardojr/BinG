from kanren import Relation, facts, var, run
from Loader import *
from LoadedXML import *

diffLowerFactor = Relation()
diffRiseFactor = Relation()
minRiseHappenings = Relation()

#infos retiradas do xml

#numero de hits em ordem de tipo de inimigo
hits = [4];
#numero de usos de ataque em ordem de tipo de inimigo
happenings = [4];

#BASEAR EM TEMPO

#infos estabelecidas aqui
facts(diffLowerFactor, ("enemy1", "0.5"),
    ("enemy2", "0.4"),
    ("enemy3", "0.3"))

facts(diffRiseFactor, ("enemy1", "0.5"),
    ("enemy2", "0.4"),
    ("enemy3", "0.3"))

facts(minRiseHappenings, ("enemy1", "3"),
    ("enemy2", "4"),
    ("enemy3", "10"))

def increaseDifficulty (factor):
    x = var()
    y = var()
    if(happenings[factor] > 0):
        if(hits[factor] / happenings[factor] >= run(1, x, (diffRiseFactor, x, "enemy" + factor)) and
           happenings[factor] >= run(1, y, (minRiseHappenings, y, "enemy" + factor))):
            return true
        else:
            return false;

def decreaseDifficulty (factor):
    x = var()
    y = var()
    if(happenings[factor] > 0):
        if(hits[factor] / happenings[factor] <= run(1, x, (diffLowerFactor, x, "enemy" + factor)) and
           happenings[factor] >= run(1, y, (minRiseHappenings, y, "enemy" + factor))):
            return true
        else:
            return false;

xml = LoadedXML(fullpath('Lucas_2.xml', 'XML'))
vertexs = xml.vertexs()

for v in vertexs:
    print('id: {0}\ntype: {1}\nlabel: {2}\ndate: {3}'.format(v.id(), v.type(), v.label(), v.date()))
    atr = v.attributes()
    aux = 0
    for a in atr:
        aux = aux + 1
        print('attributes{0} name: {1} value: {2}'.format(aux, a.name(), a.value()))
    print('_' * 10)



