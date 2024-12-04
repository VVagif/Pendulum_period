import math

def pendulum_period(lenght):
    g = 9.8 # Acceleration due to gravity
    return 2 * math.pi * math.sqrt(lenght/g)

lenght = [0.5,1.0,1.5,2.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,8.0,9.0,10.0] #pendulum lenght range
period = [pendulum_period(L) for L in lenght]

for L, T in zip(lenght, period):
    print(f"Pendulum lenght: {L} m, Period : {T:.2f} s")

