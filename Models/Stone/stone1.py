#stone, 2d-degree, g - included, throw the stone over flat Earth with gravity

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Utils'))
import utilPlot

def rhs(vec_y, t, gx, gy):
    x, y, vx, vy = vec_y
    vg = [0, 0, gx, gy]
    A = np.array([[0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0]])
    arr_y = np.array([x, y, vx, vy])
    a2 = A.dot(arr_y)
    a3 = np.array([0, 0, gx, gy])
    dydt = a2+a3
    return dydt

def E_pot(m, vec_y, gy, h0=0):
    x, y, vx, vy = vec_y
    h = y - h0
    return m*abs(gy)*h

def E_kin(m, vec_y):
    x, y, vx, vy = vec_y
    return m*(vx*vx+vy*vy)/2.0

def E_full(m, y, gy, h0=0):
    Ep = E_pot(m, y, gy, h0)
    Ek = E_kin(m, y)
    return Ep + Ek

x0 = 1.0 # IC, x0
y0 = 2.0 # IC, y0
vx0 = 0.5 # IC, vx0
vy0 = 4.0 # IC, vy0
#
vec_y0 = [x0, y0, vx0, vy0]
t0 = 0.0 # startTime
dT = 1.0 # interval for simulation
t1 = t0 + dT # endTime
N = 10 # count steps
t = np.linspace(t0, t1, N+1, endpoint=True)
vg = (0, -9.81)
sol = integrate.odeint(rhs, vec_y0, t, args = vg)
#
x = sol[:, 0]
y = sol[:, 1]
vx = sol[:, 2]
vy = sol[:, 3]

fig, axs = plt.subplots(3, 2)
ax00 = axs[0, 0]
utilPlot.preparePlot(ax00, t, y, label = 'y(t)', color = 'black')

ax10 = axs[1, 0]
utilPlot.preparePlot(ax10, t, vy, label = 'vy(t)', xlabel = 't')
ax10.sharex(ax00)

ax20 = axs[0, 1]
utilPlot.preparePlot(ax20, t, x, label = 'x(t)', xlabel = 't')
ax10.sharex(ax00)

ax11 = axs[1, 1]
utilPlot.preparePlot(ax11, t, vx, label = 'vx(t)', xlabel = 't')
ax10.sharex(ax00)

utilPlot.preparePlot(axs[2, 0], x, y, title = 'Trajectory', label = 'y(x)', xlabel = 'x', ylabel = 'y', color = 'red')
#
m = 1
h0=0

def partE_pot(y):
    return E_pot(m, y, vg[1], h0)

def partE_kin(y):
    return E_kin(m, y)

def partE_full(y):
    return E_full(m, y, vg[1], h0)

vEp = list(map(partE_pot, sol))
vEk = list(map(partE_kin, sol))
vEfull = list(map(partE_full, sol))

#chart to check Energy's balance
ax = axs[2, 1]
ax.plot(t, vEp, label = "E_pot")
ax.plot(t, vEk, label = "E_kin")
ax.plot(t, vEfull, label = "E_full")
ax.legend(loc='best')
ax.grid()

utilPlot.showScene(fig)