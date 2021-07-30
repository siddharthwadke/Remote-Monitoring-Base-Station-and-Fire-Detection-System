import tkinter as tk
import numpy as np
import random
import time
import datetime
import threading


def tick():

    time2=time.strftime('%H:%M:%S')
    clock.config(text=time2)
    clock.after(200,tick)


def get_data():

    threading.Timer(5, get_data).start()
    x = np.random.randint(60, 80, 1)
    y = np.random.randint(40, 50, 1)
    z = np.random.randint(100, 120, 1)
    l_display.config(text=x[0])
    lh_display.config(text=y[0])
    lA_display.config(text=z[0])
    print(x[0])
    print(y[0])
    print(z[0])
    return x[0]
    return y[0]
    return z[0]

mainwindow = tk.Tk()
mainwindow.geometry('640x340')
mainwindow.title("Weather Station Live Feed ")

clock=tk.Label(mainwindow,font=("Arial",30), bg='blue',fg="black")
clock.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

l_m=tk.Label(mainwindow,text="Sensor Data ",font=("Arial",30),fg="Black")
l_m.grid(row=0,column=1, padx=10, pady=10, sticky="nsew")

l_t=tk.Label(mainwindow, text="Temperature F",font=("Arial",25))
l_t.grid(row=1,column=0, padx=10, pady=10, sticky="nsew")

l_h=tk.Label(mainwindow, text="Humidity",font=("Arial",25))
l_h.grid(row=2,column=0, padx=10, pady=10, sticky="nsew")

l_A=tk.Label(mainwindow, text="AQI",font=("Arial",25))
l_A.grid(row=3,column=0, padx=10, pady=10, sticky="nsew")

l_display=tk.Label(mainwindow,font=("Arial",25),fg="red")
l_display.grid(row=1,column=1, padx=10, pady=10, sticky="nsew")

lh_display=tk.Label(mainwindow,font=("Arial",25),fg="red")
lh_display.grid(row=2,column=1, padx=10, pady=10, sticky="nsew")

lA_display=tk.Label(mainwindow,font=("Arial",25),fg="red")
lA_display.grid(row=3,column=1, padx=10, pady=10, sticky="nsew")



tick()
get_data()
mainwindow.mainloop()
