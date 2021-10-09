from flowConfig import crossFlow
from transport import FOeqns as solver

module_properties = {
    "Width":    1,  # m
    "Length":   1,  # m
    "zones":    10,  # quantity
    "mode":     'FO',
    "solver":   solver,
}

module_chars = {
    "Feed Flow Rate":    1,  # m3/s
    "Draw Flow Rate":   1,  # m3/s
    "Feed Concentration":    1,  # g/L
    "Draw Concentration":   32,  # g/L
}

module = crossFlow(module_properties)
module.initialize(module_chars)
module.iterate()