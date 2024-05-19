#ifndef PRIMARY_SENSITIVITY_H
#define PRIMARY_SENSITIVITY_H
#define N_INTER 4

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
double compute_primary_sensitivity(Point* data, int n, Point* bounds);

#endif // PRIMARY_SENSITIVITY_H

