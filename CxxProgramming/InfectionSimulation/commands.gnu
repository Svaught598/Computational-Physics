NUM_PARTICLES = 200
NUM_ITER = 1999

# Setting stuff for color palette
set cbrange [1:3]
set palette model RGB defined (1 "blue", 2 "dark-green", 3 "dark-yellow")

# plot settings and stuff
set terminal pngcairo size 800,500 enhanced font 'Verdana,10'
set datafile nofpe_trap

set key noautotitle

do for [ii=1:NUM_ITER-1] {
    # set input and output of each file
    outpng = sprintf('./out/particle_frame%05d.png',ii)
    infile = sprintf("./out/timestep%05d.txt", ii)
    set output outpng
    set multiplot layout 1,3 title "Disease Spread" font 'Verdana,14'

    # plotting for simulation
    set border lw 2
    set xtics scale default
    set ytics scale default
    set lmargin at screen 0.05
    set rmargin at screen 0.7
    set xrange [0:100]
    set yrange [0:100]
    set title sprintf('%d timesteps', ii) font 'Verdana,12'
    unset colorbox
    plot infile using 2:3:4 every :::0::0 with points pt 7 ps 2 lc palette
    unset title
    unset xrange
    unset yrange

    # plotting for histogram 
    set border 0
    unset tics
    unset ylabel
    unset xlabel
    set lmargin at screen 0.7
    set rmargin at screen 0.8
    set bmargin at screen 0.07
    set tmargin at screen 0.84
    set yrange [0:NUM_PARTICLES]
    set style data histograms
    set style histogram rowstacked
    set style fill solid border 0 
    set boxwidth 1
    set title '  '
    unset key
    plot infile using 2:xtic(1) every :::1::1 t "Healthy" lc rgb "blue", \
         '' using 3 every :::1::1 t "Infected" lc rgb "dark-green", \
         '' using 4 every :::1::1 t "Recovered" lc rgb "dark-yellow"

    # Plotting for legend
    set lmargin at screen 1. 
    set rmargin at screen 1. 
    unset tics
    unset xlabel
    unset ylabel
    unset title
    set yrange [0:1]
    set key at screen 0.95, screen 0.85
    plot 2 t 'Healthy' lw 5 lc rgb "blue", \
         2 t 'Infected' lw 5 lc rgb "dark-green", \
         2 t 'Recovered' lw 5 lc rgb "dark-yellow"
    set border

    # finish multiplot
    unset multiplot
}

# Create mp4
system('rm ./out/particle.mp4')
ENCODER = system('which ffmpeg')
if (strlen(ENCODER)==0) print '=== ffmpeg not found, exit ==='; exit
CMD = "ffmpeg -start_number 1 -framerate 60 -i ./out/particle_frame%05d.png -c:v libx264 -pix_fmt yuv420p ./out/particle.mp4"
system(CMD)

# Clear directories
system('rm ./out/*.png')