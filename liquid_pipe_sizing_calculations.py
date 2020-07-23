import numpy
import math
from scipy.optimize import root
from math import *

print('')
print('LIQUIDS PIPE SIZING CALCULATIONS')
print('')
print('INPUT DATA')
print('')
q = float(input('Please introduce liquid flow rate (US gpm): '))
ro = float(input('Please introduce liquid density (lb/ft3): '))
vi = float(input('Please introduce liquid viscosity (cP): '))
di = float(input('Please introduce pipe inner diameter (inches): '))
ru = float(input('Please introduce pipe roughness (inches): '))

def run ():
    print('')
    print('RESULTS')
    print('')
    flow_area = area (di)
    print("Pipe flow area is " + str(round(flow_area,4)) + " ft2")
    flow_velocity = velocity (q)
    print("Flow velocity is " + str(round(flow_velocity,2)) + " ft/s")
    reynolds_number = Reynolds (ro, vi)
    print("Reynolds number is " + str(round(reynolds_number,0)))
    relative_roughness = rr (ru, di)
    print("Relative roughness is " + str(round(relative_roughness,6)))
    factor = fac ()
    print("Darcy friction factor is " + str(round(factor,5)))
    droop_pressure = dp (ro,di)
    print('Droop pressure is ' + str(round(droop_pressure,5)) + ' psi/100ft')

def area (di):
    flow_area = 0.25*math.pi*((di/12)**2)
    return flow_area

def velocity (q):
    flow_area = area(di)
    flow_velocity = (0.00222801*q)/flow_area
    return flow_velocity

def Reynolds (ro, vi):
    flow_velocity = velocity (q)
    visc = vi * 0.000671969
    reynolds_number = ro * flow_velocity * (di/12) / visc
    return reynolds_number

def rr (ru, di):
    relative_roughness = ru/di
    return relative_roughness

def fac():
    reynolds_number = Reynolds (ro, vi)
    relative_roughness = rr (ru, di)
    if reynolds_number < 4000:
        friction_factor = 64/reynolds_number
        return friction_factor
    else:
        f2 = 0.01
        for i in range (1,6):
            f1 = 1/(-2*log((relative_roughness/3.7) + (2.51/(reynolds_number*sqrt(f2))),10))**2
            f2=f1
            i=i+1
        return f1

def dp (ro, di):
    flow_velocity = velocity (q)
    friction_factor = fac()
    gc = 32.17
    droop_pressure = (25/6)*friction_factor*ro*(flow_velocity**2)/(gc*di)
    return droop_pressure

if __name__ == "__main__":
    run ()
