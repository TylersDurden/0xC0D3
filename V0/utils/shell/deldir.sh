#!/bin/bash
echo 'DELETING ' $1
ls $1 | while read fname; do rm $1/$fname; done; rmdir $1; 
echo 'Finished.'
#EOF
