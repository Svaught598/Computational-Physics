#include <iostream>


class Particle
{
    public:
        
        // Attribute Declarations
        double mass;
        double x;
        double y;
        double vx;
        double vy;


        // Default constructor
        Particle(){
            mass = (double) rand()/RAND_MAX;
            x = (double) rand()/RAND_MAX;
            y = (double) rand()/RAND_MAX;
            vx = (double) rand()/RAND_MAX;
            vy = (double) rand()/RAND_MAX;
        }

        // Constructor for initial conditions
        Particle(double m, double x1, double y1, double vx1, double vy1){
            mass = m;
            x = x1;
            y = y1;
            vx = vx1;
            vy = vy1;
        }


        // Method Declarations
        void update(double timestep);
        void record(float time);
};