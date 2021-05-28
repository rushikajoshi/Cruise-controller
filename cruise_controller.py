import matplotlib
import matplotlib.pyplot as plt
m=1200
v=0
v1=[]
t=0
t1=[i for i in range(50)]
b=50
r=60
kp=50
ki=10
kd=30
old_e=0
E=0
while t!=50:
    e=r-v
    e_dot=e-old_e
    E=E+e
    u=kp*e+kd*e_dot+ki*E
    old_e=e
    v=(m*v+u*t)/(m+b*t)
    v1.append(v)
    t+=1
    print(f"{v} is velocity \n")
plt.plot(t1,v1)
plt.xlabel('Time(s)')
plt.ylabel('Velocity (m/s)')
plt.title('Cruise controller')
plt.show()
