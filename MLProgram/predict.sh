#!/bin/bash
#echo $PATH
preprocess/resample_wavs_to_16k.sh birdclef_data/test/demo
cd predict
python predict.py
cd ..

