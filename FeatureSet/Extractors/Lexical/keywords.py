import re
import _specify_dir
from typing import List
from math import log10
from FeatureSet.Extractors.utils import patterns
from FeatureSet.Extractors.data_prep import DataPrep


class KeywordExtractor(DataPrep):
    """ Extracts frequency of keywords """

    def __init__(self) -> None:
        super().__init__()
        self.JAVA_KEYWORDS = patterns["java_keywords"]
        self.COMMENTS_PATTERN = patterns["comments_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def del_comments(self) -> List[int]:
        modified_file = []
        for file in self.get_sourcecode:
            temp = re.sub(self.COMMENTS_PATTERN, "", file)
            modified_file.append(temp)
        return modified_file

    @property
    def get_keyword_frequency(self) -> List[int]:
        keyword_frequency = []
        for file in self.del_comments:
            temp = [word for word in file.split() if word in self.JAVA_KEYWORDS]
            keyword_frequency.append(self.__len__(temp))
        return keyword_frequency

    def extract_keywords(self) -> List[float]:
        lexical_features = []
        for char_freq, kw_freq in zip(self.get_character_frequency, self.get_keyword_frequency):
            try:
                lexical_features.append(log10(char_freq / kw_freq))
            except ZeroDivisionError:
                lexical_features.append(0.0)
        return lexical_features