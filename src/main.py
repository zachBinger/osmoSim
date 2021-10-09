from flowConfig import crossFlow

module_properties = {
    "Width":    1,  # m
    "Length":   1,  # m
    "zones":    10  # quantity
}

module_chars = {
    "Feed Flow Rate":    1,  # m3/s
    "Draw Flow Rate":   1,  # m3/s
}

module = crossFlow(module_properties)
module.initialize(module_chars)
module.iterate()