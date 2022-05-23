"""
File: rocket.py
Name: Andy Chi
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 7


def main():
    """
    This program creates an ASCII art => a rocket, and the size of
    the rocket can be changed by changing the SIZE above.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    This function creates the head of the rocket.
    """
    for i in range(SIZE):
        for j in range(i, SIZE):
            print(" ", end="")
        for j in range(i + 1):
            print("/", end="")
        for j in range(i + 1):
            print("\\", end="")
        print("")


def belt():
    """
    This function creates the belt of the rocket.
    """
    print("+", end="")
    for i in range(SIZE):
        print("==", end="")
    print("+")


def upper():
    """
    This function creates the upper of the rocket.
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(i + 1, SIZE):
            print(".", end="")
        for j in range(i + 1):
            print("/\\", end="")
        for j in range(i + 1, SIZE):
            print(".", end="")
        print("|", end="")
        print("")


def lower():
    """
    This function creates the lower of the rocket.
    """
    for i in range(SIZE):
        print("|", end="")
        for j in range(i):
            print(".", end="")
        for j in range(i, SIZE):
            print("\\/", end="")
        for j in range(i):
            print(".", end="")
        print("|", end="")
        print("")


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
