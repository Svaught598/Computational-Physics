#include <vector>
#include "particle.hpp"
using namespace std;

class ParticleGod
{
public: // attributes ++++++++++++++++++++++++++++

    vector<Particle> particles;
    vector<Particle> helper;
    int total;

public: // constructors ++++++++++++++++++++++++++

    // Default constructor
    ParticleGod();

    // N # of random particles
    ParticleGod(const int& num_particles)
    {
        generate_random_particles(num_particles);
        total = num_particles;
    }

    // Copy constructor
    ParticleGod(const ParticleGod &god)
    {
        particles = god.particles;
    }

public: // methods +++++++++++++++++++++++++++++++

    void generate_random_particles(const int& num_particles);
    void update(const float &time);
    void handle_collisions();
    void record_positions(const int& time_step, const float& time);
};