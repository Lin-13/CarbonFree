import numpy as np
import calc_Rho as cr
import calc_XY as cxy
from params import *
import ui
x1,y1=cxy.calcTrace(ptx,pty,2001)
rho_curve1=cxy.calcCurveRho(x1,y1)
mycar=car()
sharfR1,Rtheta1=cxy.calcThetaAndShaftR(rho=rho_curve1,mycar=mycar)
rho2,theta2=cr.calcTrace(ptx,pty,2001)
rho_curve2=cr.calcCurveRho(rho2,theta2)
sharfR2,Rtheta2=cxy.calcThetaAndShaftR(rho=rho_curve2,mycar=mycar)
ui.plot2(x1,y1,"trace_xy")
ui.plot1(rho_curve1,name="trace_rho1")
ui.plot1(rho_curve2,name="trace_rho2")
ui.plot1(sharfR1,name="trace_sharfR1")
ui.plot1(sharfR2,name="trace_sharfR2")
ui.plot1(Rtheta1,name="trace_Rtheta1")
ui.plot1(Rtheta2,name="trace_Rtheta2")
ui.show()