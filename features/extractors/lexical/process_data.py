from typing import List
import pandas as pd

class ProcessData:
	"""Processes data from dataset file"""
	def __init__(self, path) -> None:
		self.path = path
		
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}(self.path)"

	def process(self) -> List[int]:
		dataset = pd.read_csv(f"{self.path}/dataset.csv")
		return [file for file in dataset["sourcecode"]]