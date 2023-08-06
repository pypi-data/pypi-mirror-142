#We have various cutup packages here
#First one does it by splitting sentences in 50%
#This requires NLTK sentence tokeniser
#The second one does it by line, and needs to import textwrap
#The third and fourth ones do simple cut up and folds

#USES SENTENCES SPLIT IN HALF

        def cutsent(texts):
    Asec = '' #sets up the list for A
    Bsec = '' #sets up list for B
    firstpara= texts
    cutpara = int(0.5 * len(firstpara)) #cut is int 50% of length of text 5 as a whole
    cutbitspara = firstpara[:cutpara], firstpara[cutpara:]  # this cuts either side creating trianing data and test data
    Asec+=(firstpara[:cutpara]) #this puts it in a list but only as 1 thing under 0
    Bsec+=(firstpara[cutpara:]) #this creates it as a block of text in Bsec under 0
    #return Asec + Bsec
    #It creates a big block because we didnt do this for each sentence...we just dumped one load of text in there
    #TokenA = str(Asec)
    #TokenAfinal = sent_tokenize(TokenA) #now we can tokenize Token A as sentences
    Atok = str(Asec) #convert Atoken into a string
    Atoken = sent_tokenize(Atok) #tokenise Atok
    #print (Atoken[1]) #brackets are alread in here
    Btok = str(Bsec)
    Btoken = sent_tokenize(Btok)
    A1 =[]
    A2 =[]
    B1 =[]
    B2= []
    for sentence in Atoken: #for each sentence in sentnewparatoken
        cutpercent = int(0.5 * len(sentence)) #cut is 50% in number of words? (we do it over two lines of code)
        cutbitspercent = sentence[cutpercent:], sentence[:cutpercent] #this creates the cut
        A1.append(sentence[cutpercent:]) #puts these sentences into A1
        A2.append(sentence[:cutpercent]) #puts these sentence into A2
        finalsplice = sentence[cutpercent:]+sentence[:cutpercent] #this mixes the end of the sentence with the beginning
        #print(finalsplice, end = '') #prints each new sentence.
    # NOW REPEAT FOR BTOKEN
    for sentence in Btoken: #for each sentence in sentnewparatoken
        cutpercent = int(0.5 * len(sentence)) #cut is 50% in number of words? (we do it over two lines of code)
        Bcutbitspercent = sentence[cutpercent:], sentence[:cutpercent] #this creates the cut
        B1.append(sentence[cutpercent:]) #puts these sentences into A1
        B2.append(sentence[:cutpercent]) #puts these sentence into A2
        finalsplice = sentence[cutpercent:]+sentence[:cutpercent] #this mixes the end of the sentence with the beginning
        #print(finalsplice, end = '') #prints each new sentence.
    for i,j,k,l, in zip(B2,A2,B1,A1):
        print (i,j,k,l, end ='') # adding end = '' prints it out in one contiuous thing

#THIS ONE DOES IT BY LINE AND NEEDS TEXTWRAP

def linecutup(texts):
    linecut = textwrap.wrap(texts, width =80) #make our text  line by line we've gone for 80 chaarcter length
    Firsthalf = (linecut[:len(linecut)//2]) #this tajkes the first half of the list
    Secondhalf = linecut[len(linecut)//2:] #this takes the second half
    CC = []
    CD = []
    for i in Firsthalf: #for every item in linecut
        cutlines1 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines2 = i[cutlines1:], i[:cutlines1] #this flips the sentences around on each other
        #print(cutlines2)
        CC.append(i[:cutlines1]) #this puts it in a list but only as 1 thing under 0
        CD.append(i[cutlines1:])
    DD =[]
    DE = []
    for i in Secondhalf: #for every item in linecut
        cutlines2 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines3 = i[cutlines2:], i[:cutlines2] #this flips the sentences around on each other
        #print(cutlines3)
        DD.append(i[:cutlines2]) #this puts it in a list but only as 1 thing under 0
        DE.append(i[cutlines2:])
    for i,j,k,l, in zip(DE,CD,DD,CC):
        print (i,j,k,l, end ='')

#This next one orders it slightly differently

def linecutup2(texts):
    linecut = textwrap.wrap(texts, width =80) #make our text  line by line we've gone for 80 chaarcter length
    Firsthalf = (linecut[:len(linecut)//2]) #this tajkes the first half of the list
    Secondhalf = linecut[len(linecut)//2:] #this takes the second half
    CC = []
    CD = []
    for i in Firsthalf: #for every item in linecut
        cutlines1 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines2 = i[cutlines1:], i[:cutlines1] #this flips the sentences around on each other
        #print(cutlines2)
        CC.append(i[:cutlines1]) #this puts it in a list but only as 1 thing under 0
        CD.append(i[cutlines1:])
    DD =[]
    DE = []
    for i in Secondhalf: #for every item in linecut
        cutlines2 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines3 = i[cutlines2:], i[:cutlines2] #this flips the sentences around on each other
        #print(cutlines3)
        DD.append(i[:cutlines2]) #this puts it in a list but only as 1 thing under 0
        DE.append(i[cutlines2:])
    for i,j,k,l, in zip(CC,DE,DD,CD):
        print (i,j,k,l, end ='')

#NOW LETS CREATE THE FOLDOVER OPTIONS USING TWO TEXTS

def fold1 (text1, text2):
    linecut1 = textwrap.wrap(text1, width =80) #make our text 1  line by line we've gone for 80 chaarcter length
    linecut2 = textwrap.wrap(text2, width =80) #make our text 2  line by line we've gone for 80 chaarcter length
    EE = [] #empty list to put one half in
    EF = [] # empty list to put the other in
    for i in linecut1: #for every item in linecut
        cutlines1 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines2 = i[cutlines1:], i[:cutlines1] #this flips the sentences around on each other
        #print(cutlines2)
        EE.append(i[:cutlines1]) #this puts it in a list but only as 1 thing under 0
        EF.append(i[cutlines1:])
    FF =[]
    FG = []
    for i in linecut2: #for every item in linecut2
        cutlines2 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines3 = i[cutlines2:], i[:cutlines2] #this flips the sentences around on each other
        #print(cutlines3)
        FF.append(i[:cutlines2]) #this puts it in a list but only as 1 thing under 0
        FG.append(i[cutlines2:])
    for i,j, in zip(FF,EF):
        print (i,j, end ='')

#TWO text fold style 2

def fold2 (text1, text2):
    linecut1 = textwrap.wrap(text1, width =80) #make our text 1  line by line we've gone for 80 chaarcter length
    linecut2 = textwrap.wrap(text2, width =80) #make our text 2  line by line we've gone for 80 chaarcter length
    EE = [] #empty list to put one half in
    EF = [] # empty list to put the other in
    for i in linecut1: #for every item in linecut
        cutlines1 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines2 = i[cutlines1:], i[:cutlines1] #this flips the sentences around on each other
        #print(cutlines2)
        EE.append(i[:cutlines1]) #this puts it in a list but only as 1 thing under 0
        EF.append(i[cutlines1:])
    FF =[]
    FG = []
    for i in linecut2: #for every item in linecut2
        cutlines2 = int(0.5 * len(i)) #cut into it 50%
        #print (cutlines1)
        cutlines3 = i[cutlines2:], i[:cutlines2] #this flips the sentences around on each other
        #print(cutlines3)
        FF.append(i[:cutlines2]) #this puts it in a list but only as 1 thing under 0
        FG.append(i[cutlines2:])
    for i,j, in zip(EE,FG):
        print (i,j, end ='')