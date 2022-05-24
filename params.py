from cv2 import RHO
import numpy as np
ptx=np.array([100,550,1000,1550,2075,2550,3200,3700,4300,4500\
    ,4300,3700,3200,2550,2075,1550,1000,550,100])
pty=np.array([0,-900,-600,-250,-600,-750,-550,-400,-400,0,\
    400,400,550,750,600,250,600,900,0])
class car:
    BackWelR=140       #后轮半径
    ShaftR0=80             #凸轮基园半径
    l_FWel2Shaft=70    #前轮轴到凸轮轴距离
    h_FWel2Shaft=50   #前轮到凸轮轴向距离
    shaft_thick=4         #凸轮厚度
    l_BackWel2Shaft=40               #后轮到凸轮轴距离
    h_BackWelForce2Fwel=160    #后轮主动轮到凸轮轴向距离
    #应当确保L1<rho_min
    def __init__(self,BackWelR,ShaftR0,l_FWel2Shaft,h_FWel2Shaft,shaft_thick,l_BackWel2Shaft,h_BackWelForce2Fwel):
        self.BackWelR=BackWelR
        self.ShaftR0=ShaftR0
        self.l_FWel2Shaft=l_FWel2Shaft
        self.h_FWel2Shaft=h_FWel2Shaft
        self.shaft_thick=shaft_thick
        self.l_BackWel2Shaft=l_BackWel2Shaft
        self.h_BackWelForce2Fwel=h_BackWelForce2Fwel
    def __init__(self):
        self.BackWelR=140
        self.ShaftR0=80
        self.l_FWel2Shaft=70
        self.h_FWel2Shaft=70
        self.shaft_thick=4
        self.l_BackWel2Shaft=70
        self.h_BackWelForce2Fwel=160
