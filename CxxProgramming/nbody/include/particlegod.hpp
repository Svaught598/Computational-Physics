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

    // Constructor for some still particles
    ParticleGod(int num_particles, int num_infected, int num_still)
    {
        generate_infected_particles(num_particles, num_infected, num_still);
        total = num_particles;
    }

    // Copy constructor
    ParticleGod(const ParticleGod &god)
    {
        particles = god.particles;
        total = god.total;
    }

public: // methods +++++++++++++++++++++++++++++++

    void generate_random_particles(int num_particles);
    void generate_infected_particles(int num_particles, int num_infected);
    void generate_infected_particles(int num_particles, int num_infected, int num_still);
    void update(float time);
    void check_collisions();
    void record_positions(int time_step, float time);
    void record_cases(int timestep);

public: // inline methods ++++++++++++++++++++++++


    vector<int> get_statuses()
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


    bool do_particles_overlap(Particle &particle, Particle &target)
    {
        float x1 = particle.x;
        float x2 = target.x;
        float y1 = particle.y;
        float y2 = target.y;
        float min_dist_2 = (particle.radius + target.radius)*(particle.radius + target.radius);

        // if distance between centers is less that sum of radii
        if (((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2)) <= min_dist_2){
            return true;
        }
        // else they don't overlap
        return false;
    }


    void particle_collision(Particle &particle, Particle &target, float distance)
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
        float d = (1 + m*m);

        // New Velocities
        particle.vx = (vx1 - vx1*m*m + 2*m*vy1)/d;
        particle.vy = (2*m*vx1 + m*m*vy1 - vy1)/d;
        target.vx = (vx2 - vx2*m*m + 2*m*vy2)/d;
        target.vy = (2*m*vx2 + m*m*vy2 - vy2)/d;

        // check to see if either particle is still
        if (particle.still)
        {
            particle.vx = 0;
            particle.vy = 0;
        }
        if (target.still)
        {
            target.vx = 0;
            target.vy = 0;
        }
    }


    void particle_infection(Particle &particle, Particle &target)
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