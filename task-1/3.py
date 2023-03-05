"""
A procedure that appends the passed string as a new line to the file 
"""


def append_to_file(filename, string):
    with open(filename, "a") as f:
        f.write(string + "\n")
