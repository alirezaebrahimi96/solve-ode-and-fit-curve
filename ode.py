from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
def f(y, x): return [y[1], -y[1] + y[0] * np.exp(-y[0])]
y0 = [1, 0]
xs = np.linspace(0, 100, 1000)
Us = odeint(f, y0, xs)
ys = Us[:,0]
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs,ys);
from scipy.optimize import curve_fit
import warnings
warnings.filterwarnings("ignore")
def func(x, a, b, c): # x-shifted log
    return a*np.log(x + b)+c
initialParameters = np.array([1.0, 1.0, 1.0])
xData = np.array(xs, dtype=float)
yData = np.array(ys, dtype=float)
fittedParameters, pcov = curve_fit(func, xData, yData, initialParameters)
print('Parameters:', fittedParameters)
def ModelAndScatterPlot(graphWidth, graphHeight):
    f = plt.figure(figsize=(graphWidth/100.0, graphHeight/100.0), dpi=100)
    axes = f.add_subplot(111)

    # first the raw data as a scatter plot
    axes.plot(xData, yData,  'D')

    # create data for the fitted equation plot
    xModel = np.linspace(min(xData), max(xData))
    yModel = func(xModel, *fittedParameters)

    # now the model as a line plot
    axes.plot(xModel, yModel)

    axes.set_xlabel('X Data') # X axis data label
    axes.set_ylabel('Y Data') # Y axis data label

    plt.show()
    plt.close('all') # clean up after using pyplot

graphWidth = 800
graphHeight = 600
ModelAndScatterPlot(graphWidth, graphHeight)
