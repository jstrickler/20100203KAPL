#!/usr/bin/env python
from subprocess import run, PIPE, CalledProcessError
import shlex
from glob import glob

# file_list = glob("*.txt")

cmd = '''netstat -an "big deal"'''

# run(cmd, shell=True)
# OR
cmd_words = shlex.split(cmd)
print(cmd_words)
try:
    proc = run(cmd_words, stdout=PIPE, stderr=PIPE)
except CalledProcessError as err:
    print(err, err.returncode)
else:
    # print(proc.stdout.decode())
    all_lines = proc.stdout.decode().splitlines()
    for line in all_lines:
        if 'ESTAB' in line:
            print(line)






