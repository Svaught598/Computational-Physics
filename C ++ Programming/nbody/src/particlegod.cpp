#include <vector>
#include <random>
#include <fstream>
#include <string>
#include <sstream>

#include "../include/particlegod.hpp"
#include "../include/particle.hpp"
#include "../include/settings.hpp"


void ParticleGod::generate_random_particles(const int &num_particles)
{    
    // create some number of random particles put them in a attribute vector
    particles.reserve(num_particles);
    helper.reserve(num_particles);
    for (int i = 0; i<= num_particles; i++){
        particles.push_back(Particle(i));
    }

    // copy the particle vector to a helper vector
    helper = particles;
}


void ParticleGod::update(const float &time)
{
    // Update particle positions & boundary collisions
    for (auto &particle: particles)
    {
        // update positions
        particle.x += particle.vx*time;
        particle.y += particle.vy*time;
        particle.boundary_check();
    }

    // Update vector copy
    helper = particles;
    
}


void ParticleGod::handle_collisions()
{
    for (int i=0; i < total; i++)
    {
        for (int j=i+1; j < total; j++)
        {
            // Distance squared between particle centers
            float dist_2 = (particles[i].x-particles[j].x)*(particles[i].x-particles[j].x) +(particles[i].y-particles[j].y)*(particles[i].y-particles[j].y);
            float min_dist_2 = (particles[i].radius + particles[j].radius)*(particles[i].radius + particles[j].radius);

            // If particles overlap some amount
            if (dist_2 < min_dist_2)
            {
                float dist = sqrtf(dist_2);
                float overlap = 0.5f * (dist - particles[i].radius - particles[j].radius);

                // Adjust particle positions away from collision
                particles[i].x -= overlap*(particles[i].x - particles[j].x);
                particles[i].y -= overlap*(particles[i].y - particles[j].y);
                particles[j].x += overlap*(particles[i].x - particles[j].x);
                particles[j].y += overlap*(particles[i].y - particles[j].y);

                // Normal vector along collision direction
                float nx = particles[j].x - particles[i].x;
                float ny = particles[j].y - particles[i].y;

                // Tangent
                float tx = -ny;
                float ty = nx;

                // Dot Product Tangent
                float dpTan1 = particles[i].vx *tx + particles[i].vy * ty;
                float dpTan2 = particles[j].vx * tx + particles[j].vy * ty;

                // Dot Product Normal
                float dpNorm1 = particles[i].vx * nx + particles[i].vy * ny;
                float dpNorm2 = particles[j].vx * nx + particles[j].vy * ny;

                //
                float m1 = dpNorm2;
                float m2 = dpNorm1;

                // Update Velocities
                particles[i].vx = tx*dpTan1 + nx*dpNorm2;
                particles[i].vy = ty*dpTan1 + ny*dpNorm2;
                particles[j].vx = tx*dpTan2 + nx*dpNorm1;
                particles[j].vy = ty*dpTan2 + ny*dpNorm1;
            
            }
        }
    }
}


void ParticleGod::record_positions(const int& time_step, const float& time)
{
    // create buffer so we only write once (because stream overhead is HUGE)
    char buffer[_number_of_particles*_number_of_particles];
    int cx = 0;

    // record positions of each particle controlled by the GOD
    int length_of_vector = particles.size();
    for (int i = 0; i < length_of_vector; i++){

        // cx is updated so we don't overwrite the buffer
        cx += std::snprintf(buffer+cx, 10000-cx, "%d\t%0.3f\t%0.3f\n", time_step, particles[i].x, particles[i].y);
    }

    // create unique filename & output buffer to file (100 is arbitrary length)
    char filename[100];
    sprintf(filename, "./out/timestep%05d.txt", time_step);
    ofstream out(filename);
    out << buffer;
}