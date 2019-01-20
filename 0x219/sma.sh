#!/bin/sh
echo $(python p4x.py overfloweth $1) | cut -b 33-
#EOF 
