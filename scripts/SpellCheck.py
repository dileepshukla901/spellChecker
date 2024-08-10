# -*- coding: utf-8 -*-

#---------------------------------------------- Importing required liberaries -------------------------------------#
import re
from collections import Counter
import glob

#----------------------------------------------- reading word corpus --------------------------------------------------#
name_file = ''
for in_file in glob.glob('assets/word_corpus/word_corpus_*.txt'):
    text_file = open(in_file, 'r', encoding='UTF-8').read()
    name_file += text_file

#--------------------------------------------------- function defination ---------------------------------#

def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(name_file))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    wordList = re.sub(r"[^\w]", " ",  word).split()
    return_list = []
    for word_ in wordList:
        return_list.append(max(candidates(word_), key=P))
    return_list = ' '.join(item for item in return_list)
    return return_list

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


