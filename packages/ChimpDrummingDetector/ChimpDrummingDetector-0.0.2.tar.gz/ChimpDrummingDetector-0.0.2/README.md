# Chimpanzee Drumming Detector

This is a python program for detecting chimpanzee drumming in long-term rainforest recordings.

The associated publication can be read at: 
- https://arxiv.org/abs/2105.12502
- https://doi.org/10.1016/j.ecoinf.2021.101423

This program only contains the test pipeline, not the training pipeline.

## Installation

Either install the latest stable release from PyPI

    pip install ChimpDrummingDetector

Alternatively, you can install this package through to code on this repository.
Simply download this repository as a zip, and then do:

    cd path/to/downloaded/zip
    unzip ChimpDrummingDetector.zip
    cd ChimpDrummingDetector
    pip install ChimpDrummingDetector

## Usage

In your python code, do

    import chimp_detector

    path_to_wave_to_analyze = path/to/wave.wav 
    detection_result = chimp_detector.detect_drumming(path_to_wave_to_analyze)

- Input: A wave file. Might be mono or stereo
- Output: A pandas dataframe with following columns
  - timepoints_in_seconds [float]: The analyzed timepoints
  - drumming_probability [float]: Probability of chimpanzee drumming in range [0,1] for the respective timepoint
  - drumming_binarized [boolean]: Binarization of probability with threshold 0.5, where TRUE means "there is drumming in this frame".

## Dependencies

This Packages requires:

- Python version 3.8
- librosa==0.8.0
- tensorflow==2.3.1
- pandas==1.1.2
- numpy==1.18.5