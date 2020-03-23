#include <iostream>
#include "../include/particle.hpp"
#include "../include/gnuplot.hpp"
#include "../include/particlegod.hpp"

using namespace std;


// entry point of program
int main(void){

    // Initialize stuff
    ParticleGod handler(10);
    float timestep = 0.1;

    // loop through timesteps and update particle & record in txt file
    for (float t = 0; t<100; t += timestep){
        handler.update_positions(timestep);
        handler.record_positions(timestep);
    }

    // call gnuplot
    GnuplotPipe gpp;
    gpp.sendLine("load 'commands.gnu");
    gpp.sendEndOfData();
    return 0;
};

