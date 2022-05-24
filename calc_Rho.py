from cv2 import RHO
from scipy.interpolate import CubicSpline
import numpy as np
from scipy.fftpack import dct,idct
from params import *
#brief num必须为奇数
def xy2rho_theta(x,y):
    if len(x)!=len(y):
        raise Exception("xy2rho_theta:error:x,y长度不一致")
    if len(x)==1:
        rho=np.sqrt(x**2+y**2)
        if x>0:
            theta=np.arctan(y/x)
        else:
            theta=np.arctan(y/x)+np.pi
        return rho,theta
    else:
        rho=np.zeros(len(x))
        theta=np.zeros(len(x))
        for i in range(len(x)):
            rho[i]=np.sqrt(x[i]**2+y[i]**2)
            if x[i]>0:
                theta[i]=np.arctan(y[i]/x[i])
            else:
                theta[i]=np.arctan(y[i]/x[i])+np.pi
        return rho,theta
def rho2xy(rho,theta):
    x=rho*np.cos(theta)
    y=rho*np.sin(theta)
    return x,y

def calcTrace(ptx,pty,num,type='cubic'):
    t=np.linspace(1,len(ptx),len(ptx))
    rho,theta=xy2rho_theta(ptx,pty)
    rho[0]=rho[-1]
    theta[0]=theta[-1]
    if(type=='cubic'):
        prho=CubicSpline(t,rho,bc_type='periodic')
        ptheta=CubicSpline(t,theta,bc_type='periodic')
        t1=np.linspace(0,len(ptx),num=num,endpoint=True)
        rho1=prho(t1)
        theta1=ptheta(t1)
        return rho1,theta1
    elif(type=='dct'):
        prho=CubicSpline(t,rho,bc_type='periodic')
        ptheta=CubicSpline(t,theta,bc_type='periodic')
        t1=np.linspace(0,len(ptx),num=num,endpoint=True)
        rho1=prho(t1)
        theta1=ptheta(t1)
        
        Frho1=dct(rho1)
        max_r=max(np.abs(Frho1))
        for i in range(num):
            if abs(Frho1[i])<0.01*max_r:
                Frho1[i]=0
        x1=idct(Frho1/(2*num))
        
        Ftheta1=dct(y1)
        max_t=max(np.abs(Ftheta1))
        for i in range(num):
            if abs(Ftheta1[i])<0.01*max_t:
                Ftheta1[i]=0
        y1=idct(Ftheta1/(2*num))
        
        return rho1,theta1
    else:
        raise Exception('处理类型错误')
#计算曲率
def calcCurveRho(rho,theta):
    if np.mod(len(rho),2)==0:
        raise Exception("calcRho:error:长度必须为奇数")
    t=np.linspace(1,len(rho),endpoint=True)
    d_rho_t=np.diff(rho)
    d_theta_t=np.diff(theta)
    d_rho_theta=d_rho_t/d_theta_t
    dd_rho_theta=np.zeros(len(d_rho_theta))
    dd_rho_theta[0:-1]=np.diff(d_rho_theta)
    dd_rho_theta[-1]=(dd_rho_theta[0]+dd_rho_theta[-2])/2
    dd_rho_theta=dd_rho_theta/d_theta_t
    curve_rho=(rho[0:-1]**2+d_rho_theta**2)**(3.0/2)/(rho[0:-1]**2-rho[0:-1]*dd_rho_theta+2*d_rho_theta**2)
    return curve_rho
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
    return theta,ShaftR