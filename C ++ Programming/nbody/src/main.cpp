#include <iostream>
#include "../include/particle.hpp"
#include "../include/gnuplot.hpp"
#include "../include/particlegod.hpp"

using namespace std;



// entry point of program
int main(void){

    // Initialize stuff
    ParticleGod handler(100);
    float timestep = 0.1;
    int index = 0;

    // loop through timesteps and update particle & record in txt file
    for (float t=0; t<250; t += timestep){

        handler.update_positions(timestep);
        handler.record_positions(index, timestep);
        index++;
    }

    // call gnuplot
    GnuplotPipe gpp;
    gpp.sendLine("load 'commands.gnu");
    gpp.sendEndOfData();
    return 0;
};

