from typing import overload
import matplotlib.pyplot as plt
from params import ptx,pty
import numpy as np
def drawTrace(x,y,name='trace'):
    plt.figure(name)
    plt.plot(ptx,pty,'o',x,y,'-')

def drawXY(x1,y1,name='xy'):
    d_x=np.diff(x1)
    dd_x=np.diff(d_x)
    d_y=np.diff(y1)
    dd_y=np.diff(d_y)
    plt.figure(name)
    plt.subplot(221)
    plt.plot(d_x)
    plt.title("d_x")
    plt.subplot(222)
    plt.plot(dd_x)
    plt.title("dd_x")
    plt.subplot(223)
    plt.plot(d_y)
    plt.title("d_y")
    plt.subplot(224)
    plt.plot(dd_y)
    plt.title("dd_y")
def plot1(x,name):
    plt.figure(name)
    plt.plot(x)
def plot2(x,y,name):
    plt.figure(name)
    plt.plot(x,y)
def show():
    plt.show()