"""
testnight.py - Night simulation for the FOP assignment, Sem 1 2024

Written by : Nipuna Hansika Samarasinghe
Student ID : 22084280

Usage: test scenario of the night 

Versions:
    - initial version supplied 15/4/24
"""
import numpy as np
import matplotlib.pyplot as plt
import time

from creatures import MSnoopy,ESnoopy, NSnoopy
from creatures import MRover, ERover, NRover
from creatures import MSquirrel, ESquirrel, NSquirrel
from creatures import Toy, Newscar, Tree, SunMoon, Pond
from creatures import MHomeman, EHomeman, NHomeman
from creatures import MOtherman, EOtherman, NOtherman

def build_yard(dims):
    plan = np.zeros(dims)
    plan[1:100,1:199] = 5 # green grass
    plan[100:110,:] = 10 # gray walking path
    plan[110:,:] = 0  # black road
    plan[80:81,:] = 0 # black line for the gate
    plan[82:83,:] = 0 # black line for the gate
    plan[84:85,:] = 0 # black line for the gate
    plan[86:87,:] = 0 # black line for the gate
    plan[88:89,:] = 0 # black line for the gate
    plan[40:70,50:125] = 7  #yellow house
    plan[36:40,45:130] = 0 # roof
    plan[33:36,50:125] = 0 # roof
    plan[30:33,60:115] = 0 # roof
    plan[50:70,60:70] = 9 # door
    plan[50:60,85:90] = 8 # windows
    plan[50:60,95:100] = 0 # windows
    plan[50:60,105:110] = 8 # windows
    plan[57:69,75:82] = 3 # bed
    plan[57:69,117:124] = 3 # bed
    plan[70:100,55:75] = 10 # walkinig path
    plan[70:71,50:125] = 0  #black house line
    plan[115:116, 10:20] = 10 # road line
    plan[115:116, 30:40] = 10 # road line
    plan[115:116, 50:60] = 10 # road line
    plan[115:116, 70:80] = 10 # road line
    plan[115:116, 90:100] = 10 # road line
    plan[115:116, 110:120] = 10 # road line
    plan[115:116, 130:140] = 10 # road line
    plan[115:116, 150:160] = 10 # road line
    plan[115:116, 170:180] = 10 # road line
    plan[115:116, 190:200] = 10 # road line

    return plan

def build_yard2(dims):
    plan = np.zeros(dims)
    return plan
   
def update_smells(smells, creatures):
    pass

def plot_yard(ax, p):
    ax.imshow(p, cmap= 'nipy_spectral') # data visualization day

def plot_smells(ax, p):
    ax.imshow(p)
    
    # names and details
def main():
    size = (120,200)
    yard = build_yard(size)
    smells = np.zeros(size)
    
    snoopy = NSnoopy("Bark!! Bark!!", "orange/black", (50,25))
    newscar1 = Newscar("Ausi news", "white/gray", (105,25))
    newscar2 = Newscar("Ausi news", "red/gray", (105,80))
    newscar3 = Newscar("Ausi news", "blue/gray", (105,140))
    newscar4 = Newscar("Ausi news", "green/gray", (105,160))

    rover = NRover("Rover", "brown/black", (50,150))
    rocky = NSquirrel("RockY", "gray/black", (25,150))

    homeman = NHomeman("Guy", "beige/brown", (58,115))
    otherman = NOtherman("Father", "beige/black", (60,120))

    cast = [snoopy, rover, rocky, newscar1, homeman, otherman, newscar2, newscar3, newscar4]

    toy1 = Toy("Ball1", "red", (24,8), True)
    toy2 = SunMoon("Ball2", "lightyellow", (3,3), True)

    tree1 = Tree("Tree", "green/brown", (7,165))
    tree2 = Tree("Tree", "green/brown", (50,170))
    tree3 = Tree("Tree", "green/brown", (35,160))
    tree4 = Tree("Tree", "green/brown", (40,192))
    tree5 = Tree("Tree", "green/brown", (20,175))
    tree6 = Tree("Tree", "green/brown", (60,188))
    tree7 = Tree("Tree", "green/brown", (5,190))

    pond = Pond("Pond", "Blue/White", (60,140))

    items = [toy1, toy2, tree1, tree2, tree3, tree4 ,tree5, tree6, tree7, pond]

    plt.ion()
    fig, axs = plt.subplots(figsize=(15,10))
    
    # step change 
    for timestep in range(60):
        cast[0].step_change(timestep)
        cast[0].plot_me(axs, size, timestep)

        cast[1].step_change(timestep)
        cast[1].plot_me(axs, size, timestep)

        cast[2].step_change(timestep)
        cast[2].plot_me(axs, size, timestep)

        #cast[3].step_change(timestep)
        cast[3].plot_me(axs, size)
        cast[6].plot_me(axs, size)
        cast[7].plot_me(axs, size)
        cast[8].plot_me(axs, size)

        cast[4].step_change(timestep)
        cast[4].plot_me(axs, size, timestep)

        #cast[5].step_change(timestep)
        cast[5].plot_me(axs, size, timestep)

        #items[0].step_change(timestep)
        items[0].plot_me(axs, size)
    

    # title change with time step
        axs.set_title("Time step movement no: "+ str(timestep))
    
        plot_yard(axs, yard)

        
        for c in items:
            c.plot_me(axs, size)
        
        fig.savefig("Night.png")

        fig.canvas.draw()             # this and following lines allow you
                                # to refresh plot in the same window
        fig.canvas.flush_events()
        axs.clear()

    time.sleep(0.1)
if __name__ == "__main__":
    main()
