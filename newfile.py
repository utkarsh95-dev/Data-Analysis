import pandas as pd
import readability
from bs4 import BeautifulSoup
import requests
import os
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer 
import re
import string
#------------ CREATING STOPWORDS LIST------------#

stop_words =[]

data = [line.strip() for line in open("StopWords_Auditor.txt",'r')]
for w in data:
	stop_words.append(w)

data1 = [line.strip() for line in open("StopWords_Generic.txt", 'r')]
for w in data1:
	stop_words.append(w)

data2 = [line.strip() for line in open("StopWords_DatesandNumbers.txt",'r')]
for w in data2:
	stop_words.append(w)

data3 = [line.strip() for line in open("StopWords_GenericLong.txt",'r')]
for w in data3:
	stop_words.append(w)

data4 = [line.strip() for line in open("StopWords_Geographic.txt",'r')]
for w in data4:
	stop_words.append(w)

data5= [line.strip() for line in open("StopWords_Names.txt",'r')]
for w in data5:
	stop_words.append(w)

data6 = [line.strip() for line in open("StopWords_Currencies.txt",'r',encoding='latin-1')]
for w in data6:
	stop_words.append(w)
#print(stop_words)

#---------------------------------------------------------------------#

#-------------------POSTIVE LIST-----------------------------#

positive_list = [line.strip() for line in open("positive-words.txt",'r')]

#print(positive_list[0])
#---------------------------------------------------------------------#

#-------------------NEGATIVE LIST-----------------------------#

negative_list = [line.strip() for line in open("negative-words.txt",'r',encoding='latin-1')]

#print(negative_list)
#---------------------------------------------------------------------#


