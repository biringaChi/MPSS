import os
import pandas as pd
from typing import List


class DataPrep:
    """Processes data from dataset file"""

    def __init__(self) -> None:
        self._GET_DIR = "/Users/Gabriel/Documents/Research/Experimentation/DevSecOps/Scripts/dataset.csv"
        self.PATTERNS  = { "java_keywords": {"abstract", "assert", "boolean", "break", "byte", "case", "catch",
        "char", "class", "const*", "**", "***", "****", "continue", "default", "do", "double",
        "else", "enum", "extends", "final", "finally", "float", "for", "goto*", "if",
        "implements", "import", "instanceof", "int", "interface", "long", "native",
        "new", "package", "private", "protected", "public", "return", "short", "static",
        "strictfp**", "super", "switch", "synchronized", "this", "throw", "throws",
        "transient", "try", "void", "volatile", "while"},
        "imports": ("import", "package"),
        "comments_pattern": "/\*(.|[\r\n])*?\*/|//.*",
        "methods_pattern": "(public|private|protected|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *(\{?|[^;])",
        "word_pattern": "\w+",
        "space_pattern": " +",
        "tabs_pattern": "\\t+",
        }

    def __len__(self, value) -> int: return len(value)

    @property
    def _get_data_dir(self) -> str:
        _walk_up = os.path.join(os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        try:
            _subfolders = [subs.path for subs in os.scandir(_walk_up) if subs.is_dir()]
            _parent_dir = os.path.join(_subfolders[1], os.listdir(_subfolders[1])[-1])
            print(os.path.join(_parent_dir, os.listdir(_parent_dir)[-1]))
            return os.path.join(_parent_dir, os.listdir(_parent_dir)[-1])
        except OSError as e:
            raise(e)
    @property
    def get_sourcecode(self) -> List[int]:
        try:
            data = pd.read_csv(self._GET_DIR)
            return [file for file in data.iloc[:, 2]]
        except IOError as e:
            raise(e)

    @property
    def get_character_frequency(self) -> List[int]:
        return [self.__len__(file) for file in self.get_sourcecode]

    @property
    def get_codeword_frequency(self) -> List[int]:
        codeword_freq = []
        for file in self.get_sourcecode:
            codeword_freq.append(self.__len__(
                [line for line in file.split()]))
        return codeword_freq
