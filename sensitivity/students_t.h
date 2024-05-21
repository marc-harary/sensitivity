#ifndef STUDENTS_T_H
#define STUDENTS_T_H
#define MAXIT 100 
#define EPS 3.0e-7 
#define FPMIN 1.0e-30

double betacf(double a, double b, double x);
double betai(double a, double b, double x);
double t_cdf(double t, int df);
double students_t(double r, int n);

#endif // STUDENTS_T_H
