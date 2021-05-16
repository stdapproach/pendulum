#stone, 1d-degree, g - included, throw the stone at vertical direction

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Utils'))

import utilPlot

def rhs(y, t, gx, gy):
    x, vx = y
    vg = [gx, gy]
    A = np.array([[0, 1], [0, 0]])
    arr_y = np.array([x, vx])
    a2 = A.dot(arr_y)
    a3 = np.array([gx, gy])
    dydt = a2+a3
    return dydt

def E_pot(m, y, gy, h0=0):
    x, vx = y
    h = x - h0
    return m*abs(gy)*h

def E_kin(m, y):
    x, vx = y
    return m*vx*vx/2.0

def E_full(m, y, gy, h0=0):
    Ep = E_pot(m, y, gy, h0)
    Ek = E_kin(m, y)
    return Ep + Ek

x0 = 1.0 # IC, x0
vx0 = 3.0 # IC, vx0
# phase vector: [x, x_t]
y0 = [x0, vx0]
t0 = 0.0 # startTime
dT = 1 # interval for simulation
t1 = t0 + dT # endTime
N = dT*10 # count steps
t = np.linspace(t0, t1, N+1, endpoint=True)
vg = (0, -9.81)
sol = integrate.odeint(rhs, y0, t, args = vg)
#
x = sol[:, 0]
vx = sol[:, 1]

fig, axs = plt.subplots(2, 2)
ax00 = axs[0, 0]
utilPlot.preparePlot(ax00, t, x, label = 'x(t)', color = 'black', ylabel = 'x(t)')

ax10 = axs[1, 0]
utilPlot.preparePlot(ax10, t, vx, label = 'vx(t)', xlabel = 't')
ax10.sharex(ax00)

utilPlot.preparePlot(axs[0, 1], x, vx, title = 'Phase diagram', label = 'vx(x)', xlabel = 'x', ylabel = 'vx', color = 'red')

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
ax = axs[1, 1]
ax.plot(t, vEp, label = "E_pot")
ax.legend(loc='best')
ax.grid()
ax.plot(t, vEk, label = "E_kin")
ax.plot(t, vEfull, label = "E_full")
#utilPlot.hidePlot(axs[1, 1]) # example how to hide a particular plot
#
utilPlot.showScene(fig)
