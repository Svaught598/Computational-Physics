#include <vector>
#include <random>
#include <fstream>

#include "../include/particlegod.hpp"
#include "../include/particle.hpp"

using namespace std;

void ParticleGod::generate_random_particles(const int& num_particles){
    
    // create some number of random particles put them in a attribute vector
    for (int i = 0; i<= num_particles; i++){
        particles.push_back(Particle(i));
    }
}

void ParticleGod::update_positions(const float& time){

    for (vector<Particle>::iterator it = particles.begin(); it != particles.end(); ++it){
        it->update(time);
    }

}

void ParticleGod::record_positions(const int& time_step, const float& time){

    // converting time to string for filename
    char filename[100];
    sprintf(filename, "./out/timestep%05d.txt", time_step);

    // record positions of each particle controlled by the GOD
    ofstream out(filename, ios::app);
    for (vector<Particle>::iterator it = particles.begin(); it != particles.end(); ++it){
        out << time << '\t' << it->x << '\t' << it->y << endl;
    }
}