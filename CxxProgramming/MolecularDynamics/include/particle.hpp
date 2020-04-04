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

public:  // constructors +++++++++++++++++++++++++

    // constructor for random conditions & infections
    Particle(int index, bool infected, bool is_still)
    {
        //TODO: change constructor to place particle about some point with minor variation
        // between 0 and 100
        x = (double) rand()/RAND_MAX*GRID_SIZE_X;
        y = (double) rand()/RAND_MAX*GRID_SIZE_Y;

        // other attributes
        id = index;
        radius = RADIUS;

        // Still or not
        float theta = (double) rand();
        vx = VELOCITY*cos(theta);
        vy = VELOCITY*sin(theta);
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
