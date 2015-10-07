#!/bin/bash
find . -name NOTES
rm ./data/jamesm/NOTES | rm ./data/Frank_Richard/NOTES 
mkdir cleaned_data
mv ./data/* ./cleaned_data/
cd cleaned_data/
for filename in */*; do mv $filename $filename.txt; done
