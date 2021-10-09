import numpy as np
import itertools
from itertools import permutations
import matplotlib.pyplot as plt

class crossFlow:
    def __init__(self, props):
        # Initialize a spiral-wound crossflow module with properties from the dict "props"
        self.properties = props

    def initialize(self, chars):
        domain = []
        initDict = chars
        # nested for loop for creating the coordinate tuples of the discretized domain ex.[(0,0),(0,1),(1,0)]
        for i in range(self.properties["zones"]):
            for j in range(self.properties["zones"]):
                domain.append((i,j))

        # initializing all the flow parameters defined in main.py
        self.domain = dict.fromkeys(domain,initDict)

    def iterate(self):
        for i in range(1,self.properties["zones"]):
            for j in range(1,self.properties["zones"]):
                self.properties["solver"](self,[i,j])
                

    def visualize(self, char):
        plt.imshow(self.domain[char])