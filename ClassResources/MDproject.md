# Problem 1: 
Using the codes I sent out earlier as a template, simulate
the COVID-19 spread from that WaPo article.  This should be a
hard-sphere simulation within a reflecting boundary box.  Velocities
should all be equal (so don't conserve momentum in collisions).  But,
if you can't figure this out and need to keep elastic collisions,
that's OK but will have a penalty.

### Part A 
All particles move with constant velocity.  Start with 1 'red'
infected particle and all the rest non-infected 'blue' (you can choose
your own color scheme of course).  Whenever there is a collision
between an infected particle and a non-infected one, the non-infected
one becomes infected and changes color.  (again see the WaPo article).
Include a 'gets well' timescale for the infected particles.  Describe
in your Jupyter notebook that you turn in how you selected this
timescale.  (for our purposes set it such that pretty much everyone is
sick before first infected particle is 'recovered'.

See if you can include a graph above the sim like in WaPo, or failing
that, text boxes that update the numbers (Recovered, Healthy, Sick)
during the run.

### Part B 
 Now lock down 3/4 of the population, and re-run with same
'recovery' timescale as above.  Discuss results

### Part C 
Now lock down 90% of the population and re-run.
Explain your findings in a paragraph or so.

# Problem 2:
Molecular Dynamics with periodic boundary conditions.  For
full credit, implement MD with PBC and Lennard-Jones potential.  For
90% credit, you can continue to use reflective BCs.

### Part A
Write initialization routine that sets up N~25 particles on
quasi-random grid (regular grid with small random displacements).
Integrate using Verlet or Leapfrog method
Start with v=1 for all particles but random directions.
Plot every (?) timesteps the speed distribution and compare with the
Maxwell-Boltzmann distribution.
The Wikipedia page for MB distribution actually shows what I'm looking
for about 1/3 of the way down the page.
https://en.wikipedia.org/wiki/Maxwell%E2%80%93Boltzmann_distribution


### Part B
 Starting again with your initial spatial distribution, now have
1/2 your particles moving left, and 1/2 moving right.  Calculate how
long it takes before your speed distribution is "close" to the MB
distribution.  (Discuss in your writeup).
