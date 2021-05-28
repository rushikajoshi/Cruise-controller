import matplotlib
import matplotlib.pyplot as plt
import math
m=1200
v=0
v1=[]
t=0
t1=[i for i in range(100)]
b=50
vr=[60,40]
kp=10
ki=5
kd=1
old_e=0
E=0
i=0
while t!=100:
    if(t==50):
        i+=1
    e=vr[i]-v
    e_dot=e-old_e
    E=E+e
    u=kp*e+kd*e_dot+ki*E
    old_e=e
    v=(m*v+t*u)/(m+b*t)
    v1.append(v)
    t+=1
    print(f"{v} (velocity) \n")
plt.plot(t1,v1)
plt.xlabel('Time(s)')
plt.ylabel('Velocity(m/s)')
plt.grid()
plt.show()
