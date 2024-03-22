from __future__ import annotations
from scipy.optimize import fsolve
import numpy as np
import cmath
import warnings

warnings.filterwarnings('ignore', 'The iteration is not making good progress')
warnings.filterwarnings('ignore', 'Conversion of an array with ndim > 0 to a scalar is deprecated')
warnings.filterwarnings('ignore', 'Casting complex values to real discards the imaginary part')

# The following code calculates the Darcy coefficient using the general Coolebrook equation
# The equation cannot be solved analytically, so we're gonna solve it iteratively

# Returns the implicit equation. The parameters are Re => Reynolds number, Epsilon => Relative roughness, D => Hydraulic diameter
def f(x):
    global Re
    global Epsilon
    global D
    return (1 / cmath.sqrt(x) + 2 * (np.log10(((Epsilon / D) / 3.7) + (2.51 / (Re * cmath.sqrt(x))))))


####################################################################################################################################

if __name__ == "__main__":
    try:
        while True:
            Re = float(input(f"Insert Reynolds number: "))
            if Re < 0:
                raise Exception(f"Please insert a valid Reynolds number! ")
            # If Reynolds number is < 0 there's laminar flow, so λ is better evaluated using an alternative equation
            # There are only two parameters: Reynolds number and a geometry dependent coefficient
            elif Re < 2000:
                conduct_type = int(input(f"Press 1 if the pipe is circular or press 2 if the pipe is squared: "))
                if conduct_type == 1:
                    Lambda = float(64 / Re)
                elif conduct_type == 2:
                    Lambda = float(57.108 / Re)
                else:
                    raise Exception("Please insert a valid pipe type! ")
                print(f"The Darcy coefficient is: \u03BB = {Lambda}")
                break
            Epsilon = float(input(f"Insert relative roughness [m]: "))
            # If Reynolds number is greater than 2000 the flow is turbulent and we use the Coolebrook equation
            if Epsilon < 0:
                raise Exception("Please insert a valid relative toughness! ")
            D = float(input(f"Insert conduct diameter [m]: "))
            if D < 0:
                raise Exception("Please insert a valid diameter! ")
            # Solves iteratively using as a starting value 0.025, the "magic" number
            Lambda = fsolve(f, [0.025])
            print(f"The Darcy coefficient is: \u03BB = {Lambda[0]}")
            break
    except ValueError:
        print("Please insert a valid number! ")
