import numpy as np


#small angles nobody shall be any wisers
def angularResolution(diameter, waveLength):
    "returns the angular resolution when the diameter was changed"
    return ((1.22)*(diameter/waveLength))

def diffractionGrating(wavelength) -> list:
    "returns a list of the position of the nodes"
    d = 5e-6
    L = 100
    ls = []
    var = 0

    for m in range(7):
        
        angle = np.arcsin(m * wavelength / d)
        y = L * np.tan(angle)

        ls.append(y)

        # print(y-var)
        # var = y

    return(ls)


