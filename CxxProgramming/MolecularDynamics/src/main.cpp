#include <iostream>
#include <omp.h>
#include "../include/particle.hpp"
#include "../include/gnuplot.hpp"
#include "../include/particlegod.hpp"
#include "../include/settings.hpp"

using namespace std;


void plot()
{
    // call gnuplot
    GnuplotPipe gpp;
    gpp.sendLine("NUM_PARTICLES = 100");
    gpp.sendLine("NUM_ITER = 1999");
    gpp.sendLine("load 'commands.gnu");
    gpp.sendEndOfData();
    return;
}


void parallel_plot(int index)
{
    #pragma omp parallel for
    for (int i=0; i <= index; i += 1)
    {
        char infile[100];
        char outfile[100];
        char title[100];

        sprintf(infile, "infile = './out/timestep%06d.txt'", i);
        sprintf(outfile, "outpng = './out/particle_frame%06d.png'", i);
        sprintf(title, "set title '%d Timesteps' font 'Verdana,12'", i);

        GnuplotPipe gpp;
        gpp.sendLine(infile);
        gpp.sendLine(outfile);
        gpp.sendLine("set terminal pngcairo size 800,500 enhanced font 'Verdana,10'");
        gpp.sendLine("set datafile nofpe_trap");
        gpp.sendLine("set key noautotitle");
        gpp.sendLine("set output outpng");
        gpp.sendLine("set border lw 2");
        gpp.sendLine("set xtics scale default");
        gpp.sendLine("set ytics scale default");
        gpp.sendLine("set lmargin at screen 0.05");
        gpp.sendLine("set rmargin at screen 0.7");
        gpp.sendLine("set xrange [0:50]");
        gpp.sendLine("set yrange [0:50]");
        gpp.sendLine(title);
        gpp.sendLine("plot infile using 2:3 pt 7 ps 1");
        //gpp.sendEndOfData();
    }
}

void ffmpegify()
{
    system("ffmpeg -start_number 1 -framerate 120 -i ./out/particle_frame%06d.png -c:v libx264 -pix_fmt yuv420p ./out/particle.mp4");
}


// entry point of program
int main(int argc, char *argv[]){

    // Parsing through command line arguments
    for (int i = 1; i < argc; ++i)
    {
        if (std::string(argv[i]) == "--plot")
        {
            parallel_plot(2000);
            return 0;
        }
    }
    
    // Initialize stuff
    ParticleGod simulation;
    int index = 0;

    // loop through timesteps and update particle & record in txt file
    for (float t=0; t<TOTAL_TIME; t += TIMESTEP)
    {
        //simulation.check_collisions();
        simulation.update(TIMESTEP);
        simulation.new_accelerations();
        simulation.record_positions(index, TIMESTEP);
        index++;
    }
    // plot stuff
    parallel_plot(index);
    ffmpegify();
    return 0;
};

