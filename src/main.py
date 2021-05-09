#!/usr/bin/env python3

import begin
from functions import iCloudFunctions
from getpass import getpass

@begin.start
def main(func=None):

    if func is None:
        print("Error: function arg required")

    email = input("Please enter icloud email: ")
    password = getpass("Please enter icloud password: ")

    functions = iCloudFunctions(email, password)

    functions.exec(func)