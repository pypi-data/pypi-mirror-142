import sys
import os
import time
from colored import fg

blue = fg("blue")
cyan = fg("cyan")


def main():
  arg1 = sys.argv[1]
  if arg1 == "init":
    print(blue + "Creating PyPi Project...")
    print(blue + "Press enter to skip each configs")
    name = input(cyan + "Project name: ")
    while name == "":
      print(blue + "Project name cannot be empty")
      name = input(cyan + "Project name: ")
    version = input(cyan + "Version: ")
    description = input(cyan + "Description: ")
    url = input(cyan + "Project Website/Git repo: ")
    author = input(cyan + "Author: ")
    email = input(cyan + "Email: ")
    
    os.system(f"mkdir {name}")
    os.system(f"cd {name}")
    with open(f'{name}/setup.py', 'w') as config:
      config.write(f'''
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="{name}",
    version="0.2.9",
    author="{author}",
    author_email="{email}",
    description="{description}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="{url}",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]    
)''')
    os.system(f"mkdir {name}")
    with open(f'{name}/{name}/__init__.py', 'w') as init:
      init.write(f'''
from .{name.capitalize()} import *

__title__ = "{name}"
__summary__ = "{description}"
__uri__ = "{url}"
__version__ = "{version}"
__author__ = "{author}"
__email__ = "{email}"
__license__ = "MIT License"
__copyright__ = "Copyright 2022 " + __author__


def get_version():
    return __version__''')
    with open(f'{name}/{name}/{name.capitalize()}.py', 'w') as project:
      project.write('''
def foo(x, y)
  return x + y                    
                    ''')
    print(blue + "PyPi Project Created")
  elif arg1 == "upload":
    os.system("python3 setup.py bdist_wheel")
    time.sleep(5)
    os.system("pip install twine")
    time.sleep(5)
    os.system("twine upload dist/*")
  elif arg1 == "load":
    os.system("pip install -e .")
    print(blue + "Project loaded, you can now import the project in another file.")
  else:
    print(blue + "Invalid Argument")