#! /usr/bin/env bash

cd ../COVID-19
git pull
cd ../91-DIVOC/pages/covid-visualization
python3 processData.py
python3 processUrls.py