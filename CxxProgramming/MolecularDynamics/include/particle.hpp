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
    float ax;
    float ay;
    int id;
    float radius;

public:  // constructors +++++++++++++++++++++++++

    // constructor for particle placed at x0,y0 w/ random displacements
    Particle(int index, float x0, float y0)
    {
        // Place particle at x0,y0 with small displacement
        x = (float) x0 + (rand()*2/RAND_MAX - 1);
        y = (float) y0 + (rand()*2/RAND_MAX - 1);

        // other attributes
        id = index;
        radius = RADIUS;

        // Velocity & acceleration
        float theta = (float) rand();
        vx = VELOCITY*cos(theta);
        vy = VELOCITY*sin(theta);
        ax = 0;
        ay = 0;
    }


public:  // inline methods +++++++++++++++++++++++

    void boundary_check()
    {
        // Periodic over x-boundaries
        if (x > GRID_SIZE_X)
        {
            x -= GRID_SIZE_X;
        }
        else if (x < 0)
        {
            x += GRID_SIZE_X;
        }

        // Periodic over y-boundaries
        if (y > GRID_SIZE_Y)
        {
            y -= GRID_SIZE_Y;
        }
        else if (y < 0)
        {
            y += GRID_SIZE_Y;
        }
    }
};
