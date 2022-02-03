set HOME=%~dsp0home/portable
set "MSYSTEM=MINGW64"
start %~dsp0usr/bin/mintty /bin/sh -l -c "cd ~/chipwhisperer/wheels; python -m pip install *; cd ..; python setup.py develop"