#Extracting data for URLID -37
'''-----------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url1 = 'https://insights.blackcoffer.com/ai-in-healthcare-to-improve-patient-outcomes/'

page1 = requests.get(url1)

html1= BeautifulSoup(page1.content,'html.parser')

found1 = html1.findAll(attrs ={'class':'tdb-bred-no-url-last'})

title1 = found1[1].text
#print(title1)

content1 = html1.findAll(attrs={'class':'tdb-block-inner td-fix-index'})
main = content1[14].text
sentence = sent_tokenize(content1[14].text)

wordsofall = word_tokenize(main)
#stop = set(stopwords.words('english'))
#stop_words.extend(stop)
content = title1 + main
print(len(wordsofall))
filtered_list = [ ]
filtered_list = [w for w in wordsofall if w not in stop_words]

content_tok = word_tokenize(content)
content_sent = sent_tokenize(content)
print(len(content_tok))
#print(content_sent)
#print(wordsofall)

positive_score=0
negative_score =0


#print("postive ", positive_list,"\n")

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue
	
for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue
pro = ['I','we','my','ours','us']

print(positive_score)
print(negative_score)

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

#print(polarity_score)

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)
#print(subjectivity_score)
res = readability.getmeasures(content,lang='en')
#print(res)
pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
#print(x)
sent = content.split('.')
wordd = content.split(' ')
print(sent)
print(wordd)
print(len(sent))
print(len(wordd))

words = content.split()
avg = sum(len(word) for word in words)//len(words)
print(avg)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -38

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url2 = 'https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/'

newfile= open('old.txt','w')
newname = "URLID-38.txt"
oldname = "old.txt"


page2 = requests.get(url2)

html2 = BeautifulSoup(page2.content,'html.parser')

#print(html2)

found2= html2.findAll(attrs={'class':'entry-title'})
#print(title2)

title2= found2[16].text
#print(title2)
#newfile.write(title2+"\n")
content2 = html2.findAll(attrs={'class':'td-post-content tagdiv-type'})

main = content2[0].text
#newfile.write(content2[0].text)

#os.rename(oldname,newname)

#----------CREATING A FILTERED LISTS-----------#

content = title2 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''



'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -39

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url3= 'https://insights.blackcoffer.com/what-jobs-will-robots-take-from-humans-in-the-future/'


newfile1= open('old1.txt','w')
newname1 = "URLID-39.txt"
oldname1= "old1.txt"
page3= requests.get(url3)

html3 = BeautifulSoup(page3.content,'html.parser')


found3= html3.findAll(attrs={'class':'entry-title'})
#print(title3)

title3= found3[16].text
#newfile1.write(title3+"\n")
#print(title3)


content3 = html3.findAll(attrs={'class':'td-post-content tagdiv-type'})
main = content3[0].text
#newfile1.write(content3[0].text)
#print(content3[0].text)
#os.rename(oldname1,newname1)


#----------CREATING A FILTERED LISTS-----------#

content = title3 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -40

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url4 = 'https://insights.blackcoffer.com/will-machine-replace-the-human-in-the-future-of-work/'


newfile2= open('old2.txt','w')
newname2 = "URLID-40.txt"
oldname2= "old2.txt"
page4 = requests.get(url4)

html4 = BeautifulSoup(page4.content,'html.parser')


found4= html4.findAll(attrs={'class':'entry-title'})
#print(title3)

title4= found4[16].text
#newfile2.write(title4+"\n")
#print(title4)


content4= html4.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile2.write(content4[0].text)
main = content4[0].text
#print(content4[0].text)
#os.rename(oldname2,newname2) 

#----------CREATING A FILTERED LISTS-----------#

content = title4 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -41

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url5 = 'https://insights.blackcoffer.com/will-ai-replace-us-or-work-with-us/'



newfile3= open('old3.txt','w')
newname3 = "URLID-41.txt"
oldname3= "old3.txt"
page5 = requests.get(url5)

html5 = BeautifulSoup(page5.content,'html.parser')


found5= html5.findAll(attrs={'class':'entry-title'})
#print(title3)

title5= found5[16].text
#newfile3.write(title5+"\n")
#print(title5)


content5= html5.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile3.write(content5[0].text)
main = content5[0].text
#print(content5[0].text)
#os.rename(oldname3,newname3) 

#----------CREATING A FILTERED LISTS-----------#

content = title5 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -42

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url6 = 'https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/'




newfile4= open('old4.txt','w')
newname4 = "URLID-42.txt"
oldname4= "old4.txt"
page6 = requests.get(url6)

html6 = BeautifulSoup(page6.content,'html.parser')


found6= html6.findAll(attrs={'class':'entry-title'})
#print(title3)

title6= found6[16].text
#newfile4.write(title6+"\n")
#:print(title6)


content6= html6.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile4.write(content6[0].text)
#print(content6[0].text)
main = content6[0].text
#os.rename(oldname4,newname4)


#----------CREATING A FILTERED LISTS-----------#

content = title6 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -43

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url7 = 'https://insights.blackcoffer.com/in-future-or-in-upcoming-years-humans-and-machines-are-going-to-work-together-in-every-field-of-work/'





newfile5= open('old5.txt','w')
newname5= "URLID-43.txt"
oldname5= "old5.txt"
page7 = requests.get(url7)

html7 = BeautifulSoup(page7.content,'html.parser')


found7= html7.findAll(attrs={'class':'entry-title'})
#print(title3)

title7= found7[16].text
#newfile5.write(title7+"\n")
#print(title7)


content7= html7.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile5.write(content7[0].text)
main = content7[0].text
#print(content7[0].text)
#os.rename(oldname5,newname5)

#----------CREATING A FILTERED LISTS-----------#

content = title7 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -45

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url8 = 'https://insights.blackcoffer.com/how-machine-learning-will-affect-your-business/'






newfile6= open('old6.txt','w')
newname6= "URLID-45.txt"
oldname6= "old6.txt"
page8 = requests.get(url8)

html8 = BeautifulSoup(page8.content,'html.parser')


found8= html8.findAll(attrs={'class':'entry-title'})
#print(title3)

title8= found8[16].text
#newfile6.write(title8+"\n")
#print(title8)


content8= html8.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile6.write(content8[0].text)
#print(content8[0].text)
#os.rename(oldname6,newname6)
main = content8[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title8 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -46

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url9 = 'https://insights.blackcoffer.com/deep-learning-impact-on-areas-of-e-learning/'






newfile7= open('old7.txt','w')
newname7= "URLID-46.txt"
oldname7= "old7.txt"
page9 = requests.get(url9)

html9 = BeautifulSoup(page9.content,'html.parser')


found9= html9.findAll(attrs={'class':'entry-title'})
#print(title3)

title9= found9[16].text
#newfile7.write(title9+"\n")
#print(title9)


content9= html9.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile7.write(content9[0].text)
#print(content9[0].text)
#os.rename(oldname7,newname7) 
main = content9[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title9 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -47

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url10 = 'https://insights.blackcoffer.com/how-to-protect-future-data-and-its-privacy-blackcoffer/'






newfile8= open('old8.txt','w')
newname8= "URLID-47.txt"
oldname8= "old8.txt"
page10 = requests.get(url10)

html10 = BeautifulSoup(page10.content,'html.parser')


found10= html10.findAll(attrs={'class':'entry-title'})
#print(title3)

title10= found10[16].text
#newfile8.write(title10+"\n")
#print(title10)


content10= html10.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile8.write(content10[0].text)
#print(content10[0].text)
#os.rename(oldname8,newname8) 
main = content10[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title10 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -48

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url11 = 'https://insights.blackcoffer.com/how-machines-ai-automations-and-robo-human-are-effective-in-finance-and-banking/'






newfile9= open('old9.txt','w')
newname9= "URLID-48.txt"
oldname9= "old9.txt"
page11 = requests.get(url11)

html11 = BeautifulSoup(page11.content,'html.parser')


found11= html11.findAll(attrs={'class':'entry-title'})
#print(title3)

title11= found11[16].text
#newfile9.write(title11+"\n")
#print(title11)


content11= html11.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile9.write(content11[0].text)
main  = content11[0].text
#os.rename(oldname9,newname9) 

#----------CREATING A FILTERED LISTS-----------#

content = title11 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -49

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url12 = 'https://insights.blackcoffer.com/ai-human-robotics-machine-future-planet-blackcoffer-thinking-jobs-workplace/'






newfile10= open('old10.txt','w')
newname10= "URLID-49.txt"
oldname10= "old10.txt"
page12 = requests.get(url12)

html12 = BeautifulSoup(page12.content,'html.parser')


found12= html12.findAll(attrs={'class':'entry-title'})
#print(title3)

title12= found12[16].text
#newfile10.write(title12+"\n")
#print(title12)


content12= html12.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile10.write(content12[0].text)
#print(content12[0].text)
#os.rename(oldname10,newname10)
main = content12[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title12 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -50

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url13 = 'https://insights.blackcoffer.com/how-ai-will-change-the-world-blackcoffer/'






newfile11= open('old11.txt','w')
newname11= "URLID-50.txt"
oldname11= "old11.txt"
page13 = requests.get(url13)

html13 = BeautifulSoup(page13.content,'html.parser')


found13= html13.findAll(attrs={'class':'entry-title'})
#print(title3)

title13= found13[16].text
#newfile11.write(title13+"\n")
#print(title13)


content13= html13.findAll(attrs={'class':'td-post-content tagdiv-type'})
#newfile11.write(content13[0].text)
#print(content13[0].text)
os.rename(oldname11,newname11) 
main= content13[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title13 + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -51

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url14 = 'https://insights.blackcoffer.com/future-of-work-how-ai-has-entered-the-workplace/'






newfile12= open('old12.txt','w')
newname12= "URLID-51.txt"
oldname12= "old12.txt"
page14 = requests.get(url14)

html14 = BeautifulSoup(page14.content,'html.parser')



title14= html14.findAll(attrs={'class':'tdb-title-text'})
#newfile12.write(title14[0].text + "\n")
title = title14[0].text
print(title14[0].text)

content14= html14.findAll(attrs={'class':'tdb-block-inner td-fix-index'})
#print(content14[14].text)


#newfile12.write(content14[14].text)
#os.rename(oldname12,newname12) .
main= content14[14].text

#----------CREATING A FILTERED LISTS-----------#

content = title + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -52

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url15 = 'https://insights.blackcoffer.com/ai-tool-alexa-google-assistant-finance-banking-tool-future/'






newfile13= open('old13.txt','w')
newname13= "URLID-52.txt"
oldname13= "old13.txt"

page15 = requests.get(url15)

html15 = BeautifulSoup(page15.content,'html.parser')



title15= html15.findAll(attrs={'class':'td-bred-no-url-last'})


#newfile13.write(title15[1].text + "\n")
title = title15[1].text


content15= html15.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content15[0].text)

#newfile13.write(content15[0].text)
#os.rename(oldname13,newname13) 
main = content15[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title+ main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -53

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url16 = 'https://insights.blackcoffer.com/ai-healthcare-revolution-ml-technology-algorithm-google-analytics-industrialrevolution/'






newfile14= open('old14.txt','w')
newname14= "URLID-53.txt"
oldname14= "old14.txt"

page16 = requests.get(url16)

html16 = BeautifulSoup(page16.content,'html.parser')



title16= html16.findAll(attrs={'class':'td-bred-no-url-last'})
#print(title16[1].text)

#newfile14.write(title16[1].text + "\n")
title = title16[1].text


content16= html16.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content16[0].text)

#newfile14.write(content16[0].text)
#os.rename(oldname14,newname14) 
main = content16[0].text
#----------CREATING A FILTERED LISTS-----------#

content = title + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -54

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url17 = 'https://insights.blackcoffer.com/all-you-need-to-know-about-online-marketing/'






#newfile15= open('old15.txt','w')
newname15= "URLID-54.txt"
oldname15= "old15.txt"

page17 = requests.get(url17)

html17 = BeautifulSoup(page17.content,'html.parser')



title17= html17.findAll(attrs={'class':'td-bred-no-url-last'})
print(title17[1].text)
title = title17[1].text

#newfile15.write(title17[1].text + "\n")



content17= html17.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content17[0].text)

#newfile15.write(content17[0].text)
#os.rename(oldname15,newname15) 
main = content17[0].text

#----------CREATING A FILTERED LISTS-----------#

content = title + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -55

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url18 = 'https://insights.blackcoffer.com/evolution-of-advertising-industry/'






newfile16= open('old16.txt','w')
newname16= "URLID-55.txt"
oldname16= "old16.txt"

page18 = requests.get(url18)

html18 = BeautifulSoup(page18.content,'html.parser')



title18= html18.findAll(attrs={'class':'entry-title'})


#newfile16.write(title18[16].text + "\n")



content18= html18.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content18[0].text)
title = title18[16].text

#newfile16.write(content18[0].text)
#os.rename(oldname16,newname16) 
main = content18[0].text
#----------CREATING A FILTERED LISTS-----------#

content = title + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -56

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url19 = 'https://insights.blackcoffer.com/how-data-analytics-can-help-your-business-respond-to-the-impact-of-covid-19/'






newfile17= open('old17.txt','w')
newname17= "URLID-56.txt"
oldname17= "old17.txt"

page19 = requests.get(url19)

html19 = BeautifulSoup(page19.content,'html.parser')
#print(html19)


title19= html19.findAll(attrs={'class':'entry-title'})

title = title19[16].text 


#newfile17.write(title19[16].text + "\n")



content19= html19.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content19[0].text)

#newfile17.write(content19[0].text)
#os.rename(oldname17,newname17) 
main = content19[0].text


#----------CREATING A FILTERED LISTS-----------#

content = title + main

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -58

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url20 = 'https://insights.blackcoffer.com/environmental-impact-of-the-covid-19-pandemic-lesson-for-the-future/'






newfile18= open('old18.txt','w')
newname18= "URLID-58.txt"
oldname18= "old18.txt"

page20 = requests.get(url20)

html20 = BeautifulSoup(page20.content,'html.parser')



title20= html20.findAll(attrs={'class':'entry-title'})
#print(title20[16].text)

#newfile18.write(title20[16].text + "\n")
t = title20[16].text


content20= html20.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content20[0].text)

#newfile18.write(content20[0].text)
#os.rename(oldname18,newname18)  
m = content20[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t + m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -59

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url21 = 'https://insights.blackcoffer.com/how-data-analytics-and-ai-are-used-to-halt-the-covid-19-pandemic/'






newfile19= open('old19.txt','w')
newname19= "URLID-59.txt"
oldname19= "old19.txt"

page21 = requests.get(url21)

html21 = BeautifulSoup(page21.content,'html.parser')



title21= html21.findAll(attrs={'class':'entry-title'})
#print(title21[16].text)

newfile19.write(title21[16].text + "\n")

t  = title21[16].text

content21= html21.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content21[0].text)

newfile19.write(content21[0].text)
os.rename(oldname19,newname19)  
m = content21[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -60

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url22 = 'https://insights.blackcoffer.com/difference-between-artificial-intelligence-machine-learning-statistics-and-data-mining/'






newfile20= open('old20.txt','w')
newname20= "URLID-60.txt"
oldname20= "old20.txt"

page22 = requests.get(url22)

html22 = BeautifulSoup(page22.content,'html.parser')



title22= html22.findAll(attrs={'class':'entry-title'})
#print(title22[16].text)

newfile20.write(title22[16].text + "\n")

t  = title22[16].text

content22= html22.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content22[0].text)

newfile20.write(content22[0].text)
os.rename(oldname20,newname20)  

m = content22[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -61

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url23 = 'https://insights.blackcoffer.com/how-python-became-the-first-choice-for-data-science/'






newfile21= open('old21.txt','w')
newname21= "URLID-61.txt"
oldname21= "old21.txt"

page23 = requests.get(url23)

html23 = BeautifulSoup(page23.content,'html.parser')



title23= html23.findAll(attrs={'class':'entry-title'})
#print(title23[16].text)

newfile21.write(title23[16].text + "\n")



content23= html23.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content23[0].text)

newfile21.write(content23[0].text)
os.rename(oldname21,newname21) 

t = title23[16].text
m = content23[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -62

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
''''
url24 = 'https://insights.blackcoffer.com/how-google-fit-measure-heart-and-respiratory-rates-using-a-phone/'






newfile22= open('old22.txt','w')
newname22= "URLID-62.txt"
oldname22= "old22.txt"

page24 = requests.get(url24)

html24 = BeautifulSoup(page24.content,'html.parser')



title24= html24.findAll(attrs={'class':'entry-title'})
#print(title24[16].text)
t = title24[16].text
newfile22.write(title24[16].text + "\n")



content24= html24.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content24[0].text
#print(content24[0].text)

newfile22.write(content24[0].text)
os.rename(oldname22,newname22)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -63

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url25 = 'https://insights.blackcoffer.com/what-is-the-future-of-mobile-apps/'






