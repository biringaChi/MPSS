import csv
import pandas as pd
import _specify_dir
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

	def get_build(self) -> List[float]:
		data = pd.read_csv(self._get_dir)
		return [build for build in data.iloc[:, 3]]
	
	def get_test(self) -> List[float]:
		data = pd.read_csv(self._get_dir)
		return [test for test in data.iloc[:, 4]]
	
	def feature_extractors(self) -> Dict:
		return {
			"EmptyLines" : EmptyLinesExtractor().extract_emptylines(), 
			"Space" : SpaceTabsExtractor().extract_space(),
			"Tabs" : SpaceTabsExtractor().extract_tabs(),
			"MeanCodelines" : CodeLinesExtractor().extract_mean_codelines(),
			"SDCodelines" : CodeLinesExtractor().extract_sd_codelines(),
			"ImportStmts" : CodeLinesExtractor().extract_import_statements(),
			"Comments" : CommentsExtractor().extract_comments(),
			"Keywords" : KeywordExtractor().extract_keywords(),
			"Methods": MethodsExtractor().extract_methods(),
			"Build(sec)" : self.get_build(),
			"Test(sec)" : self.get_test(),
			"Conditionals" : "",
			"Literals" : "",
			"Loops" : "",
			"Nodes" : ""
			}

	def build_dataset(self) -> None:
		try:
			with open(self.file_path, "w") as file:
				with file:
					write = csv.writer(file)
					write.writerows(self.feature_extractors().values())
		except OSError as e:
			raise e
	
	def transpose_dataset_rename_columns(self) -> None:
		data = pd.read_csv(self.FILE_PATH)
		data = data.T.reset_index()
		column_names = list(self.feature_extractors().keys())
		data.rename(columns = {"index" : column_names[0], 0 : column_names[1], 1 : column_names[2], 
									2 : column_names[3], 3 : column_names[4], 4 : column_names[5],
                                    5 : column_names[6], 6 : column_names[7], 7 : column_names[8], 
                                    8 : column_names[9], 9 : column_names[10], 10 : column_names[11],
									11 : column_names[12], 12 : column_names[13], 13 : column_names[14]}, inplace = True)
		return data