import numpy as np

#small angles nobody shall be any wisers
def angularResolution(diameter, waveLength):
    "returns the angular resolution when the diameter was changed"
    return ((1.22)*(waveLength/diameter))

def diffractionGrating(wavelength) -> list:
    "returns a list of the position of the nodes"
    d = 5e-6
    L = 100
    ls = []

    for m in range(5):
        
        angle = np.arcsin(m * wavelength / d)
        y = L * np.tan(angle)

        ls.append(y)

        # print(y-var)
        # var = y

    return(ls)

def Intensity(wavelength) -> list:
    d = 5e-6
    ls = []
    L = 100
    lsy = diffractionGrating(wavelength)
    for m in range(5):
        intensity = np.square(np.cos(np.pi*d*lsy[m]/(L*wavelength)))

        ls.append(float(intensity))
    return ls



def refractAngleGlass(index, initAngle) -> float:
    initAngle = np.deg2rad(initAngle)
    newAngle = np.arcsin(1.000 * np.sin(initAngle) / index)
    return np.rad2deg(newAngle)

def diameter(angularResolution, waveLenght):
    return((1.22)*waveLenght/angularResolution)

def wavelength(angle, diameter):
    return (angle*diameter)/1.22
