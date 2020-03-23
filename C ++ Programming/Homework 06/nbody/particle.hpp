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
            mass = (double) srand()/RAND_MAX;
            x = (double) srand()/RAND_MAX;
            y = (double) srand()/RAND_MAX;
            vx = (double) srand()/RAND_MAX;
            vy = (double) srand()/RAND_MAX;
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
        void record();
};