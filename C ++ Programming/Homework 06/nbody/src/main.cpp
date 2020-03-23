#include <iostream>
#include "particle.hpp"

using namespace std;



int main(void){

    // Initialize stuff
    Particle particle(4, 40, 30, 2, 6);
    double timestep = 0.1;

    for (float t = 0; t<100; t += timestep){
        particle.update(timestep);
        particle.record();
    }
    return 0;
};