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
    ParticleGod(const int& num_particles, int num_infected)
    {
        generate_infected_particles(num_particles, num_infected);
        total = num_particles;
    }

    // Copy constructor
    ParticleGod(const ParticleGod &god)
    {
        particles = god.particles;
        total = god.total;
    }

public: // methods +++++++++++++++++++++++++++++++

    void generate_random_particles(const int& num_particles);
    void generate_infected_particles(int num_particles, int num_infected);
    void update(const float &time);
    void check_collisions();
    void record_positions(const int& time_step, const float& time);

public: // inline methods ++++++++++++++++++++++++

    vector<int> inline get_statuses()
    {
        // Iniitailize counts to 0
        vector<int> r(3, 0);

        // Count number of each status
        for (auto &particle: particles)
        {
            switch(particle.status)
            {
                case SUSCEPTIBLE:
                {
                    r[0] += 1;
                    continue;
                }
                case INFECTED:
                {
                    r[1] += 1;
                    continue;
                }
                case RECOVERED:
                {
                    r[2] += 1;
                    continue;
                }
            }
        }
        return r;
    }

    bool inline do_particles_overlap(Particle &particle, Particle &target)
    {
        float x1 = particle.x;
        float x2 = target.x;
        float y1 = particle.y;
        float y2 = target.y;
        if (((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)) <= 4){
            return true;
        }
        return false;
    }

    void inline particle_collision(Particle &particle, Particle &target, float distance)
    {
        // Positions
        float x1 = particle.x;
        float x2 = target.x;
        float y1 = particle.y;
        float y2 = target.y;

        // Velocities
        float vx1 = particle.vx;
        float vx2 = target.vx;
        float vy1 = particle.vy;
        float vy2 = target.vy;

        // Intermediate Calculations
        float nx = (x2 - x1)/distance;
        float ny = (y2 - y1)/distance;
        float m = -nx/ny;
        float d1 = (vx1 + vy1*m)/(1 + m*m);
        float d2 = (vx2 + vy2*m)/(1 + m*m);

        // New Velocities
        particle.vx = 2*d1 - vx1;
        particle.vy = 2*d1*m - vy1;
        target.vx = 2*d2 - vx2;
        target.vy = 2*d2*m - vy2;
    }

    void inline particle_infection(Particle &particle, Particle &target)
    {
        // Unpack statuses to make code readable
        int stat1 = particle.status;
        int stat2 = target.status;

        // Both are healthy
        if (stat1 == SUSCEPTIBLE && stat2 == SUSCEPTIBLE)
        {
            return;
        }

        // Particle 1 is infected
        if (stat1 == INFECTED)
        {
            if (stat2 == SUSCEPTIBLE)
            {
                target.status = INFECTED;
                return;
            }
        }

        // Particle 2 is infected
        if (stat2 == INFECTED)
        {
            if (stat1 == SUSCEPTIBLE)
            {
                particle.status = INFECTED;
                return;
            }
        }
    }

};