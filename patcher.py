from chaospy.distributions.sampler.sequences.halton import create_halton_samples
from pyDOE import *
import re
import numpy as np

def tolister(list):
    new = np.array(re.split("\s+", list.replace('[','').replace(']','')), dtype=float)
    return new.tolist()

import json
f = open('data-total.json')
data = json.load(f)

from scipy.stats import wasserstein_distance, norm
normality = norm.rvs(loc=0,scale=1,size=100000)
distances = []
for element in data:
    normalised = norm.ppf(element)
    distances.append(wasserstein_distance(normalised,normality))

import matplotlib.pyplot as plt
number_of_samples = [1, 3, 5, 7, 9, 11, 15, 25, 30, 35, 45, 50, 55, 65, 100]


monte_carlo_sampling = []
monte_carlo_distances = []
for element in number_of_samples:
    toappend = norm.rvs(loc=0, scale=1, size=element)
    monte_carlo_sampling.append(toappend)
    monte_carlo_distances.append(wasserstein_distance(toappend,normality))

lh_sampling = []
lh_distances = []
for element in number_of_samples:
    toappend = []
    lhd = lhs(1, samples=element)
    lhd = norm(loc=0, scale=1).ppf(lhd)
    for i in range(len(lhd)):
        toappend.append(lhd[i][0])
    lh_sampling.append(toappend)
    lh_distances.append(wasserstein_distance(toappend,normality))

halton_sampling = []
halton_distances = []
for element in number_of_samples:
    toappend = []
    sample = create_halton_samples(order=element)
    normals = norm(loc=0,scale=1).ppf(sample)
    for i in range(len(normals)):
        toappend.append(normals[i])
    halton_sampling.append(toappend)
    halton_distances.append(wasserstein_distance(toappend[0], normality))

plt.scatter(number_of_samples, distances, color='blue', s=4)
plt.plot(number_of_samples, distances, label='Wasserstein Sampling', color='blue')
plt.scatter(number_of_samples, monte_carlo_distances, color='black', s=4)
plt.plot(number_of_samples, monte_carlo_distances, color='black', label='Monte Carlo')
plt.scatter(number_of_samples, lh_distances, color='green', s=4)
plt.plot(number_of_samples, lh_distances, color='green', label='Latin Hypercube')
plt.scatter(number_of_samples, halton_distances, color='red', s=4)
plt.plot(number_of_samples, halton_distances, color='red', label='Halton')
plt.xlabel("Number of samples")
plt.ylabel("Wasserstein distance")
plt.legend(loc='best')
plt.title("Distance to Normal(0,1)")
plt.savefig("wass-vs-mc.png")
