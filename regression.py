#!/usr/bin/env python
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
y1 = file["Distance in trial 1(cm)"].to_numpy()
y2 = file["Distance in trial 2(cm)"].to_numpy()
y3 = file["Distance in trial 3(cm)"].to_numpy()
y_avg = file["Average distance(cm)"].to_numpy()

stdev = np.std(np.column_stack((y1,y2,y3)),axis=1,ddof=1)

y_sem = stdev/np.sqrt(3)

parameters, covariance = curve_fit(function,x,y_avg,inital)
velocity, inital_h = parameters

print(parameters)

x_model = np.linspace(x.min(),x.max(),13)

y_pred = function(x, velocity, inital_h)
ss_res = np.sum((y_avg - y_pred)**2)
ss_tot = np.sum((y_avg - np.mean(y_avg))**2)
r_squared = 1 - (ss_res / ss_tot)

plt.scatter(x,y1,label = "trial 1")
plt.scatter(x,y2,label = "trial 2")
plt.scatter(x,y3,label = "trial 3")
plt.scatter(x,y_avg,label="Average",color='red')

plt.xlabel("Angle (°)")
plt.ylabel("Horizontal range (cm)")
plt.xticks(np.arange(0,97.5,7.5))
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=20))

plt.grid()

plt.errorbar(x,y_avg,yerr=y_sem,fmt='o',linestyle='None',color='red')

plt.plot(x_model, function(x_model,velocity,inital_h),label=f"Modelled fit ($R^2$ = {r_squared:.5f})")
plt.legend()
plt.show()
