import random
import math
import datetime
import os
import sys
import time

# Random module
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random float between 0 and 1:", random.random())
print("Random choice from a list:", random.choice([1, 2, 3, 4, 5]))
print("Random sample from a list:", random.sample([1, 2, 3, 4, 5], 3))

# Math module
print("Square root of 16:", math.sqrt(16))
print("Value of pi:", math.pi)
print("Cosine of 0 radians:", math.cos(0))
print("Sine of 0 radians:", math.sin(0))

# Datetime module
current_time = datetime.datetime.now()
print("Current date and time:", current_time)
print("Current date:", current_time.date())
print("Current time:", current_time.time())

# OS module
print("Current working directory:", os.getcwd())
print("List of files in current directory:", os.listdir())
print("Environment variables:", os.environ)
print("Home directory:", os.path.expanduser("~"))
print("Path separator:", os.pathsep)

# Sys module
print("Python version:", sys.version)
print("Platform:", sys.platform)
print("Command line arguments:", sys.argv)