newfile23= open('old23.txt','w')
newname23= "URLID-63.txt"
oldname23= "old23.txt"

page25 = requests.get(url25)

html25 = BeautifulSoup(page25.content,'html.parser')



title25= html25.findAll(attrs={'class':'entry-title'})
#print(title25[16].text)

newfile23.write(title25[16].text + "\n")
t = title25[16].text


content25= html25.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content25[0].text)

newfile23.write(content25[0].text)
os.rename(oldname23,newname23)  

m = content25[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -64

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url26 = 'https://insights.blackcoffer.com/impact-of-ai-in-health-and-medicine/'






newfile24= open('old24.txt','w')
newname24= "URLID-64.txt"
oldname24= "old24.txt"

page26 = requests.get(url26)

html26 = BeautifulSoup(page26.content,'html.parser')



title26= html26.findAll(attrs={'class':'entry-title'})
#print(title26[16].text)

newfile24.write(title26[16].text + "\n")

t  = title26[16].text

content26= html26.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content26[0].text)

newfile24.write(content26[0].text)
os.rename(oldname24,newname24)  
m = content26[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -65

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url27 = 'https://insights.blackcoffer.com/telemedicine-what-patients-like-and-dislike-about-it/'






newfile25= open('old25.txt','w')
newname25= "URLID-65.txt"
oldname25= "old25.txt"

page27 = requests.get(url27)

html27 = BeautifulSoup(page27.content,'html.parser')



title27= html27.findAll(attrs={'class':'entry-title'})
#print(title27[16].text)

newfile25.write(title27[16].text + "\n")

t = title27[16].text

content27= html27.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content27[0].text)

newfile25.write(content27[0].text)
os.rename(oldname25,newname25)  
m = content27[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -66

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url28 = 'https://insights.blackcoffer.com/how-we-forecast-future-technologies/'






newfile26= open('old26.txt','w')
newname26= "URLID-66.txt"
oldname26= "old26.txt"

page28 = requests.get(url28)

html28 = BeautifulSoup(page28.content,'html.parser')



title28= html28.findAll(attrs={'class':'entry-title'})
#print(title28[16].text)

newfile26.write(title28[16].text + "\n")
t = title28[16].text


content28= html28.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content28[0].text)

newfile26.write(content28[0].text)
os.rename(oldname26,newname26) 
m= content28[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -67

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url29 = 'https://insights.blackcoffer.com/can-robots-tackle-late-life-loneliness/'






newfile27= open('old27.txt','w')
newname27= "URLID-67.txt"
oldname27= "old27.txt"

page29 = requests.get(url29)

html29 = BeautifulSoup(page29.content,'html.parser')



title29= html29.findAll(attrs={'class':'entry-title'})
#print(title29[16].text)

newfile27.write(title29[16].text + "\n")
t = title29[16].text


content29= html29.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content29[0].text)
m = content29[0].text

newfile27.write(content29[0].text)
os.rename(oldname27,newname27) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -68

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url30 = 'https://insights.blackcoffer.com/embedding-care-robots-into-society-socio-technical-considerations/'






newfile28= open('old28.txt','w')
newname28= "URLID-68.txt"
oldname28= "old28.txt"

page30 = requests.get(url30)

html30= BeautifulSoup(page30.content,'html.parser')



title30= html30.findAll(attrs={'class':'entry-title'})
#print(title30[16].text)

newfile28.write(title30[16].text + "\n")

t = title30[16].text

content30= html30.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content30[0].text)
m = content30[0].text
newfile28.write(content30[0].text)
os.rename(oldname28,newname28)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -69

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url31 = 'https://insights.blackcoffer.com/management-challenges-for-future-digitalization-of-healthcare-services/'






newfile29= open('old29.txt','w')
newname29= "URLID-69.txt"
oldname29= "old29.txt"

page31 = requests.get(url31)

html31= BeautifulSoup(page31.content,'html.parser')



title31= html31.findAll(attrs={'class':'entry-title'})
#print(title31[16].text)

newfile29.write(title31[16].text + "\n")
t  = title31[16].text


content31= html31.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content31[0].text
#print(content31[0].text)

newfile29.write(content31[0].text)
os.rename(oldname29,newname29)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -70

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url32 = 'https://insights.blackcoffer.com/are-we-any-closer-to-preventing-a-nuclear-holocaust/'






newfile30= open('old30.txt','w')
newname30= "URLID-70.txt"
oldname30= "old30.txt"

page32 = requests.get(url32)

html32= BeautifulSoup(page32.content,'html.parser')



title32= html32.findAll(attrs={'class':'entry-title'})
#print(title32[16].text)

newfile30.write(title32[16].text + "\n")
t = title32[16].text


content32= html32.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content32[0].text)
m = content32[0].text
newfile30.write(content32[0].text)
os.rename(oldname30,newname30) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''



'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -71

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url33 = 'https://insights.blackcoffer.com/will-technology-eliminate-the-need-for-animal-testing-in-drug-development/'






newfile31= open('old31.txt','w')
newname31= "URLID-71.txt"
oldname31= "old31.txt"

page33 = requests.get(url33)

html33= BeautifulSoup(page33.content,'html.parser')



title33= html33.findAll(attrs={'class':'entry-title'})
#print(title33[16].text)

newfile31.write(title33[16].text + "\n")
t = title33[16].text


content33= html33.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content33[0].text)
m = content33[0].text
newfile31.write(content33[0].text)
os.rename(oldname31,newname31)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -72

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url34 = 'https://insights.blackcoffer.com/will-we-ever-understand-the-nature-of-consciousness/'






newfile32= open('old32.txt','w')
newname32= "URLID-72.txt"
oldname32= "old32.txt"

page34 = requests.get(url34)

html34= BeautifulSoup(page34.content,'html.parser')



title34= html34.findAll(attrs={'class':'entry-title'})
#print(title34[16].text)

newfile32.write(title34[16].text + "\n")
t = title34[16].text


content34= html34.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content34[0].text
#print(content34[0].text)

newfile32.write(content34[0].text)
os.rename(oldname32,newname32)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -73

'''------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url35 = 'https://insights.blackcoffer.com/will-we-ever-colonize-outer-space/'






newfile33= open('old33.txt','w')
newname33= "URLID-73.txt"
oldname33= "old33.txt"

page35 = requests.get(url35)

html35= BeautifulSoup(page35.content,'html.parser')



title35= html35.findAll(attrs={'class':'entry-title'})
#print(title35[16].text)

newfile33.write(title35[16].text + "\n")

t = title35[16].text

content35= html35.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content35[0].text
#print(content35[0].text)

newfile33.write(content35[0].text)
os.rename(oldname33,newname33) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -74

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url36 = 'https://insights.blackcoffer.com/what-is-the-chance-homo-sapiens-will-survive-for-the-next-500-years/'






newfile34= open('old34.txt','w')
newname34= "URLID-74.txt"
oldname34= "old34.txt"

page36 = requests.get(url36)

html36= BeautifulSoup(page36.content,'html.parser')



title36= html36.findAll(attrs={'class':'entry-title'})
#print(title36[16].text)

newfile34.write(title36[16].text + "\n")

t= title36[16].text

content36= html36.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content36[0].text)
m = content36[0].text
newfile34.write(content36[0].text)
os.rename(oldname34,newname34)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -75

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url37 = 'https://insights.blackcoffer.com/why-does-your-business-need-a-chatbot/'






newfile35= open('old35.txt','w')
newname35= "URLID-75.txt"
oldname35= "old35.txt"

page37 = requests.get(url37)

html37= BeautifulSoup(page37.content,'html.parser')



title37= html37.findAll(attrs={'class':'entry-title'})
#print(title37[16].text)

newfile35.write(title37[16].text + "\n")
t = title37[16].text


content37= html37.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content37[0].text)
m = content37[0].text
newfile35.write(content37[0].text)
os.rename(oldname35,newname35)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -76

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url38 = 'https://insights.blackcoffer.com/how-you-lead-a-project-or-a-team-without-any-technical-expertise/'






newfile36= open('old36.txt','w')
newname36= "URLID-76.txt"
oldname36= "old36.txt"

page38 = requests.get(url38)

html38= BeautifulSoup(page38.content,'html.parser')



title38= html38.findAll(attrs={'class':'entry-title'})
#print(title38[16].text)

newfile36.write(title38[16].text + "\n")

t = title38[16].text

content38= html38.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content38[0].text)
m = content38[0].text
newfile36.write(content38[0].text)
os.rename(oldname36,newname36) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -77

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url39 = 'https://insights.blackcoffer.com/can-you-be-great-leader-without-technical-expertise/'






newfile37= open('old37.txt','w')
newname37= "URLID-77.txt"
oldname37= "old37.txt"

page39 = requests.get(url39)

html39= BeautifulSoup(page39.content,'html.parser')



title39= html39.findAll(attrs={'class':'entry-title'})
print(title39[16].text)

newfile37.write(title39[16].text + "\n")

t = title39[16].text

content39= html39.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content39[0].text)
m = content39[0].text
newfile37.write(content39[0].text)
os.rename(oldname37,newname37)

 
#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
  
   
   '''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -78

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url40 = 'https://insights.blackcoffer.com/how-does-artificial-intelligence-affect-the-environment/'






newfile38= open('old38.txt','w')
newname38= "URLID-78.txt"
oldname38= "old38.txt"

page40 = requests.get(url40)

