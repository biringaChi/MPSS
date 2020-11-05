from typing import List
import pandas as pd

class ProcessData:
	"""Processes data from dataset file"""
	def __init__(self) -> None:
		# Figure out a way to walk up directory without absolutely specifying path
		self.path = "/Users/Gabriel/Documents/research/experimentaion/dataset_creator/dataset.csv"
		
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}(self.path)"
	
	def __len__(self, value):
		return len(value)

	def process(self) -> List[int]:
		dataset = pd.read_csv(self.path)
		return [file for file in dataset["sourcecode"]]
	
	def get_character_frequency(self) -> List[int]:
		return [len(file) for file in self.process()]
	
