import re
import _specify_dir
from typing import List
from math import log10
from FeatureSet.Extractors.utils import patterns
from FeatureSet.Extractors.data_prep import DataPrep


class CommentsExtractor(DataPrep):
    """ Extracts frequency of comments """

    def __init__(self) -> None:
        super().__init__()
        self.COMMENTS_PATTERN = patterns["comments_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def get_comments_frequency(self) -> List[int]:
        comments_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.COMMENTS_PATTERN, file)
            comments_frequency.append(self.__len__(temp))
        return comments_frequency

    def extract_comments(self) -> List[float]:
        comments_features = []
        for char_freq, cmnt_freq in zip(self.get_character_frequency, self.get_comments_frequency):
            try:
                comments_features.append(log10(char_freq / cmnt_freq))
            except ZeroDivisionError:
                comments_features.append(0.0)
        return comments_features