html40= BeautifulSoup(page40.content,'html.parser')



title40= html40.findAll(attrs={'class':'entry-title'})
print(title40[16].text)

newfile38.write(title40[16].text + "\n")

t = title40[16].text

content40= html40.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content40[0].text)

newfile38.write(content40[0].text)
os.rename(oldname38,newname38) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -79

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url41 = 'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes-2/'






newfile39= open('old39.txt','w')
newname39= "URLID-79.txt"
oldname39= "old39.txt"

page41 = requests.get(url41)

html41= BeautifulSoup(page41.content,'html.parser')



title41= html41.findAll(attrs={'class':'entry-title'})
print(title41[16].text)

newfile39.write(title41[16].text + "\n")

t = title41[16].text

content41= html41.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content41[0].text)

newfile39.write(content41[0].text)
os.rename(oldname39,newname39) 
m = content41[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -80

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url42 = 'https://insights.blackcoffer.com/is-perfection-the-greatest-enemy-of-productivity/'






newfile40= open('old40.txt','w')
newname40= "URLID-80.txt"
oldname40= "old40.txt"

page42 = requests.get(url42)

html42= BeautifulSoup(page42.content,'html.parser')



title42= html42.findAll(attrs={'class':'entry-title'})
print(title42[16].text)

newfile40.write(title42[16].text + "\n")

t = title42[16].text

content42= html42.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content42[0].text)

newfile40.write(content42[0].text)
os.rename(oldname40,newname40) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -81

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url43 = 'https://insights.blackcoffer.com/global-financial-crisis-2008-causes-effects-and-its-solution/'






newfile41= open('old41.txt','w')
newname41= "URLID-81.txt"
oldname41= "old41.txt"

page43 = requests.get(url43)

html43= BeautifulSoup(page43.content,'html.parser')



title43= html43.findAll(attrs={'class':'entry-title'})
print(title43[16].text)

newfile41.write(title43[16].text + "\n")
t = title43[16].text


content43= html43.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content43[0].text)

newfile41.write(content43[0].text)
os.rename(oldname41,newname41)
m = content43[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)


'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -82

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url44 = 'https://insights.blackcoffer.com/gender-diversity-and-equality-in-the-tech-industry/'






newfile42= open('old42.txt','w')
newname42= "URLID-82.txt"
oldname42= "old42.txt"

page44 = requests.get(url44)

html44= BeautifulSoup(page44.content,'html.parser')



title44= html44.findAll(attrs={'class':'entry-title'})
print(title44[16].text)

newfile42.write(title44[16].text + "\n")

t = title44[16].text

content44= html44.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content44[0].text)
m = content44[0].text
newfile42.write(content44[0].text)
os.rename(oldname42,newname42) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -83

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url45 = 'https://insights.blackcoffer.com/how-to-overcome-your-fear-of-making-mistakes/'






newfile43= open('old43.txt','w')
newname43= "URLID-83.txt"
oldname43= "old43.txt"

page45 = requests.get(url45)

html45= BeautifulSoup(page45.content,'html.parser')



title45= html45.findAll(attrs={'class':'entry-title'})
#print(title45[16].text)

newfile43.write(title45[16].text + "\n")

t = title45[16].text

content45= html45.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content45[0].text)
m = content45[0].text
newfile43.write(content45[0].text)
os.rename(oldname43,newname43)

 
#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
  '''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -84

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url46 = 'https://insights.blackcoffer.com/how-small-business-can-survive-the-coronavirus-crisis/'






newfile44= open('old44.txt','w')
newname44= "URLID-84.txt"
oldname44= "old44.txt"

page46 = requests.get(url46)

html46= BeautifulSoup(page46.content,'html.parser')



title46= html46.findAll(attrs={'class':'entry-title'})
#print(title46[16].text)
t = title46[16].text
newfile44.write(title46[16].text + "\n")



content46= html46.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content46[0].text)
m = content46[0].text
newfile44.write(content46[0].text)
os.rename(oldname44,newname44)


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -85

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url47 = 'https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors-and-food-stalls/'






newfile45= open('old45.txt','w')
newname45= "URLID-85.txt"
oldname45= "old45.txt"

page47 = requests.get(url47)

html47= BeautifulSoup(page47.content,'html.parser')



title47= html47.findAll(attrs={'class':'entry-title'})
#print(title47[16].text)

newfile45.write(title47[16].text + "\n")
t = title47[16].text


content47= html47.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content47[0].text)
m = content47[0].text
newfile45.write(content47[0].text)
os.rename(oldname45,newname45)

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -86

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url48 = 'https://insights.blackcoffer.com/impacts-of-covid-19-on-vegetable-vendors/'






newfile46= open('old46.txt','w')
newname46= "URLID-86.txt"
oldname46= "old46.txt"

page48 = requests.get(url48)

html48= BeautifulSoup(page48.content,'html.parser')



title48= html48.findAll(attrs={'class':'entry-title'})
#print(title48[16].text)

newfile46.write(title48[16].text + "\n")

t = title48[16].text

content48= html48.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content48[0].text)
m = content48[0].text
newfile46.write(content48[0].text)
os.rename(oldname46,newname46)

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -87

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url49 = 'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-tourism-aviation-industries/'






newfile47= open('old47.txt','w')
newname47= "URLID-87.txt"
oldname47= "old47.txt"

page49 = requests.get(url49)

html49= BeautifulSoup(page49.content,'html.parser')



title49= html49.findAll(attrs={'class':'entry-title'})
#print(title49[16].text)
t = title49[16].text
newfile47.write(title49[16].text + "\n")



content49= html49.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content49[0].text
#print(content49[0].text)

newfile47.write(content49[0].text)
os.rename(oldname47,newname47) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -88

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url50 = 'https://insights.blackcoffer.com/impact-of-covid-19-pandemic-on-sports-events-around-the-world/'






newfile48= open('old48.txt','w')
newname48= "URLID-88.txt"
oldname48= "old48.txt"

page50 = requests.get(url50)

html50= BeautifulSoup(page50.content,'html.parser')



title50= html50.findAll(attrs={'class':'entry-title'})
#print(title50[16].text)

newfile48.write(title50[16].text + "\n")

t = title50[16].text

content50= html50.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

#print(content50[0].text)

newfile48.write(content50[0].text)
os.rename(oldname48,newname48) 
m = content50[0].text


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -89

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url51 = 'https://insights.blackcoffer.com/changing-landscape-and-emerging-trends-in-the-indian-it-ites-industry/'






newfile49= open('old49.txt','w')
newname49= "URLID-89.txt"
oldname49= "old49.txt"

page51 = requests.get(url51)

html51= BeautifulSoup(page51.content,'html.parser')



title51= html51.findAll(attrs={'class':'entry-title'})
print(title51[16].text)

newfile49.write(title51[16].text + "\n")
t = title51[16].text


content51= html51.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content51[0].text)
m = content51[0].text
newfile49.write(content51[0].text)
os.rename(oldname49,newname49) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -90
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url52 = 'https://insights.blackcoffer.com/online-gaming-adolescent-online-gaming-effects-demotivated-depression-musculoskeletal-and-psychosomatic-symptoms/'






newfile50= open('old50.txt','w')
newname50= "URLID-90.txt"
oldname50= "old50.txt"

page52 = requests.get(url52)

html52= BeautifulSoup(page52.content,'html.parser')



title52= html52.findAll(attrs={'class':'entry-title'})
print(title52[16].text)

newfile50.write(title52[16].text + "\n")

t = title52[16].text

content52= html52.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content52[0].text)
m = content52[0].text
newfile50.write(content52[0].text)
os.rename(oldname50,newname50)  




#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)  '''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -91
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url53 = 'https://insights.blackcoffer.com/human-rights-outlook/'






newfile51= open('old51.txt','w')
newname51= "URLID-91.txt"
oldname51= "old51.txt"

page53 = requests.get(url53)

html53= BeautifulSoup(page53.content,'html.parser')
#print(html53)


title53= html53.findAll(attrs={'class':'tdb-title-text'})
#print(title53[0].text)


newfile51.write(title53[0].text + "\n")
t = title53[0].text


content53= html53.findAll(attrs={'class':'tdb-block-inner td-fix-index'}) 

print(content53[14].text)

m = content53[14].text



newfile51.write(content53[14].text)
os.rename(oldname51,newname51) 



#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -92
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url54 = 'https://insights.blackcoffer.com/how-voice-search-makes-your-business-a-successful-business/'





newfile52= open('old52.txt','w')
newname52= "URLID-92.txt"
oldname52= "old52.txt"

page54 = requests.get(url54)

html54= BeautifulSoup(page54.content,'html.parser')
#print(html53)


title54= html54.findAll(attrs={'class':'tdb-title-text'})
print(title54[0].text)


newfile52.write(title54[0].text + "\n")

t = title54[0].text
content54= html54.findAll(attrs={'class':'tdb-block-inner td-fix-index'}) 

print(content54[14].text)

m = content54[14].text


newfile52.write(content54[14].text)
os.rename(oldname52,newname52) 



#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -93
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url55 = 'https://insights.blackcoffer.com/how-the-covid-19-crisis-is-redefining-jobs-and-services/'





newfile53= open('old53.txt','w')
newname53= "URLID-93.txt"
oldname53= "old53.txt"

page55 = requests.get(url55)

html55= BeautifulSoup(page55.content,'html.parser')
#print(html55)


