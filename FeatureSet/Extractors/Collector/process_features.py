import csv
import _specify_dir
import pandas as pd
from typing import Dict, List
from FeatureSet.Extractors.data_prep import DataPrep
from FeatureSet.Extractors.Layout.emptylines import EmptyLinesExtractor
from FeatureSet.Extractors.Layout.spacetabs import SpaceTabsExtractor
from FeatureSet.Extractors.Lexical.codelines import CodeLinesExtractor
from FeatureSet.Extractors.Lexical.comments import CommentsExtractor
from FeatureSet.Extractors.Lexical.keywords import KeywordExtractor
from FeatureSet.Extractors.Lexical.methods import MethodsExtractor


class ProcessFeatures(DataPrep):
	""" Collects feature extractors and builds dataset """
	
	def __init__(self) -> None:
		super().__init__()
		self.FILE_PATH = "/Users/Gabriel/Documents/Research/Experimentation/ML/Models/processed_data.csv"
		self.COLUMNS = ["Tabs", "EmptyLines", "Space", "MeanCodelines", 
		"SDCodelines", "ImportStmts", "Comments", "Keywords", "Methods", 
		"Build(sec)", "Test(sec)", "Conditionals", "Literals", "Loops", "Nodes"]

	def get_build(self) -> List[float]:
		data = pd.read_csv(self._GET_DIR)
		return [build for build in data.iloc[:, 3]]
	
	def get_test(self) -> List[float]:
		data = pd.read_csv(self._GET_DIR)
		return [test for test in data.iloc[:, 4]]
	
	def feature_extractors(self) -> Dict:
		return [SpaceTabsExtractor().extract_tabs(),
			EmptyLinesExtractor().extract_emptylines(), 
			SpaceTabsExtractor().extract_space(),
			CodeLinesExtractor().extract_mean_codelines(),
			CodeLinesExtractor().extract_sd_codelines(),
			CodeLinesExtractor().extract_import_statements(),
			CommentsExtractor().extract_comments(),
			KeywordExtractor().extract_keywords(),
			MethodsExtractor().extract_methods(),
			self.get_build(),
			self.get_test(),
			]

	def build_dataset(self) -> None:
		try:
			with open(self.FILE_PATH, "w") as file:
				with file:
					write = csv.writer(file)
					write.writerows(self.feature_extractors())
		except OSError as e:
			raise e
	
	def transpose_dataset_rename_columns(self) -> None:
		data = pd.read_csv(self.FILE_PATH)
		data = data.T.reset_index()
		data.rename(columns = {"index" : self.COLUMNS[0], 0 : self.COLUMNS[1], 1 : self.COLUMNS[2], 2 : self.COLUMNS[3], 
		3 : self.COLUMNS[4], 
		4 : self.COLUMNS[5],
		5 : self.COLUMNS[6], 
		6 : self.COLUMNS[7], 
		7 : self.COLUMNS[8], 
		8 : self.COLUMNS[9], 
		9 : self.COLUMNS[10], 
		10 : self.COLUMNS[11], 
		11 : self.COLUMNS[12], 
		12 : self.COLUMNS[13], 
		13 : self.COLUMNS[14]}, inplace = True)
		data.drop("Tabs", axis = 1, inplace = True)
		return data
