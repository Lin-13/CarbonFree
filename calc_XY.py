from cv2 import RHO
from scipy.interpolate import CubicSpline
import numpy as np
from scipy.fftpack import dct,idct
from params import *
#brief num必须为奇数
def calcTrace(ptx,pty,num,type='cubic'):
    t=np.linspace(1,len(ptx),len(ptx))
    ptx[0]=ptx[-1]
    pty[0]=pty[-1]
    if(type=='cubic'):
        px=CubicSpline(t,ptx,bc_type='periodic')
        py=CubicSpline(t,pty,bc_type='periodic')
        t1=np.linspace(0,len(ptx),num=num,endpoint=True)
        x1=px(t1)
        y1=py(t1)
        return x1,y1
    elif(type=='dct'):
        px=CubicSpline(t,ptx,bc_type='periodic')
        py=CubicSpline(t,pty,bc_type='periodic')
        t1=np.linspace(0,len(ptx),num=num,endpoint=True)
        x1=px(t1)
        y1=py(t1)
        
        Fx1=dct(x1)
        max_x=max(np.abs(Fx1))
        for i in range(num):
            if abs(Fx1[i])<0.01*max_x:
                Fx1[i]=0
        x1=idct(Fx1/(2*num))
        
        Fy1=dct(y1)
        max_y=max(np.abs(Fx1))
        for i in range(num):
            if abs(Fx1[i])<0.01*max_y:
                Fx1[i]=0
        y1=idct(Fy1/(2*num))
        
        return x1,y1
    else:
        raise Exception('处理类型错误')
    
def calcCurveRho(x,y):
    if np.mod(len(x),2)==0:
        raise Exception("calcRho:error:长度必须为奇数")
    t=np.linspace(1,len(x),endpoint=True)
    d_x=np.diff(x)
    dd_x=d_x
    dd_x=np.diff(d_x)
    #dd_x[len(dd_x)]=dd_x[len(dd_x)-1]
    d_y=np.diff(y)
    dd_y=np.diff(d_y)
    dd_yx=np.zeros(len(x)-1)
    dd_yx[0:-2]=np.diff(d_y/d_x)[0:-1]
    dd_yx[-1]=dd_yx[-2]
    rho=np.float_power((1+(d_y/d_x)**2.0),(3.0/2))/(dd_yx/d_x)
    return rho
def calcThetaAndShaftR(rho,mycar):
    L1=mycar.l_BackWel2Shaft+mycar.l_FWel2Shaft
    L1=np.ones(len(rho))*L1
    theta=np.arcsin(L1/rho)
    theta_sum=sum(theta)
    #计算凸轮
    d=mycar.ShaftR0-mycar.l_FWel2Shaft
    h=mycar.h_FWel2Shaft
    ShaftR=np.zeros(len(theta))
    for i in range(len(theta)):
        ShaftR[i]=d*np.cos(theta[i])+(h+d*np.sin(theta[i])*np.tan(theta[i]))
    return ShaftR,theta