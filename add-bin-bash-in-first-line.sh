#!/bin/bash

if [ -z "$1" ]; then
	newfile=~/Desktop/scripts/newscript_`date +%m%d-%S`
else
	newfile=~/Desktop/scripts/$1
fi

if ! grep "^#!" $newfile &>/dev/null; then
	cat >> $newfile << EOF
#!/bin/bash
# Author:
# Date: `date +"%F %T"`
# Description:
EOF
fi
vim +5 $newfile

