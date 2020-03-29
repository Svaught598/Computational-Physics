#include <iostream>
#include "../include/particle.hpp"
#include "../include/gnuplot.hpp"
#include "../include/particlegod.hpp"
#include "../include/settings.hpp"

using namespace std;


// entry point of program
int main(void){

    // Initialize stuff
    ParticleGod simulation(_number_of_particles);
    int index = 0;

    // loop through timesteps and update particle & record in txt file
    for (float t=0; t<_total_time; t += _timestep){

        simulation.update(_timestep);
        simulation.handle_collisions();
        simulation.record_positions(index, _timestep);
        index++;
    }

    // call gnuplot
    GnuplotPipe gpp;
    gpp.sendLine("load 'commands.gnu");
    gpp.sendEndOfData();
    return 0;
};

