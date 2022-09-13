#! /usr/bin/env python

import numpy as np

b = 50
a = -0.4e6
noise = 2.0

def exp(x, a, b):
    """Straight line equation for generating data and fitting """
    return b * np.exp(a*x)
    
x = np.arange(15)*1e-6
y = exp(x, a, b) + noise* np.random.randn(len(x))
yerr = np.ones_like(y) * noise

fname = "exp_data_errors.txt"

np.savetxt(fname,
           np.c_[x,y,yerr],
           header=f"{a=} {b=} {noise=}")

print("Successfully made", fname)

