import _specify_dir
from typing import List
from math import floor, log10
from nltk import RegexpTokenizer
from FeatureSet.Extractors.utils import patterns
from FeatureSet.Extractors.data_prep import DataPrep


class WordToken(DataPrep):
    """Extracts word tokens"""

    def __init__(self) -> None:
        super().__init__()
        self.WORD_PATTERN = patterns["word_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def get_word_tokens(self) -> List[int]:
        tokens = []
        for file in self.get_sourcecode:
            tokenizer = RegexpTokenizer(self.WORD_PATTERN)
            word_token = tokenizer.tokenize(file)
            tokens.append(self.__len__(word_token))
        return tokens

    def extract_word_tokens(self) -> List[int]:
        token_features = []
        for char_freq, token_freq in zip(self.get_character_frequency, self.get_word_tokens):
            try:
                token_features.append(floor(log10(char_freq / token_freq)))
            except ZeroDivisionError:
                token_features.append(0)
        return token_features