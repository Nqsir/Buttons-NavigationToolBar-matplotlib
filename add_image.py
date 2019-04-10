import sys
import os
from shutil import copy2


if __name__ == '__main__':
    mpl_path = os.path.join(sys.path[-1], os.path.join('matplotlib', os.path.join('mpl-data', 'images')))
    copy2('name.png', mpl_path)
    copy2('name_large.png', mpl_path)
