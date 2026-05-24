"""
testEOtherman.py - Evening Father test code for FOP Assignment

Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: Testing the father in the evening

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import EOtherman

def main():
    size = (20,20)
    yard = np.zeros(size)
    
    otherman = EOtherman("Guy", "beige/brown", (5,5))
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):
        otherman.step_change(t)
        
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        otherman.plot_me(ax, size, t)
        
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
