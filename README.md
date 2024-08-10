# spellChecker

Simple statistical spellChecker function capable of scaling well on local corpus of words

## Description

spellChecker generates all possible candidates for a given word, sorted by probability of word in given corpus. we generates possible candidates using edit distance 1 and 2, it can be easily extended for higher order edits / mistakes. 

## Getting Started

### Executing program

* run example.ipynb notebook 

```
from scripts import SpellCheck

SpellCheck.correction("franch fryes")

```

## Acknowledgments

* [Using the Web for Language Independent Spellchecking and Autocorrection](https://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/36180.pdf)