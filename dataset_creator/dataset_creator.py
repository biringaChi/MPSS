import sys
import os
import argparse
import csv

# Usage: dataset_creator.py [-h] [-v VERSION] [-H HASH] [-b BUILD] [-t TEST]

parser = argparse.ArgumentParser(description = "Creates datasets")
parser.add_argument("-v", "--version", help = "Repository version")
parser.add_argument("-H", "--hash", help = "Repository commit hash value")
parser.add_argument("-b", "--build", type = float, help = "Repository build time")
parser.add_argument("-t", "--test", type = float, help = "Repository test time")
args = parser.parse_args()

class DatasetCreator:
	"""Create a dataset using GitHub repositories"""
	def __init__(self, path):
		self.fieldnames  = ["version", "hash", "sourcecode", "build", "test"]
		self.path = path

	def create_csv_file(self) -> None:
		with open("dataset.csv", "w") as dataset:
			writer = csv.DictWriter(dataset, fieldnames = self.fieldnames)
			writer.writeheader()

	def populate_csv_file(self, version, hash, build, test) -> None:		
		for (root, subdirectories, files) in os.walk(self.path):
			for file in files:
				if file.endswith(".java"):
					temp = os.path.join(root, file)
					try: 
						with open(temp, "r") as java_file:
							with open("dataset.csv", "a") as dataset:
								writer = csv.DictWriter(dataset, fieldnames = self.fieldnames)
								writer.writerow({"version" : version,
												"hash" : hash, 
												"sourcecode" : java_file.read(),
												"build" : build, 
												"test" : test
												})
					except Exception as e:
						print(e)
						continue
												

if __name__ == '__main__':
	path = "/Users/Gabriel/Documents/research/data_source/sc1/addressbook-level2-5.0"
	dc = DatasetCreator(path)
	# dc.create_csv_file()
	# dc.populate_csv_file(args.version, args.hash, args.build, args.test)