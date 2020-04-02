#pragma once


// Simulation settings
static const int NUM_PARTICLES = 50;
static const int NUM_INFECTED = 1;
static const float TIMESTEP = 0.05;
static const float TOTAL_TIME = 100;
static const int GRID_SIZE_X = 100;
static const int GRID_SIZE_Y = 100;

// Particle Settings
static const float RADIUS = 1.0;

// Infection Settings
static const float RECOVERY_TIME = 300.0;
enum Status{
    SUSCEPTIBLE = 1,
    INFECTED = 2,
    RECOVERED = 3
};