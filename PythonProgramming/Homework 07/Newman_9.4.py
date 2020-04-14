"""
Newman 9.4

Thermal Diffusion in the Earth's Crust
"""
import numpy as np
import matplotlib.pyplot as plt


# Constant Declaration
A = 10      #constant temp in celsius
B = 12      #constant temp in celsius
tau = 365   #Period of Earth orbit
L = 20      #depth in meters
D = 0.1     #thermal diffusivity
N = 100     #No. of grid divisions
a = L/N     #grid spacing
h = 1.e-2   #timestep
seasons = {
    1: "Spring",
    2: "Summer",
    3: "Autumn",
    4: "Winter"
}


# initialize
Temps = np.zeros(N+1,float)
Temps[1:N]=10


# function to calculate new temps
def CalcTemp(t):
	return A + B*np.sin(2*np.pi*t/tau)


# function to iterate differential equation from t_min to t_max
# Tlist is the initial set of temperatures
def iterate(Tlist ,t_min, t_max):
	t = t_min
	c = h*D/(a*a)

	while t<t_max:
	    # Calculate the new values of T
		Tlist[0] = CalcTemp(t)
		Tlist[N] = 11
		Tlist[1:N] = Tlist[1:N] + c*(Tlist[2:N+1]+Tlist[0:N-1]-2*Tlist[1:N])
		t += h

	return Tlist

#iterate first 9 years
temps_nine = iterate(Temps,0,365*9)

#initialize tenth year to nine year end
temps_ten = temps_nine
t_min = 365*9

# loop through every three months
for t_max in [365*9 + i*(365//4) for i in range(4)]:
    # find new temps & plot them
    temps_ten = iterate(temps_ten,t_min,t_max)
    index = int(t_max%365/(365//4)+1)
    plt.plot(temps_ten,label=f"{seasons[index]}")

    # move min time up for next iteration
    t_min = t_max


# Plotting stuff
plt.legend()
plt.xlabel("Depth (meters)")
plt.ylabel("Temperature (Celsius)")
plt.show()