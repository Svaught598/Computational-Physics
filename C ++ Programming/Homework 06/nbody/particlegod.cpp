#include <vector>
#include <random>

#include "particlegod.hpp"
#include "particle.hpp"


using namespace std;

vector<Particle> ParticleGod::generate_random_particles(int number_of_particles){

    // declare particle vector
    vector<Particle> particles;

    // create some number of random particles
    for (int i = 0; i<= number_of_particles; i++){
        particles.push_back(Particle());
    }

    // return them
    return particles;
}