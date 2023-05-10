from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import matplotlib.pyplot as plt
import numpy as np
  

root = Tk()
root.geometry("500x450")
root.title("Lorenz Control Panel")

def runPlotter():


    q = E5.get()
    s = E6.get()
    t = E7.get()
    v = E8.get()

    sigCheck= v1.get()
    bCheck = v2.get()
    NCheck = v3.get()
    rayCheck = v4.get()

    lorenz = v11.get()
    wheel = v21.get()



    M = 10

    #gravity (m/s)
    g = 9.8
    #wheel radius (m)
    R = 2
    #leakage rate (vol/s)
    K = 2
    #rotational damping rate (?)
    vn = 5
    #moment of inertia of wheel
    I = M*pow(R,2)

    q1 = 10


    #Prandtl number
    sigma = vn/(K*I)
    #Rayleigh number

    def rayleigh(q1,v):
       return (np.pi*g*R*q1)/(pow(K,2)*v)

    if lorenz == 1:
             if sigCheck == 1:
                sigStep = float(F13.get())
                s1 = float(F5.get())
                s2 = float(F9.get())

             if sigCheck == 0:
                sigStep = 1
                s1 = float(q)
                s2 = s1

             if bCheck == 1:
                bStep = float(F14.get())
                b1 = float(F6.get())
                b0 = b1
                b2 = float(F10.get())
             if bCheck == 0:
                bStep = 1
                b1 = float(s)
                b0 = b1
                b2 = b1

             if NCheck == 1:
                NStep = float(F15.get())
                N1 = int(F7.get())
                N0 = N1
                N2 = int(F11.get())
             if NCheck == 0:
                NStep = 1
                N1 = int(t)
                N0 = N1
                N2 = N1

             if rayCheck == 1:
                rayStep = float(F16.get())
                ray1 = float(F8.get())
                ray0 = ray1
                ray2 = float(F12.get())
             if rayCheck == 0:
                rayStep = 1
                ray1 = 1
                ray0 = 1
                ray2 = 1
    if wheel == 1:
             if sigCheck == 1:
                sigStep = float(F13.get())
                s1 = float(F5.get())
                s2 = float(F9.get())
             if sigCheck == 0:
                sigStep = 1
                s1 = vn/(K*I)
                s2 = s1

             if bCheck == 1:
                bStep = float(F14.get())
                b1 = float(F6.get())
                b0 = b1
                b2 = float(F10.get())
             if bCheck == 0:
                bStep = 1
                b1 = 1
                b0 = b1
                b2 = b1

             if NCheck == 1:
                NStep = float(F15.get())
                N1 = int(F7.get())
                N0 = N1
                N2 = int(F11.get())
             if NCheck == 0:
                NStep = 1
                N1 = int(t)
                N0 = N1
                N2 = N1

             if rayCheck == 1:
                rayStep = float(F16.get())
                ray1 = float(F8.get())
                ray0 = ray1
                ray2 = float(F12.get())
             if rayCheck == 0:
                rayStep = 1 
                ray1 = rayleigh(q1,vn)
                ray0 = ray1
                ray2 = ray1


    while s1 <= s2:
         
         b1 = b0
         while b1 <= b2:
              N1 = N0
              while N1 <= N2:
                 ray1 = ray0
                 while ray1 <= ray2:
                        
                        print(ray1)
                        
                        sigma = s1
                        b =  b1
                        N = N1
                        if v == "-":
                            if wheel == 1:
                                r = ray1
                            if wheel == 0:
                                r = sigma*(sigma+b+3)/(sigma-b-1)
                        if v != "-":
                            if rayCheck == 0:
                                r = float(v)
                            if rayCheck == 1:
                                r = ray1

                        # r = sigma*(sigma+b+3)/(sigma-b-1)

                        #Lorenz equations

                        print(sigma,b,N,r)

                        def dx(x,y):
                            return sigma*(y-x)

                        def dy(x,y,z):
                            return -x*z+r*x-y

                        def dz(x,y,z):
                            return x*y-b*z


                        h = 1/N

                        #initial conditions
                        x = 10
                        y = 10
                        z = 10

                        xhold = []
                        yhold = []
                        zhold = []

                        i = 0

                        while i <= N:

                                k1 = h*dx(x,y)
                                l1 = h*dy(x,y,z)
                                g1 = h*dz(x,y,z)


                                k2 = h*dx(x+(1/2)*k1,y+(1/2)*l1)
                                l2 = h*dy(x+(1/2)*k1,y+(1/2)*l1,z+(1/2)*g1)
                                g2 = h*dz(x+(1/2)*k1,y+(1/2)*l1,z+(1/2)*g1)
    
                                k3 = h*dx(x+(1/2)*k2,y+(1/2)*l2)
                                l3 = h*dy(x+(1/2)*k2,y+(1/2)*l2,z+(1/2)*g2)
                                g3 = h*dz(x+(1/2)*k2,y+(1/2)*l2,z+(1/2)*g2)
    
                                k4 = h*dx(x+k3,y+l3)
                                l4 = h*dy(x+k3,y+l3,z+g3)
                                g4 = h*dz(x+k3,y+l3,z+g3)

                                xn = x + (1/6)*(k1+ 2*k2+2*k3+k4)
                                yn = y + (1/6)*(l1+ 2*l2+2*l3+l4)
                                zn = z + (1/6)*(g1+ 2*g2+2*g3+g4)

                                xhold.append(xn)
                                yhold.append(yn)
                                zhold.append(zn)

    

                                x = xn
                                y = yn
                                z = zn

                                i+=h

                        
                        

                        titleStr = 'Sig = '+ str(s1) + ', b = ' + str(b1) + ', Rayleigh# = ' + str(r) + ', N = ' + str(N1)


                        plt.figure()
                        print(s1)

                        ax = plt.axes(projection = '3d')
                        ax.plot3D(xhold,yhold,zhold)
                        ax.set_title(titleStr)
                
                        ray1+=rayStep
                 N1+=NStep
              b1+=bStep
         s1+=sigStep
       
    plt.show()

