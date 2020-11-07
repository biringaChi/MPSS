import os
import sys
import pandas as pd
from typing import List

class ProcessData:
	"""Processes data from dataset file"""
	def __init__(self) -> None:
		pass
	
	def __repr__(self) -> str:
		return f"{self.__class__.__name__}(self.path)"
	
	def __len__(self, value):
		return len(value)

	@property
	def _get_data_path(self) -> str:
		walk_up = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
		subfolders = [subs.path for subs in os.scandir(walk_up) if subs.is_dir()]
		data_file_path = os.path.join([subs.path for subs in os.scandir(walk_up) if subs.is_dir()][-1], os.listdir(subfolders[-1])[-1])
		return data_file_path

	@property
	def sourcecode(self) -> List[int]:
		dataset = pd.read_csv(self._get_data_path)
		return [file for file in dataset["sourcecode"]]
	
	@property
	def get_character_frequency(self) -> List[int]:
		return [len(file) for file in self.sourcecode]