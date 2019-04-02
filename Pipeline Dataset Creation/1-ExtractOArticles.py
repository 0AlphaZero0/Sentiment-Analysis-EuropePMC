#!/usr/bin/env python
#-*- coding: utf-8 -*-
# THOUVENIN Arthur athouvenin@outlook.fr
# 01/04/2019
########################
import codecs # Allows to load a file containing UTF-8 characters
import os # Allows to modify some things on the os
import random # Allows to use random variables
import requests # Allows to make http requests

"""
This script take place in a pipeline that extract citation of data in scientific papers, thanks to EuropePMC, RESTful API and Annotation API.

This script should extract two type of information from EuropePMC, first Full-text papers in XML format, anf then an XML that contain all Accession Number of this paper.
Papers are extract randomly thanks to "random" library, they are identify by a PMCID that looks like PMCXXXXXXX where each X can take a value from 0 to 9.
Then thanks to PMCID created a request is made to see if the extracted papers contain a data citation,
thanks to the "<name>" tag (in the XML file containing data citations) that indicate there is at least one data citation.
Then a second request is made to extract the fullText file in XML format and to be sure that it's an Open Access paper, it look at the tag "<?properties open_access?>".
Downloaded files are store in a directory named articlesOA and this script will make those requests until there is 400 files in the directory or 200 open access papers.
In the terminal it display some information like the advancement of the extraction, at the number of papers that were requested and the number of open access one and non open access ones.
"""



###################################################    Main     ###################################################

nbArticlesScan,nonOA=0,0

while len(os.listdir("./articlesOA"))<399:
    pmcid=str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))
    rAccessionNb=requests.get("https://www.ebi.ac.uk/europepmc/annotations_api/annotationsByArticleIds?articleIds=PMC%3A"+pmcid+"&type=Accession%20Numbers&format=XML")
    if "<name>" in rAccessionNb.text:
        rFullTxt=requests.get("https://www.ebi.ac.uk/europepmc/webservices/rest/PMC"+pmcid+"/fullTextXML")
        if "<?properties open_access?>" in rFullTxt.text:
            fileAccessionNb=codecs.open("./articlesOA/PMC"+pmcid+"-AccessionNb.xml","w",encoding="utf-8")
            fileAccessionNb.write(rAccessionNb.text)
            fileAccessionNb.close()
            fileFullTxt=codecs.open("./articlesOA/PMC"+pmcid+"-fulltxt.xml","w",encoding="utf-8")
            fileFullTxt.write(rFullTxt.text)
            fileFullTxt.close()
            nbArticlesScan+=1
        else:
            nonOA+=1
            nbArticlesScan+=1
    else:
        nonOA+=1
        nbArticlesScan+=1
    os.system('clear')
    advancement=(len(os.listdir("./articlesOA"))/400)*100
    print ("Extraction of articles..........",str(int(advancement))+"%")
print ("There is "+str(nonOA)+" articles that are non OA.")
print ("There is "+str(nbArticlesScan-nonOA)+" articles that are OA.")
print ("There is a total of "+str(nbArticlesScan)+" articles that were 'scanned'.")
print ("\nDONE\n")

