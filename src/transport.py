def FOeqns(module, zone):

    module.domain[zone[0],zone[1]]["Feed Flow Rate"] = module.domain[zone[0]-1,zone[1]-1]["Feed Flow Rate"] + 1

    # print(module.domain[zone[0],zone[1]])
