#!/usr/bin/env python
import shutil

shutil.make_archive('datafiles', 'zip', 'DATA')

shutil.make_archive('datafiles', 'tar', 'DATA')
shutil.make_archive('datafiles', 'gztar', 'DATA')
shutil.make_archive('datafiles', 'bztar', 'DATA')

print(shutil.disk_usage('.'))
