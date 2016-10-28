#!/usr/bin/env python3
import sys

def valid(pin):
    """
    Takes a 4 digit input and checks it against a valid code.
    Args:
        pin - a 4 digit passcode
    """
    #1) Check the length
    #2) Check the type
    #3) Check against the code
    len(pin) = strLength
    if strLength > 4:
        print("Invalid PIN length. Correct format is <9876>")
    try:
        pinVal = int(pin)
    except ValueError:
        print("Invalid Pin Character. Correct format is <9876>")
    if pin == 1234:
        print("Your PIN is correct.")


def main():
    """
    Test Function
    """
    pass

if __name__ == '__main__':
    

    exit(0)