title55= html55.findAll(attrs={'class':'entry-title'})
print(len(title55))

t = title55[16].text


newfile53.write(title55[16].text + "\n")



content55= html55.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content55[0].text)
m = content55[0].text

newfile53.write(content55[0].text)
os.rename(oldname53,newname53)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -94
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url56 = 'https://insights.blackcoffer.com/how-to-increase-social-media-engagement-for-marketers/'





newfile54= open('old54.txt','w')
newname54= "URLID-94.txt"
oldname54= "old54.txt"

page56 = requests.get(url56)

html56= BeautifulSoup(page56.content,'html.parser')
#print(html55)


title56= html56.findAll(attrs={'class':'entry-title'})


t = title56[16].text


newfile54.write(title56[16].text + "\n")



content56= html56.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content56[0].text)
m = content56[0].text

newfile54.write(content56[0].text)
os.rename(oldname54,newname54) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -95
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url57 = 'https://insights.blackcoffer.com/impacts-of-covid-19-on-streets-sides-food-stalls/'





newfile55= open('old55.txt','w')
newname55= "URLID-95.txt"
oldname55= "old55.txt"

page57 = requests.get(url57)

html57= BeautifulSoup(page57.content,'html.parser')
#print(html55)


title57= html57.findAll(attrs={'class':'entry-title'})

print(title57[16].text)

t = title57[16].text

newfile55.write(title57[16].text + "\n")



content57= html57.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content57[0].text)
m = content57[0].text

newfile55.write(content57[0].text)
os.rename(oldname55,newname55) 



#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -96
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url58 = 'https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets-2/'





newfile56= open('old56.txt','w')
newname56= "URLID-96.txt"
oldname56= "old56.txt"

page58 = requests.get(url58)

html58= BeautifulSoup(page58.content,'html.parser')
#print(html55)


title58= html58.findAll(attrs={'class':'entry-title'})

print(title58[16].text)



newfile56.write(title58[16].text + "\n")
t = title58[16].text


content58= html58.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content58[0].text)
m = content58[0].text

newfile56.write(content58[0].text)
os.rename(oldname56,newname56)


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -97
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url59 = 'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-5/'





newfile57= open('old57.txt','w')
newname57= "URLID-97.txt"
oldname57= "old57.txt"

page59 = requests.get(url59)

html59= BeautifulSoup(page59.content,'html.parser')
#print(html55)


title59= html59.findAll(attrs={'class':'entry-title'})

print(title59[16].text)


t = title59[16].text
newfile57.write(title59[16].text + "\n")



content59= html59.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content59[0].text)
m = content59[0].text

newfile57.write(content59[0].text)
os.rename(oldname57,newname57) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -98
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url60 = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-4/'





newfile58= open('old58.txt','w')
newname58= "URLID-98.txt"
oldname58= "old58.txt"

page60 = requests.get(url60)

html60= BeautifulSoup(page60.content,'html.parser')
#print(html55)


title60= html60.findAll(attrs={'class':'entry-title'})

print(title60[16].text)

t = title60[16].text

newfile58.write(title60[16].text + "\n")



content60= html60.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content60[0].text)
m = content60[0].text

newfile58.write(content60[0].text)
os.rename(oldname58,newname58)


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -99
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url61 = 'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-2/'





newfile59= open('old59.txt','w')
newname59= "URLID-99.txt"
oldname59= "old59.txt"

page61 = requests.get(url61)

html61= BeautifulSoup(page61.content,'html.parser')
#print(html55)


title61= html61.findAll(attrs={'class':'entry-title'})

print(title61[16].text)

t = title61[16].text

newfile59.write(title61[16].text + "\n")



content61= html61.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

print(content61[0].text)
m = content61[0].text

newfile59.write(content61[0].text)
os.rename(oldname59,newname59) 



#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -100
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url62 = 'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work-3/'





newfile60= open('old60.txt','w')
newname60= "URLID-100.txt"
oldname60= "old60.txt"

page62 = requests.get(url62)

html62= BeautifulSoup(page62.content,'html.parser')



title62= html62.findAll(attrs={'class':'tdb-title-text'})

#print(title62[0].text)
t = title62[0].text

newfile60.write(title62[0].text + "\n")



content62= html62.findAll(attrs={'class':'tdb-block-inner td-fix-index'}) 

#for i in range(19):
#	print(f"{i}.) {content62[i]}\n")

#print(content62[14].text)
newfile60.write(content62[14].text)
os.rename(oldname60,newname60)

m = content62[14].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -101
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url63 = 'https://insights.blackcoffer.com/travel-and-tourism-outlook/'





newfile61= open('old61.txt','w')
newname61= "URLID-101.txt"
oldname61= "old61.txt"

page63 = requests.get(url63)

html63= BeautifulSoup(page63.content,'html.parser')



title63= html63.findAll(attrs={'class':'entry-title'})

print(title63[16].text)

t = title63[16].text
newfile61.write(title63[16].text + "\n")



content63= html63.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content63[0].text

print(content63[0].text)
newfile61.write(content63[0].text)
os.rename(oldname61,newname61) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -102
'''------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url64 = 'https://insights.blackcoffer.com/gaming-disorder-and-effects-of-gaming-on-health/'





newfile62= open('old62.txt','w')
newname62= "URLID-102.txt"
oldname62= "old62.txt"

page64= requests.get(url64)

html64= BeautifulSoup(page64.content,'html.parser')



title64= html64.findAll(attrs={'class':'entry-title'})

print(title64[16].text)
t = title64[16].text

newfile62.write(title64[16].text + "\n")



content64= html64.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content64[0].text
print(content64[0].text)
newfile62.write(content64[0].text)
os.rename(oldname62,newname62) 



#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -103
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url65 = 'https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation/'





newfile63= open('old63.txt','w')
newname63= "URLID-103.txt"
oldname63= "old63.txt"

page65= requests.get(url65)

html65= BeautifulSoup(page65.content,'html.parser')



title65= html65.findAll(attrs={'class':'entry-title'})

print(title65[16].text)


newfile63.write(title65[16].text + "\n")
t = title65[16].text


content65= html65.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content65[0].text
print(content65[0].text)
newfile63.write(content65[0].text)
os.rename(oldname63,newname63) 



#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -104
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url66 = 'https://insights.blackcoffer.com/what-is-the-repercussion-of-the-environment-due-to-the-covid-19-pandemic-situation-2/'





newfile64= open('old64.txt','w')
newname64= "URLID-104.txt"
oldname64= "old64.txt"

page66= requests.get(url66)

html66= BeautifulSoup(page66.content,'html.parser')



title66= html66.findAll(attrs={'class':'entry-title'})

print(title66[16].text)

t = title66[16].text
newfile64.write(title66[16].text + "\n")



content66= html66.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content66[0].text

print(content66[0].text)
newfile64.write(content66[0].text)
os.rename(oldname64,newname64)

 #----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
  
    '''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -105
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url67 = 'https://insights.blackcoffer.com/contribution-of-handicrafts-visual-arts-literature-in-the-indian-economy/'





newfile65= open('old65.txt','w')
newname65= "URLID-105.txt"
oldname65= "old65.txt"

page67= requests.get(url67)

html67= BeautifulSoup(page67.content,'html.parser')



title67= html67.findAll(attrs={'class':'entry-title'})

print(title67[16].text)

t = title67[16].text
newfile65.write(title67[16].text + "\n")



content67= html67.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content67[0].text

print(content67[0].text)
newfile65.write(content67[0].text)
os.rename(oldname65,newname65) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)


'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -106
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url68 = 'https://insights.blackcoffer.com/how-covid-19-is-impacting-payment-preferences/'





newfile66= open('old66.txt','w')
newname66= "URLID-106.txt"
oldname66= "old66.txt"

page68= requests.get(url68)

html68= BeautifulSoup(page68.content,'html.parser')
#print(html68)


title68= html68.findAll(attrs={'class':'tdb-title-text'})
t = title68[0].text
print(title68[0].text)


newfile66.write(title68[0].text + "\n")



content68= html68.findAll(attrs={'class':'tdb-block-inner td-fix-index'}) 

m = content68[14].text

print(content68[14].text)
newfile66.write(content68[14].text)
os.rename(oldname66,newname66) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -107
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url69 = 'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-2/'





newfile67= open('old67.txt','w')
newname67= "URLID-107.txt"
oldname67= "old67.txt"

page69= requests.get(url69)

html69= BeautifulSoup(page69.content,'html.parser')
#print(html68)


title69= html69.findAll(attrs={'class':'tdb-title-text'})

print(title69[0].text)
t = title69[0].text

newfile67.write(title69[0].text + "\n")



content69= html69.findAll(attrs={'class':'tdb-block-inner td-fix-index'}) 

m = content69[14].text

print(content69[14].text)
newfile67.write(content69[14].text)
os.rename(oldname67,newname67) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)


'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -108
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url70 = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/'





newfile68= open('old68.txt','w')
newname68= "URLID-108.txt"
oldname68= "old68.txt"

page70= requests.get(url70)

html70= BeautifulSoup(page70.content,'html.parser')

#print(html70)


title70= html70.findAll(attrs={'class':'entry-title'})


print(title70[16].text)
t = title70[16].text

newfile68.write(title70[16].text + "\n")



content70= html70.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content70[0].text

print(content70[0].text)
newfile68.write(content70[0].text)
os.rename(oldname68,newname68) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)


