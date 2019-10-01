#!/usr/bin/env python3

# Created by DJ Watson
# Created on September 2019
# this program is a guessing game where the user has to guess a number
# that the system has in memory


import constants


def main():
    # input

    numinput = int(input("Guess the number I am thinking of (0-9): "))
    # process

    if numinput == constants.NUMBER:
        # output
        print("Correct!")
    if numinput != constants.NUMBER:
        # output
        print("Incorrect!")


if __name__ == "__main__":
    main()
