import numpy as np
import itertools
from itertools import permutations
from transport import FOeqns as solver

class crossFlow:
    def __init__(self, props):
        # Initialize a spiral-wound crossflow module with properties from the dict "props"
        self.properties = props

    def initialize(self, chars):
        domain = []
        for i in range(self.properties["zones"]):
            for j in range(self.properties["zones"]):
                domain.append((i,j))

        self.domain = dict.fromkeys(domain,dict.fromkeys(chars,0))

    def iterate(self):
        for i in range(self.properties["zones"]):
            for j in range(self.properties["zones"]):
                solver(self,[i,j])
                
