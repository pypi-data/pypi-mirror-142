import random
import string 
import sys
import os


def main():
  arg1 = sys.argv[1]
  if arg1 == "create":
    name = input("Project name: ")
    vers = input("Version: ")
    desc = input("Description: ")
    categ = input("Category")
    
    os.system(f"mkdir {name}")
    os.system(f"cd {name}")
    with open('config.wize', 'w') as config:
      config.write(f"[[package]]\nname={name}\ndescription={desc}category={categ}\n\nversion={vers}")

    print("Dependencies will now be updated regularly")
  