import os
from os.path import join, dirname, abspath
import inspect
import sys

current_dir = dirname(abspath(inspect.getfile(inspect.currentframe())))
tide_dir = join(current_dir, "../../tide")
os.chdir(tide_dir)
paths_list = [current_dir, tide_dir]
paths_list = []

for default in ['actions', 'editor_wrappers', 'filters', 'functions', '.']:
    paths_list.append(join(tide_dir, "defaults", default))

for insert_path in paths_list:
    sys.path.insert(0, abspath(insert_path))

import lib_paths
