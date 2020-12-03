import os
import sys

# Adds a file paths to sys.path in python 
sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

# print(sys.path)


