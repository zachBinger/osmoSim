from scipy.optimize import fsolve

def FOeqns(module, zone):

    def waterFlux(Jw):
        return Jw - (module.properties["Water Permeability"]*(1)                    )

    print(fsolve(waterFlux,0))