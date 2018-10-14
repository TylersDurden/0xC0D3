#!/bin/bash
echo "Geo Locating " $1
GET https://ipinfo.io/$1 >> result.txt
#EOF
