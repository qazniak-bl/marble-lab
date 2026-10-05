#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.optimize import curve_fit

def function (angle, velocity, inital_h):
    g = 981 #cm/s^2
    theta = np.radians(angle)
    time = (-velocity*np.sin(theta)-np.sqrt(velocity**2 * np.sin(theta)**2 - 4*(-0.5*g)*inital_h))/(-g)
    return velocity*np.cos(theta)*time

file = pd.read_csv('data.csv')

initial_v = 100 #cm/s
inital_height = 6 #cm above the table when shot point-blank

inital = [initial_v,inital_height]


x = file["Angle(°)"].to_numpy()
y_avg = file["Average distance(cm)"].to_numpy()


parameters, covariance = curve_fit(function,x,y_avg,inital)
velocity, inital_h = parameters

y_pred = function(x,velocity,inital_h)

residuals = y_pred - y_avg

x_model = np.linspace(x.min(),x.max(),13)

plt.scatter(x,residuals,label = "predicted range - average range")

plt.xlabel("Angle (°)")
plt.ylabel("Difference in horizontal range (cm)")
plt.axhline(0, color='black', linewidth=5)
plt.xticks(np.arange(0,97.5,7.5))
plt.grid()
plt.legend()
plt.show()