'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''

#Extracting data for URLID -109
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url71 = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis/'





newfile69= open('old69.txt','w')
newname69= "URLID-109.txt"
oldname69= "old69.txt"

page71= requests.get(url71)

html71= BeautifulSoup(page71.content,'html.parser')

#print(html70)


title71= html71.findAll(attrs={'class':'entry-title'})

t = title71[16].text
print(title71[16].text)


newfile69.write(title71[16].text + "\n")



content71= html71.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content71[0].text
print(content71[0].text)
newfile69.write(content71[0].text)
os.rename(oldname69,newname69) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)



'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -110
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url72 = 'https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding/'





newfile70= open('old70.txt','w')
newname70= "URLID-110.txt"
oldname70= "old70.txt"

page72= requests.get(url72)

html72= BeautifulSoup(page72.content,'html.parser')

#print(html70)


title72= html72.findAll(attrs={'class':'entry-title'})
t = title72[16].text

print(title72[16].text)


newfile70.write(title72[16].text + "\n")



content72= html72.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content72[0].text

print(content72[0].text)
newfile70.write(content72[0].text)
os.rename(oldname70,newname70)

 
  #----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
   
    
    '''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -111
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url73 = 'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-2/'





newfile71= open('old71.txt','w')
newname71= "URLID-111.txt"
oldname71= "old71.txt"

page73= requests.get(url73)

html73= BeautifulSoup(page73.content,'html.parser')

#print(html70)


title73= html73.findAll(attrs={'class':'entry-title'})


print(title73[16].text)
t = title73[16].text

newfile71.write(title73[16].text + "\n")



content73= html73.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content73[0].text
print(content73[0].text)
newfile71.write(content73[0].text)
os.rename(oldname71,newname71)

 #----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
  
   '''
     
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -112
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url74 = 'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-3/'





newfile72= open('old72.txt','w')
newname72= "URLID-112.txt"
oldname72= "old72.txt"

page74= requests.get(url74)

html74= BeautifulSoup(page74.content,'html.parser')

#print(html74)


title74= html74.findAll(attrs={'class':'tdb-title-text'})


print(title74[0].text)


newfile72.write(title74[0].text + "\n")


t = title74[0].text
content74= html74.findAll(attrs={'class':'tdb-block-inner td-fix-index'}) 
print(len(content74))

m = content74[14].text

print(content74[14].text)
newfile72.write(content74[14].text)
os.rename(oldname72,newname72) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -113
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url75 = 'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-3/'





newfile73= open('old73.txt','w')
newname73= "URLID-113.txt"
oldname73= "old73.txt"

page75= requests.get(url75)

html75= BeautifulSoup(page75.content,'html.parser')




title75= html75.findAll(attrs={'class':'entry-title'})


#print(title75[16].text)


newfile73.write(title75[16].text + "\n")


t = title75[16].text
content75= html75.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content75[0].text
#print(content75[0].text)
newfile73.write(content75[0].text)
os.rename(oldname73,newname73)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -114
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url76 = 'https://insights.blackcoffer.com/estimating-the-impact-of-covid-19-on-the-world-of-work/'




newfile74= open('old74.txt','w')
newname74= "URLID-114.txt"
oldname74= "old74.txt"

page76= requests.get(url76)

html76= BeautifulSoup(page76.content,'html.parser')




title76= html76.findAll(attrs={'class':'entry-title'})


print(title76[16].text)
t = title76[16].text

newfile74.write(title76[16].text + "\n")



content76= html76.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content76[0].text

print(content76[0].text)
newfile74.write(content76[0].text)
os.rename(oldname74,newname74)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -115
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url77 = 'https://insights.blackcoffer.com/covid-19-how-have-countries-been-responding-2/'




newfile75= open('old75.txt','w')
newname75= "URLID-115.txt"
oldname75= "old75.txt"

page77= requests.get(url77)

html77= BeautifulSoup(page77.content,'html.parser')




title77= html77.findAll(attrs={'class':'entry-title'})


#print(title77[16].text)

t = title77[16].text
newfile75.write(title77[16].text + "\n")



content77= html77.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content77[0].text
#print(content77[0].text)
newfile75.write(content77[0].text)
os.rename(oldname75,newname75)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''



'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -116
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url78 = 'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work-4/'




newfile76= open('old76.txt','w')
newname76= "URLID-116.txt"
oldname76= "old76.txt"

page78= requests.get(url78)

html78= BeautifulSoup(page78.content,'html.parser')




title78= html78.findAll(attrs={'class':'entry-title'})


print(title78[16].text)
t = title78[16].text

newfile76.write(title78[16].text + "\n")



content78= html78.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content78[0].text

print(content78[0].text)
newfile76.write(content78[0].text)
os.rename(oldname76,newname76)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -117
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url79 = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-2/'




newfile77= open('old77.txt','w')
newname77= "URLID-117.txt"
oldname77= "old77.txt"

page79= requests.get(url79)

html79= BeautifulSoup(page79.content,'html.parser')




title79= html79.findAll(attrs={'class':'entry-title'})


print(title79[16].text)
t = title79[16].text

newfile77.write(title79[16].text + "\n")



content79= html79.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content79[0].text

print(content79[0].text)
newfile77.write(content79[0].text)
os.rename(oldname77,newname77)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -118
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url80 = 'https://insights.blackcoffer.com/lessons-from-the-past-some-key-learnings-relevant-to-the-coronavirus-crisis-3/'




newfile78= open('old78.txt','w')
newname78= "URLID-118.txt"
oldname78= "old78.txt"

page80= requests.get(url80)

html80= BeautifulSoup(page80.content,'html.parser')




title80= html80.findAll(attrs={'class':'entry-title'})
t = title80[16].text

print(title80[16].text)


newfile78.write(title80[16].text + "\n")



content80= html80.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content80[0].text

print(content80[0].text)
newfile78.write(content80[0].text)
os.rename(oldname78,newname78)   
#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -119
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url81 = 'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry-4/'




newfile79= open('old79.txt','w')
newname79= "URLID-119.txt"
oldname79= "old79.txt"

page81= requests.get(url81)

html81= BeautifulSoup(page81.content,'html.parser')




title81= html81.findAll(attrs={'class':'entry-title'})


print(title81[16].text)

t = title81[16].text
newfile79.write(title81[16].text + "\n")



content81= html81.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content81[0].text

print(content81[0].text)
newfile79.write(content81[0].text)
os.rename(oldname79,newname79) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -120
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url82 = 'https://insights.blackcoffer.com/why-scams-like-nirav-modi-happen-with-indian-banks/'




newfile80= open('old80.txt','w')
newname80= "URLID-120.txt"
oldname80= "old80.txt"

page82= requests.get(url82)

html82= BeautifulSoup(page82.content,'html.parser')




title82= html82.findAll(attrs={'class':'entry-title'})


print(title82[16].text)


newfile80.write(title82[16].text + "\n")

t = title82[16].text

content82= html82.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content82[0].text

print(content82[0].text)
newfile80.write(content82[0].text)
os.rename(oldname80,newname80)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -121
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url83 = 'https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy/'




newfile81= open('old81.txt','w')
newname81= "URLID-121.txt"
oldname81= "old81.txt"

page83= requests.get(url83)

html83= BeautifulSoup(page83.content,'html.parser')




title83= html83.findAll(attrs={'class':'entry-title'})


print(title83[16].text)
t = title83[16].text

newfile81.write(title83[16].text + "\n")



content83= html83.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content83[0].text

print(content83[0].text)
newfile81.write(content83[0].text)
os.rename(oldname81,newname81) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -122
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url84 = 'https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy-2/'




newfile82= open('old82.txt','w')
newname82= "URLID-122.txt"
oldname82= "old82.txt"

page84= requests.get(url84)

html84= BeautifulSoup(page84.content,'html.parser')




title84= html84.findAll(attrs={'class':'entry-title'})

t = title84[16].text
print(title84[16].text)


newfile82.write(title84[16].text + "\n")



content84= html84.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content84[0].text

print(content84[0].text)
newfile82.write(content84[0].text)
os.rename(oldname82,newname82)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -123
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url85 = 'https://insights.blackcoffer.com/impact-of-covid-19-on-the-global-economy-2/'




newfile83= open('old83.txt','w')
newname83= "URLID-123.txt"
oldname83= "old83.txt"

page85= requests.get(url85)

html85= BeautifulSoup(page85.content,'html.parser')




title85= html85.findAll(attrs={'class':'entry-title'})


print(title85[16].text)


newfile83.write(title85[16].text + "\n")

t = title85[16].text

content85= html85.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m= content85[0].text
print(content85[0].text)
newfile83.write(content85[0].text)
os.rename(oldname83,newname83) 


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -124
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url86 = 'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-3/'




newfile84= open('old84.txt','w')
newname84= "URLID-124.txt"
oldname84= "old84.txt"

page86= requests.get(url86)

html86= BeautifulSoup(page86.content,'html.parser')




title86= html86.findAll(attrs={'class':'entry-title'})


print(title86[16].text)
t = title86[16].text

newfile84.write(title86[16].text + "\n")



content86= html86.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content86[0].text

print(content86[0].text)
newfile84.write(content86[0].text)
os.rename(oldname84,newname84)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -125
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url87 = 'https://insights.blackcoffer.com/should-celebrities-be-allowed-to-join-politics/'




