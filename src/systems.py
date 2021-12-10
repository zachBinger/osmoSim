import numpy as np
import itertools
from itertools import permutations
import matplotlib.pyplot as plt

class System:
    def __init__(self):
        self.subsystems = []

    def add(self,sub, loc):
        sub.loc = loc
        self.subsystems.append(sub)

    def simulate(self):
        pass

    def report(self):
        indent = '      '
        arrow = '|\n'+indent
        print('\n'+indent+'Main'+indent+'Waste'+indent+'\n')
        for idx, subsys in enumerate(self.subsystems):
            if subsys.loc == 'main':
                print(indent+subsys.name)
                print(indent+arrow)
            if subsys.loc == 'waste':
                print(indent+indent+'---> '+subsys.name)
                # print(indent+arrow)


class FO:
    def __init__(self, module, models):
        self.name = 'FO'
        pass

class PRO:
    def __init__(self, module, models):
        self.name = 'PRO'
        pass

class RO:
    def __init__(self, module, models):
        self.name = 'RO'
        pass

class MD:
    def __init__(self, module, models):
        self.name = 'MD'
        pass

class GAC:
    def __init__(self, module, models):
        self.name = 'GAC'
        pass

class UV:
    def __init__(self, module, models):
        self.name = 'UV'
        pass

class UF:
    def __init__(self, module, models):
        self.name = 'UV'
        pass