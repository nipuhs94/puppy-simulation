"""
testEHomeman.py -  Evening Home Man test code for FOP Assignment

Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: test Guy in the evening 

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import EHomeman

def main():
    size = (20,20)
    yard = np.zeros(size)
    
    homeman = EHomeman("Guy", "beige/brown", (5,5))
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):
        homeman.step_change(t)
        
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        homeman.plot_me(ax, size, t)
        
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
