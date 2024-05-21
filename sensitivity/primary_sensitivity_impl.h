#ifndef PRIMARY_SENSITIVITY_H
#define PRIMARY_SENSITIVITY_H
#define N_INTER 4

#include "students_t.h"  // Include the header for students_t

typedef struct {
    double x;
    double y;
} Point;

typedef struct {
    int n;
    double mean_x;
    double mean_y;
    double s_x;
    double s_y;
    double s_xy;
} WelfordParams;

void compute_welford_params(Point* data, int n, WelfordParams* params);
double compute_primary_sensitivities(Point* data, int n, Point* bounds, double* delta_r, double* delta_p);
double students_t(double r, int n);

#endif // PRIMARY_SENSITIVITY_H
