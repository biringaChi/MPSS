import os
import sys
import _specify_dir
from features.extractors.process_data import ProcessData
from typing import List
from math import floor, log10
import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize


class NgramExtractor(ProcessData):
    """Extract ngrams"""

    def __init__(self, n) -> None:
        super().__init__()
        self.ngram = n

    def __repr__(self) -> str:
        return f"Class: {self.__class__.__name__}"

    def extract_ngrams(self) -> List[str]:
        ngrams = []
        for file in self.get_sourcecode:
            n_gram = ngrams(word_tokenize(file), self.ngram)
            ngrams.append([''.join(grams) for grams in n_gram])
        return ngrams


if __name__ == "__main__":
    NgramExtractor.extract_ngrams(1)
