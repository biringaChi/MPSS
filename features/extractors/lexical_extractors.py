import os
import sys
import pandas as pd
import utils

print(utils.java_keywords)


class LexicalExtractor:
	"""Extracts lexical features"""
	def __init__(self, path, java_keywords):
		self.path = path
		self.java_keywords = None # from import

	def process_data(self) -> list[str]:
		# Reads in our dataset and extracts sourcecode column
		dataset = pd.read_csv("dataset.csv")
		source_code = [file for file in dataset["sourcecode"]]
		return source_code


	def character_count(self) -> int:
		# counts the number of characters in a source code
		character_count = [len(file) for file in self.process_data()]
		return character_count
	
	def keyword_featues(self) -> int:
		# counts the number of characters in a file
		pass
	
	def extract(self) -> int:
		pass


if __name__ == "__main__":
	pass
