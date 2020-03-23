#include <iostream>
#include "../include/particle.hpp"
#include "../include/gnuplot.hpp"

using namespace std;


// entry point of program
int main(void){

    // Initialize stuff
    Particle particle(4, 40, 30, 2, 6);
    float timestep = 0.1;

    // loop through timesteps and update particle & record in txt file
    for (float t = 0; t<100; t += timestep){
        particle.update(timestep);
        particle.record(t+timestep);
    }

    // call gnuplot
    GnuplotPipe gpp;
    gpp.sendLine("load 'commands.gnu");
    gpp.sendEndOfData();
    return 0;
};

