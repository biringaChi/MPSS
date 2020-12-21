import _specify_dir
from FeatureSet.Extractors.process_extractors import ProcessFeatures
import numpy as np
import matplotlib.pyplot as plt
from typing import Dict, List
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge, Lasso
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.pipeline import make_pipeline


class HandleData(ProcessFeatures):
	"""Prepares data"""
	
	def __init__(self) -> None: super().__init__()

	def data(self) -> Dict:
		X = np.array(self.transpose_dataset_rename_columns().drop("Test(sec)", axis = 1))
		y = np.array(self.transpose_dataset_rename_columns()["Test(sec)"])
		X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 5)
		return {"X_train" : X_train, "X_test" : X_test, "y_train" : y_train, "y_test" : y_test, "X" : X, "y" : y}


class RegressionModels(HandleData):
	"""Experiments with Regression models"""

	def __init__(self) -> Dict:
		super().__init__()
		self.MODELS = [LinearRegression(), 
		make_pipeline(StandardScaler(), SGDRegressor(max_iter = 1000, tol = 1e-3)), 
		Ridge(alpha = 1, solver = "cholesky"),
		Lasso(alpha = 0.1), 
		DecisionTreeRegressor(max_depth = 2), 
		RandomForestRegressor(max_depth = 2)]
	
	def cv_models(self) -> List[Dict]:
		metrics = []
		for model in self.MODELS:
				scores = -cross_val_score(model, self.data().get("X"), self.data().get("y"), 
				scoring = "neg_mean_absolute_error", cv = 10)
				metric = {model.__class__.__name__ : scores.mean() * 100}
				metrics.append(metric)
		return metrics 
	
	def fit_models(self) -> List[List]:
		models = []
		for model in self.MODELS:
			models.append(model.fit(self.data().get("X_train"), self.data().get("y_train")))
		return models

	def model_evaluation(self) -> List[Dict]:
		metrics = []
		for model in self.fit_models():
			metric = {}
			y_pred = model.predict(self.data().get("X_test"))
			metric[model.__class__.__name__] = [mean_squared_error(
				self.data().get("y_test"), y_pred, squared = False) * 100, mean_absolute_error(
				self.data().get("y_test"), y_pred) * 100]
			metrics.append(metric)
		return metrics

	def visualize_evaluation(self) -> None:
		mae = []
		model = [model.__class__.__name__.replace("Pipeline", "SGDRegressor") for model in self.MODELS]
		for measure in self.cv_models():
			for error in measure.values():
				mae.append(error)
		plt.plot(model, mae, alpha = 0.5, label = "Mean Absolute Error (MAE)")
		plt.xlabel("Model")
		plt.ylabel("Mean Absolute Error (MAE)")
		plt.title("Model Evaluation")
		plt.tight_layout()
		plt.show()
		