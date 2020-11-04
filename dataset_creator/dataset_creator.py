import sys
import os
import argparse
import csv

# Step 1: Call "create_csv_file" method without argument  
# Step 2: Comment out "create_csv_file" method
# Step 3: Call "populate_csv_file" with argument 
# Usage: dataset_creator.py [-h] [-v VERSION] [-H HASH] [-b BUILD] [-t TEST]

parser = argparse.ArgumentParser(description = "Creates datasets")
parser.add_argument("-v", "--version", help = "Repository version")
parser.add_argument("-H", "--hash", help = "Repository commit hash value")
parser.add_argument("-b", "--build", type = float, help = "Repository build time")
parser.add_argument("-t", "--test", type = float, help = "Repository test time")
args = parser.parse_args()

class DatasetCreator:
	"""Create a dataset using GitHub repositories"""
	def __init__(self, path, filename, version, hash, build, test):
		self.fieldnames  = ["version", "hash", "sourcecode", "build", "test"]
		self.path = path
		self.filename = filename
		self.version = version
		self.hash = hash
		self.build = build
		self.test = test

	def create_csv_file(self) -> None:
		with open(f"{self.filename}.csv", "w") as dataset:
			writer = csv.DictWriter(dataset, fieldnames = self.fieldnames)
			writer.writeheader()

	def populate_csv_file(self) -> None:		
		for (root, subdirectories, files) in os.walk(self.path):
			for file in files:
				if file.endswith(".java"):
					temp = os.path.join(root, file)
					try: 
						with open(temp, "r") as java_file:
							with open(f"{self.filename}.csv", "a") as dataset:
								writer = csv.DictWriter(dataset, fieldnames = self.fieldnames)
								writer.writerow({"version" : self.version,
												"hash" : self.hash, 
												"sourcecode" : java_file.read(),
												"build" : self.build, 
												"test" : self.test
												})
					except Exception as e:
						print(e)
						continue
												

if __name__ == '__main__':
	path = "/Users/Gabriel/Documents/research/data_source/sc1/addressbook-level2-1.0"
	filename = "dataset"
	dc = DatasetCreator(path, filename, args.version, args.hash, args.build, args.test)
	# dc.create_csv_file()
	# dc.populate_csv_file()