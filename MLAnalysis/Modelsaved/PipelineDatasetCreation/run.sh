#!/bin/sh
directory="./articlesOA"
numberofpaper=10
python t1-ExtractOArticles.py $directory $numberofpaper
python t2-RemoveTables.py $directory
bash t3-Sentencizer.sh $directory
python t4-RepareSplitedXML.py $directory
python t5-ExtractCitations.py $directory
rm ./articlesOA/*