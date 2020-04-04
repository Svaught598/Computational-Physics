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
    plot infile using 2:3 pt 7 ps 1 
}

# Create mp4
system('rm ./out/particle.mp4')
ENCODER = system('which ffmpeg')
if (strlen(ENCODER)==0) print '=== ffmpeg not found, exit ==='; exit
CMD = "ffmpeg -start_number 1 -framerate 60 -i ./out/particle_frame%05d.png -c:v libx264 -pix_fmt yuv420p ./out/particle.mp4"
system(CMD)

# Clear directories
system('rm ./out/*.png')