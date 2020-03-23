#include <vector>
#include "particle.hpp"
using namespace std;

class ParticleGod
{
public: // attributes +++++++++++++++++++++++++++

    vector<Particle> particles;

public:  // constructors +++++++++++++++++++++++++
    // Default constructor
    ParticleGod();

    // N # of random particles
    ParticleGod(const int& num_particles){
        generate_random_particles(num_particles);
    }

public: // methods ++++++++++++++++++++++++++++++


    void generate_random_particles(const int& num_particles);
    void update_positions(const float& time);
    void record_positions(const float& time);

};