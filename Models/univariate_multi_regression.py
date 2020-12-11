import _specify_dir
from FeatureSet.Extractors.process_extractors import ProcessFeatures
import numpy as np
from typing import Dict, List, Tuple
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, Lasso, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error, accuracy_score
from sklearn.pipeline import make_pipeline


class HandleData(ProcessFeatures):
	"""Prepares data for ML"""
	
	def __init__(self) -> None: super().__init__()

	def train_test_method(self) -> Tuple:
		X = np.array(self.transpose_dataset_rename_columns().drop("Test(sec)", axis = 1))
		y = np.array(self.transpose_dataset_rename_columns()["Test(sec)"])
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)
		le = LabelEncoder()
		y_train_encoded = le.fit_transform(y_train)
		y_test_encoded = le.fit_transform(y_test)
		return X_train, X_test, y_train, y_test, y_train_encoded, y_test_encoded


class RegressionModels(HandleData):
	"""Experiments with Regression models"""

	def __init__(self) -> Dict:
		super().__init__()
		self.MODELS = [LinearRegression(), 
		make_pipeline(StandardScaler(), SGDRegressor(max_iter = 1000, tol = 1e-3)), 
		Ridge(alpha = 1, solver = "cholesky"),
		Lasso(alpha = 0.1), 
		LogisticRegression(max_iter = 1000), 
		DecisionTreeRegressor(max_depth = 2), 
		RandomForestRegressor(max_depth = 2)]

	def fit_models(self) -> List[List]:
		models = []
		for model in self.MODELS:
			if "LogisticRegression" not in model.__class__.__name__:
				models.append(model.fit(self.train_test_method()[0], self.train_test_method()[2]))
			else: models.append(model.fit(self.train_test_method()[0], self.train_test_method()[4]))
		return models
	
	def evaluate_model(self) -> List[Dict]:
		metrics = []
		for model in self.fit_models():
			metric = {}
			if "LogisticRegression" not in model.__class__.__name__:
				y_pred = model.predict(self.train_test_method()[1])
				metric[f"{model.__class__.__name__}: {mean_squared_error.__name__} || {mean_absolute_error.__name__}"] = [mean_squared_error(
					self.train_test_method()[3], y_pred, squared = False) * 100, mean_absolute_error(
					self.train_test_method()[3], y_pred) * 100]
				metrics.append(metric)
			else: 
				y_pred = model.predict(self.train_test_method()[1])
				metric[f"{model.__class__.__name__} - {accuracy_score.__name__}"] = accuracy_score(
					self.train_test_method()[5], y_pred) * 100
				metrics.append(metric)
		return metrics

	def visualize_model(self):
		pass
		