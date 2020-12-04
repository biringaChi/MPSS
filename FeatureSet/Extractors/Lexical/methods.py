import re
import _specify_dir
from typing import List
from math import log10
from FeatureSet.Extractors.utils import patterns
from FeatureSet.Extractors.data_prep import DataPrep


class MethodsExtractor(DataPrep):
    """ Extracts frequency of methods """

    def __init__(self) -> None:
        super().__init__()
        self.METHODS_PATTERN = patterns["methods_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def get_methods_frequency(self) -> List[int]:
        methods_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.METHODS_PATTERN, file)
            methods_frequency.append(self.__len__(temp))
        return methods_frequency

    def extract_methods(self) -> List[float]:
        methods_features = []
        for char_freq, method_freq in zip(self.get_character_frequency, self.get_methods_frequency):
            try:
                methods_features.append(log10(char_freq / method_freq))
            except ZeroDivisionError:
                methods_features.append(0.0)
        return methods_features