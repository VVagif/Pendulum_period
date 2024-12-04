import math

def pendulum_period(lenght):
    g = 9.8 # Acceleration due to gravity
    return 2 * math.pi * math.sqrt(lenght/g)

lenght = int(input("Enter the lenght of the pendulum: ")) #pendulum lenght range
period = pendulum_period(lenght)

print(f"Pendulum lenght: {lenght} m, Period : {period:.2f} s")

