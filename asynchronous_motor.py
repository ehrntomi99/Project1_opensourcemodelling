#Calculation of the torque/speed characteristic curve of an asynchronous motor
#Given parameters are continious- and maximum power, maximum speed and rated speed

import math

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def torques (P_max, P_min, n_n):
    #P_max is peak power, P_min is continious power, n_n is rated speed
    M_max = (30 * P_max)/(n_n * math.pi)
    M_n = (30 * P_min)/(n_n * math.pi)
    return M_n, M_max
    """
    Calculation of maximum and minimum torque in SI Units
    
    """

P_max, P_min, n_n = 200000, 100000, 5000 #in Watt and min^-1
M_n, M_max = torques(P_max, P_min, n_n)
print(f"minimum torque M_n: {M_n:.2f} Nm")
print(f"maximum torque M_max: {M_max:.2f} Nm")

#Torques for maximum speed 15000min^-1
def torques_15000 (M_n, M_max):
    M_n_15000 = M_n/3
    M_max_15000 = M_max/3
    return M_n_15000, M_max_15000
    """
    
    Since n_max is 15000 min^-1 and is three times as high as n_nenn 5000 min^-1
    the torque in the field weakening region drops to 1/3 (M ~ 1/n)
    because the power (P = M * omega) remains constant.
    
    """
    
M_n_15000, M_max_15000 = torques_15000 (M_n, M_max)
print(f"M_n_15000: {M_n_15000:.2f} Nm")
print(f"M_max_15000: {M_max_15000:.2f} Nm")

def torque_curve(n_list, M_constant, n_n):
    solution = []
    for n in n_list:
        if n == 0: # Avoid  division by zero
            solution.append(M_constant)
        elif n <= n_n: #Range 1 for constant torque up to rated speed 
            solution.append(M_constant)
        else: #Range 2 for field weakening from rated speed 
            value = M_constant * (n_n / n)
            solution.append(value)
    return solution

def characteristic_curve():
    plt.clf() # delete old curve create new one
    n_n = 5000
    n_range = np.linspace(0, 18000, 500) #Generates 500 points from 0 to 18000 min^-1

    
    M_n_curve = torque_curve(n_range, M_n, n_n)
    M_max_curve = torque_curve(n_range, M_max, n_n)

    #Convert speed from min^-1 to 10^3 min^-1 for better readability in plot 
    plt.plot(n_range / 1000, M_max_curve, color='green', label='Maximum torque curve') 
    plt.plot(n_range / 1000, M_n_curve, color='navy', label='Minimum torque curve')
    
   
    plt.xticks(np.arange(0, 20, 1))
    plt.yticks(np.arange(0, 500, 50))
    plt.xlabel('n / 10^3 min^-1')
    plt.ylabel('M / Nm')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()

    # Display maximum- and minimum torque values
    plt.text(15.5, 135, f'{M_max_15000:.2f} Nm', fontsize=9)
    plt.text(15.5, 70, f'{M_n_15000:.2f} Nm', fontsize=9)
    plt.text(1, 405, f'{M_max:.2f} Nm', fontsize=9)
    plt.text(1, 205, f'{M_n:.2f} Nm', fontsize=9)
    
    plt.savefig('Characteristic_curve.png')
    
characteristic_curve()




"""Stylized data set"""
#Test-speed 
n_test = [0, 2500, 5000, 7500, 10000, 12500, 15000]

#Calculation of torques
m_test = torque_curve(n_test, 381.97, 5000)

#Building data set
df_motor = pd.DataFrame({
    'Speed [min^-1]': n_test,
    'Torque [Nm]': [round(m, 2) for m in m_test]
})

#Show data set
print("Stylized Dataset - Motor Characteristics:")
print(df_motor)