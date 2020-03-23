#pragma once
#include <iostream>
#include <random>



class Particle
{
public:  // attributes +++++++++++++++++++++++++++
    
    // Attribute Declarations
    double mass;
    double x;
    double y;
    double vx;
    double vy;

public:  // constructors +++++++++++++++++++++++++
    // Default constructor
    Particle(){
        // between 0 and 100
        mass = (double) (rand()/RAND_MAX*100);
        x = (double) rand()/RAND_MAX*100;
        y = (double) rand()/RAND_MAX*100;

        // between -5 and 5
        vx = (double) (rand()/RAND_MAX*2 - 1)*5;
        vy = (double) (rand()/RAND_MAX*2 - 1)*5;
    }

    // Constructor for initial conditions
    Particle(const double& m, const double& x1, const double& y1, const double& vx1, const double& vy1){
        mass = m;
        x = x1;
        y = y1;
        vx = vx1;
        vy = vy1;
    }

public:  // methods ++++++++++++++++++++++++++++++
    void update(const float& timestep);
    void record(const float& timestep);
};