#A. Thomer - modding from spring 2013 text mining code for use in paratext project

#python 2.7.2 or NLTK won't work

path=("../Text Mining/test")

def ack1(path):

        from bs4 import BeautifulSoup
#        import re
        import os
        import nltk.data
        import csv

        outfile = open("preprocessedText.txt","a")#, encoding="latin-1") <-- commented out because code was originally written for python 3.2 but then discovered that it broke 2.7
        #also, outfile = original, untokenized text.  not really necessary but leaving in the code to show preprocessing step
        #outfile2=open("finalAbstracts.txt", "a")#, encoding="latin-1")
        #summaryreport=open("summaryReport.txt","a")
        walk=os.walk(path)
#        p=re.compile('(?<=(NSF Org     :)).+?(?=\n)')
#        n=re.compile('(?<=(Abstract    :)).*', re.DOTALL)
        datalist=[]
#        tally={}
        abstractNum=0
        tokenizer=nltk.data.load('tokenizers/punkt/english.pickle') #modded from http://mailman.uib.no/public/corpora/2007-October/005426.html (thanks, internet!)
        summary={}

        for dirpath, dirnames, listing in walk: #also modded from something on stack overflow that I now can't find
                

                for a in listing:
                        soup = BeautifulSoup(open(a))
                        ID = 


                        
                        if a.endswith('.txt'):
                                abstractNum=abstractNum+1
                                toWrite=str(a).strip(".txt")#+"|"+abstractNum+"|"
                                datalist.append(a)
#                                print(a)
                                infile = os.path.join(dirpath,a)
                                pageText = open(infile,'r')#,encoding="latin-1")
                                currentFile = pageText.read()
  		
                                iterator1=p.finditer(str(currentFile)) #not sure if this is the best place for this bit, but so it goes.  I know this isn't the best way to do this but I'm reusing code from another project and can refactor later if necessary
                                iterator2=n.finditer(str(currentFile))
                                for i in iterator1:
#                                        org=i.group()
#                                        print(i.group())
                                        
                                        datalist.append(i.group())
                                        if str(i.group()) in tally:
                                                tally[str(i.group())]=tally[str(i.group())]+1
                                        else:
                                                tally[str(i.group())]=1
                                for i in iterator2:
                                        number=1
#                                        print(i.group())
                                        abstract=(i.group())
                                        abstract=re.sub('\s+',' ', abstract)
                                        sentences=tokenizer.tokenize(abstract)
                                        for sentence in sentences:
                                                outfile2.write(toWrite+"|"+str(number)+"|"+sentence+"\n")
                                                number=number+1
                                        
                                        datalist.append(abstract)
                                if str(number) in summary:
                                        summary[str(number)]=summary[str(number)]+1
                                else:
                                        summary[str(number)]=1
                                
                        thingToWrite=str(datalist)
                        outfile.write(thingToWrite+'\n')
                        datalist=[]
                        print (tally)
#                        print("SENTENCE TOTALS=")
                        print(summary)

        w=csv.writer(summaryreport)
        w.writerow(["SENTENCE TOTALS"])
        for key, val in summary.items():
                w.writerow([str(key)+"|"+str(val)])
#              datalist=[]
        w.writerow(['ORG TOTALS'])
        for key,val in tally.items():
                w.writerow([str(key)+"|"+str(val)])
        outfile.close()
        outfile2.close()
        summaryreport.close()
