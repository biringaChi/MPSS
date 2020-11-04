import os
import sys
from typing import List
import pandas as pd
import utils as ut
from math import floor, log


class KeywordExtractor:
	"""Extracts frequency of keywords"""
	def __init__(self, path):
		self.path = path
		self.java_keywords = ut.java_keywords

	def process_data(self) -> List[int]:
		# Reads in our dataset and extracts sourcecode column
		dataset = pd.read_csv(f"{self.path}/dataset.csv")
		source_code = [file for file in dataset["sourcecode"]]
		return source_code

	def get_character_frequency(self) -> List[int]:
		# gets the frequency of characters
		character_frequency = [len(file) for file in self.process_data()]
		return character_frequency
	
	def get_keyword_frequency(self) -> List[int]:
		# gets the frequency of keywords
		keyword_frequency = []
		for file in self.process_data():
			temp = [word for word in file.split() if word in self.java_keywords]
			keyword_frequency.append(len(temp))
		return keyword_frequency
	
	def extract_keywords(self) -> List[int]:
		# extract keyword features
		lexical_features = []
		for cf, kf in zip(self.get_character_frequency(), self.get_keyword_frequency()):
			lexical_features.append(floor(log(cf / kf)))
		return lexical_features


if __name__ == "__main__":
	path = "/Users/Gabriel/Documents/research/experimentaion/dataset_creator"
	le = KeywordExtractor(path)
	print(le.extract_keywords()) 