newfile85= open('old85.txt','w')
newname85= "URLID-125.txt"
oldname85= "old85.txt"

page87= requests.get(url87)

html87= BeautifulSoup(page87.content,'html.parser')




title87= html87.findAll(attrs={'class':'entry-title'})


print(title87[16].text)


newfile85.write(title87[16].text + "\n")

t = title87[16].text

content87= html87.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content87[0].text

print(content87[0].text)
newfile85.write(content87[0].text)
os.rename(oldname85,newname85)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -126
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url88 = 'https://insights.blackcoffer.com/how-prepared-is-india-to-tackle-a-possible-covid-19-outbreak/'




newfile86= open('old86.txt','w')
newname86= "URLID-126.txt"
oldname86= "old86.txt"

page88= requests.get(url88)

html88= BeautifulSoup(page88.content,'html.parser')




title88= html88.findAll(attrs={'class':'entry-title'})


print(title88[16].text)


newfile86.write(title88[16].text + "\n")

t = title88[16].text

content88= html88.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content88[0].text
print(content88[0].text)
newfile86.write(content88[0].text)
os.rename(oldname86,newname86)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -127
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url89 = 'https://insights.blackcoffer.com/how-will-covid-19-affect-the-world-of-work/'




newfile87= open('old87.txt','w')
newname87= "URLID-127.txt"
oldname87= "old87.txt"

page89= requests.get(url89)

html89= BeautifulSoup(page89.content,'html.parser')




title89= html89.findAll(attrs={'class':'entry-title'})


print(title89[16].text)


newfile87.write(title89[16].text + "\n")
t = title89[16].text


content89= html89.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content89[0].text
print(content89[0].text)
newfile87.write(content89[0].text)
os.rename(oldname87,newname87)  

 #----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
  
   '''
     
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -128
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url90 = 'https://insights.blackcoffer.com/controversy-as-a-marketing-strategy/'




newfile88= open('old88.txt','w')
newname88= "URLID-128.txt"
oldname88= "old88.txt"

page90= requests.get(url90)

html90= BeautifulSoup(page90.content,'html.parser')




title90= html90.findAll(attrs={'class':'entry-title'})


print(title90[16].text)


newfile88.write(title90[16].text + "\n")

t = title90[16].text

content90= html90.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content90[0].text

print(content90[0].text)
newfile88.write(content90[0].text)
os.rename(oldname88,newname88)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -129
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url91 = 'https://insights.blackcoffer.com/coronavirus-impact-on-the-hospitality-industry/'




newfile89= open('old89.txt','w')
newname89= "URLID-129.txt"
oldname89= "old89.txt"

page91= requests.get(url91)

html91= BeautifulSoup(page91.content,'html.parser')




title91= html91.findAll(attrs={'class':'entry-title'})


print(title91[16].text)


newfile89.write(title91[16].text + "\n")

t = title91[16].text

content91= html91.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content91[0].text
print(content91[0].text)
newfile89.write(content91[0].text)
os.rename(oldname89,newname89)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -130
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url92 = 'https://insights.blackcoffer.com/coronavirus-impact-on-energy-markets/'




newfile90= open('old90.txt','w')
newname90= "URLID-130.txt"
oldname90= "old90.txt"

page92= requests.get(url92)

html92= BeautifulSoup(page92.content,'html.parser')




title92= html92.findAll(attrs={'class':'entry-title'})


print(title92[16].text)


newfile90.write(title92[16].text + "\n")

t = title92[16].text

content92= html92.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content92[0].text

print(content92[0].text)
newfile90.write(content92[0].text)
os.rename(oldname90,newname90)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE-----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -131
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url93 = 'https://insights.blackcoffer.com/what-are-the-key-policies-that-will-mitigate-the-impacts-of-covid-19-on-the-world-of-work/'




newfile91= open('old91.txt','w')
newname91= "URLID-131.txt"
oldname91= "old91.txt"

page93= requests.get(url93)

html93= BeautifulSoup(page93.content,'html.parser')




title93= html93.findAll(attrs={'class':'entry-title'})


print(title93[16].text)


newfile91.write(title93[16].text + "\n")

t = title93[16].text

content93= html93.findAll(attrs={'class':'td-post-content tagdiv-type'}) 


print(content93[0].text)
newfile91.write(content93[0].text)
os.rename(oldname91,newname91)   
m = content93[0].text

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -132
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url94 = 'https://insights.blackcoffer.com/marketing-drives-results-with-a-focus-on-problems/'




newfile92= open('old92.txt','w')
newname92= "URLID-132.txt"
oldname92= "old92.txt"

page94= requests.get(url94)

html94= BeautifulSoup(page94.content,'html.parser')




title94= html94.findAll(attrs={'class':'entry-title'})


print(title94[16].text)


newfile92.write(title94[16].text + "\n")

t = title94[16].text

content94= html94.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content94[0].text
print(content94[0].text)
newfile92.write(content94[0].text)
os.rename(oldname92,newname92) 

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -133
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url95 = 'https://insights.blackcoffer.com/continued-demand-for-sustainability/'




newfile93= open('old93.txt','w')
newname93= "URLID-133.txt"
oldname93= "old93.txt"

page95= requests.get(url95)

html95= BeautifulSoup(page95.content,'html.parser')




title95= html95.findAll(attrs={'class':'entry-title'})


print(title95[16].text)


newfile93.write(title95[16].text + "\n")

t = title95[16].text

content95= html95.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content95[0].text

print(content95[0].text)
newfile93.write(content95[0].text)
os.rename(oldname93,newname93)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -134
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url96= 'https://insights.blackcoffer.com/coronavirus-disease-covid-19-effect-the-impact-and-role-of-mass-media-during-the-pandemic/'




newfile94= open('old94.txt','w')
newname94= "URLID-134.txt"
oldname94= "old94.txt"

page96= requests.get(url96)

html96= BeautifulSoup(page96.content,'html.parser')




title96= html96.findAll(attrs={'class':'entry-title'})


print(title96[16].text)
t = title96[16].text

newfile94.write(title96[16].text + "\n")



content96= html96.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content96[0].text

print(content96[0].text)
newfile94.write(content96[0].text)
os.rename(oldname94,newname94)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -135
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url97= 'https://insights.blackcoffer.com/should-people-wear-fabric-gloves-seeking-evidence-regarding-the-differential-transfer-of-covid-19-or-coronaviruses-generally-between-surfaces/'




newfile95= open('old95.txt','w')
newname95= "URLID-135.txt"
oldname95= "old95.txt"

page97= requests.get(url97)

html97= BeautifulSoup(page97.content,'html.parser')




title97= html97.findAll(attrs={'class':'entry-title'})


print(title97[16].text)


newfile95.write(title97[16].text + "\n")

t = title97[16].text

content97= html97.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content97[0].text

print(content97[0].text)
newfile95.write(content97[0].text)
os.rename(oldname95,newname95)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -136
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url98= 'https://insights.blackcoffer.com/why-is-there-a-severe-immunological-and-inflammatory-explosion-in-those-affected-by-sarms-covid-19/'




newfile96= open('old96.txt','w')
newname96= "URLID-136.txt"
oldname96= "old96.txt"

page98= requests.get(url98)

html98= BeautifulSoup(page98.content,'html.parser')




title98= html98.findAll(attrs={'class':'entry-title'})


print(title98[16].text)


newfile96.write(title98[16].text + "\n")
t = title98[16].text


content98= html98.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content98[0].text

print(content98[0].text)
newfile96.write(content98[0].text)
os.rename(oldname96,newname96)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -137
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url99= 'https://insights.blackcoffer.com/what-do-you-think-is-the-lesson-or-lessons-to-be-learned-with-covid-19/'




newfile97= open('old97.txt','w')
newname97= "URLID-137.txt"
oldname97= "old97.txt"

page99= requests.get(url99)

html99= BeautifulSoup(page99.content,'html.parser')




title99= html99.findAll(attrs={'class':'entry-title'})


print(title99[16].text)


newfile97.write(title99[16].text + "\n")

t = title99[16].text

content99= html99.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content99[0].text

print(content99[0].text)
newfile97.write(content99[0].text)
os.rename(oldname97,newname97)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -138
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url100= 'https://insights.blackcoffer.com/coronavirus-the-unexpected-challenge-for-the-european-union/'




newfile98= open('old98.txt','w')
newname98= "URLID-138.txt"
oldname98= "old98.txt"

page100= requests.get(url100)

html100= BeautifulSoup(page100.content,'html.parser')




title100= html100.findAll(attrs={'class':'entry-title'})


print(title100[16].text)


newfile98.write(title100[16].text + "\n")

t = title100[16].text

content100= html100.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content100[0].text

print(content100[0].text)
newfile98.write(content100[0].text)
os.rename(oldname98,newname98)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -139
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url101= 'https://insights.blackcoffer.com/industrial-revolution-4-0-pros-and-cons/'




newfile99= open('old99.txt','w')
newname99= "URLID-139.txt"
oldname99= "old99.txt"

page101= requests.get(url101)

html101= BeautifulSoup(page101.content,'html.parser')




title101= html101.findAll(attrs={'class':'entry-title'})


print(title101[16].text)


newfile99.write(title101[16].text + "\n")

t = title101[16].text

content101= html101.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content101[0].text

print(content101[0].text)
newfile99.write(content101[0].text)
os.rename(oldname99,newname99)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -140
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url102= 'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy/'




newfile100= open('old100.txt','w')
newname100= "URLID-140.txt"
oldname100= "old100.txt"

page102= requests.get(url102)

html102= BeautifulSoup(page102.content,'html.parser')




title102= html102.findAll(attrs={'class':'entry-title'})


print(title102[16].text)


newfile100.write(title102[16].text + "\n")
t = title102[16].text


content102= html102.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content102[0].text

print(content102[0].text)
newfile100.write(content102[0].text)
os.rename(oldname100,newname100)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -141
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url103= 'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-indian-economy-2/'




newfile101= open('old101.txt','w')
newname101= "URLID-141.txt"
oldname101= "old101.txt"

page103= requests.get(url103)

html103= BeautifulSoup(page103.content,'html.parser')




title103= html103.findAll(attrs={'class':'entry-title'})


print(title103[16].text)


newfile101.write(title103[16].text + "\n")

t = title103[16].text

content103= html103.findAll(attrs={'class':'td-post-content tagdiv-type'}) 

m = content103[0].text
print(content103[0].text)
newfile101.write(content103[0].text)
os.rename(oldname101,newname101)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''


'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -142
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url104= 'https://insights.blackcoffer.com/impact-of-covid-19coronavirus-on-the-indian-economy/'




newfile102= open('old102.txt','w')
newname102= "URLID-142.txt"
oldname102= "old102.txt"

page104= requests.get(url104)

html104= BeautifulSoup(page104.content,'html.parser')




title104= html104.findAll(attrs={'class':'entry-title'})


print(title104[16].text)


newfile102.write(title104[16].text + "\n")
t = title104[16].text


content104= html104.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content104[0].text

print(content104[0].text)
newfile102.write(content104[0].text)
os.rename(oldname102,newname102)  


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -143
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url105= 'https://insights.blackcoffer.com/impact-of-covid-19-coronavirus-on-the-global-economy/'




newfile103= open('old103.txt','w')
newname103= "URLID-143.txt"
oldname103= "old103.txt"

page105= requests.get(url105)

html105= BeautifulSoup(page105.content,'html.parser')




title105= html105.findAll(attrs={'class':'entry-title'})


print(title105[16].text)


newfile103.write(title105[16].text + "\n")

t = title105[16].text

content105= html105.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content105[0].text

print(content105[0].text)
newfile103.write(content105[0].text)
os.rename(oldname103,newname103)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -145
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url106= 'https://insights.blackcoffer.com/blockchain-in-fintech/'




newfile104= open('old104.txt','w')
newname104= "URLID-145.txt"
oldname104= "old104.txt"

page106= requests.get(url106)

html106= BeautifulSoup(page106.content,'html.parser')




title106= html106.findAll(attrs={'class':'entry-title'})


print(title106[16].text)


newfile104.write(title106[16].text + "\n")

t = title106[16].text

content106= html106.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content106[0].text

print(content106[0].text)
newfile104.write(content106[0].text)
os.rename(oldname104,newname104)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''



#Extracting data for URLID -146
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url107= 'https://insights.blackcoffer.com/blockchain-for-payments/'




newfile105= open('old105.txt','w')
newname105= "URLID-146.txt"
oldname105= "old105.txt"

page107= requests.get(url107)

html107= BeautifulSoup(page107.content,'html.parser')




title107= html107.findAll(attrs={'class':'entry-title'})


print(title107[16].text)
t = title107[16].text

newfile105.write(title107[16].text + "\n")



content107= html107.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content107[0].text

print(content107[0].text)
newfile105.write(content107[0].text)
os.rename(oldname105,newname105)   


#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -147
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url108= 'https://insights.blackcoffer.com/the-future-of-investing/'




newfile106= open('old106.txt','w')
newname106= "URLID-147.txt"
oldname106= "old106.txt"

page108= requests.get(url108)

html108= BeautifulSoup(page108.content,'html.parser')




title108= html108.findAll(attrs={'class':'entry-title'})


print(title108[16].text)


newfile106.write(title108[16].text + "\n")

t = title108[16].text

content108= html108.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content108[0].text

print(content108[0].text)
newfile106.write(content108[0].text)
os.rename(oldname106,newname106)  

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -148
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url109= 'https://insights.blackcoffer.com/big-data-analytics-in-healthcare/'




newfile107= open('old107.txt','w')
newname107= "URLID-148.txt"
oldname107= "old107.txt"

page109= requests.get(url109)

html109= BeautifulSoup(page109.content,'html.parser')




title109= html109.findAll(attrs={'class':'entry-title'})


print(title109[16].text)
t = title109[16].text

newfile107.write(title109[16].text + "\n")



content109= html109.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content109[0].text

print(content109[0].text)
newfile107.write(content109[0].text)
os.rename(oldname107,newname107)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)

'''

