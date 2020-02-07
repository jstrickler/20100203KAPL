#!/usr/bin/env python
import os
from humanize import naturalsize
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print("file path:", file_path)

with open(file_path) as file_in:
    pass

print("Exists?", os.path.exists(file_path))
file_size = os.path.getsize(file_path)
print("size:", file_size)
print("natural size:", naturalsize(file_size))
print("dirname:", os.path.dirname(file_path))
print("filename:", os.path.basename(file_path))
print("path + extension", os.path.splitext(file_path))
raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)
timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)
print("file date:", timestamp.date())
print("file hour:", timestamp.hour)
