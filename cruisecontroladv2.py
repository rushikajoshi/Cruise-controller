import matplotlib
import matplotlib.pyplot as plt
import math
m=1200
v=0
v1=[]
t=0
t1=[i for i in range(50)]
b=50
r=60
kp=120
ki=20
kd=10
old_e=0
theta=5*math.pi/6;
E=0
fr=0.01*m*9.8*math.cos(theta)
while t!=50:
    e=r-v
    e_dot=e-old_e
    E=E+e
    u=kp*e+kd*e_dot+ki*E
    old_e=e
    if(math.tan(theta)>=0):
        v=(m*v+t*(u-fr-m*9.8*math.sin(theta)))/(m+b*t)
    else:
        v=(m*v+t*(u-fr+m*9.8*math.sin(theta)))/(m+b*t)
    v1.append(v)
    t+=1
    print(f"{v} (velocity) \n")
plt.plot(t1,v1)
plt.xlabel('Time(s)')
plt.ylabel('Velocity(m/s)')
plt.grid()
plt.show()
