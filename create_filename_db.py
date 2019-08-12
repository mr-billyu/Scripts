#!/usr/bin/env python3

import subprocess
import sys
import os
import argparse

# Get command line parameters. User is required to enter start path,
# database name and list of file extensions to find.
parser = argparse.ArgumentParser(description='Script to find all of' +
                                             ' filenames with the' +
                                             ' specified extensions' +
                                             ' recursively in start path' +
                                             ' and ouptut the filenames' +
                                             ' to the specified database.')
parser.add_argument('start_path', help='Path to start recursive find at.')
parser.add_argument('db_name', help='Database filename to output the' +
                                    ' results to.')
parser.add_argument('file_types', help='File extentions to find.' +
                                       'ie. "jpg, jpeg, img".')
args = parser.parse_args()
start_path = args.start_path
db_name = args.db_name
file_types = args.file_types

print(start_path)
print(db_name)
print(file_types)

# Reformat file_types to work with the 'find' command.
# file_type of "jpg, img" need to be converted to
# \( -name "*.jpg" -o -name "*.img" \)
# to be in
types = "\( "
index = 0
extensions = file_types.split(',')
for type in (extensions):
    if index > 0:
        types = types + "-o "
    index = index + 1
    types = types + "-name \"*." + type + "\" "
types = types + "\)"
print(types)

