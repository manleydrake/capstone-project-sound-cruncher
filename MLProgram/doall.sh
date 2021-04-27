#!/bin/bash
preprocess/resample_wavs_to_16k.sh birdclef_data/TrainingSet/wav
preprocess/resample_wavs_to_16k.sh birdclef_data/test/wav2015
cd preprocess
python loadData.py
cd ..
cd train
mkdir modelWeights
python trainModel.py
cd ..
