#A. Thomer - modding from spring 2013 text mining code for use in paratext project

#python 2.7.2 or NLTK won't work


def ack1():

        from bs4 import BeautifulSoup
        import re
        import os
        import nltk.data
        import csv


        outfile = open("preprocessedTextASIST.csv","a")#, encoding="latin-1") <-- commented out because code was originally written for python 3.2 but then discovered that it broke 2.7

        w=csv.writer(outfile)
        w.writerow(["filename ","PMID ", "Abstract ", "AcknowledgementsText"])


        for dirname, dirnames, filenames in os.walk('./sampleData'): #also modded from something on stack overflow that I now can't find
                
                
                for filename in filenames:
                        if filename.endswith('.nxml'):
                                infile=os.path.join(dirname, filename)

                                
                                soup = BeautifulSoup(open(infile), "lxml") #not sure if xml parsing is actually necessary/helpful
                                for i in soup.findAll():
                                        i.name=i.name.replace("-","_") #replaces hyphens with underscores, which makes some of the processing easier
                                pmidline= soup.findAll("article_id", attrs={"pub-id-type": "pmid"})

                        
                                if not pmidline:   # "Using the implicit booleanness of the empty list is quite pythonic." http://stackoverflow.com/questions/53513/python-what-is-the-best-way-to-check-if-a-list-is-empty
                                        pmid=["None"]
                                else:
                                        pmid=pmidline[0].contents


                                ack=soup.ack
                                abstract=soup.abstract
                                
                                print(infile, str(pmid[0]))
                                w.writerow([filename, pmid[0], abstract, ack])

        outfile.close()

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

#        for key, val in summary.items():
#                w.writerow([str(key)+"|"+str(val)])
#              datalist=[]
#        w.writerow(['ORG TOTALS'])
#        for key,val in tally.items():
#                w.writerow([str(key)+"|"+str(val)])
#        outfile.close()
#        outfile2.close()
#        summaryreport.close()

