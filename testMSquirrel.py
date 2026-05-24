"""
testMSquirrel.py - Morning Squirrel test code for FOP Assignment

Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: testing squirrel in the morning

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import MSquirrel

def main():
    size = (20,20)
    yard = np.zeros(size)
    
    rocky = MSquirrel("RockY", "gray/black", (15,5))
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):    
        rocky.step_change(t)
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        rocky.plot_me(ax, size, t)
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
