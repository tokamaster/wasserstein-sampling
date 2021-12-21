"""
    The objective of this script is to generate a plot showing
    [x: number of samples] vs [y: Wasserstein distance]

    Such plot will show the best distance possible for a given
    number of samples, since the samples will be optimised to
    minimise the Wasserstein distance (i.e. any other sampling
    method will perform worse).
"""
import json
from scipy.stats import norm, uniform, wasserstein_distance
from scipy.optimize import minimize
import scipy.integrate as integrate
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np

def ppfecdf(ecdf, value):
    x = ecdf.x
    y = ecdf.y
    z = np.max(np.where(y < value))

    return x[z+1]

def iterater(u):
    x = uniform
    def k(z): return abs(x.ppf(z)-ppfecdf(ECDF(x.ppf(u)), z))

    return integrate.quad(k, 0, 1)[0]

def measurer(number_of_samples):
    """
    Measures the Wasserstein distance between the samples
    and a Gaussian distribution ~ N(0,1)

    Args:
        number_of_samples ([int]): Wasserstein samples

    Returns:
        [float]: Wasserstein distance
        [array]: Optimal samples
    """
    s = [(0, 1) for i in range(0, number_of_samples)]
    s = tuple(s)
    x0 = [np.random.rand() for i in range(0, number_of_samples)]
    res = minimize(iterater, x0, method='SLSQP', bounds=s)
    print("Wasserstein samples:", res.x)
    tocompare = norm.ppf(res.x)
    normal = norm.rvs(loc=0, scale=1, size=100000)

    return wasserstein_distance(tocompare, normal), res.x


f = open('data-total.json')
data = json.load(f)

import matplotlib.pyplot as plt

distance1, data1 = measurer(7)
distance2, data2 = measurer(9)
distance2, data3 = measurer(11)

data_new = [data1.tolist(), data2.tolist(), data3.tolist()]
print(data_new)
for element in data_new:
    data.append(data_new)
with open('data-new.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print('\007')
