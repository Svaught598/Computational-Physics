#include <iostream>
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


// entry point of program
int main(int argc, char *argv[]){

    // Parsing through command line arguments
    for (int i = 1; i < argc; ++i)
    {
        if (std::string(argv[i]) == "--plot")
        {
            plot();
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
    plot();
    return 0;
};

