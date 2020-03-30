#! /usr/bin/env bash

pushd ../COVID-19
git pull
popd
cd pages/covid-visualization
python3 processData.py
python3 processUrls.py