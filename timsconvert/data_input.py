import os
import logging
from timsconvert.timestamp import *


# Scan directory for Bruker .d files.
def dot_d_detection(input_directory):
    print(get_timestamp() + ':' + 'trying to find .d files...')
    return [os.path.join(dirpath, directory) for dirpath, dirnames, filenames in os.walk(input_directory)
            for directory in dirnames if directory.endswith('.d')]


# Detect whether .d file is .tdf or .tsf.
def schema_detection(bruker_dot_d_file):
    exts = [os.path.splitext(fname)[1] for dirpath, dirnames, filenames in os.walk(bruker_dot_d_file)
            for fname in filenames]
    print(get_timestamp() + ':' + 'detecting schema...')
    print(get_timestamp() + ':' + 'extensions are ' + exts)
    if '.tdf' in exts and '.tsf' not in exts and '.baf' not in exts:
        print(get_timestamp() + ':' + 'detected TDF')
        return 'TDF'
    elif '.tsf' in exts and '.tdf' not in exts and '.baf' not in exts:
        print(get_timestamp() + ':' + 'detected TSF')
        return 'TSF'
    elif '.baf' in exts and '.tdf' not in exts and '.tsf' not in exts:
        print(get_timestamp() + ':' + 'detected BAF')
        return 'BAF'
