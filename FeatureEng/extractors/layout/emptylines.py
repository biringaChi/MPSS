import _specify_dir
from typing import List
from statistics import pstdev
from math import floor, log10
from FeatureEng.Extractors.utils import patterns
from FeatureEng.Extractors.data_prep import DataPrep


class EmptyLinesExtractor(DataPrep):
    """Extracts frequency of empty lines"""

    def __init__(self) -> None:
        super().__init__()
        self.imports = patterns["imports"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def get_emptylines_frequency(self) -> List[int]:
        emptyline_frequency = []
        for file in self.get_sourcecode:
            emptyline = [emptyline for emptyline in file.splitlines() if emptyline == ""]
            emptyline_frequency.append(self.__len__(emptyline))
        return emptyline_frequency

    def extract_emptylines(self) -> List[int]:
        emptyline_features = []
        for char_freq, emptyline_freq in zip(self.get_character_frequency, self.get_emptylines_frequency):
            try:
                emptyline_features.append(round(log10(char_freq / emptyline_freq), 2))
            except ZeroDivisionError:
                emptyline_features.append(0)
        return emptyline_features