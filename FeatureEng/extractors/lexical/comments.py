import re
import _specify_dir
from typing import List
from math import floor, log10
from FeatureEng.Extractors.utils import patterns
from FeatureEng.Extractors.data_prep import DataPrep


class CommentsExtractor(DataPrep):
    """Extracts frequency of comments"""

    def __init__(self) -> None:
        super().__init__()
        self.comments_pattern = patterns["comments_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def get_comments_frequency(self) -> List[int]:
        comments_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.comments_pattern, file)
            comments_frequency.append(self.__len__(temp))
        return comments_frequency

    def extract_comments(self) -> List[int]:
        comments_features = []
        for char_freq, cmnt_freq in zip(self.get_character_frequency, self.get_comments_frequency):
            try:
                comments_features.append(
                    round(log10(char_freq / cmnt_freq), 2))
            except ZeroDivisionError:
                comments_features.append(0)
        return comments_features
