from generateTesting import generateData
from generateTesting import TorsiConvertion

if __name__ == '__main__':
    ob=generateData()
    ob.geneTeta()
    obj=TorsiConvertion()
    print ("teta2 =", obj.calTeta2(5))
    obj.calTeta1(0)
    obj.updateTeta()
    print ("teta :", obj.teta)
    print ("degree :",obj.rad2deg())

