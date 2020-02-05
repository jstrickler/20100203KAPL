#!/usr/bin/env python

users_by_shell = {}
with open("../DATA/passwd") as passwd_in:
    for line in passwd_in:
        shell = line.rstrip().split(":")[0]
        # or
        # *_, shell = line.rstrip().split(":")
        if shell == "":
            shell = "NONE"

        if shell in users_by_shell:
            users_by_shell[shell] = users_by_shell[shell] + 1
        else:
            users_by_shell[shell] = 1

for shell, count in users_by_shell.items():
    print("{:5d} {}".format(count, shell))
