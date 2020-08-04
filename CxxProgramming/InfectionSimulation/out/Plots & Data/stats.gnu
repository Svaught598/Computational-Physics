# Setting stuff for color palette
set cbrange [1:3]
set palette model RGB defined (1 "blue", 2 "dark-green", 3 "dark-yellow")

# set input and output files
unset multiplot
outpng = "./comparison.png"
infile00 = "./Infection.0%Still.txt"
infile70 = "./Infection.70%Still.txt"
infile90 = "./Infection.90%Still.txt"
set output "./comparison.png"

# General plot settings
set terminal pngcairo size 1000,400 enhanced font 'Verdana,10'
set multiplot layout 1,2 title "Disease Spread" font 'Verdana,14'
set key noautotitle
set xrange [0:1500]
set xtics 0,500,1500

# Plotting Healthy vs. Timestep
set title "Healthy Particles"
set xlabel "Timestep"
set ylabel "No. of Particles"
set key inside bottom right
plot infile00 using 1:2 t "No Still Particles" pt 7 ps 1, \
     infile70 using 1:2 t "3/4 Still Particles" pt 7 ps 1, \
     infile90 using 1:2 t "9/10 Still Particles" pt 7 ps 1

# Plotting Healthy vs. Timestep
set title "Infected Particles"
set xlabel "Timestep"
set ylabel "No. of Particles"
set key inside top right
plot infile00 using 1:3 t "No Still Particles" pt 7 ps 1, \
     infile70 using 1:3 t "3/4 Still Particles" pt 7 ps 1, \
     infile90 using 1:3 t "9/10 Still Particles" pt 7 ps 1


#ot infile using 2:xtic(1) every :::1::1 t "Healthy" lc rgb "blue", \
#    '' using 3 every :::1::1 t "Infected" lc rgb "dark-green", \
#    '' using 4 every :::1::1 t "Recovered" lc rgb "dark-yellow"

# finish multiplot
unset multiplot

