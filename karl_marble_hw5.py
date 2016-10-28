#!/usr/bin/env python3
import sys

def valid():
    """
    Takes a 4 digit input and checks it against a valid code.
    Args:
        None
    Returns:
        None
    """
    #1) Take the Pin Input
    #2) Check the length
    #2) Check the type
    #3) Check against the code
    pin = input("Enter your PIN:")
    strLength = len(pin)
    if strLength > 4:
        print("Invalid PIN length. Correct format is <9876>")
    try:
        pinVal = int(pin)
    except ValueError:
        print("Invalid Pin Character. Correct format is <9876>")
    if pin == "1234":
        print("Your PIN is correct.")


def main():
    """
    Test Function
    """
    pass

if __name__ == '__main__':
    

    exit(0)
