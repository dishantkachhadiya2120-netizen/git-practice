#!/bin/bash

for file in hello.sh  info .sh check_file.sh random.txt
do 
   if [ -f "$file" ]
   then
    echo "$file exists"
   else
    echo "$file does not exist"
   fi
done  
