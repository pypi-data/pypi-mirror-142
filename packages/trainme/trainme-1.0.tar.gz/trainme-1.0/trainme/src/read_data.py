'''
@aditta_das_nishd

This class will automatically read path and analyze path

read_path: 
1. csv
2. excel
3. json
4. feather
5. sqlite3
'''
import os
import json
import joblib
import pandas as pd
import numpy as np
import wandb
import matplotlib.pyplot as plt
from sklearn.preprocessing import OrdinalEncoder, LabelEncoder
from tabulate import tabulate
from .logger import logger
from IPython.display import display
from .utils import label_encode, normal_data_split, null_checker, reduce_mem_usage, train_model, predict_model
from .visualize import *
from .params import without_compare


from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression, PassiveAggressiveClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import KFold, StratifiedKFold


class ReadFile:
	def __init__(
		self, 
		train_path, 
		test_path=None, 
		submission_path=None, 
		drop_col=None,
		label=None,
		features=None,
		random_state=42,
		no_of_fold=5,
		shuffle=True,
		test_size=0.3,
		n_trials=10,
		use_gpu=False,
		fill_value=None,
		compare=True,
		task_type="binary_classification",
		scaler="standard",
		fold="kfold",
		model_name="RandomForest",
		output_path="output",
		study_name="train",
		folder_output="new_store",
		direction="minimize",
		kaggle=True,
	):
		self.train_path = train_path
		self.test_path = test_path
		self.submission_path = submission_path
		self.drop_col = drop_col
		self.label = label
		self.features=features
		self.random_state=random_state
		self.shuffle=shuffle
		self.test_size=test_size
		self.use_gpu=use_gpu
		self.no_of_fold=no_of_fold
		self.task_type = task_type
		self.fold = fold
		self.compare = compare
		self.output_path = output_path
		self.study_name = study_name
		self.n_trials = n_trials
		self.folder_output = folder_output
		self.direction = direction
		self.kaggle = kaggle
		if self.compare is False:
			self.model_name = model_name

	# def wandb_visualize(project_name="new"):
	# 	os.environ["WANDB_SILENT"] = "true"
	# 	wandb.init(project=project_name)


	def auto_output_folder(self):
		# base_path = os.path.dirname(os.getcwd())
		directory = os.path.join(self.output_path, self.folder_output)
		print(directory)
		if not os.path.exists(directory):
			logger.info(f"Create folder name : {self.folder_output} folder")
			os.mkdir(directory)
		else:
			logger.info("Folder already exists, create new one")
			raise Exception("Folder already exists, specify new one")

	def load_path(self):
		self.auto_output_folder()

		# self.wandb_visualize()

		train_file = pd.read_csv(self.train_path)
		train_file = reduce_mem_usage(train_file)

		if self.test_path is not None:
			test_file = pd.read_csv(self.test_path)
			test_file = reduce_mem_usage(test_file)
			test_file.drop(self.drop_col, axis=1, inplace=True)
			test_file.to_feather(f"{os.path.join(self.output_path, self.folder_output)}/reduced_dataset_test.feather")
		
		logger.info(f"Output folder : {self.output_path} created")
		if self.drop_col is not None:
			train_file.drop(self.drop_col, axis=1, inplace=True)
		return train_file

	def report(self):
		train_file = self.load_path()
		logger.info("Description of data")
		display(
			tabulate([
				[train_file.describe()]
			])
		)
		logger.info("Is there any null values?")

		# null_checker(train_file)
		
		if self.task_type == "binary_classification" or self.task_type == "multi_classification":
			logger.info(f"Label: {self.label} balanced or not?")
			display(
				tabulate([
					[train_file[self.label].value_counts()]
				])
			)
		else: pass # for regression

		train_file.to_csv(f"{os.path.join(self.output_path, self.folder_output)}/reduced_dataset.csv", index=False)
		
		logger.info("Dataset created and saved")	

	def visualize(self):
		pass

	def _process_data(self):
		path = os.path.join(f"{os.path.join(self.output_path, self.folder_output)}")
		df = pd.read_csv(os.path.join(f"{path}/reduced_dataset.csv"))
	
		if df[self.label].dtype == "object":
			lbl_encoder = LabelEncoder()
			df[self.label] = lbl_encoder.fit(
				df[self.label].values.reshape(-1,)
			)
			df.loc[:, self.label] = lbl_encoder.transform(
                df[self.label].values.reshape(
                    -1,
                )
            )
			logger.info(">>> LabelEncoder Saving")
			joblib.dump(lbl_encoder, f"{os.path.join(self.output_path, self.folder_output)}/lbl_encod.joblib")

		categorical = []
		for col in df.columns:
			if df[col].dtype == "object":
				categorical.append(col)
			else:
				pass		
		

		# fold system
		if self.fold == "kfold":
			df["kfold"] = -1
			kf = KFold(
            	n_splits=self.no_of_fold, 
				shuffle=self.shuffle, 
				random_state=self.random_state
        	)
			for f, (tr_, val_) in enumerate(kf.split(X=df)):
				df.loc[val_, "kfold"] = f
			logger.info("Kfold Done >>>")

		# stratified Kfold test_prediction.append(test_pred)system
		elif self.fold == "skfold":
			df["kfold"] = -1
			skf = StratifiedKFold(
            	n_splits=self.no_of_fold, shuffle=self.shuffle, random_state=self.random_state
        	)
			for f, (tr_, val_) in enumerate(skf.split(X=df, y=df[f"{self.label}"])):
				df.loc[val_, "kfold"] = f
			logger.info("Stratified Kfold >>>")

		# random fold system
		elif self.fold == "random":
			xtrain, xtest, ytrain, ytest = normal_data_split(
				df, 
				self.label, 
				self.random_state, 
				self.shuffle, 
				self.test_size
			)
			logger.info("Random fold >>>")

		ignore_fields = ["kfold", self.label]
		if self.features is None:
			self.features = list(df.columns)
			self.features = [x for x in self.features if x not in ignore_fields]
			json_features = {
				'features': self.features,
				'label': self.label,
				'path': os.path.dirname(os.getcwd()),
				'output_path': self.output_path,
				'folder_output': self.folder_output,
				'test_path': self.test_path,
				'submission_path': self.submission_path,
				'model_name': self.model_name,
				'random_state': self.random_state,
				'shuffle': self.shuffle,
				'test_size': self.test_size,
				'no_of_fold': self.no_of_fold,
				'use_gpu': self.use_gpu,
				'problem_type': self.task_type,
				'study_name': self.study_name,
				'n_trials': self.n_trials,
				'compare': self.compare,
				'direction': self.direction,
				'categorical': categorical,
				'kaggle': self.kaggle
			}
			with open(os.path.join(f"{os.path.join(self.output_path, self.folder_output)}/features.json"), "w") as file:
				json.dump(json_features, file)
		'''
		1. if kfold or stratified then we will save
		   as feather file for train and test data
		2. if test file is not none then save test file as feather file
		'''
		
		if self.fold == "skfold" or self.fold == "kfold":
			categorical_encod = {}
			for fold in range(self.no_of_fold):
				train_fold = df[df.kfold != fold].reset_index(drop=True)
				test_fold = df[df.kfold == fold].reset_index(drop=True)

				if len(categorical) > 0:
					ordi_encoder = OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value=np.nan)
					train_fold[categorical] = ordi_encoder.fit_transform(train_fold[categorical].values)
					test_fold[categorical] = ordi_encoder.transform(test_fold[categorical].values)

					if self.test_path is not None:
						test_file = pd.read_feather(os.path.join(f"{path}/reduced_dataset_test.feather"))
						test_file[categorical] = ordi_encoder.transform(test_file[categorical].values)
						test_file.to_feather(os.path.join(f"{os.path.join(self.output_path, self.folder_output)}/test_file_{fold}.feather"))

					categorical_encod[fold] = ordi_encoder

				logger.info(">>> Categorical Encoder saving")
				joblib.dump(categorical_encod, f"{os.path.join(self.output_path, self.folder_output)}/cat_encod.joblib")

				# save fold as feather file
				train_fold.to_feather(os.path.join(f"{os.path.join(self.output_path, self.folder_output)}/train_fold_{fold}.feather"))
				test_fold.to_feather(os.path.join(f"{os.path.join(self.output_path, self.folder_output)}/test_fold_{fold}.feather"))

				logger.info(f">>> train fold {fold} save")
				logger.info(f">>> test fold {fold} save")

		# if self.task_type == "binary_classification" or self.task_type == "multi_classification":
		# 	if self.compare is True:
		# 		#TODO : compare 2 or more algorithoms
		# 		pass
		# 	else:
		# 		pass
				'''
				# TODO : Using GridSearch using one algorithom
				scores = []
				for model_name, params in without_compare().items():
					if model_name == self.model_name:
						clf = GridSearchCV(params["model"], params["params"], cv=5, return_train_score=False)
						clf.fit(xtrain, ytrain)
						scores.append({
							"model": self.model_name,
							"best_params": clf.best_params_,
							"best_scores": clf.best_score_,
						})
				'''

				# TODO : optuna trial

						
			# with open(f"{path}/best_params_{self.model_name}.json", "w") as file:
			# 	json.dump(model.get_params(), file)
			# logger.info(f"Saving best params >> best_params_{self.model_name}.json")
			# return model.best_params_


	
	
	def train(self):
		self._process_data()
		with open(f"{os.path.join(os.path.join(self.output_path, self.folder_output))}/features.json") as f:
			model_config = json.load(f)
			bp = train_model(model_config)
		predict_model(model_config, best_params=bp)
	
