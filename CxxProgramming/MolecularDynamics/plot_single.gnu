NUM_PARTICLES = 100

# plot settings and stuff
set terminal pngcairo size 800,500 enhanced font 'Verdana,10'
set datafile nofpe_trap

set key noautotitle

# set input and output of each file
set output outpng

# plotting for simulation
set border lw 2
set xtics scale default
set ytics scale default
set lmargin at screen 0.05
set rmargin at screen 0.7
set xrange [0:50]
set yrange [0:50]
set title sprintf('%d timesteps', ii) font 'Verdana,12'
unset colorbox
plot infile using 2:3 pt 7 ps 1 