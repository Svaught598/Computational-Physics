#pragma once
#include <iostream>
#include <random>
#include <cmath>

using namespace std;


class Particle
{
public:  // attributes +++++++++++++++++++++++++++
    
    // declare grid size
    static const int GRID_SIZE_X = 100;
    static const int GRID_SIZE_Y = 100;

    // Attribute Declarations
    double x;
    double y;
    double vx;
    double vy;
    double mass;

public:  // constructors +++++++++++++++++++++++++
    // constructor for random conditions
    Particle(){
        // between 0 and 100
        mass = (double) (rand()/RAND_MAX*100);
        x = (double) rand()/RAND_MAX*100;
        y = (double) rand()/RAND_MAX*100;

        // between -5 and 5
        double theta = (double) rand();
        double velocity = (double) rand()/RAND_MAX*10;
        vx = velocity*cos(theta);
        vy = velocity*sin(theta);
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
    void inline update(const float& timestep){

        // update positions
        x = x + vx*timestep;
        y = y + vy*timestep;
    }

    void inline check_collisions(){

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
};
