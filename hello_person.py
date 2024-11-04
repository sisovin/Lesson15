# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:51:46 2024

@author: chien
"""
# %%
from turtle import title
import argparse


print("")
title = " Lesson 15: Command Line Arguments in hello_person.py "
print(f"{title}".upper().center(80, "="))
print("")

title = " # Create a function called 'hello': # "
print(f"{title}".center(80, "_"))
# Creating a function called 'hello' that takes a string argument called 'name' and a string argument called 'lang'.

def hello(name, lang):
  greetings = {
    "English": "Hello",
    "Spanish": "Hola",
    "German": "Hallo",
    "Cambodian": "Sua s'dei",
  }
  msg = f"{greetings[lang]}, {name}!"
  print(msg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
      description="Provides a personal greeting."
    )
    
    
    parser.add_argument(
      "-n", "--name", metavar="name",
      required=True, help="The name of the person to greet."
    )

    parser.add_argument(
      "-l", "--lang", metavar="language",
      required=True, choices=["English", "Spanish", "German", "Cambodian"],
      help="The language of the greeting."
    )
    
    args = parser.parse_args()
    
hello(args.name, args.lang)
  
print("")

