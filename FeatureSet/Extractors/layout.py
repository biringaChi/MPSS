import _specify_dir
import re
from typing import List
from math import log10
from FeatureSet.Extractors.prep_utils import DataPrep


class EmptyLinesExtractor(DataPrep):
    """Extracts frequency of empty lines"""

    def __init__(self) -> None: super().__init__()

    @property
    def get_emptylines_frequency(self) -> List[int]:
        emptyline_frequency = []
        for file in self.get_sourcecode:
            emptyline = [emptyline for emptyline in file.splitlines() if emptyline == ""]
            emptyline_frequency.append(self.__len__(emptyline))
        return emptyline_frequency

    def extract_emptylines(self) -> List[float]:
        emptyline_features = []
        for char_freq, emptyline_freq in zip(self.get_character_frequency, self.get_emptylines_frequency):
            try:
                emptyline_features.append(log10(char_freq / emptyline_freq))
            except ZeroDivisionError:
                emptyline_features.append(0.0)
        return emptyline_features


class SpaceTabsExtractor(DataPrep):
    """Extracts frequency of space and tabs"""

    def __init__(self) -> None:
        super().__init__()
        self.SPACE_PATTERN = self.PATTERNS["space_pattern"]
        self.TABS_PATTERN = self.PATTERNS["tabs_pattern"]

    @property
    def get_space_frequency(self) -> List[int]:
        space_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.SPACE_PATTERN, file)
            space_frequency.append(self.__len__(temp))
        return space_frequency

    @property
    def get_tabs_frequency(self) -> List[int]:
        tabs_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.TABS_PATTERN, file)
            tabs_frequency.append(self.__len__(temp))
        return tabs_frequency

    def extract_space(self) -> List[float]:
        space_features = []
        for char_freq, space_freq in zip(self.get_character_frequency, self.get_space_frequency):
            try:
                space_features.append(log10(char_freq / space_freq))
            except ZeroDivisionError:
                space_features.append(0.0)
        return space_features

    def extract_tabs(self) -> List[float]:
        tabs_features = []
        for char_freq, tab_freq in zip(self.get_character_frequency, self.get_tabs_frequency):
            try:
                tabs_features.append(log10(char_freq / tab_freq))
            except ZeroDivisionError:
                tabs_features.append(0.0)
        return tabs_features