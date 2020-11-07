import os
import sys
import pandas as pd
from typing import List

class ProcessData:
	"""Processes data from dataset file"""
	def __init__(self) -> None: pass

	def __repr__(self) -> str: return f"{self.__class__.__name__}"
	
	def __len__(self, value) -> int: return len(value)

	@property
	def _get_data_path(self) -> str:
		_walk_up = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
		_subfolders = [subs.path for subs in os.scandir(_walk_up) if subs.is_dir()]
		return os.path.join([subs.path for subs in os.scandir(_walk_up) if subs.is_dir()][-1], os.listdir(_subfolders[-1])[-1])

	@property
	def get_sourcecode(self) -> List[int]:
		data = pd.read_csv(self._get_data_path)
		return [file for file in data.iloc[:, 2]]
	
	@property
	def get_character_frequency(self) -> List[int]:
		return [len(file) for file in self.get_sourcecode]
