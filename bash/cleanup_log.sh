#!/bin/bash

echo "Cleaning log files"

for file in *.log
do
  echo "Deleting $file"
  rm "$file"
done

echo "Cleanup Complete"
