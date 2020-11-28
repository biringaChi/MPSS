from typing import Dict, List
from nltk import RegexpTokenizer
from gensim.models import KeyedVectors
from gensim.models import Word2Vec


class ASTVectors:
	"""Creates vectors for ASTs"""

	def get_nodes(self):
		try:
			with open("ASTData.txt") as ast_file:
				ast = ast_file.readlines()
				return ast
		except FileNotFoundError as e:
			raise e
	
	def node_types(self) -> List[List[int]]:
		nodes = []
		for node in self.get_nodes():
			temp = [n.strip() for n in node.split(",")]
			if len(temp) == 1: 
				temp = None
			nodes.append(temp)
		return nodes
	
	def model(self) -> None:
		tokenizer = RegexpTokenizer("\w+")
		tokens = [tokenizer.tokenize(node) for node in self.get_nodes()]
		return Word2Vec(sentences = tokens, min_count = 1, size = 32)
	
	def save_vectors(self) -> None:
		node_vecs = self.model().wv
		node_vecs.save('node_vecs.wordvectors')
	
	def assign_vectors(self) -> List[List[float]]:
		vec_dict = {}
		node_vecs = KeyedVectors.load("node_vecs.wordvectors", mmap = "r")
		for key in node_vecs.vocab:
			vec_dict[key] = node_vecs[key]
		node_vecs = []
		for node_vec in self.node_types():
			temp = []
			if node_vec is not None:
				for node in node_vec:
					if node in vec_dict:
						temp.append(vec_dict.get(node))
			node_vecs.append(temp)
		return node_vecs
		

if __name__ == "__main__":
	print(len(ASTVectors().assign_vectors()))