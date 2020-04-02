#pragma once


// Simulation settings
static const int _number_of_particles = 50;
static const int _number_of_infected = 1;
static const float _timestep = 0.05;
static const float _total_time = 100;
static const int GRID_SIZE_X = 100;
static const int GRID_SIZE_Y = 100;

// Particle Settings
static const float _radius = 1.0;

// Infection Settings
static const float RecoveryTime = 300.0;
enum Status{
    SUSCEPTIBLE = 1,
    INFECTED = 2,
    RECOVERED = 3
};