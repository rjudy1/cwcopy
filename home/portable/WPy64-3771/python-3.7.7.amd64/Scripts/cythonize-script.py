#!C:\Users\rjudy\CHIPWH~1\cw\home\portable\WPy64-3771\python-3.7.7.amd64\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Cython','console_scripts','cythonize'
__requires__ = 'Cython'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Cython', 'console_scripts', 'cythonize')()
    )
