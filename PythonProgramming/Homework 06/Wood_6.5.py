"""
Problem 5

Baseball - Motion of a Batted Ball
"""
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, sin, cos, pi, exp


""" Part A +++++++++++++++++++++++++++++++++++++++++++++++"""

# declare constants
v0 = 49
g = 9.81                 # m/s^2
angles = np.arange(0, 90, 1)

# function for rk4 method
def rk4(func, theta, a, b, N):
    
    # initializtaion
    h = (b-a)/N
    t_rads = theta*pi/180.
    R = np.array([0, 0, v0*cos(t_rads), v0*sin(t_rads)], float)
    
    # empty lists
    tpoints = np.arange(a, b, h)
    xpoints = []
    ypoints = []
    y = 1
    
    # rk4 main loop
    for t in tpoints:
        while y >=0:
            xpoints.append(R[0])
            ypoints.append(R[1])

            # rk4 update for R
            k1 = h*func(R, t)
            k2 = h*func(R+0.5*k1, t+0.5*h)
            k3 = h*func(R+0.5*k2, t+0.5*h)
            k4 = h*func(R+k3, t+h)
            R += (k1 + 2*k2 + 2*k3 + k4)/6.
            y = R[1]
    
    return np.array(xpoints), np.array(ypoints)


# Diff eq function
def baseball_1(R, t):
    
    # unpacking vector
    x, y = R[0], R[1]
    vx, vy = R[2], R[3]
    
    # intermediate calculations
    _v = sqrt(vx*vx + vy*vy)
    k = 0.0039 + 0.0058/(1+exp((_v-35)/5.))
    
    # new values and return
    dx = vx 
    dy = vy 
    dvx = - k*vx*_v
    dvy = -g - k*vy*_v
    return np.array([dx, dy, dvx, dvy], float)


# plotting and finding best angle
longest = (0, 0)
colors = plt.cm.jet(np.linspace(0,1,len(angles)))

# heres a loop
for angle, color in zip(angles, colors):
    
    # calling rk4 for an angle
    xs, ys = rk4(baseball_1, angle, 0, 15, 1000)
    
    # take new distance if greater than distance travelled
    longest = (angle, xs[-1]) if xs[-1] > longest[1] else longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)
    
# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, 91, 1)
CS3 = plt.contourf(Z, levels, cmap='jet')
plt.colorbar(CS3) 

# putting it all together
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('No Wind')
plt.show()
print(f'The greatest distance is travelled for ~{longest[0]:2.0f} degrees\n')



""" Part B +++++++++++++++++++++++++++++++++++++++++++++++"""



# declare constants
wind = 0
headwind = 11.1
tailwind = -10.7
angles = np.arange(0, 90, 1)


# Diff eq function
def baseball_2(R, t):
    
    # unpacking vector
    x, y = R[0], R[1]
    vx, vy = R[2], R[3]
    
    # intermediate calculations
    _v = sqrt((vx-wind)**2 + vy*vy)
    k = 0.0039 + 0.0058/(1+exp((_v-35)/5.))
    
    # new values and return
    dx = vx 
    dy = vy 
    dvx = - k*(vx-wind)*_v
    dvy = -g - k*vy*_v
    return np.array([dx, dy, dvx, dvy], float)

""" Everything below this is function call and plotting +++++++++++"""
# declare figsize
plt.figure(figsize=(15, 10))


# plotting and best angle for headwind
head_longest = (0, 0)
wind = headwind
colors = plt.cm.jet(np.linspace(0,1,len(angles)))
plt.subplot(2, 1, 1)
for angle, color in zip(angles, colors):
    
    # calling rk4 for an angle
    xs, ys = rk4(baseball_2, angle, 0, 15, 1000)
    
    # take new distance if greater than distance travelled
    head_longest = (angle, xs[-1]) if xs[-1] > head_longest[1] else head_longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.ylim(0, 120)
    plt.xlim(0, 150)
    plt.title('With Headwind')
    
# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, 91, 1)
CS3 = plt.contourf(Z, levels, cmap='jet')
plt.colorbar(CS3) 
    
    
# plotting and best angle for tailwind
tail_longest = (0, 0)
wind = tailwind
colors = plt.cm.jet(np.linspace(0,1,len(angles)))
plt.subplot(2, 1, 2)
for angle, color in zip(angles, colors):
    
    # calling rk4 for an angle
    xs, ys = rk4(baseball_2, angle, 0, 15, 1000)
    
    # take new distance if greater than distance travelled
    tail_longest = (angle, xs[-1]) if xs[-1] > tail_longest[1] else tail_longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)
    plt.xlabel('x (m)')
    plt.ylabel('y (m)')
    plt.ylim(0, 120)
    plt.xlim(0, 150)
    plt.title('With Tailwind')
    
# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, 91, 1)
CS3 = plt.contourf(Z, levels, cmap='jet')
plt.colorbar(CS3) 

# putting it all together
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('With Tailwind')
plt.tight_layout()
plt.show()
print(f'Max Range With Headwind is at {head_longest[0]:2.0f} degrees\n')
print(f'Max Range With Tailwind is at {tail_longest[0]:2.0f} degrees\n')



""" Part C +++++++++++++++++++++++++++++++++++++++++++++++"""

# declare constants
v0 = 44.7043 # m/s
xf = 18.4404 # m

# Diff eq function
def baseball_2(R, t):
    
    # unpacking vector
    x, y = R[0], R[1]
    vx, vy = R[2], R[3]
    
    # intermediate calculations
    _v = sqrt((vx)**2 + vy*vy)
    k = 0.0039 + 0.0058/(1+exp((_v-35)/5.))
    
    # new values and return
    dx = vx 
    dy = vy 
    dvx = - k*(vx)*_v
    dvy = -g - k*vy*_v
    return np.array([dx, dy, dvx, dvy], float)


# function for rk4 method
def rk4(func, theta, a, b, N):
    
    # initializtaion
    h = (b-a)/N
    t_rads = theta*pi/180.
    R = np.array([0, 0, v0*cos(t_rads), v0*sin(t_rads)], float)
    tpoints = np.arange(a, b, h)
    x = 1
    
    # rk4 main loop
    for t in tpoints:
        while x <= xf:
            # rk4 update for R
            k1 = h*func(R, t)
            k2 = h*func(R+0.5*k1, t+0.5*h)
            k3 = h*func(R+0.5*k2, t+0.5*h)
            k4 = h*func(R+k3, t+h)
            R += (k1 + 2*k2 + 2*k3 + k4)/6.
            x = R[0]
            v = sqrt(R[2]**2 + R[3]**2)
    
    return v

""" Everything below this is function call and printing +++++++++++"""

# calling rk4 for an angle of 0 degrees
velocity = rk4(baseball_2, 0, 0, 2, 100000)

print(f'''
    with the assumptions:
        - There is no wind
        - The ball was thrown at an angle of 0 degrees w.r.t. the horizontal
        
    The velocity when the ball crosses home plate is about ~{velocity:0.2f} m/s
''')