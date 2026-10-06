#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.optimize import curve_fit
from scipy.stats import shapiro

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

y1 = file["Distance in trial 1(cm)"].to_numpy()
y2 = file["Distance in trial 2(cm)"].to_numpy()
y3 = file["Distance in trial 3(cm)"].to_numpy()

parameters, covariance = curve_fit(function,x,y_avg,inital)
velocity, inital_h = parameters

y_pred = function(x,velocity,inital_h)

residuals1 = y_pred - y1
residuals2 = y_pred - y2
residuals3 = y_pred - y3
residuals_avg = y_pred - y_avg

residuals = np.concatenate((residuals1,residuals2,residuals3))







x_model = np.linspace(x.min(),x.max(),13)

t, pvalue = shapiro(residuals)

plt.scatter(x,residuals_avg,label = "predicted range - average range",color="red")
plt.scatter(x,residuals1,label = "predicted range - ranges of trial 1")
plt.scatter(x,residuals2,label = "predicted range - ranges of trial 2")
plt.scatter(x,residuals3,label = "predicted range - ranges of trial 3")

print(f"The test statistic is: {t}")
print(f"The pvalue is: {pvalue}")

plt.xlabel("Angle (°)")
plt.ylabel("Difference in horizontal range (cm)")
plt.axhline(0, color='black', linewidth=5)
plt.xticks(np.arange(0,97.5,7.5))
plt.grid()
plt.legend()
plt.show()
