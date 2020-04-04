#include <vector>
#include <random>
#include <fstream>
#include <string>
#include <sstream>

#include "../include/particlegod.hpp"
#include "../include/particle.hpp"
#include "../include/settings.hpp"


void ParticleGod::generate_infected_particles(int num_particles, int num_infected)
{    
    // create some number of random particles put them in a attribute vector
    particles.reserve(num_particles);
    for (int i = 0; i< num_particles; i++){

        // Infected particles
        if (i < num_infected)
        {
            particles.push_back(Particle(i, true, false));
        }

        // Healthy Particles
        else
        {
            particles.push_back(Particle(i, false, false));
        }
    }
}


void ParticleGod::generate_infected_particles(int num_particles, int num_infected, int num_still)
{
    // create some number of random particles put them in a attribute vector
    particles.reserve(num_particles);
    for (int i = 0; i< num_particles; i++){

        // INfected Particles
        if (i < num_infected)
        {
            particles.push_back(Particle(i, true, false));
        }

        // Still Particles
        if (i < num_infected + num_still)
        {
            particles.push_back(Particle(i, false, true));
        }

        // Healthy Particles
        else
        {
            particles.push_back(Particle(i, false, false));
        }
    }
}


void ParticleGod::update(float time)
{
    // Update particle stuff
    for (auto &particle: particles)
    {
        // update positions
        particle.x += particle.vx*time;
        particle.y += particle.vy*time;
        particle.boundary_check();

        // update time_infected counter if infected and check for recovery
        if (particle.status == INFECTED)
        {
            particle.time_infected += 1;
            particle.status = (particle.time_infected >= RECOVERY_TIME) ? RECOVERED : INFECTED;
        }
    }
}


void ParticleGod::check_collisions()
{
    for (auto &particle: particles)
    {
        for (auto &target: particles)
        {
            if (particle.id != target.id)
            {
                // If particles overlap some amount
                if (do_particles_overlap(particle, target))
                {   
                    // Calculate overlap between particles
                    float x1 = particle.x;
                    float x2 = target.x;
                    float y1 = particle.y;
                    float y2 = target.y;
                    float distance_2 = (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2);
                    float distance = sqrtf(distance_2);
                    float overlap = 0.5*(distance - RADIUS*2);
                    
                    // Move the particles
                    particle.x -= overlap*(x1 - x2)/distance;
                    particle.y -= overlap*(y1 - y2)/distance;
                    target.x += overlap*(x1 - x2)/distance;
                    target.y += overlap*(y1 - y2)/distance;

                    // move back if still particle
                    particle.x = (particle.still) ? x1 : particle.x;
                    particle.y = (particle.still) ? y1 : particle.y;
                    target.x = (target.still) ? x2 : target.x;
                    target.y = (target.still) ? y2 : target.y;

                    particle_collision(particle, target, distance);
                    particle_infection(particle, target);
                }
            }
        }
    }
}

void ParticleGod::record_positions(int time_step, float time)
{
    // create buffer so we only write once (because stream overhead is HUGE apparently)
    const int buff_size = NUM_PARTICLES*NUM_PARTICLES;
    char buffer[buff_size];
    int cx = 0;
    vector<int> stats = get_statuses();

    // record positions of each particle controlled by the ParticleGod
    int length_of_vector = particles.size();
    for (int i = 0; i < length_of_vector; i++)
    {
        // cx is updated so we don't overwrite the buffer
        cx += std::snprintf(buffer+cx, buff_size-cx, 
            "%d\t%0.3f\t%0.3f\t%d\n", 
            time_step, particles[i].x, particles[i].y, particles[i].status);
    }

    // Write the status counts on a new block (separated by two blank lines)
    // This has to be done for gnuplot reading
    cx += std::snprintf(buffer+cx, buff_size-cx, "\n");
    cx += std::snprintf(buffer+cx, buff_size-cx, 
        "StatusCounts\t%d\t%d\t%d",
        stats[0], stats[1], stats[2]);

    // create unique filename & output buffer to file (100 is arbitrary length)
    char filename[100];
    sprintf(filename, "./out/timestep%05d.txt", time_step);
    ofstream out(filename);
    out << buffer;
}

void ParticleGod::record_cases(int timestep)
{
    // create buffer so we only write once
    const int buff_size = NUM_PARTICLES*NUM_PARTICLES;
    char buffer[buff_size];
    int cx = 0;

    vector<int> stats = get_statuses();
    int healthy = stats[0] + stats[2];
    int cases = stats[1];

    // create unique filename & output buffer to file (100 is arbitrary length)
    char filename[100];
    sprintf(buffer, "%d\t%d\t%d\n", timestep, healthy, cases);
    ofstream out("./out/cases.txt", std::ios::app);
    out << buffer;
}
