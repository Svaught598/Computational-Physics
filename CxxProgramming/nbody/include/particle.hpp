#pragma once

#include <iostream>
#include <random>
#include <cmath>

#include "../include/settings.hpp"

using namespace std;


class Particle
{
public:  // attributes +++++++++++++++++++++++++++
    
    // Attribute Declarations
    float x;
    float y;
    float vx;
    float vy;
    int id;
    float radius;

    // Infection Attributes
    Status status = SUSCEPTIBLE;
    int time_infected = 0;




public:  // constructors +++++++++++++++++++++++++

    // constructor for random conditions & infections
    Particle(int index, bool infected)
    {
        // between 0 and 100
        x = (double) rand()/RAND_MAX*50;
        y = (double) rand()/RAND_MAX*50;

        // between -5 and 5
        float theta = (double) rand();
        float velocity = 5;
        vx = velocity*cos(theta);
        vy = velocity*sin(theta);

        // other attributes
        id = index;
        radius = _radius; 

        // infected or not
        if (infected)
        {
            status = INFECTED;
        }
        else 
        {
            status = SUSCEPTIBLE;
        }
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
