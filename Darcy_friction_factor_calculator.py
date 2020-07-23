import numpy
import math
from scipy.optimize import root
from math import *

print('')
print('DARCY FRICTION FACTOR CALCULATOR')
print('')
re = float(input('Please introduce the Reynolds numer: '))
ks = float(input('Please introduce the pipe absolute roughness (inches): '))
di = float(input('Please introduce pipe inner diameter (inches): '))

def run ():
    print('')
    print('RESULT')
    print('')
    friction_factor = factor (re, ks, di)
    print("Darcy friction factor is " + str(round(friction_factor,5)))

def factor (re, ks, di):
    relative_roughness = ks/di
    if re < 4000:
        friction_factor = 64/re
        return friction_factor
    else:
        f2 = 64/re
        for i in range (1,6):
            f1 = 1/(-2*math.log10((relative_roughness/3.7) + (2.51/(re*sqrt(f2)))))**2
            f2=f1
            i=i+1
        return f1

if __name__ == "__main__":
    run ()
