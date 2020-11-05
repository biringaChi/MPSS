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
		dataset = pd.read_csv(f"{self.path}/dataset.csv")
		return [file for file in dataset["sourcecode"]]

	def get_character_frequency(self) -> List[int]:
		return [len(file) for file in self.process_data()]
	
	def get_keyword_frequency(self) -> List[int]:
		keyword_frequency = []
		for file in self.process_data():
			temp = [word for word in file.split() if word in self.java_keywords]
			keyword_frequency.append(len(temp))
		return keyword_frequency
	
	def extract_keywords(self) -> List[int]:
		lexical_features = []
		for cf, kf in zip(self.get_character_frequency(), self.get_keyword_frequency()):
			lexical_features.append(floor(log(cf / kf)))
		return lexical_features


class TernaryExtractor:
	""""Extracts frequency of ternary operators"""
	pass


if __name__ == "__main__":
	path = "/Users/Gabriel/Documents/research/experimentaion/dataset_creator"
	le = KeywordExtractor(path)
	print(le.extract_keywords()) 
