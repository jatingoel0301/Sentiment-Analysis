import nltk
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

sentiment_dictionary={}
for line in open('C:\\Users\\Jatin\\Desktop\\Sentiment Analysis\\Term Weights.txt'):
    word, score = line.split('\t')
    sentiment_dictionary[word] = int(score)
#forming the sentiment dictionary is complete

directory="C:\\Users\\Jatin\\Desktop\\Sentiment Analysis\\Test"
doc=PlaintextCorpusReader(directory,'.*')
#reading the corpus

sentwise_dict=dict()
def ScoreReview(text):
 rawText=doc.raw(text+'.txt')
 sentence=sent_tokenize(rawText)
 #print(sentence)
 sentiment_arr=[]
 for s in sentence:
  words=word_tokenize(s)
  sent_score=sum(sentiment_dictionary.get(word,0)for word in words)
  #print(sent_score)
  sentiment_arr.append(sent_score)
  sentwise_dict.setdefault(sent_score, [])
  sentwise_dict[sent_score].append(s)
 total_score=sum(sentiment_arr)
 if(total_score<=-3):
  print('The review of '+text+' is majorly negative with a score of '+str(total_score)+'. Major Improvement is required.')
 elif(total_score>-3 and total_score<0):
  print('The review of '+text+' is minorly negative with a score of '+str(total_score)+'. Minor Improvement is required.')
 elif(total_score==0):
  print('The review of '+text+' is '+str(total_score)+'. No definitive sentiment.')
 elif(total_score>0 and total_score<3):
  print('The review of '+text+' is minorly positive with a score of '+str(total_score)+'. Minor Improvement is can be done.')
 elif(total_score>=3):
  print('The review of '+text+' is majorly positive with a score of '+str(total_score)+'. Not immediate need for improvement.')


ScoreReview('Plasma TV')

def DispNeg():
    i=1
    for key in sentwise_dict:
     if(key<0):
       for w in sentwise_dict[key]:
        print('Negative sentence '+str(i)+': '+w)
        i=i+1

def DispPos():
    i=1
    for key in sentwise_dict:
     if(key>0):
       for w in sentwise_dict[key]:
        print('Positive sentence '+str(i)+': '+w)
        i=i+1

def DispNeu():
    i=1
    for key in sentwise_dict:
     if(key==0):
       for w in sentwise_dict[key]:
        print('Neutral sentence '+str(i)+': '+w)
        i=i+1


#print(sentwise_dict)
DispNeg()
DispPos()
DispNeu()
