# CLEANING TEXT
# 1) Create a text file and take text from it.
# 2) Covert the letters into lowercase.
# 3) Remove punctuation marks from the text.
# 4) Creating array from given sentencs.
# 5) Removing stop words: words that do not have any emotional meaning ex. Am, go, of, etc..

#Note: In str.maketrans(), the parameters are:-
# str1: specifies the list of charaters that need to be replaced.
# str2: specifies the list of characters with which the characters to be replaced.
# str3: specifies the list of characters that needed to be deleted(independent if str1 and str2)
# str.punction() shows the list of punctuations present in python

import string

from collections import Counter

text = open('text.txt', encoding='utf-8').read()                                #1
lower_case = text.lower()                                                       #2
clean_text = lower_case.translate(str.maketrans('','',string.punctuation))      #3
tokenised = clean_text.split()                                                  #4


stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now", "going", "sitting", "saw", "walking", 
              "pass", "crossing","file", "read", "hello", "hi", "hey","hii", "feel"]                                                

#5
#To filter the stop words from tokenised sentence
final_words = []
for word in tokenised:
    if word not in stop_words:
        final_words.append(word)

#First we split emotion list into two parts i.e. word associated with emotion and the emotion itself
#Then we find the word in our tokenised final-list and match it with the corresponding emotions.
emotion_list =[]
with open('emotions.txt','r') as file:
    for line in file:
        clear_line = line.replace("\n","").replace("'", "").replace(",","").replace(" ","").strip()
        try:
            [word, emotion] = clear_line.split(':')
        except:
            pass
        if word in final_words:
            emotion_list.append(emotion)

#Counting the number of emotions.
w = Counter(emotion_list)
#print(w)

#Coverting the above dictionary into list and printing the dominant emotion which will be at index 0.
result_list = list(w.items())
final = result_list[0]
#print(final)
final_word, final_emotion = final
print(final_word)
