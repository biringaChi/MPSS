import _specify_dir
from typing import List
from statistics import pstdev
from math import log10
from FeatureSet.Extractors.utils import patterns
from FeatureSet.Extractors.data_prep import DataPrep


class CodeLinesExtractor(DataPrep):
    """
    Extracts statistics of lines of code
    Examples: mean and standard deviation
    """

    def __init__(self) -> None:
        super().__init__()
        self.IMPORTS = patterns["imports"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    def extract_mean_codelines(self) -> List[float]:
        mean_codelines = []
        for file in self.get_sourcecode:
            try:
                codeline = [self.__len__(codeline) for codeline in file.splitlines() if codeline.strip()]
                mean_codelines.append(log10(sum(codeline) / self.__len__(codeline)))
            except ZeroDivisionError:
                mean_codelines.append(0.0)
        return mean_codelines

    def extract_sd_codelines(self) -> List[float]:
        sd_codelines = []
        for codelines in self.get_sourcecode:
            try:
                codeline = [self.__len__(codeline) for codeline in codelines.splitlines() if codeline.strip()]
                sd_codelines.append(log10(pstdev(codeline)))
            except ZeroDivisionError:
                sd_codelines.append(0.0)
        return sd_codelines

    def extract_import_statements(self) -> List[float]:
        import_statements = []
        for file in self.get_sourcecode:
            try:
                codeline = self.__len__([line for line in file.splitlines() if line.strip()])
                importline = self.__len__([line for line in file.splitlines() if line.startswith(self.IMPORTS)])
                import_statements.append(log10(codeline / importline))
            except ZeroDivisionError:
                import_statements.append(0.0)
        return import_statements