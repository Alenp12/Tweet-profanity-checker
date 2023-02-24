# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j9BVEIY3HTsgiLAAb7Z39WSugEis_h8B
"""

import re

# Set of racial slurs
racial_slurs = {'slur1','slur2','slur3','slur4','slur5','slur6','slur7','slur8','slur9','slur10','slur11'}



def get_degree_of_profanity(tweet):

  """
    Calculates the degree of profanity for a given tweet based on a set of racial slurs.
    
    Parameters:
        tweet (str): The tweet to analyze.
        
    Returns:
        int: The degree of profanity, which is the number of racial slurs found in the tweet.
    """

# Count the number of racial slurs in the tweet
  count = 0

  for word in racial_slurs :
    if re.search(r'\b{}\b'.format(word),tweet,re.IGNORECASE):
      count += 1

  return count


# Reads tweet from the text file

with open('tweets1.txt', 'r') as f :
  tweets = f.readlines()


# Calculate the degree of profanity of each tweet and print the resluts

# loop through each tweet
for  tweet in tweets :

  # Remove whitespace from the beginning and end of the tweet
  tweet = tweet.strip()
  
  profanity_degree = get_degree_of_profanity(tweet)

  print(f'Tweet: {tweet} | Degree of Profanity: {profanity_degree}')