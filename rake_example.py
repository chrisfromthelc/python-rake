from __future__ import absolute_import
from __future__ import print_function
import six

import rake
import operator
import io
import csv
import os

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
rake_object = rake.Rake(stoppath, 4, 4, 3)

# 2. run on RAKE on a given text
sample_file = io.open("blogposts.txt", 'r',encoding="iso-8859-1")
text = sample_file.read().encode('utf-8')
keywords = rake_object.run(text)

# 3. Print results to screen
print("Keywords:", keywords)

print("----------")

# 4. Print results to CSV

def WriteListToCSV(csv_file,csv_columns,data_list):
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(csv_columns)
            for data in data_list:
                writer.writerow(data)
    except IOError as (errno, strerror):
            print("I/O error({0}): {1}".format(errno, strerror))
    return

csv_columns = ['Keyword','Score']
# Line 144 of rake.py rounds the score to 5 decimal places: word_score[item] = round(word_prescore, 5)
currentPath = os.getcwd()
csv_file = os.path.join("output","keywords.csv")

WriteListToCSV(csv_file,csv_columns,keywords)

#### More examples ####

# Split text into sentences
sentenceList = rake.split_sentences(text)

# Outputs detected sentences to screen
# for sentence in sentenceList:
#     print("Sentence:", sentence)

## Outputs detected phrases, candidates, and top 1/3rd scoring keywords to screen.

# generate candidate keywords
print(" ")
print("----------")
print("Phrases")
print("----------")
stopwordpattern = rake.build_stop_word_regex(stoppath)
phraseList = rake.generate_candidate_keywords(sentenceList, stopwordpattern)
for phrase in phraseList:
    # print("Phrases:", phraseList)
    print("Phrases: ", phrase)

# calculate individual word scores
wordscores = rake.calculate_word_scores(phraseList)

# generate candidate keyword scores
print(" ")
print("----------")
print("Candidates")
print("----------")
keywordcandidates = rake.generate_candidate_keyword_scores(phraseList, wordscores)
for candidate in keywordcandidates.keys():
    print("Candidate: ", candidate, ", score: ", keywordcandidates.get(candidate))

# sort candidates by score to determine top-scoring keywords
sortedKeywords = sorted(six.iteritems(keywordcandidates), key=operator.itemgetter(1), reverse=True)
totalKeywords = len(sortedKeywords)

# for example, you could just take the top third as the final keywords
print(" ")
print("----------")
print("Top Third")
print("----------")
for keyword in sortedKeywords[0:int(totalKeywords / 10)]:
    print("Keyword: ", keyword[0], "   Score: ", keyword[1])
