#pragma once


// Simulation settings
static const int NUM_PARTICLES = 200;
static const int NUM_INFECTED = 1;
static const int NUM_STILL = 0;
static const float TIMESTEP = 0.05;
static const float TOTAL_TIME = 100;
static const int GRID_SIZE_X = 100;
static const int GRID_SIZE_Y = 100;

// Particle Settings
static const float RADIUS = 1.0;
static const float VELOCITY = 7.5;

// Infection Settings
static const float RECOVERY_TIME = 300.0;
enum Status{
    SUSCEPTIBLE = 1,
    INFECTED = 2,
    RECOVERED = 3
};