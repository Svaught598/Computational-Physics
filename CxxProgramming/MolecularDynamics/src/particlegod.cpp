#include <vector>
#include <random>
#include <fstream>
#include <string>
#include <sstream>

#include "../include/particlegod.hpp"
#include "../include/particle.hpp"
#include "../include/settings.hpp"

void ParticleGod::generate_particles()
{
    int idx = 1;
    // Generate particles on a quasi random grid 
    // each particle has a unique id (idx)
    for (int i=8; i<GRID_SIZE_X; i+=8)
    {
        for (int j=8; j<GRID_SIZE_Y;j+=8)
        {
            particles.push_back(Particle(idx, i, j));
            idx += 1;
        }
    }
}

void ParticleGod::update(float time)
{
    // Update particle stuff
    for (auto &particle: particles)
    {
        // update positions
        particle.x += particle.vx*time + particle.ax*time*time*0.5;
        particle.y += particle.vy*time + particle.ay*time*time*0.5;

        // update velocities
        particle.vx += particle.ax*time;
        particle.vy += particle.ay*time;

        // check boundaries
        particle.boundary_check();
    }
}


void ParticleGod::new_accelerations()
{
    for (auto &particle: particles)
    {
        // initialize accel to 0 and declare working variables
        particle.ax = 0;
        particle.ay = 0;
        double rx = 0;
        double ry = 0;
        double r2 = 0;

        double nx = 0;
        double ny = 0;
        double accel = 0;

        for (auto &target: particles)
        {
            // Don't count force between particle and itself!
            if (particle.id == target.id) continue;

            // Distance between particle centers & normal vector along that axis
            rx = particle.x - target.x;
            ry = particle.y - target.y;
            r2 = sqrtf(rx*rx + ry*ry);
            nx = rx/r2;
            ny = ry/r2;

            
            // accelerations from potential & add to particle accels.
            accel = (2*powf((1/r2),13) - powf((1/r2),7));
            particle.ax += accel*nx;
            particle.ay += accel*ny;

        }
    }
}


void ParticleGod::check_collisions()
{

    for (int i=0; i < total; ++i)
    {
        for (int j=i+1; j<total; ++j)
        {   

            // references for readability
            Particle &particle = particles[i];
            Particle &target = particles[j];

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

void ParticleGod::record_positions(int time_step, float time)
{
    // create buffer so we only write once (because stream overhead is HUGE apparently)
    const int buff_size = NUM_PARTICLES*NUM_PARTICLES;
    char buffer[buff_size];
    int cx = 0;

    // record positions of each particle controlled by the ParticleGod
    for (auto &particle: particles)
    {
        // cx is updated so we don't overwrite the buffer
        cx += std::snprintf(buffer+cx, buff_size-cx, 
            "%d\t%0.3f\t%0.3f\n", 
            time_step, particle.x, particle.y);
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
