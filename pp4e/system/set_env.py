#!/usr/bin/env python
import os
from icecream import ic


ic('Hello', os.environ['USER'])

os.environ['USER'] = 'Tom'
os.system('./echo_env.py')

os.environ['USER'] = 'Peter'
print(os.popen('./echo_env.py').read())
