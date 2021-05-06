#!/bin/bash
cd ..
pwd
cd birdclef_data/test/demo
FILES=*
for f in $FILES
do
  echo "Processing ./$f file to ../wav_16khz/$f"
  # take action on each file. $f store current file name
  sox ./$f -r 16000 ../wav_16khz/$f
done

