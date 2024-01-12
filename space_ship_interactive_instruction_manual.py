# # Space Ship's Interactive Instruction Manual
# this line is added here in vscode because this is not Jupyter notebook (formally IPython) so we need to import the display function.
from IPython import display   


import ipywidgets as widgets

ignition = widgets.ToggleButton(
    value=False,
    description='Start Engine',
    button_style='success',
    tooltip='Engage your Engine',
    icon='rocket'
)

output = widgets.Output()

display(ignition, output)

def on_value_change(change):
    with output:
        if change['new'] == True:
            print("engine started!")
        else:   
            print("engine stopped")

ignition.observe(on_value_change, names='value')


# Create a bar chart of your ship's daily statistics,
# visualization to show your ship's oxygen levels 
# by using Matplotlib

# pip install numpy * type in terminal
# pip install matplotlib * type in terminal
# ## Oxygen levels
# Display ten minutes of oxygen levels in your ship. 
# This data is a mockuup of real data, 
# using numpy to an array of 10 integers between 1 and 10.


import numpy as np 
import matplotlib.pyplot as plt 
data = np.random.default_rng(12345)
oxy_nums = data.integers(low=0, high=10, size=10)
plt.bar(range(len(oxy_nums)), oxy_nums)
plt.show()


# Show the time that your ship needs to take to get up to a good speed. 
# Annotate and create an equation that 
# will allow you to input your ship's start velocity, 
# desired end velocity, and acceleration in meters per second.

# ## Ship's velocity
# Show the seconds needed to get from 0 to 60 meters per second, 
# Given the ship's acceleration in meters per second. 
# Determine how long it will take to reach desired velocity.

endVelocity = 60
startVelocity = 0
acceleration = 9.8

time = (endVelocity-startVelocity)/acceleration
print("Time to reach desired velocity = ", time)
