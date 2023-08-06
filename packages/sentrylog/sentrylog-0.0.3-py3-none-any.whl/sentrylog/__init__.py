# -*- coding:utf-8 -*-
from pathlib import Path
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

for _path in os.listdir(os.path.dirname(__file__)):
    path = os.path.join(os.path.dirname(__file__), _path)
    my_path = Path(path)
    if my_path.is_dir():
        sys.path.insert(0, my_path)
        
from sentrylog.logger import *
from sentrylog.config import *

# try:
#     import colorlog
# except ImportError as e:
#     raise Exception("Please install colorlog use : pip install colorlog")

try:
    import sentry_sdk
except ImportError as e:
    raise Exception("Please install sentry_sdk use : pip install --upgrade sentry-sdk")
