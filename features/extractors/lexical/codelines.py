import _specify_dir
from typing import List
from statistics import pstdev
from math import floor, log10
from features.extractors.utils import patterns
from features.extractors.process_data import ProcessData


class CodeLinesExtractor(ProcessData):
    """Extracts statistics of code lines"""

    def __init__(self) -> None:
        super().__init__()
        self.imports = patterns["imports"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    def mean_codelines(self) -> List[int]:
        codelines_avg = []
        for file in self.get_sourcecode:
            codeline = [self.__len__(codeline)
                        for codeline in file.splitlines() if codeline.strip()]
            codelines_avg.append(
                floor(log10(sum(codeline) / self.__len__(codeline))))
        return codelines_avg

    def sd_codelines(self) -> List[int]:
        codelines_sd = []
        for codelines in self.get_sourcecode:
            codeline = [self.__len__(
                codeline) for codeline in codelines.splitlines() if codeline.strip()]
            codelines_sd.append(floor(log10(pstdev(codeline))))
        return codelines_sd

    def import_codelines(self) -> List[int]:
        import_codelines = []
        for file in self.get_sourcecode:
            codeline = len(
                [line for line in file.splitlines() if line.strip()])
            importline = len([line for line in file.splitlines()
                              if line.startswith(self.imports)])
            import_codelines.append((floor(log10(codeline/importline))))
        return import_codelines


if __name__ == "__main__":
    CodeLinesExtractor().import_codelines()
