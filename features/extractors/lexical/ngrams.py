import os
import sys
import _specify_dir
from features.extractors.process_data import ProcessData
from typing import List
from math import floor, log10
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize  

class NgramExtractor(ProcessData):
	"""Extracts frequency of comments"""
	def __init__(self, n) -> None:
		super().__init__()
		self.unigram = 1

	def __repr__(self) -> str:
		return f"Class: {self.__class__.__name__}"
	
	def extract_ngrams(self) -> List[str]:
		ngram_files = []
		for file in self.sourcecode:
			n_grams = ngrams(word_tokenize(file), self.unigram)
			ngram_files.append([''.join(grams) for grams in n_grams])
		return ngram_files

if __name__ == "__main__":
	NgramExtractor.extract_ngrams()
