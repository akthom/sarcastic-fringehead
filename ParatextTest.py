#A. Thomer - modding from spring 2013 text mining code for use in paratext project

#python 2.7.2 or NLTK won't work

#path=("../sampleData")

def ack1():

        from bs4 import BeautifulSoup
        import re
        import os
        import nltk.data
        import csv


        outfile = open("preprocessedText.txt","a")#, encoding="latin-1") <-- commented out because code was originally written for python 3.2 but then discovered that it broke 2.7
        #also, outfile = original, untokenized text.  not really necessary but leaving in the code to show preprocessing step
#        walk=os.walk(path)
#        datalist=[]
#        tally={}

#        tokenizer=nltk.data.load('tokenizers/punkt/english.pickle') #modded from http://mailman.uib.no/public/corpora/2007-October/005426.html (thanks, internet!)
#        summary=[]
        data=[]
        w=csv.writer(outfile)
        w.writerow(["filename ","PMID ", "AcknowledgementsText"])


        for dirname, dirnames, filenames in os.walk('./sampleData'): #also modded from something on stack overflow that I now can't find
                
                
                for filename in filenames:
                        if filename.endswith('.nxml'):
                                infile=os.path.join(dirname, filename)

                                
                                soup = BeautifulSoup(open(infile), "lxml") #not sure if xml parsing is actually necessary/helpful
                                for i in soup.findAll():
                                        i.name=i.name.replace("-","_") #replaces hyphens with underscores, which makes some of the processing easier
                                pmidline= soup.findAll("article_id", attrs={"pub-id-type": "pmid"})
                                #if pmidline == True:
#                                        pmid=pmidline[0].contents
#                                else:
#                                        pmid=["None"]
                                pmid=pmidline[0].contents
                                ack=soup.ack
                                print(infile, str(pmid[0]), ack)
                                w.writerow([filename, pmid[0], ack])

                       
#                        if a.endswith('.txt'):
#                                abstractNum=abstractNum+1
#                                toWrite=str(a).strip(".txt")#+"|"+abstractNum+"|"
#                                datalist.append(a)
#                                print(a)
#                                infile = os.path.join(dirpath,a)
#                                pageText = open(infile,'r')#,encoding="latin-1")
#                                currentFile = pageText.read()
  		
#                                for i in iterator1:
#                                        org=i.group()
#                                        print(i.group())
                                        
#                                        datalist.append(i.group())
#                                        if str(i.group()) in tally:
#                                                tally[str(i.group())]=tally[str(i.group())]+1
#                                        else:
#                                                tally[str(i.group())]=1
#                                for i in iterator2:
#                                        number=1
#                                        print(i.group())
#                                        abstract=(i.group())
#                                        abstract=re.sub('\s+',' ', abstract)
#                                        sentences=tokenizer.tokenize(abstract)
#                                        for sentence in sentences:
#                                                outfile2.write(toWrite+"|"+str(number)+"|"+sentence+"\n")
#                                                number=number+1
                                        
#                                        datalist.append(abstract)
#                                if str(number) in summary:
#                                        summary[str(number)]=summary[str(number)]+1
#                                else:
#                                        summary[str(number)]=1
                                
#                        thingToWrite=str(datalist)
#                        outfile.write(thingToWrite+'\n')
#                        datalist=[]
#                        print (tally)
#                        print("SENTENCE TOTALS=")
#                        print(summary)

#                w.writerow([filename, pmid[0], ack])
        outfile.close()
#        for key, val in summary.items():
#                w.writerow([str(key)+"|"+str(val)])
#              datalist=[]
#        w.writerow(['ORG TOTALS'])
#        for key,val in tally.items():
#                w.writerow([str(key)+"|"+str(val)])
#        outfile.close()
#        outfile2.close()
#        summaryreport.close()

