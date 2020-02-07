#!/usr/bin/env python
import os
from datetime import datetime

# (CURR_DIR, SUBDIRS, FILES) = os.walk(START_DIR)

START_DIR = "."

for curr_dir, sub_dirs, files in os.walk(START_DIR):
    if '.git' in sub_dirs:
        sub_dirs.remove('.git')
    if "__" in curr_dir:
        continue
    print(curr_dir)
    for file_name in files:
        if '__' in file_name:
            continue
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            timestamp = os.path.getmtime(file_path)
            file_date = datetime.fromtimestamp(timestamp).date()
            print(f"    {file_date} {file_size:8d} {file_name}")
