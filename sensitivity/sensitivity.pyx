# distutils: language = c

from libc.stdlib cimport malloc, free

cdef extern from "primary_sensitivity_impl.h":
    ctypedef struct Point:
        double x
        double y

    double compute_primary_sensitivities(Point* data, int n, Point* bounds, double* delta_r, double* delta_p)

def primary_sensitivity(data, bounds):
    cdef int n = len(data)
    cdef Point* data_points = <Point*>malloc(n * sizeof(Point))
    cdef Point* bounds_points = <Point*>malloc(2 * sizeof(Point))
    cdef double* delta_r = <double*>malloc(sizeof(double))
    cdef double* delta_p = <double*>malloc(sizeof(double))
    cdef int i
    cdef double result

    if data_points == NULL or bounds_points == NULL or delta_r == NULL or delta_p == NULL:
        if data_points != NULL:
            free(data_points)
        if bounds_points != NULL:
            free(bounds_points)
        if delta_r != NULL:
            free(delta_r)
        if delta_p != NULL:
            free(delta_p)
        raise MemoryError("Unable to allocate memory for points or deltas")

    try:
        for i in range(n):
            data_points[i].x = data[i][0]
            data_points[i].y = data[i][1]

        bounds_points[0].x = bounds[0][0]
        bounds_points[0].y = bounds[0][1]
        bounds_points[1].x = bounds[1][0]
        bounds_points[1].y = bounds[1][1]

        result = compute_primary_sensitivities(data_points, n, bounds_points, delta_r, delta_p)
        delta_r_value = delta_r[0]
        delta_p_value = delta_p[0]
    finally:
        free(data_points)
        free(bounds_points)
        free(delta_r)
        free(delta_p)

    return delta_r_value, delta_p_value

