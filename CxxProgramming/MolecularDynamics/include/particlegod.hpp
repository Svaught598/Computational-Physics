#include <vector>
#include "particle.hpp"
using namespace std;

class ParticleGod
{
public: // attributes ++++++++++++++++++++++++++++

    vector<Particle> particles;
    int total;

public: // constructors ++++++++++++++++++++++++++

    // N # of random particles
    ParticleGod()
    {
        particles.reserve(100);
        generate_particles();
        total = particles.size();
    }

public: // methods +++++++++++++++++++++++++++++++

    void generate_particles();
    void update(float time);
    void new_accelerations();
    void check_collisions();
    void record_positions(int time_step, float time);
    void record_velocities();

public: // inline methods ++++++++++++++++++++++++

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
        double x1 = particle.x;
        double x2 = target.x;
        double y1 = particle.y;
        double y2 = target.y;

        // Velocities
        double vx1 = particle.vx;
        double vx2 = target.vx;
        double vy1 = particle.vy;
        double vy2 = target.vy;

        // Intermediate Calculations
        double nx = (target.x - particle.x)/distance;
        double ny = (target.y - particle.y)/distance;
        double tx = -ny;
        double ty = nx;
        double tan1 = vx1*tx + vy1*ty;
        double tan2 = vx2*tx + vy2*ty;
        double dp1 = vx1*nx + vy1*ny;
        double dp2 = vx2*nx + vy2*ny;

        // New Velocities
        particle.vx = tx*tan1 + nx*dp2;
        particle.vy = ty*tan1 + ny*dp2;
        target.vx =tx*tan2 + nx*dp1;
        target.vy = ty*tan2 + ny*dp1;

        /*
        // Renormalize
        float v1 = sqrtf(particle.vx*particle.vx + particle.vy*particle.vy);
        particle.vx = particle.vx/v1*VELOCITY;
        particle.vy = particle.vy/v1*VELOCITY;
        float v2 = sqrtf(target.vx*target.vx + target.vy*target.vy);
        target.vx = target.vx/v2*VELOCITY;
        target.vy = target.vy/v2*VELOCITY;
        */
    }
};