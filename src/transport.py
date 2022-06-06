from scipy.optimize import fsolve
import waterProperties

def FOeqns(module, zone):

    def solve_osm_transport(Jw):
        feed_osmP = waterProperties.molarity(module.domain[zone]['Inside Concentration'])*2*8.314*298
        draw_osmP = waterProperties.molarity(module.domain[zone]['Outside Concentration'])*2*8.314*298

        del_conc = module.domain[zone]['Outside Concentration'] - module.domain[zone]['Inside Concentration']
        del_pi = feed_osmP - draw_osmP

        del_P = module.domain[zone]['Outside Pressure'] - module.domain[zone]['Inside Pressure']
        
        return Jw - (module.properties["Water Permeability"]*(del_pi - del_P))

    Jw = fsolve(solve_osm_transport,0.1)
    flux_lmh = Jw*(1000*3600)
    perm_rate = (flux_lmh*((module.properties['Length']*module.properties['Width'])/module.properties['zones'])*24)/1000
    
    return {'Jw':Jw,'flux_lmh':flux_lmh,'perm_rate':perm_rate}

    

# module.initialize(module_chars)
# module.iterate()

# # print(module.domain)

# # print(list(module.domain.keys()))

# # a = (list(module.domain.keys()))
# # b,c = zip(*a)
# # print(b)
# # print(c)
# # module.visualize()