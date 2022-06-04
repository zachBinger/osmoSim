from scipy.optimize import fsolve
import transport

def FOeqns(module, zone):

    def waterFlux(Jw):
        return Jw - (module.properties["Water Permeability"]*(1)                    )

    print(fsolve(waterFlux,0))




# module.initialize(module_chars)
# module.iterate()

# # print(module.domain)

# # print(list(module.domain.keys()))

# # a = (list(module.domain.keys()))
# # b,c = zip(*a)
# # print(b)
# # print(c)
# # module.visualize()