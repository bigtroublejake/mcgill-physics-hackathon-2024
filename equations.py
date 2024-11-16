import numpy as np


#small angles nobody shall be any wisers
def angularResolution(diameter, waveLength):
    "returns the angular resolution when the diameter was changed"
    return ((1.22)*(diameter/waveLength))

