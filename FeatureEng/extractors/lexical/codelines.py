import _specify_dir
from typing import List
from statistics import pstdev
from math import floor, log10
from FeatureEng.extractors.utils import patterns
from FeatureEng.extractors.data_prep import DataPrep


class CodeLinesExtractor(DataPrep):
    """Extracts statistics of codelines"""

    def __init__(self) -> None:
        super().__init__()
        self.imports = patterns["imports"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    def mean_codelines(self) -> List[int]:
        codelines_avg = []
        for file in self.get_sourcecode:
            try:
                codeline = [self.__len__(codeline) for codeline in file.splitlines() if codeline.strip()]
                codelines_avg.append(round(log10(sum(codeline) / self.__len__(codeline)), 2))
            except ZeroDivisionError:
                codelines_avg.append(0)
        return codelines_avg

    def sd_codelines(self) -> List[int]:
        codelines_sd = []
        for codelines in self.get_sourcecode:
            try:
                codeline = [self.__len__(
                    codeline) for codeline in codelines.splitlines() if codeline.strip()]
                codelines_sd.append(round(log10(pstdev(codeline)), 2))
            except ZeroDivisionError:
                codelines_sd.append(0)
        return codelines_sd

    def import_statements(self) -> List[int]:
        import_statements = []
        for file in self.get_sourcecode:
            try:
                codeline = self.__len__([line for line in file.splitlines() if line.strip()])
                importline = self.__len__([line for line in file.splitlines() if line.startswith(self.imports)])
                import_statements.append(round(log10(codeline / importline), 2))
            except ZeroDivisionError:
                import_statements.append(0)
        return import_statements