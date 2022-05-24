from scipy.fftpack import fft,ifft,dct,idct
import numpy as np
from matplotlib import pyplot as plt
from params import ptx,pty
#sample

x=np.linspace(0,1,512)
y=2+3*np.cos(2*np.pi*50*x)+1.5*np.cos(2*np.pi*75*x+np.pi/2)
y1=dct(y)
i_y=idct(y1/1024)
plt.figure(1)
plt.subplot(211)
plt.plot(y1)
plt.title("y")
plt.subplot(212)
plt.plot(x,i_y,'r',x,y,'b')

#ptx,pty
x,y=ptx,pty
N=len(x)
y1=dct(y)
x1=dct(x)
y_max=np.max(abs(y1))
x_max=np.max(abs(x1))
'''
for i in range(N):
    if abs(y1[i])<0.0000001*y_max:
        y1[i]=0
    if abs(x1[i])<0.0000001*x_max:
        x1[i]=0
        ''''''
k=100
num=k*N
t=np.linspace(0,N,num)
tempy=np.zeros(num)
tempx=np.zeros(num)
for i in range(N):
    tempy[k*i-1]=y1[i-1]
    tempx[k*i-1]=x1[i-1]
y1=tempy/k
x1=tempx/k
'''
i_y1=idct(y1/(2*N))
i_x1=idct(x1/(2*N))

plt.figure(2)
plt.subplot(211)
plt.plot(y1)
plt.title("dct y")
plt.subplot(212)
plt.title("x")
plt.plot(y,'r',i_y1[0:len(y)],'b')
plt.figure(3)
plt.subplot(211)
plt.plot(x1)
plt.title("dct x")
plt.subplot(212)
plt.title("x")
plt.plot(x,'r',i_x1[0:len(x)],'b')
plt.show()
