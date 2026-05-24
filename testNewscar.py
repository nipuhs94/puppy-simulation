"""
testNewscar.py - News car test code for FOP Assignment

Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: test the news paper van 

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import Newscar

def main():
    size = (50,50)
    yard = np.zeros(size)
    
    newscar = Newscar("Ausi news", "white/gray", (5,5))
    
    
    fig = plt.figure(figsize=(15,15))

    for t in range(5):
        newscar.step_change(t)
        
        plt.imshow(yard, cmap="Blues_r")
        ax = plt.axes()
        newscar.plot_me(ax, size)
        
        plt.pause(1)
        plt.clf()

if __name__ == "__main__":
    main()
