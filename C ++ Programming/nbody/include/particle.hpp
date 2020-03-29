#pragma once

#include <iostream>
#include <random>
#include <cmath>

using namespace std;


class Particle
{
public:  // attributes +++++++++++++++++++++++++++
    
    // declare some constants
    static const int GRID_SIZE_X = 100;
    static const int GRID_SIZE_Y = 100;
    static const int radius = 1;

    // Attribute Declarations
    double x;
    double y;
    double vx;
    double vy;
    int id;

public:  // constructors +++++++++++++++++++++++++

    // constructor for random conditions
    Particle(int index)
    {
        // between 0 and 100
        x = (double) rand()/RAND_MAX*100;
        y = (double) rand()/RAND_MAX*100;

        // between -5 and 5
        double theta = (double) rand();
        double velocity = 5;
        vx = velocity*cos(theta);
        vy = velocity*sin(theta);

        // id declaration
        id = index;
    }

    // Constructor for initial conditions
    Particle(const double& m, const double& x1, const double& y1, const double& vx1, const double& vy1)
    {
        x = x1;
        y = y1;
        vx = vx1;
        vy = vy1;
    }

public:  // inline methods +++++++++++++++++++++++

    void inline boundary_check()
    {

        // Bounce off x boundaries
        if (x > GRID_SIZE_X){
            vx *= -1;
            x = GRID_SIZE_X;
        }
        else if (x < 0){
            vx *= -1;
            x = 0;
        }

        // Bounce off y boundaries
        if (y > GRID_SIZE_Y){
            vy *= -1;
            y = GRID_SIZE_Y;
        }
        else if (y < 0){
            vy *= -1;
            y = 0;
        }
    }

    void inline collide_with(Particle other)
    {

        // Distance^2 between the particles
        float dist_2 = (x - other.x)*(x - other.x) + (y - other.y)*(y - other.y);
        float min_dist_2 = (radius + other.radius)*(radius + other.radius);

        // If collision, do some stuff
        if (min_dist_2 > dist_2){

            // Resetting positions & displacing both balls
            float dist = sqrtf(dist_2);
            float overlap = 0.5f * (dist - radius - other.radius);
            x -= overlap * (x - other.x)/dist;
            y -= overlap * (y - other.y)/dist;
            other.x += overlap * (x - other.x)/dist;
            other.y += overlap * (y - other.y)/dist;

            // Change velocities to new directions
            float dv1 = vx;
            float dv2 = vy;
            vx = other.vx;
            vy = other.vy;
            other.vx = dv1;
            other.vy = dv2;

        }
    }
};
