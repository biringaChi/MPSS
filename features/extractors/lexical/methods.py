from utils import methods_pattern
from  process_data import ProcessData
from typing import List
from math import floor, log10
import re 

class MethodsExtractor(ProcessData):
	"""Extracts frequency of methods"""
	def __init__(self) -> None:
		super().__init__()
		self.methods_pattern = methods_pattern

	def __repr__(self) -> str:
		return f"Class: {self.__class__.__name__}"
	
	def __str__(self) -> str:
		return f"Methods Regex: {self.methods_pattern}"
	
	def get_methods_frequency(self) -> List[int]:
		methods_frequency = []
		for file in self.process():
			temp = re.findall(methods_pattern, file)
			methods_frequency.append(self.__len__(temp))
		return methods_frequency

	def extract_methods(self) -> List[int]:
		methods_features = []
		for cf, mf in zip(self.get_character_frequency(), self.get_methods_frequency()):
			try:
				methods_features.append(floor(log10(cf / mf)))
			except ZeroDivisionError:
				methods_features.append(0)
		return methods_features


if __name__ == "__main__":
	MethodsExtractor().extract_methods()