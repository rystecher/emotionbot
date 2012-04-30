##
## Sentiment analysis tool
## Benjamin Gleitzman (gleitz@mit.edu)
##
import sys
import word_bag

def create_dictionary():
    dictionary = {}
    f = open('AFINN.txt', 'r')
    for line in f.readlines():
        value_splitter = line.split("\t")
        dictionary[value_splitter[0]] = int(value_splitter[1].strip())
        # Part 1: Create the dictionary from the AFINN.txt file
        # A tab character in Python is '\t'
        # YOUR CODE HERE
    j = open('MiscEmotions.txt', 'r')
    for line in j.readlines():
        value_splitter = line.split("\t")
        dictionary[value_splitter[0]] = int(value_splitter[1].strip())
    for word in word_bag.positive:
         value_splitter = line.split("\t")
         dictionary[value_splitter[0]] = 1
    for word in word_bag.negative:
         value_splitter = line.split("\t")
         dictionary[value_splitter[0]] = -1
    return dictionary

USER_INPUT = ""
MY_DICTIONARY = create_dictionary()

def split_into_words(sentence):
    input_list = sentence.split(" ")
    # Part 2: Split a sentence of words into individual words
    # The split() function might be helpful
    # YOUR CODE HERE
    return input_list

def score(word):
    if word in MY_DICTIONARY:
        word_score = MY_DICTIONARY[word]
    else:
        word_score= 0
    # Part 3: Given a word, return its score
    # Hint: use MY_DICTIONARY
    # YOUR CODE HERE
    return word_score

def score_words(words):
    total_score = 0
    for word in words:
        total_score += score(word)
        # Part 4: For each word, add it's score to the total score
        # YOUR CODE HERE
    return total_score

def analyze_sentiment(sentence):
    words = split_into_words(sentence)
    score = score_words(words)
    print "Score is", score
    if score >= 5:
        return "Trippin on happy pills"
    elif score == 4:
        return "Life for you is nothing but unicorns and butterflies"
    elif score == 3:
        return "You are living the dream life"
    elif score == 2:
        return "Everything is chill"
    elif score == 1:
        return "Uhh life is good... I guess"
    elif score == 0:
        return "Meh."
    elif score == -1:
        return "Today's bad but tomorrow might be better"
    elif score == -2:
        return "If I were an animal I'd be a ferret. Cause no one likes ferrets"
    elif score == -3:
        return "I wish I was emo, cause at least those guys have each other"
    elif score == -4:
        return "I like playing tic-tac-toe on my wrists. With a knife"
    elif score == -5:
        return "F**k this sh*t, I'm going back to sleep"
    elif score < -5:
        return "On a good day, only most of your hopes and dreams are crushed into a fine powder"
    # Part 5: Based on the total score, determine if the sentence is positive or negative
    # YOUR CODE HERE

