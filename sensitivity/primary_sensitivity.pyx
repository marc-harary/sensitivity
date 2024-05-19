# distutils: language = c

from libc.stdlib cimport malloc, free

cdef extern from "primary_sensitivity_impl.h":
    ctypedef struct Point:
        double x
        double y
    
    double compute_primary_sensitivity(Point* data, int n, Point* bounds)

def primary_sensitivity(data, bounds):
    cdef int n = len(data)
    cdef Point* data_points = <Point*>malloc(n * sizeof(Point))
    cdef Point* bounds_points = <Point*>malloc(2 * sizeof(Point))
    cdef int i
    cdef double result
    
    if data_points == NULL or bounds_points == NULL:
        raise MemoryError("Unable to allocate memory for points")

    try:
        for i in range(n):
            data_points[i].x = data[i][0]
            data_points[i].y = data[i][1]

        bounds_points[0].x = bounds[0][0]
        bounds_points[0].y = bounds[0][1]
        bounds_points[1].x = bounds[1][0]
        bounds_points[1].y = bounds[1][1]
        
        result = compute_primary_sensitivity(data_points, n, bounds_points)
    finally:
        free(data_points)
        free(bounds_points)
    
    return result

