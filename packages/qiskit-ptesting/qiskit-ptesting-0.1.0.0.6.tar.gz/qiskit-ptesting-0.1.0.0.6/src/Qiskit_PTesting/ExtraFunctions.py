from math import acos, sin

def cordsComplexToThetaPhi(coords):
    #coords is a tuple/list of 2 complex numbers
    if not len(coords) == 2:
        raise Exception(f"Length of input is not 2: {coords}")
    if not isinstance(coords[0], complex) or isinstance(coords[1], complex):
        raise Exception(f"Inputs are not 2 complex numbers: {coords}")

    if coords[0].real == 1:
        theta = 0
        phi = 0
    elif coords[0].real == 0:
        theta = 180
        phi = 0
    else:
        theta = acos(coords[0].real) / 2
        phi = acos(coords[1].real / sin(theta / 2))

    return (theta, phi)
