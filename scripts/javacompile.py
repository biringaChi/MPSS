import sys
import os
import argparse

# Usage in command line: python [path arg] [compiler arg]

parser = argparse.ArgumentParser(description = "Compiles java files")
parser.add_argument("path")
parser.add_argument("compiler")
args = parser.parse_args()

def compile_files(path, compiler):
	# Compiles all java files in datasource
	for (root, subdirectories, files) in os.walk(path):
		for file in files:
			if file.endswith(".java"):
				os.system(compiler + " " + file)


if __name__ == '__main__':
	compile_files(args.path, args.compiler)