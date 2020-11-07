import os
import sys
import _specify_dir
import re 
from features.extractors.utils import comments_pattern
from features.extractors.process_data import ProcessData
from typing import List
from math import floor, log10


class CommentsExtractor(ProcessData):
	"""Extracts frequency of comments"""
	def __init__(self) -> None:
		super().__init__()
		self.comments_pattern = comments_pattern

	def __repr__(self) -> str:
		return f"Class: {self.__class__.__name__}"
	
	def __str__(self) -> str:
		return f"Comments Regex: {self.comments_pattern}"
	
	@property
	def get_comments_frequency(self) -> List[int]:
		comments_frequency = []
		for file in self.get_sourcecode:
			temp = re.findall(comments_pattern, file)
			comments_frequency.append(self.__len__(temp))
		return comments_frequency

	def extract_comments(self) -> List[int]:
		comments_features = []
		for cf, cmf in zip(self.get_character_frequency, self.get_comments_frequency):
			try:
				comments_features.append(floor(log10(cf / cmf)))
			except ZeroDivisionError:
				comments_features.append(0)
		return comments_features


if __name__ == "__main__":
	CommentsExtractor().extract_comments()