# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien
"""

import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple example script.")

# Add arguments
parser.add_argument("name", type=str, help="The name of the person to greet.")
parser.add_argument("-a", "--age", type=int, help="The age of the person.")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
""" print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.") """

# Use the arguments
if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Hello, World!")

if args.age:
    print(f"You are {args.age} years old.")
else:
    print("Age not provided.")