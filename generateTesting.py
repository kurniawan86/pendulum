import math
import matplotlib.pyplot as plt

class generateData:
    takhir = 500
    f = 8
    pi = math.pi
    dt = 0.001

    def __init__(self):
        pass

    def calTeta(self, t):
        hasil = 90*math.sin(2*self.pi*self.f*t)
        return hasil

    def geneTeta(self):
        teta = []
        t = 0
        for i in range (self.takhir):
            t = t+self.dt
            teta.append(self.calTeta(t))
        plt.plot(teta)
        plt.show()

class TorsiConvertion:
    massa = 20
    g = 9.8
    l = 1.5
    teta = 0
    inertia = 8
    teta1 = 0
    dt = 0.001

    def __init__(self):
        pass

    def calTeta2(self, tho):
        temp1 = tho-(self.massa*self.g*self.l*
                     math.sin(self.teta))
        temp2 = (self.massa*math.pow(self.l, 2)
                 )+self.inertia
        return temp1/temp2

    def calTeta1(self,tho):
        teta1 = self.teta1 + self.calTeta2(tho)*self.dt
        self.teta1 = teta1

    def updateTeta(self):
        teta=self.teta+self.teta1*self.dt
        self.teta=teta

    def rad2deg(self):
        return self.teta*180/math.pi