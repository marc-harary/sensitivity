import numpy as np
from scipy.stats import t

def p_value_for_pcc(r, n):
    if abs(r) == 1:
        return 0.0
    t_statistic = r * np.sqrt((n - 2) / (1 - r**2))
    df = n - 2
    p_value = 2 * t.sf(np.abs(t_statistic), df)
    return p_value

def compute_correlation(data):
    """Compute the correlation for a given dataset."""
    x_vals, y_vals = zip(*data)
    mean_x, mean_y = np.mean(x_vals), np.mean(y_vals)
    cov = np.mean([(x - mean_x) * (y - mean_y) for x, y in data])
    var_x, var_y = np.var(x_vals), np.var(y_vals)
    return cov / (
        np.sqrt(var_x * var_y)# + 1e-10
    )  # Small value to avoid division by zero

def brute_force_search(data, x_range, y_range, grid_size=10):
    """Brute force search to compute the maximal change in correlation."""
    og_r = compute_correlation(data)
    og_p = p_value_for_pcc(og_r, len(data))

    max_p_diff = -np.inf
    max_r_diff = -np.inf

    x_grid = np.linspace(x_range[0], x_range[1], grid_size)
    y_grid = np.linspace(y_range[0], y_range[1], grid_size)

    for x in x_grid:
        for y in y_grid:
            new_data = data + [(x, y)]
            new_r = compute_correlation(new_data)
            new_p = p_value_for_pcc(new_r, len(new_data))
            max_p_diff = max(max_p_diff, abs(og_p - new_p))
            max_r_diff = max(max_r_diff, abs(og_r - new_r))

    return max_r_diff, max_p_diff
