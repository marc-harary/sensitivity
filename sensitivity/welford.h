#ifndef WELFORD_H
#define WELFORD_H

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

void update_welford_params(WelfordParams* params, Point p, WelfordParams* updated_params);

#endif // WELFORD_H
