set HOME=%~dsp0home/portable
set "MSYSTEM=MINGW64"
start %~dsp0usr/bin/mintty /bin/sh -l -c "cd ~/chipwhisperer; python -m jupyter notebook"