"""
testTree.py - Tree test code for FOP Assignment


Written by : Nipuna Samarasinghe
Student ID : 22084280

Usage: Testing trees

Versions:
    - initial version supplied 1/4/24
"""
import numpy as np
import matplotlib.pyplot as plt

from creatures import Tree

def main():
    size = (20,20)
    yard = np.zeros(size)
    
    tree = Tree("Tree", "green/brown", (5,10))

    
    
    fig = plt.figure(figsize=(5,5))

    
    plt.imshow(yard, cmap="Blues_r")
    ax = plt.axes()
    tree.plot_me(ax, size)
    
    plt.show()

if __name__ == "__main__":
    main()
