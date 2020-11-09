import re
import _specify_dir
from typing import List
from math import floor, log10
from features.extractors.utils import patterns
from features.extractors.data_prep import DataPrep


class SpaceTabs(DataPrep):
    """Extracts frequency of space and tabs"""

    def __init__(self) -> None:
        super().__init__()
        self.space_pattern = patterns["space_pattern"]
        self.tabs_pattern = patterns["tabs_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    @property
    def get_space_frequency(self) -> List[int]:
        space_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.space_pattern, file)
            space_frequency.append(self.__len__(temp))
        return space_frequency

    @property
    def get_tabs_frequency(self) -> List[int]:
        tabs_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.tabs_pattern, file)
            tabs_frequency.append(self.__len__(temp))
        return tabs_frequency

    def extract_space(self) -> List[int]:
        space_features = []
        for char_freq, space_freq in zip(self.get_character_frequency, self.get_space_frequency):
            try:
                space_features.append(floor(log10(char_freq / space_freq)))
            except ZeroDivisionError:
                space_features.append(0)
        return space_features

    def extract_tabs(self) -> List[int]:
        tabs_features = []
        for char_freq, tab_freq in zip(self.get_character_frequency, self.get_tabs_frequency):
            try:
                tabs_features.append(floor(log10(char_freq / tab_freq)))
            except ZeroDivisionError:
                tabs_features.append(0)
        return tabs_features


if __name__ == "__main__":
    SpaceTabs().extract_tabs()
