#include "../include/particle.hpp"
#include <fstream>
using namespace std;

int GRID_SIZE_X = 100;
int GRID_SIZE_Y = 100;

void Particle::update(const float& timestep){

    // update positions
    x += vx*timestep;
    y += vy*timestep;

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
};

void Particle::record(const float& timestep){
    // output positions to txt file
    ofstream out("./out/output.txt", ios::app);
    out << time << '\t' << x << '\t' << endl;
    out << endl;
    out << endl;
};