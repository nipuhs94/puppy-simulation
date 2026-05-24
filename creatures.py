"""
creatures.py - class definitions for the creatures and items in FOP Assignment, Sem 1 2024

Written by : Nipuna Samarasinghe
Student ID : 22084280

Includes:
    Puppy
    Person
    Friend (child class of Person)
    Stranger (child class of Person)
    Squirrel
    Animal

Versions:
    - initial version supplied 1/4/24
"""
import random
import matplotlib.pyplot as plt
import matplotlib.patches as pat

def flip_coords(pos, LIMITS):
    return((pos[1],pos[0]))

class MSnoopy():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos
 # Step changes with limitations
    def step_change(self, step):
        # 1.1.1 Runs behind the news van
        if step < 13:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 13 and step < 38:
            move = (0,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.1.2 Walks back home with the newspaper
        elif step >= 39 and step < 46:
            move = (-1,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 46 and step < 60:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 3, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Rectangle((fpos[0] -1.2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +1 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth

# Annotations with limitations
        if step < 15:
            ax.annotate("Strangerrr", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 15 and step < 38:
            ax.annotate("Go Awaaay!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 39 and step < 46:
            ax.annotate("Oh Treats!! ", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 46 and step < 55:
            ax.annotate(":)", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class ESnoopy():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.2.1 Runs for the ball
        if step > 3 and step < 8:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 8 and step < 24:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 25 and step < 30:
            move = (-1,-1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 30 and step < 32:
            move = (0,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.2.2 Comes with the ball
        elif step >= 32 and step < 45:
            move = (2,-1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.2.3 Runs for the Guy
        elif step >= 45 and step < 60:
            move = (2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 3, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Rectangle((fpos[0] -1.2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +1 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth

# Annotations with limitations      
        if step > 3 and step < 8:
            ax.annotate("Toyy!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 8 and step < 15:
            ax.annotate("I Want Toy!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 32 and step < 40:
            ax.annotate("Yum Yumm!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 40 and step < 50:
            ax.annotate("Is That Guy", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 50 and step < 55:
            ax.annotate("Guuyyy", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 55 and step < 60:
            ax.annotate("Im Comingg!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class NSnoopy():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.3.1 Walks to the frontyard
        if step > 5 and step < 13:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 13 and step < 21:
            move = (2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 22 and step < 45:
            move = (0,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.3.2 Sleeps
        elif step >= 46 and step < 55:
            move = (0,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 3, color=self.colour1)
        ax.add_patch(patch)
# Sleeping eyes animation
        if step >44:
            patch = pat.Ellipse((fpos[0]-1.2, fpos[1]-0.8), height= 0.4, width= 1.2, color=self.colour2)
            ax.add_patch(patch) # closed eyes
        else:
            patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
            ax.add_patch(patch) # open eyes

        if step >44:
            patch = pat.Ellipse((fpos[0]+1.2, fpos[1]-0.8), height= 0.4, width= 1.2, color=self.colour2)
            ax.add_patch(patch) # closed eyes
        else:
            patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
            ax.add_patch(patch) # open eyes
        
        patch = pat.Rectangle((fpos[0] -1.2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +1 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth

# Annotation with limitations       
        if step < 8:
            ax.annotate("Tired Now!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 15 and step < 20:
            ax.annotate("Yawning!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 39 and step < 44:
            ax.annotate("Sleeepy", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        # Sleeping annotation change with step
        elif step >44 and step %2 == 0:
            ax.annotate("Zz!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >44 and step %2 == 1:
            ax.annotate("Zz!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class MRover():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.4.1 chases the ball
        if step > 3 and step < 8:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 8 and step < 24:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 25 and step < 30:
            move = (-1,-1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 30 and step < 32:
            move = (0,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.4.2 Comes back with the ball
        elif step >= 32 and step < 50:
            move = (2,-1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 3, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Rectangle((fpos[0] -1.2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +1 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth
        
# Annotation with limitations
        if step > 3 and step < 8:
            ax.annotate("My Toyy!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 8 and step < 15:
            ax.annotate("Waitt!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 32 and step < 40:
            ax.annotate("Yum Yumm!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 40 and step < 50:
            ax.annotate("Catch mee", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 50 and step < 55:
            ax.annotate("Now you Run", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 55 and step < 60:
            ax.annotate("Ha! Ha! Ha!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class ERover():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.5.1 Chases the squirrel
        if step > 3 and step < 8:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 8 and step < 15:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 15 and step < 45:
            move = (0,3)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 45 and step < 55:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 3, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Rectangle((fpos[0] -1.2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +1 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth

# Annotations with limitations
        if step > 3 and step < 8:
            ax.annotate("Squirrel!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 8 and step < 15:
            ax.annotate("Waitt!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 15 and step < 45:
            ax.annotate("Lets Play!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 45 and step < 55:
            ax.annotate("Where are you :(", (fpos[0], fpos[1]-4), ha = "center", va = "center")

class NRover():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step Change with limitations
    def step_change(self, step):
        # 1.6.1 Walks around the backyard
        if step > 3 and step < 20:
            move = (-2,-1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 20 and step < 45:
            move = (0,-3)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 45 and step < 50:
            move = (1,-3)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 50 and step < 60:
            move = (2,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 3, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Rectangle((fpos[0] -1.2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +1 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour2)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # ears

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth
        
    # Annotation with limitations
        if step > 3 and step < 8:
            ax.annotate("It's Cold!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 15 and step < 20:
            ax.annotate("I'll Protect!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 35 and step < 40:
            ax.annotate("I'm Bored!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 45 and step < 50:
            ax.annotate("Hummmm", (fpos[0], fpos[1]-4), ha = "center", va = "center")
              
class Car():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.7.1 Drives to the house
        if step < 14:
            move = (0,4)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 14 and step < 17:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Rectangle(fpos, height=5, width= 10, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]+1.2, fpos[1]+5.5), radius=1.2, color=self.colour2)
        ax.add_patch(patch) # wheels

        patch = pat.Circle((fpos[0]+9, fpos[1]+5.5), radius=1.2, color=self.colour2)
        ax.add_patch(patch) # wheels

        patch = pat.Rectangle((fpos[0] +1, fpos[1] +1), height= 2, width= 3, color=self.colour2)
        ax.add_patch(patch) # glass
        patch = pat.Rectangle((fpos[0] +5 , fpos[1] +1), height= 2, width= 3, color=self.colour2)
        ax.add_patch(patch) # glass

        patch = pat.Ellipse((fpos[0] +10, fpos[1] +2.1 ), height= 4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # glass
        
        #ax.annotate("News Papers", (fpos[0], fpos[1]-4), ha = "center", va = "center")

class Newscar():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.8.1 Drives on the road
        if step > 3:
            move = (0,4)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        
    def plot_me(self ,ax, LIMITS):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Rectangle(fpos, height=5, width= 10, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]+1.2, fpos[1]+5.5), radius=1.2, color=self.colour2)
        ax.add_patch(patch) # wheels

        patch = pat.Circle((fpos[0]+9, fpos[1]+5.5), radius=1.2, color=self.colour2)
        ax.add_patch(patch) # wheels

        patch = pat.Rectangle((fpos[0] +1, fpos[1] +1), height= 2, width= 3, color=self.colour2)
        ax.add_patch(patch) # glass
        patch = pat.Rectangle((fpos[0] +5 , fpos[1] +1), height= 2, width= 3, color=self.colour2)
        ax.add_patch(patch) # glass

        patch = pat.Ellipse((fpos[0] +10, fpos[1] +2.1 ), height= 4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # glass
        
        ax.annotate("News Papers", (fpos[0], fpos[1]-4), ha = "center", va = "center")

class Newspaper():
    """
    Holds information and behaviour of squirrel creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.9.1 Goes to the house in the dogs mouth
        if step >= 39 and step < 46:
            move = (-1,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 46 and step < 60:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        if step > 17:
            fpos = flip_coords(self.pos, LIMITS)
            patch = pat.Rectangle((fpos[0] , fpos[1]  ), height= 1, width= 3, color=self.colour2)
            ax.add_patch(patch) 
        
class MSquirrel():
    """
    Holds information and behaviour of squirrel creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.10.1 Walks around in the woods
        if step < 15:
            move = (0,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 15 and step < 20:
            move = (1,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 20 and step < 30:
            move = (1,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 30 and step < 46:
            move = (1,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 46 and step < 60:
            move = (-1,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.1, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.1, color=self.colour2)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0] , fpos[1]  ), height= 0.6, width= 1.5, color=self.colour2)
        ax.add_patch(patch) # mouth

        patch = pat.Ellipse((fpos[0] -2.7, fpos[1] +0.4 ), height= 1, width= 3.5, color=self.colour2)
        ax.add_patch(patch) # tail

# Annotation with limitations
        if step < 25:
            ax.annotate("Bum Bum Bum", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 25 and step < 44:
            ax.annotate("Bum Bum", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 46 and step < 60:
            ax.annotate("Bum Bum Bum", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class ESquirrel():
    """
    Holds information and behaviour of squirrel creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.11.1 Getting chased by Rover
        if step < 25:
            move = (0,4)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 25 and step < 46:
            move = (1,4)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.1, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.1, color=self.colour2)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0] , fpos[1]  ), height= 0.6, width= 1.5, color=self.colour2)
        ax.add_patch(patch) # mouth

        patch = pat.Ellipse((fpos[0] -2.7, fpos[1] +0.4 ), height= 1, width= 3.5, color=self.colour2)
        ax.add_patch(patch) # tail

# Annotation with limitations
        if step < 25:
            ax.annotate("Dooooggg!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 25 and step < 44:
            ax.annotate("Leave Me Be!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class NSquirrel():
    """
    Holds information and behaviour of squirrel creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.12.1 Walks around in the woods
        if step < 15:
            move = (0,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 15 and step < 20:
            move = (1,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 20 and step < 30:
            move = (1,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 30 and step < 46:
            move = (1,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 46 and step < 60:
            move = (-1,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=1, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]-0.5, fpos[1]-0.5), radius=0.1, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0]+0.5, fpos[1]-0.5), radius=0.1, color=self.colour2)
        ax.add_patch(patch)

        patch = pat.Ellipse((fpos[0] , fpos[1]  ), height= 0.6, width= 1.5, color=self.colour2)
        ax.add_patch(patch) # mouth

        patch = pat.Ellipse((fpos[0] -2.7, fpos[1] +0.4 ), height= 1, width= 3.5, color=self.colour2)
        ax.add_patch(patch) # tail
# Automated annotation for a random moving squirrel 
        if step %2 == 0:
            ax.annotate("Nippy!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        else:
            ax.annotate("Nappy!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class MHomeman():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.13.1 Runs behind Snoopy
        if step > 10 and step < 28:
            move = (2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 28 and step < 35:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 35 and step < 38:
            move = (0,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.13.2 Walks Snoopy back with the newspaper
        elif step >= 39 and step < 46:
            move = (-1,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 46 and step < 60:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 2, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+1.5), height= 3, width= 2, color=self.colour2)
        ax.add_patch(patch) # body

        patch = pat.Rectangle((fpos[0] -2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand
        patch = pat.Rectangle((fpos[0] +1.5 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+4.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +0.5 , fpos[1]+4.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth
        
# Annotation with limitations
        if step < 10:
            ax.annotate("What a Day!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 10 and step < 28:
            ax.annotate("Waait!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 28 and step < 35:
            ax.annotate("Snooopyy", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 35 and step < 38:
            ax.annotate("Stop!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 39 and step < 46:
            ax.annotate("Oh Papper", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 46 and step < 55:
            ax.annotate("Let's Go Home", (fpos[0], fpos[1]-4), ha = "center", va = "center")

class EHomeman():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # Other moves which are invisible till he gets down from the car
        if step > 10 and step < 28:
            move = (2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 28 and step < 35:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 35 and step < 38:
            move = (0,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.14.1 Walks home from the car
        elif step >= 39 and step < 48:
            move = (-1,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 48 and step < 60:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        if step > 38:
            fpos = flip_coords(self.pos, LIMITS)
            patch = pat.Circle(fpos, radius= 2, color=self.colour1)
            ax.add_patch(patch)


            patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
            ax.add_patch(patch) # eyes

            patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
            ax.add_patch(patch) # eyes

            patch = pat.Rectangle((fpos[0] -1, fpos[1]+1.5), height= 3, width= 2, color=self.colour2)
            ax.add_patch(patch) # body

            patch = pat.Rectangle((fpos[0] -2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
            ax.add_patch(patch) # hand
            patch = pat.Rectangle((fpos[0] +1.5 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
            ax.add_patch(patch) # hand

            patch = pat.Rectangle((fpos[0] -1, fpos[1]+4.5), height= 1.2, width= 0.5, color=self.colour1)
            ax.add_patch(patch) # leg
            patch = pat.Rectangle((fpos[0] +0.5 , fpos[1]+4.5), height= 1.2, width= 0.5, color=self.colour1)
            ax.add_patch(patch) # leg

            patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
            ax.add_patch(patch) # nose

            patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
            ax.add_patch(patch) # mouth
        
    # Annotation with limitations
        if step >= 39 and step < 46:
            ax.annotate("Finally!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 46 and step < 55:
            ax.annotate("I'm Homeeee", (fpos[0], fpos[1]-4), ha = "center", va = "center")

class NHomeman():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.15.1 Checks on father and walks to bed
        if step > 5 and step < 21:
            move = (-1,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 21 and step < 40:
            move = (0,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 40 and step < 49:
            move = (2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 2, color=self.colour1)
        ax.add_patch(patch)

        if step > 48:
            patch = pat.Ellipse((fpos[0]-1.2, fpos[1]-0.8), height= 0.2, width= 1.2, color=self.colour2)
            ax.add_patch(patch) # closed eyes
        else:
            patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
            ax.add_patch(patch) # open eyes

        if step > 48:
            patch = pat.Ellipse((fpos[0]+1.2, fpos[1]-0.8), height= 0.2, width= 1.2, color=self.colour2)
            ax.add_patch(patch) # closed eyes
        else:
            patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
            ax.add_patch(patch) # open eyes

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+1.5), height= 3, width= 2, color=self.colour2)
        ax.add_patch(patch) # body

        patch = pat.Rectangle((fpos[0] -2, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand
        patch = pat.Rectangle((fpos[0] +1.5 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+4.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +0.5 , fpos[1]+4.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth

# Annotations with limitations 
        if step < 5:
            ax.annotate("Night Father!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 7 and step < 12:
            ax.annotate("Yawning", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 14 and step < 20:
            ax.annotate("Im Tired", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 43 and step < 48:
            ax.annotate("Nightt!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
    # Automated annotation for sleeping
        elif step > 48 and step %2 == 0:
            ax.annotate("Zz!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step > 48 and step %2 == 1:
            ax.annotate("Zz!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        

class MOtherman():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.16.1 Follows Rover to make him bring the ball back
        if step > 4 and step < 8:
            move = (-2,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 8 and step < 15:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 15 and step < 22:
            move = (1,-2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 22 and step < 26:
            move = (-2,1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.16.2 Runs behind Rover to get the ball back
        elif step >= 35 and step < 60:
            move = (2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 2, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+1.5), height= 3, width= 2, color=self.colour2)
        ax.add_patch(patch) # body

        patch = pat.Ellipse((fpos[0] , fpos[1] +3.5 ), height= 5, width= 3.5, color=self.colour2)
        ax.add_patch(patch) # tummy

        patch = pat.Rectangle((fpos[0] -2.5, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand
        patch = pat.Rectangle((fpos[0] +2 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+6), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +0.5 , fpos[1]+6), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth
        
    # Annotation with limitations
        if step < 4:
            ax.annotate("Catch!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step > 4 and step < 8:
            ax.annotate("Get it Boy!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 8 and step < 15:
            ax.annotate("C'On!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 15 and step < 45:
            ax.annotate("Come To Me!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 45 and step < 55:
            ax.annotate("Gimme The Toyy!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 55 and step < 60:
            ax.annotate("Daamn you Rover!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class EOtherman():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        # 1.17.1 Chases Rover to stop him from chasing the squirrel
        if step > 4 and step < 8:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 8 and step < 15:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 15 and step < 45:
            move = (0,3)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 45 and step < 55:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 2, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Circle((fpos[0]-1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Circle((fpos[0]+1.2, fpos[1]-0.8), radius=0.8, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+1.5), height= 3, width= 2, color=self.colour2)
        ax.add_patch(patch) # body

        patch = pat.Ellipse((fpos[0] , fpos[1] +3.5 ), height= 5, width= 3.5, color=self.colour2)
        ax.add_patch(patch) # tummy

        patch = pat.Rectangle((fpos[0] -2.5, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand
        patch = pat.Rectangle((fpos[0] +2 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+6), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +0.5 , fpos[1]+6), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth
        
    # Annotation with limitations
        if step < 4:
            ax.annotate("Catch!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step > 4 and step < 8:
            ax.annotate("Wait!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 8 and step < 15:
            ax.annotate("Not The Squirrel!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 15 and step < 45:
            ax.annotate("Roverr! Stooop!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        elif step >= 45 and step < 55:
            ax.annotate("Im Old, Stop!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        
class NOtherman():
    """
    Holds information and behaviour of puppy creature
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

# Step change with limitations
    def step_change(self, step):
        if step > 4 and step < 8:
            move = (-2,0)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 8 and step < 15:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 15 and step < 45:
            move = (0,3)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        elif step >= 45 and step < 55:
            move = (1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self ,ax, LIMITS, step):
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius= 2, color=self.colour1)
        ax.add_patch(patch)


        patch = pat.Ellipse((fpos[0]-1.2, fpos[1]-0.8), height= 0.2, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Ellipse((fpos[0]+1.2, fpos[1]-0.8), height= 0.2, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # eyes

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+1.5), height= 3, width= 2, color=self.colour2)
        ax.add_patch(patch) # body

        patch = pat.Ellipse((fpos[0] , fpos[1] +3.5 ), height= 5, width= 3.5, color=self.colour2)
        ax.add_patch(patch) # tummy

        patch = pat.Rectangle((fpos[0] -2.5, fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand
        patch = pat.Rectangle((fpos[0] +2 , fpos[1]+2.5), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # hand

        patch = pat.Rectangle((fpos[0] -1, fpos[1]+6), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg
        patch = pat.Rectangle((fpos[0] +0.5 , fpos[1]+6), height= 1.2, width= 0.5, color=self.colour1)
        ax.add_patch(patch) # leg

        patch = pat.Circle((fpos[0], fpos[1] ), radius=0.2, color=self.colour2)
        ax.add_patch(patch) # nose

        patch = pat.Ellipse((fpos[0], fpos[1] +0.3 ), height= 0.4, width= 1.2, color=self.colour2)
        ax.add_patch(patch) # mouth
    # Automated annotation for sleeping
        if step %2 == 0:
            ax.annotate("Zz!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")
        else:
            ax.annotate("Zz!!!", (fpos[0], fpos[1]-4), ha = "center", va = "center")

class Toy():
    """
    Multiple types of toys for puppy simulation
    """
    def __init__(self, name, colour, pos, vis):
        self.name = name
        self.colour = colour
        self.pos = pos
        self.visible = vis

    def get_pos(self):
        return self.pos
# Step change for playing ball
    def step_change(self, step):
        # 1.19.1 Ball being thrown
        if step > 1 and step < 25:
            move = (-1,2)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])
        # 1.19.2 Ball returning in dogs mouth
        elif step >= 32 and step < 60:
            move = (2,-1)
            self.pos = (self.pos[0] + move[0], self.pos[1] + move[1])

    def plot_me(self,ax, LIMITS):
        if self.visible:
            fpos = flip_coords(self.pos, LIMITS)
            patch = pat.Circle(fpos, radius=0.5, color=self.colour)
            ax.add_patch(patch)
            

class SunMoon():
    """
    Multiple types of toys for puppy simulation
    """
    def __init__(self, name, colour, pos, vis):
        self.name = name
        self.colour = colour
        self.pos = pos
        self.visible = vis

    def get_pos(self):
        return self.pos
    

    def plot_me(self,ax, LIMITS):
        if self.visible:
            fpos = flip_coords(self.pos, LIMITS)
            patch = pat.Circle(fpos, radius=10, color=self.colour)
            ax.add_patch(patch)
            

class Tree():
    """
    Multiple types of toys for puppy simulation
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def plot_me(self,ax, LIMITS):
        
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle(fpos, radius=2, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] +1.5, fpos[1] +4.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] -1.5, fpos[1] +4.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] -3, fpos[1] +8.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] +3, fpos[1] +8.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Rectangle((fpos[0] -1.5, fpos[1]+8.5), height= 6, width= 4, color=self.colour2)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] , fpos[1] +8.5), radius=4, color=self.colour1)
        ax.add_patch(patch)

class Pond():
    """
    Multiple types of toys for puppy simulation
    """
    def __init__(self, name, colour, pos):
        self.name = name
        csplit = colour.split("/")
        self.colour1 = csplit[0]
        if len(csplit) == 2:
            self.colour2 = csplit[1]
        else:
            self.colour2 = csplit[0]
        self.pos = pos

    def get_pos(self):
        return self.pos

    def plot_me(self,ax, LIMITS):
        
        fpos = flip_coords(self.pos, LIMITS)
        patch = pat.Circle((fpos[0] +1.5, fpos[1] +4.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] -1.5, fpos[1] +4.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] -3, fpos[1] +9.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] +3, fpos[1] +8.5), radius=4, color=self.colour1)
        ax.add_patch(patch)
        patch = pat.Circle((fpos[0] , fpos[1] +10), radius=4, color=self.colour1)
        ax.add_patch(patch)   
        patch = pat.Circle((fpos[0] , fpos[1] +5.5), radius=2, color=self.colour2)
        ax.add_patch(patch)   
        
