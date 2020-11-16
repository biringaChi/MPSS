import re
import _specify_dir
from typing import List
from math import floor, log10
from FeatureEng.Extractors.utils import patterns
from FeatureEng.Extractors.data_prep import DataPrep


class KeywordExtractor(DataPrep):
    """Extracts frequency of keywords"""

    def __init__(self) -> None:
        super().__init__()
        self.java_keywords = patterns["java_keywords"]
        self.comments_pattern = patterns["comments_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def del_comments(self) -> List[int]:
        modified_file = []
        for file in self.get_sourcecode:
            temp = re.sub(self.comments_pattern, "", file)
            modified_file.append(temp)
        return modified_file

    @property
    def get_keyword_frequency(self) -> List[int]:
        keyword_frequency = []
        for file in self.del_comments:
            temp = [word for word in file.split() if word in self.java_keywords]
            keyword_frequency.append(self.__len__(temp))
        return keyword_frequency

    def extract_keywords(self) -> List[int]:
        lexical_features = []
        for char_freq, kw_freq in zip(self.get_character_frequency, self.get_keyword_frequency):
            try:
                lexical_features.append(round(log10(char_freq / kw_freq), 2))
            except ZeroDivisionError:
                lexical_features.append(0)
        return lexical_features