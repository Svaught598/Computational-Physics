# must specify number of particles & iterations
NUM_PARTICLES = 100
NUM_ITER = 5000

# plot settings and stuff
set terminal pngcairo size 350,200 enhanced font 'Verdana,10'
set datafile nofpe_trap
set key noautotitle
set xrange [0:100]
set yrange [0:100]

do for [ii=1:NUM_ITER-1] {
    # set input and output of each file
    outpng = sprintf('./out/particle_frame%05d.png',ii)
    infile = sprintf("./out/timestep%05d.txt", ii)

    set label  1 sprintf('%d timesteps', ii) at 90, 90 right front font 'Verdana,12'
    set output outpng
    plot infile using 2:3 with points pt 7 ps 1
    unset label
}

# Create mp4
system('rm ./out/particle.mp4')
ENCODER = system('which ffmpeg')
if (strlen(ENCODER)==0) print '=== ffmpeg not found, exit ==='; exit
CMD = "ffmpeg -start_number 1 -framerate 45 -i ./out/particle_frame%05d.png -c:v libx264 -pix_fmt yuv420p ./out/particle.mp4"
system(CMD)

# Clear directories
system('rm ./out/*.png')
system('rm ./out/*.txt')