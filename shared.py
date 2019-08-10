#!/usr/bin/env python3

import subprocess
import sys
import os
import argparse

# Get command line parameters. User is required to enter remote directory
#path and user space mount point.
parser = argparse.ArgumentParser(description='Script to mount remote' +
                                             ' directory to mount point' +
                                             ' in user space.')
parser.add_argument('remote_directory', help='Remote directory path')
parser.add_argument('mount_point', help='Mount point in user space')
args = parser.parse_args()
remote_directory = args.remote_directory
mount_point = args.mount_point

print(remote_directory)
print(mount_point)

# Check if mount point exists.
if os.path.isdir(mount_point):
    pass
else:
    print('mount_point ' + mount_point + ' does not exist.')
    sys.exit(1)

# Check if mount_point is empty. findmnt will return an exception if 
# the mount point is empty.
cmd = 'findmnt ' + mount_point
cmd = cmd.split()
try:
    results = subprocess.check_output(cmd)
except subprocess.CalledProcessError:
    # Mount point is empty.
    cmd = 'sshfs ' + remote_directory + ' ' + mount_point
    cmd = cmd.split()
    try:
        results = subprocess.check_output(cmd)
    except subprocess.CalledProcessError:
        print("Mount Error")
        sys.exit(1)

print("Mounted")

