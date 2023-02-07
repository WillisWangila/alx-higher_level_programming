#!/usr/bin/python3

"""
Defines function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Searches text for specific string and inserts new string after it

    Args:
        filename (str, optional): File containing text. Defaults to "".
        search_string (str, optional): string to search for. Defaults to "".
        new_string (str, optional): string to be inserted. Defaults to "".
    """
    doc = ""
    with open(filename, 'r') as read_file:
        for line in read_file:
            doc += line
            if search_string in line:
                doc += new_string
    with open(filename, 'w') as write_file:
        write_file.write(doc)
