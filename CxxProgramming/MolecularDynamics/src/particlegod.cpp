#include <vector>
#include <random>
#include <fstream>
#include <string>
#include <sstream>

#include "../include/particlegod.hpp"
#include "../include/particle.hpp"
#include "../include/settings.hpp"

void ParticleGod::generate_particles(int num_particles)
{
    // TODO: generate particles on a quasi random grid.
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

                    particle_collision(particle, target, distance);
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

    // record positions of each particle controlled by the ParticleGod
    int length_of_vector = particles.size();
    for (int i = 0; i < length_of_vector; i++)
    {
        // cx is updated so we don't overwrite the buffer
        cx += std::snprintf(buffer+cx, buff_size-cx, 
            "%d\t%0.3f\t%0.3f\t%d\n", 
            time_step, particles[i].x, particles[i].y, particles[i].status);
    }

    // create unique filename & output buffer to file (100 is arbitrary length)
    char filename[100];
    sprintf(filename, "./out/timestep%05d.txt", time_step);
    ofstream out(filename);
    out << buffer;
}


void ParticleGod::record_velocities()
{
    //TODO: write function that records the velocites at each timestep
}
