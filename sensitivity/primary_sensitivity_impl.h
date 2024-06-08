#ifndef PRIMARY_SENSITIVITY_H
#define PRIMARY_SENSITIVITY_H
#define N_INTER 4

#include "welford.h"

double compute_primary_sensitivities(Point* data, int n, Point* bounds, double* delta_r, double* delta_p);
double students_t(double r, int n);

#endif // PRIMARY_SENSITIVITY_H
