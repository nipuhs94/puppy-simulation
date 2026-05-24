"""
testCar.py - car test code for FOP Assignment

Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: testing the Guy's car

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import Car

def main():
    size = (50,50)
    yard = np.zeros(size)
    
    postcar = Car("Car", "red/gray", (5,5))
    
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):
        postcar.step_change(t)
        
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        postcar.plot_me(ax, size)
        
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
