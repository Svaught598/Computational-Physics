"""
Problem 7

Golf Drive
"""
import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi


# constant declaration
magnus = 0.25
rho = 1.207
A = 0.04**2*pi
m = 0.050
v0 = 70
g = 9.81
angles = np.arange(0, 80, 1)

# lambda functions for intermediate stuff
C = lambda v: 1./2. if v<=14. else 7./v
F = lambda v: C(v)*rho*A*v**2


# 
def magnus_eqs(R):
    
    # unpacking vector
    x, y = R[0], R[1]
    vx, vy = R[2], R[3]
    
    # updating positions
    fx = vx
    fy = vy
    
    # updating velocities
    fvx = -F(vx)/m - magnus*vy
    fvy = -F(vy)/m - magnus*vx - g
    
    return np.array([fx, fy, fvx, fvy], float)


# function for eulers method
def euler(func, angle, a, b, N):
    
    # initialization
    h = (b-a)/N
    rad = angle*pi/180.
    r = np.array([0, 0, v0*cos(rad), v0*sin(rad)], float)
    tpoints = np.arange(a, b, h)
    xpoints = []
    ypoints = []
    
    # loop breaks when the ball hits the ground
    for t in tpoints:
        xpoints.append(r[0])
        ypoints.append(r[1])
        r += h*func(r)
        if r[1] <= 0:
            break
            
    return xpoints, ypoints


# plotting and finding best angle
plt.figure(figsize=(21,7))
longest = (0, 0)
colors = plt.cm.cividis(np.linspace(0,1,len(angles)))

# heres a loop
for angle, color in zip(angles, colors):
    
    # calling euler for an angle
    xs, ys = euler(magnus_eqs, angle, 0, 10, 10000)
    
    # take new distance if greater than distance travelled
    longest = (angle, xs[-1]) if xs[-1] > longest[1] else longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)

# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, len(angles)+1, 1)
CS3 = plt.contourf(Z, levels, cmap='cividis')
plt.colorbar(CS3) 

# putting it all together
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('Golf Ball Antics')
plt.show()
print(f"""
    Yeah, this angle is pretty shallow
    The following assumptions were made:
    
        - golf ball mass is about 50 grams
        - golf ball radius is about 2 cm
        - density of air is about 1.207 kg/m3
    
    The greatest distance is travelled for ~{longest[0]:2.0f} degrees\n'
    
    Protip: if you plan everything really carefully, you can
    use the magnus effect to hit yourself with the same golfball
    you were trying to drive!
""")


""" Double Magnus Force ++++++++++++++++++++++++++++++++"""
plt.figure(figsize=(20,10))

# plotting and finding best angle
angles = np.arange(0, 69, 1)
plt.subplot(2, 1, 1)
magnus = 0.5
longest = (0, 0)
colors = plt.cm.cividis(np.linspace(0,1,len(angles)))

# heres a loop
for angle, color in zip(angles, colors):
    
    # calling euler for an angle
    xs, ys = euler(magnus_eqs, angle, 0, 5, 10000)
    
    # take new distance if greater than distance travelled
    longest = (angle, xs[-1]) if xs[-1] > longest[1] else longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)
    plt.xlim(-10, 80)

# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, len(angles)+1, 1)
CS3 = plt.contourf(Z, levels, cmap='cividis')
plt.colorbar(CS3) 

# putting it all together
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('Double Magnus Force')

""" Double Magnus Force ++++++++++++++++++++++++++++++++"""

# plotting and finding best angle
angles = np.arange(0, 90, 1)
plt.subplot(2, 1, 2)
magnus = 0
longest = (0, 0)
colors = plt.cm.cividis(np.linspace(0,1,len(angles)))

# heres a loop
for angle, color in zip(angles, colors):
    
    # calling euler for an angle
    xs, ys = euler(magnus_eqs, angle, 0, 10, 10000)
    
    # take new distance if greater than distance travelled
    longest = (angle, xs[-1]) if xs[-1] > longest[1] else longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)
    plt.xlim(-10, 80)

# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, len(angles)+1, 1)
CS3 = plt.contourf(Z, levels, cmap='cividis')
plt.colorbar(CS3) 

# putting it all together
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('No Magnus Force')
plt.show()


""" Smooth Ball ++++++++++++++++++++++++++++++++++++++++++++++++="""


# plotting and finding best angle
angles = np.arange(0, 80, 1)
magnus = 0.25
C = lambda v: 0.2
plt.figure(figsize=(21,7))
longest = (0, 0)
colors = plt.cm.cividis(np.linspace(0,1,len(angles)))

# heres a loop
for angle, color in zip(angles, colors):
    
    # calling euler for an angle
    xs, ys = euler(magnus_eqs, angle, 0, 10, 10000)
    
    # take new distance if greater than distance travelled
    longest = (angle, xs[-1]) if xs[-1] > longest[1] else longest
    
    # plot that mofo!
    plt.plot(xs, ys, color=color)

# setting colorbar values
Z = [[0,0],[0,0]]
levels = range(0, len(angles)+1, 1)
CS3 = plt.contourf(Z, levels, cmap='cividis')
plt.colorbar(CS3) 

# putting it all together
plt.xlabel('x (km)')
plt.ylabel('y (km)')
plt.title('Smooth Ball')
plt.show()
print(f"""
    The following assumptions were made:
    
        - golf ball mass is about 50 grams
        - golf ball radius is about 2 cm
        - density of air is about 1.207 kg/m3
        - smooth ball means C = 0.2 (from here http://www.physics.csbsju.edu/~jcrumley/222_2007/projects/awwerner/project.pdf)
    
    The greatest distance is travelled for ~{longest[0]:2.0f} degrees\n'
""")