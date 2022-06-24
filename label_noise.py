import numpy as np
import random

def flip(x):
    return 1-x

def add_noise(labels, noise_frac, seed=0):
    random.seed(seed)
    noise_n = int(len(labels) * noise_frac)
    y_index = np.arange(0,len(labels),1)
    flip_index = random.sample(list(y_index), noise_n)
    
    for i in flip_index:
        labels[i] = flip(labels[i])
    
    return labels