'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -149
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url110= 'https://insights.blackcoffer.com/business-analytics-in-the-healthcare-industry/'




newfile108= open('old108.txt','w')
newname108= "URLID-149.txt"
oldname108= "old108.txt"

page110= requests.get(url110)

html110= BeautifulSoup(page110.content,'html.parser')




title110= html110.findAll(attrs={'class':'entry-title'})


print(title110[16].text)

t = title110[16].text
newfile108.write(title110[16].text + "\n")



content110= html110.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content110[0].text

print(content110[0].text)
newfile108.write(content110[0].text)
os.rename(oldname108,newname108)   

#----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)


'''
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''


#Extracting data for URLID -150
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
'''
url111= 'https://insights.blackcoffer.com/challenges-and-opportunities-of-big-data-in-healthcare/'




newfile109= open('old109.txt','w')
newname109= "URLID-150.txt"
oldname109= "old109.txt"

page111= requests.get(url111) 

html111= BeautifulSoup(page111.content,'html.parser')




title111= html111.findAll(attrs={'class':'entry-title'})


print(title111[16].text)


newfile109.write(title111[16].text + "\n")

t = title111[16].text

content111= html111.findAll(attrs={'class':'td-post-content tagdiv-type'}) 
m = content111[0].text

print(content111[0].text)
newfile109.write(content111[0].text)
os.rename(oldname109,newname109)  

 #----------CREATING A FILTERED LISTS-----------#

content = t+ m

words = word_tokenize(content)
sentences = sent_tokenize(content)

filtered_list = [ ]

filtered_list = [w for w in words if w not in stop_words]

filtered_sentence = " ".join(filtered_list)


#print(sentences)
#print(len(sentences))
#print(wordsofall)

#----------CALCULATING POSITIVE SCORE----------#

positive_score=0

for w in filtered_list:
	if w in positive_list:
		positive_score+=1
	else:
		continue

print("1. positivity score: ",positive_score)

#---------CALCULATING NEGATIVE SCORE-----------#

negative_score =0	

for w in filtered_list:
	if w in negative_list:
		negative_score-=1
	else:
		continue

print("2. negativity score: ",negative_score)

#---------CALCULATING POLARITY SCORE-----------#

polarity_score = (positive_score - negative_score)//((positive_score + negative_score)+0.000001)

print("3. polarity score: ",polarity_score)

#------CALCULATING SUBJECTIVITY SCORE--------#

subjectivity_score = (positive_score + negative_score)//((len(filtered_list))+0.000001)

print("4. subjectivity score: ",subjectivity_score)

#-------------ANALYSIS OF READABILITY----------------#

result = readability.getmeasures(content,lang='en')
print(result)

#--------CALCULATING WORDS/SENTENCE---------#

wps = len(words)//len(sentences)
print("5. Avg words per sentences :", wps)


#--------CALCULATING COMPLEX WORDS---------#


count = 0

for word in words:
    d = {}.fromkeys('aeiou',0)
    haslotsvowels = False
    for x in word.lower():
        if x in d:
            d[x] += 1
    for q in d.values():
        if q > 2:
            haslotsvowels = True
    if haslotsvowels:
        count += 1
        
print("6. The number of complex words are: ",count)


#-----------CALCULATING WORDS COUNT------------#
string.punctuation
sentence_new = filtered_sentence
#print("\n \n content with punc  :  \n", sentence_new)
for char in sentence_new:
	if char in string.punctuation:
		sentence_new = sentence_new.replace(char,' ')


#print("\n \n content without punc  :  \n", sentence_new)

tokenized_sent = word_tokenize(sentence_new)
print("7. The words count is : ", len(tokenized_sent))

#-----Extracting Number of syllables per word----#

def syllable_count(word):
    word = word.lower()
    count = 0
    vowels = "aeiou"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("es") and word.endswith("ed"):
        count -= 1
    if count == 0:
        count += 1
    return count
output_list = list(map(syllable_count, words))
  
Num = sum(output_list)
av_sy_pw = Num//len(words)
print("8. avg syllables per word is ",av_sy_pw)


#-----Extracting Number of Personal Pronouns----#

pronounRegex = re.compile(r'\b(I|we|my|ours|(?-i:us))\b',re.I)
x = pronounRegex.findall(content)
print("9. The personal Pronoun count is: ", len(x))

sent = content.split('.')
wordd = content.split(' ')
#print(sent)
#print(wordd)
#print(len(sent))
#print(len(wordd))


#-------CALCULATING AVG WORD LENGTH--------#

wordss = content.split()
average = sum(len(word) for word in wordss)//len(wordss)
print("10. avg word length: ",average)
  
   '''
     
'''-------------------------------------------------------------------------------------------------------------------------------------------------------------------'''
