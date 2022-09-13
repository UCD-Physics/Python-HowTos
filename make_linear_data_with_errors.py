#! /usr/bin/env python

import numpy as np

m = 0.6
c = 2.5
noise = 1.0

def line(x, m, c):
    """Straight line equation for generating data and fitting """
    return m * x + c
    
x = np.arange(10)
y = line(x, m, c) + np.random.randn(len(x))
yerr = np.ones_like(y) * noise

fname = "linear_data_with_errors.txt"

np.savetxt(fname,
           np.c_[x,y,yerr],
           header=f"{m=} {c=} {noise=}")

print("Successfully made", fname)

