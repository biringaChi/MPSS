import _specify_dir
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import nltk
from math import floor, log10
from typing import List
from features.extractors.process_data import ProcessData


class NgramExtractor(ProcessData):
    """Extract ngrams"""

    def __init__(self, n) -> None:
        super().__init__()
        self.ngram = n

    def __repr__(self) -> str:
        return f"Class: {self.__class__.__name__}"

    def extract_ngrams(self) -> List[str]:
        ngrams_ex = []
        for file in self.get_sourcecode:
            n_gram = ngrams(nltk.word_tokenize(file), self.ngram)
            ngrams_ex.append([''.join(grams) for grams in n_gram])
        return ngrams_ex


if __name__ == "__main__":
    result = NgramExtractor(1).extract_ngrams()
    print(result[0])


class TF_IDF(NgramExtractor):
    """Extracts TF-IDF"""

    def __init__(self, n) -> None:
        super().__init__(n)
