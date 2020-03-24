#include <vector>
#include <random>
#include <fstream>
#include <string>
#include <sstream>

#include "../include/particlegod.hpp"
#include "../include/particle.hpp"

using namespace std;

void ParticleGod::generate_random_particles(const int& num_particles){
    
    // create some number of random particles put them in a attribute vector
    particles.reserve(num_particles);
    for (int i = 0; i<= num_particles; i++){
        particles.push_back(Particle());
    }
}

void ParticleGod::update_positions(const float& time){

    // update positions of each particle
    int length_of_vector = particles.size();
    for (int i = 0; i < length_of_vector; i++){
        particles[i].update(time);
        particles[i].check_collisions();
    }

}

void ParticleGod::record_positions(const int& time_step, const float& time){

    // create buffer so we only write once (because stream overhead is HUGE)
    char buffer[10000];
    int cx = 0;

    // record positions of each particle controlled by the GOD
    int length_of_vector = particles.size();
    for (int i = 0; i < length_of_vector; i++){

        // cx is updated so we don't overwrite the buffer
        cx += snprintf(buffer+cx, 10000-cx, "%d\t%0.3f\t%0.3f\n", time_step, particles[i].x, particles[i].y);
    }

    // create unique filename & output buffer to file
    char filename[100];
    sprintf(filename, "./out/timestep%05d.txt", time_step);
    ofstream out(filename);
    out << buffer;
}