frame0 = LabelFrame(root,text="Parameter Entry")
frame0.grid(row=0,column=0)
L1 = Label(frame0,text = 'Sigma (Standard: 10)',bd = 8)
L2 = Label(frame0,text = 'b (Standard: 2.66)', bd = 8)
L3 = Label(frame0,text = 'Number of steps', bd = 8)
L4 = Label(frame0,text = 'Rayleigh number', bd = 8)
L1.pack(side = TOP)
L2.pack(side = TOP)
L3.pack(side = TOP)
L4.pack(side = TOP)

frame1 = LabelFrame(root,text="Enter:")
frame1.grid(row=0,column=1)
E5 = Entry(frame1,bd = 5,width=4)
E6= Entry(frame1,bd = 5,width=4)
E7 = Entry(frame1,bd = 5,width=4)
E8 = Entry(frame1,bd = 5,width=4)
E5.pack(side = TOP)
E6.pack(side = TOP)
E7.pack(side = TOP)
E8.pack(side = TOP)

frame4 = LabelFrame(root,text="Parameter Sweep")
frame4.grid(row=2,column=0)
M1 = Label(frame4,text = 'Sigma range',bd = 8,)
M2 = Label(frame4,text = 'b range', bd = 8)
M3 = Label(frame4,text = 'Step range', bd = 8)
M4 = Label(frame4,text = 'Rayleigh number range', bd = 8)
M1.pack(side = TOP)
M2.pack(side = TOP)
M3.pack(side = TOP)
M4.pack(side = TOP)

frame9 = LabelFrame(root,text="Include?")
frame9.grid(row=2,column=1)
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()

F17 = Checkbutton(frame9, bd = 10,pady = 8, variable = v1)
F18 = Checkbutton(frame9, bd = 10,pady = 8, variable = v2)
F19 = Checkbutton(frame9, bd = 10,pady = 8, variable = v3)
F20 = Checkbutton(frame9, bd = 10,pady = 8, variable = v4)

F17.pack(side = TOP)
F18.pack(side = TOP)
F19.pack(side = TOP)
F20.pack(side = TOP)


frame5 = LabelFrame(root,text="Start:")
frame5.grid(row=2,column=2)
F5 = Entry(frame5,bd = 5,width=4)
F6= Entry(frame5,bd = 5,width=4)
F7 = Entry(frame5,bd = 5,width=4)
F8 = Entry(frame5,bd = 5,width=4)
F5.pack(side = TOP)
F6.pack(side = TOP)
F7.pack(side = TOP)
F8.pack(side = TOP)


frame6 = LabelFrame(root,text="End:")
frame6.grid(row=2,column=3)
F9 = Entry(frame6,bd = 5,width=4)
F10 = Entry(frame6,bd = 5,width=4)
F11 = Entry(frame6,bd = 5,width=4)
F12 = Entry(frame6,bd = 5,width=4)
F9.pack(side = TOP)
F10.pack(side = TOP)
F11.pack(side = TOP)
F12.pack(side = TOP)

frame8 = LabelFrame(root,text="In steps of:")
frame8.grid(row=2,column=4)
F13 = Entry(frame8,bd = 5,width=4)
F14 = Entry(frame8,bd = 5,width=4)
F15 = Entry(frame8,bd = 5,width=4)
F16 = Entry(frame8,bd = 5,width=4)
F13.pack(side = TOP)
F14.pack(side = TOP)
F15.pack(side = TOP)
F16.pack(side = TOP)


frame11 = LabelFrame(root,text="Model type")
frame11.grid(row=3,column=0)
M11 = Label(frame11,text = 'General Lorenz',bd = 8,)
M21 = Label(frame11,text = 'Chaotic Waterwheel', bd = 8)
M11.pack(side = TOP)
M21.pack(side = TOP)


frame10 = LabelFrame(root,text="Select:")
frame10.grid(row=3,column=1)
v11 = IntVar()
v21 = IntVar()

F21 = Checkbutton(frame10, bd = 10,pady = 5, variable = v11)
F22 = Checkbutton(frame10, bd = 10,pady = 5, variable = v21)

F21.pack(side = TOP)
F22.pack(side = TOP)


frame7 = LabelFrame(root)
frame7.grid(row=4,column=0)

b1 = Button(frame7, text="Run", command = runPlotter)
b1.pack()


root.mainloop()

