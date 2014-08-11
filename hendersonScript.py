#Author: Andrea Thomer
#27 Dec 2011
#goal the first: scan field note doc and automatically create wiki links. - done i think
#early issues: there are non-ascii characters from word transferred to the text file - make sure to export an ASCII or utf-8 version of the doc or python will give you no end of hell
#goal the second: find and somehow tag dates


import re

def amendTaxon (taxonNames, inFile, outFile):
         
        taxonDict = open(taxonNames, "r") #opens list of taxa already extracted from text via UBio
        fieldNotes = open(inFile, "r") #opens the field note file
        amendedNotes=open(outFile, "a") #creates a file to write amended notes to
        
        taxa = taxonDict.readlines() #reads the list of taxa
        notes = fieldNotes.readlines() #reads the field notes
        a = 0 #sets list index to zero
        for i in notes:
                while a < len(notes)-1: #my probably sloppy way to tell this when to stop incremmenting
                        a=a+1
                        newText=notes[a] #variable for line to be written to new file
                
                        for i in taxa:
                                taxalist=i.split("\t") #splits list of taxa by dictionary
                                lookup=taxalist[0] #not sure if this variable is necessary
                                
                                if lookup in notes[a]: #if the animal is there, then make it a wiki link
                                        replacementText="{{taxon|"+taxalist[1]+"|"+taxalist[0]+"}}"
                                        newText=notes[a].replace(lookup,replacementText)
                                        amended=1
#                                        print("i found ", lookup, "in paragraph", a)  #included for early testing


                        amendedNotes.write(newText) #writes amended or unamended text to file
                        print("writing paragraph",a) 





        taxonDict.close()
        fieldNotes.close()
        amendedNotes.close()

        
# test text for easy copy paste: amendTaxon("taxaallnotes.txt","henderson-Notebook10-reformatted.txt","Henderson-10-tagged.txt")


        
