import sys
import os
import argparse
import csv

parser = argparse.ArgumentParser(description = "Creates a dataset")
parser.add_argument("version")
parser.add_argument("build")
parser.add_argument("test")
args = parser.parse_args()

class DatasetCreator:
	def __init__(self, path):
		self.fieldnames  = ["version", "source_code", "build", "test"]
		self.path = path

	def create_csv_file(self):
		with open("dataset.csv", "w") as dataset:
			writer = csv.DictWriter(dataset, fieldnames = self.fieldnames)
			writer.writeheader()

	def populate_csv_file(self, version, build, test):		
		for (root, subdirectories, files) in os.walk(self.path):
			for file in files:
				if file.endswith(".java"):
					temp = os.path.join(root, file)
					try: 
						with open(temp, "r") as java_file:
							with open("dataset.csv", "a") as dataset:
								writer = csv.DictWriter(dataset, fieldnames = self.fieldnames)
								writer.writerow({"version" : version,
												"source_code" : java_file.read(),
												"build" : build, 
												"test" : test
												})
					except Exception as e:
						print(e)
						continue
												

if __name__ == '__main__':
	path = "/Users/Gabriel/Documents/research/data_source/addressbook-level2"
	dc = DatasetCreator(path)
	dc.create_csv_file()
	dc.populate_csv_file(args.version, args.build, args.test)
		
