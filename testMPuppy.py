"""
testMPuppy.py - Morning Puppies test code for FOP Assignment

Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: testing puppies in the morning

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import MRover, MSnoopy

def main():
    size = (60,60)
    yard = np.zeros(size)
    
    snoopy = MSnoopy("Snoopy", "white/black", (5,15))
    rover = MRover("Rover", "brown/black", (10,5))
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):
        snoopy.step_change(t)
        rover.step_change(t)
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        snoopy.plot_me(ax, size, t)
        rover.plot_me(ax, size, t)
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
