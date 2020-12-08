import _specify_dir
from FeatureSet.Extractors.Collector.process_features import ProcessFeatures
import numpy as np
from typing import Dict, List, Tuple
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import SGDRegressor
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


class HandleData(ProcessFeatures):
	def __init__(self) -> None:
		super().__init__()

	def train_test_method(self) -> Tuple:
		X = self.transpose_dataset_rename_columns().drop("Test(sec)", axis = 1)
		y = self.transpose_dataset_rename_columns()["Test(sec)"]
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)
		return X_train, X_test, y_train, y_test
	
	def cross_val_method(self) -> Tuple:
		X = self.transpose_dataset_rename_columns().drop("Test(sec)", axis = 1)
		y = self.transpose_dataset_rename_columns()["Test(sec)"]
		return X, y


class RegressionModels(HandleData):
	def __init__(self) -> Dict:
		super().__init__()
		self.MODELS =[LinearRegression(), 
		make_pipeline(StandardScaler(), SGDRegressor(max_iter = 1000, tol = 1e-3)), 
		Ridge(alpha = 1, solver = "cholesky"),
		Lasso(alpha = 0.1), 
		DecisionTreeRegressor(max_depth = 2), 
		RandomForestRegressor(max_depth = 2)]

	def build_models(self) -> List[Dict]:
		results = []
		for model in self.MODELS:
			model.fit(self.train_test_method()[0], self.train_test_method()[2])
			result = {f"{model.__class__.__name__} - root_{mean_squared_error.__name__} : {mean_squared_error(self.train_test_method()[3], model.predict(self.train_test_method()[1]), squared = False) * 100}"}
			results.append(result)
		return results
	
	def build_models_cv(self) -> List[Dict]:
		results = []
		for name, model in self.MODELS:
			scores = -cross_val_score(model, self.cross_val_method()[0], 
			self.cross_val_method()[1], scoring = "neg_mean_squared_error", cv = 10)
			rmse = np.sqrt(scores).mean() * 100
			result = {f"{model.__class__.__name__} - RMSE : {rmse}"}
			results.append(result)
		return results