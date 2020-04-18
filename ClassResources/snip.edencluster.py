import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randint    # single random integer in range
from IPython.display import clear_output, display

show_growth = True

def ctest(x,y,c):
    if c[x,y]==1:
        return True
    if c[x+1,y]==1 or c[x-1,y]==1 or c[x,y-1]==1 or c[x,y+1]==1:
        return True

def cluster_size(c):
    x,y = np.nonzero(c)
    r = np.sqrt((x-mid)**2 + (y-mid)**2)
    return max(r)+3

def draw_box(r):
    xmin = mid-rstart
    xmax = mid+rstart
    x = [xmin,xmax,xmax,xmin,xmin]
    y = [xmin,xmin,xmax,xmax,xmin]
    plt.plot(x,y,'r',alpha=0.3)

fig, ax = plt.subplots(figsize=(8,8))

ntry = 50000
ngrid = 101
mid = int(ngrid/2)
pltlim = 100

c = np.zeros([ngrid,ngrid],dtype='int')
c[mid,mid] = 1

for i in range(ntry):
    if i%1000==0:
        print("Trial: ",i)
    rstart = int(cluster_size(c))
    x = randint(mid-rstart,mid+rstart)
    y = randint(mid-rstart,mid+rstart)

    if ctest(x,y,c):
        c[x,y] = 1

    if show_growth and i%1000==0:
        plt.clf()
        xc,yc = np.nonzero(c)
        plt.scatter(xc,yc,color="k",s=4)
        plt.axis([0,ngrid,0,ngrid])
        draw_box(rstart)
        display(fig)

plt.clf()
xc,yc = np.nonzero(c)
plt.scatter(xc,yc,color="k",s=4)
plt.axis([0,ngrid,0,ngrid])

plt.show()
plt.figure()

# Now calculate the effective area

ry, rx = np.mgrid[0:ngrid,0:ngrid]

ry = ry-mid
rx = rx-mid

# radii of each cell from center of grid
r = np.sqrt(ry**2 + rx**2)

# rc gives the radii, but only for occupied cells.
rc = r*c

# compute "mass" within different radii

rad = np.arange(2,int(rstart*.7))
m_r = []
for i in range(2,int(rstart*.7)):
    a = rc[rc<i]
    m_r.append(len(a[a>0]))
print(rad,m_r)

logr = np.log10(rad)
logm = np.log10(m_r)
plt.plot(logr,logm,label='data')
m, b = np.polyfit(logr,logm,1)
xfit = np.linspace(min(logr),max(logr),100)
yfit = m*xfit + b
plt.plot(xfit,yfit,'r-',label='fit')
print("slope = ",m)
plt.legend(loc=2)
plt.show()
