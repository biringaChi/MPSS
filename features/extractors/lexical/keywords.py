import argparse
import pandas as pd
import utils as ut
from  process_data import ProcessData
from typing import List
from math import floor, log

# usage: keywords.py [-h] [-p PATH]

parser = argparse.ArgumentParser(description = "Creates keywords features")
parser.add_argument("-p", "--path", help = "Dataset path")
args = parser.parse_args()


class KeywordExtractor:
	"""Extracts frequency of keywords"""
	def __init__(self, path) -> None:
		self.java_keywords = ut.java_keywords
		self.prd = ProcessData(path)
	
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}(self.path)"

	def get_character_frequency(self) -> List[int]:
		return [len(file) for file in self.prd.process()]
	
	def get_keyword_frequency(self) -> List[int]:
		keyword_frequency = []
		for file in self.prd.process():
			temp = [word for word in file.split() if word in self.java_keywords]
			keyword_frequency.append(len(temp))
		return keyword_frequency
	
	def extract_keywords(self) -> List[int]:
		lexical_features = []
		for cf, kf in zip(self.get_character_frequency(), self.get_keyword_frequency()):
			lexical_features.append(floor(log(cf / kf)))
		return lexical_features


if __name__ == "__main__":
	le = KeywordExtractor(args.path)
	le.extract_keywords()