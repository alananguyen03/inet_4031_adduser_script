#!/usr/bin/python3

# INET4031
# Alana Nguyen
# Date Created: 03-22-2026
# Date Last Modified: 03-22-2026

# os - executes system commands
# re - search and manipulate lines
# sys - read input lines from standard input
import os
import re
import sys

def main():

    # Prompt user to choose dry-run mode or not
    dry_run = input("Run in dry-run mode? (Y/N): ").strip().upper() == "Y"

    for line in sys.stdin:

        # Checks if the line starts with '#' and skips it if it does
        # Lines that start with '#' are comments and need to be skipped
        match = re.match("^#", line)

        # Splits the line into different fields at the ':'
        fields = line.strip().split(':')

        # Skips the line if it doesn't have 5 fields or if it is a comment
        if match or len(fields) != 5:
            if dry_run:
                # Prints out message that a line was skipped if it was marked to be skipped
                if match:
                    print("[DRY RUN] Skipping comment line:", line.strip())
                else:
                    print("[DRY RUN] Skipping line with not enough fields:", line.strip())
            continue  # Move to next line

        # Takes the user information from the respective fields in the input line
        # This extracted information is stored in the passwd file
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the fields into a list to allow users to be assigned to multiple groups
        groups = fields[4].split(',')

        # Prints message letting the user know that the account is being created
        print("==> Creating account for %s..." % username)

        # Variable 'cmd' contains command that creates user account with disabled password and set GECOS
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos, username)

        # The lines below should be left commented out when the code is ran for the first time
        # If uncommented, the statement will execute the command and create the user account
        if dry_run:
            print(cmd)
        else:  # Run normally if not a dry run
            os.system(cmd)

        # Prints message that the password is being set
        print("==> Setting the password for %s..." % username)

        # Variable 'cmd' contains command that will set the user's password
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password, password, username)

        # The lines below should be left commented out when the code is ran for the first time
        # If uncommented, the statement will execute the command and create the user account
        if dry_run:
            print(cmd)
        else:  # Run normally if not a dry run
            os.system(cmd)

        for group in groups:
            # Add user to group if group is not '-' which indicates that there is no group
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)

                if dry_run:
                    print(cmd)
                else:  # Run normally if not a dry run
                    os.system(cmd)

if __name__ == '__main__':
    main()
