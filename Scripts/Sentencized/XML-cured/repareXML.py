#!/usr/bin/env python
#-*- coding: utf-8 -*-
# THOUVENIN Arthur
# 01/04/2019
########################
import codecs # Allows to load a file containing UTF-8 characters
import os # Allows to modify some things on the os
import re # Allows to make regex requests

"""
This script take place in a pipeline that extract citation of data in scientific papers, thanks to EuropePMC, RESTful API and Annotation API.

This script will look at the mistakes made by the sentence splitter, indeed sometimes, the sentence splitter just split sentences in the wrong places so it need to be fix.
So here thanks to regular expression it will fix some mistakes made by the splitter in the xml files containing the sentences.

"""

###################################################    Main     ###################################################

for file in os.listdir("./"):
    if file.endswith(".xml"):
        oldFile=codecs.open(file,"r",encoding="utf-8")
        tmpFile=oldFile.read()
        oldFile.close()
        matchesEtAl=re.findall(r'\set\sal\.\s(</plain></SENT>\n<[^>]+pm=\"\.\"><plain>)',tmpFile)
        matchesSurname=re.findall(r'\s[^h\d%;]\.\s(</plain></SENT>\n<[^>]+pm=\"\.\"><plain>)',tmpFile)
        matchesCa=re.findall(r'\sca\.\s(</plain></SENT>\n<[^>]+pm=\"\.\"><plain>)',tmpFile)
        matchesApprox=re.findall(r'\sapprox\.\s(</plain></SENT>\n<[^>]+pm=\"\.\"><plain>)',tmpFile)
        matchesRef=re.findall(r'\(ref\.\s(</plain></SENT>\n<[^>]+pm=\"\.\"><plain>)',tmpFile)
        for match in matchesEtAl:
            #print ("match1")
            tmpFile=tmpFile.replace(match,'')
        for match in matchesSurname:
            #print ("match2")
            tmpFile=tmpFile.replace(match,'')
        for match in matchesCa:
            #print ("match3")
            tmpFile=tmpFile.replace(match,'')
        for match in matchesApprox:
            #print ("match4")
            tmpFile=tmpFile.replace(match,'')
        for match in matchesRef:
            #print ("match5")
            tmpFile=tmpFile.replace(match,'')
        newFile=codecs.open(file,"w",encoding="utf-8")
        newFile.write(tmpFile)
        newFile.close()
    else:
        print (file)