from audioop import cross
from operator import mod
import numpy as np
import itertools
from itertools import permutations
import matplotlib.pyplot as plt
import math
import transport

class crossFlow:
    def __init__(self, props):
        # Initialize a spiral-wound crossflow module with properties from the dict "props"
        self.properties = props

    def initialize(self, chars):
        initDict = chars
        self.domain =  np.asmatrix(np.array([[chars.copy() for i in range(self.properties["zones"])] for i in range(self.properties["zones"])]))
        # self.domain =  np.array([[chars for i in range(10)] for i in range(10)])
        for x, y in np.ndindex(self.domain.shape):
            self.domain[x,y]['Index'] = (x,y)

    def adjustFlow(self,x,y,solver_ans,loop):
        if loop == 1:
            self.domain[y+1,x]['Inside Flow Rate'] = self.domain[y,x]['Inside Flow Rate'] + solver_ans
            self.domain[y,x+1]['Outside Flow Rate'] = self.domain[y,x]['Outside Flow Rate'] - solver_ans
        
            self.domain[y+1,x]['Inside Concentration'] = self.domain[y,x]['Inside Concentration']*(self.domain[y,x]['Inside Flow Rate']*1000) \
                /(self.domain[y+1,x]['Inside Flow Rate']*1000)
            self.domain[y,x+1]['Outside Concentration'] = self.domain[y,x]['Outside Concentration']*(self.domain[y,x]['Outside Flow Rate']*1000) \
                /(self.domain[y,x+1]['Outside Flow Rate']*1000)
        
        if loop == 2:
            self.domain[y-1,x]['Inside Flow Rate'] = self.domain[y,x]['Inside Flow Rate'] + solver_ans
            self.domain[y,x]['Outside Flow Rate'] = self.domain[y,x-1]['Outside Flow Rate'] - solver_ans

        if loop == 'flip':
            for x in range(0,int(self.properties["zones"]/2)):
                solverAns = transport.FOeqns(module, (1,1))['perm_rate'][0]
                self.domain[math.floor(self.properties["zones"]-1),x+1]['Outside Flow Rate'] = self.domain[math.floor(self.properties["zones"]-1),x]['Outside Flow Rate'] - solverAns
        # Flip the values at the baffle turn
            for idx in range(self.domain[self.properties["zones"]-1,int(self.properties["zones"]/2):].size):
                self.domain[self.properties["zones"]-1,int(self.properties["zones"]/2+idx)]['Inside Flow Rate'] = self.domain[self.properties["zones"]-1,int(idx)]['Inside Flow Rate'] - solverAns
                # self.domain[self.properties["zones"]-1,int(self.properties["zones"]/2+idx)]['Inside Concentration'] = self.domain[self.properties["zones"]-1,int(idx)]['Inside Concentration']
                # self.domain[self.properties["zones"]-1,int(self.properties["zones"]/2+idx)]['Inside Flow Rate'] = self.domain[self.properties["zones"]-1,int(idx)]['Inside Flow Rate']
        
    def iterate(self):

        # ## 1st loop
        # i direction will go along the whole width of the membrane
        for y in range(0,math.floor(self.properties["zones"]-1)):
            # #j direction will go along the length of the membrane and will initially stop at the baffle (half way)
            for x in range(0,int(self.properties["zones"]/2)):
                solverAns = transport.FOeqns(module, (1,1))['perm_rate'][0]
                crossFlow.adjustFlow(self,x,y,solverAns, 1)

        # Flip across baffle
        crossFlow.adjustFlow(self,x,y,0, 'flip')

        ## 2nd loop
        # i direction will go along the whole width of the membrane
        for y in range(self.properties["zones"]-1,0,-1):
            # j direction will go along the length of the membrane and will initially stop at the baffle (half way)
            for x in range(int(self.properties["zones"]/2),self.properties["zones"]):
                solverAns = transport.FOeqns(module, (1,1))['perm_rate'][0]
                crossFlow.adjustFlow(self,x,y,solverAns,2)
        
        for x in range(int(self.properties["zones"]/2),self.properties["zones"]):
            solverAns = transport.FOeqns(module, (1,1))['perm_rate'][0]
            self.domain[0,x]['Outside Flow Rate'] = self.domain[0,x-1]['Outside Flow Rate'] - solverAns

    def visualize(self, side, char):
        D = np.zeros(shape=self.domain.shape)
        for x, y in np.ndindex(self.domain.shape):
            D[x][y] = self.domain[x,y][char]
        plt.imshow(D)
        plt.show()







module_properties = {
    "Width":                1,  # m
    "Length":               1,  # m
    "zones":                10,  # quantity
    "Water Permeability":   1e-9,
    "Salt Permeability":    1e-6,
    "Defects":              0,
    "mode":                 'FO',
    
    # "solver":   solver,
}

module_chars = {
    "Index":                (0,0),
    "Outside Flow Rate":        2,  # m3/s
    "Inside Flow Rate":         1,  # m3/s
    "Outside Concentration":    1,  # g/L
    "Inside Concentration":     32,  # g/L
    "Outside Pressure":    10,  # Pa
    "Inside Pressure":     10,  # Pa
}

module = crossFlow(module_properties)
module.initialize(module_chars)
module.iterate()
# module.visualize('Inside','Inside Flow Rate')
# module.visualize('Outside','Outside Flow Rate')
module.visualize('Inside','Inside Concentration')
module.visualize('Outside','Outside Concentration')
