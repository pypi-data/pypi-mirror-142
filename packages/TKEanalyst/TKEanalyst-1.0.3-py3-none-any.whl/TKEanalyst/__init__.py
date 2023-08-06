import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from profile_analyst import *

try:
    import logging
    logging.getLogger()
except NameError:
    pass
