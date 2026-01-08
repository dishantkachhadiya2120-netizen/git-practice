#!/bin/bash

echo "Enter file name : "
read filename

if [ -f "$filename" ]
then
  echo "File Exists"
else 
  echo "File does not exist"
fi

