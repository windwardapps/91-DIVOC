#! /usr/bin/env bash

echo "[$(date "+%Y-%m-%dT%H:%M:%S")] start"

pushd ../COVID-19
git pull
popd
cd pages/covid-visualization
python3 processData.py
python3 processUrls.py
bundle exec jekyll build

echo "[$(date "+%Y-%m-%dT%H:%M:%S")] end"