# must specify number of particles
NUM = 10

# plot settings and stuff
set terminal pngcairo size 350,200 enhanced font 'Verdana,10'
stats './out/output.txt' nooutput
set key noautotitle
set xrange [0:100]
set yrange [0:100]

do for [ii=1:STATS_blocks] {
    # set output of each data point to a png
    title = sprintf('./out/particle_frame%04d.png',ii)
    set output title
    plot for [jj=0:NUM-1] './out/output.txt' index ii using 2:3 with circles 
    unset label
    set label  1 sprintf('%d seconds', ii*0.01) at 90, 90 right front font 'Verdana,12'
}

# Create mp4
system('rm ./out/particle.mp4')
ENCODER = system('which ffmpeg')
if (strlen(ENCODER)==0) print '=== ffmpeg not found, exit ==='; exit
CMD = "ffmpeg -start_number 1 -framerate 90 -i ./out/particle_frame%04d.png -c:v libx264 -pix_fmt yuv420p ./out/particle.mp4"
system(CMD)

# Clear directories
system('rm ./out/*.png')
system('rm ./out/output.txt')