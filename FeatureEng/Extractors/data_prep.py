import os
import pandas as pd
from typing import List


class DataPrep:
    """Processes data from dataset file"""

    def __init__(self) -> None: pass

    def __repr__(self) -> str: return f"{self.__class__.__name__}"

    def __len__(self, value) -> int: return len(value)

    @property
    def _get_data_dir(self) -> str:
        _walk_up = os.path.join(os.path.dirname(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        try:
            _subfolders = [subs.path for subs in os.scandir(_walk_up) if subs.is_dir()]
            _parent_dir = os.path.join(_subfolders[1], os.listdir(_subfolders[1])[-1])
            return os.path.join(_parent_dir, os.listdir(_parent_dir)[-1])
        except OSError as e:
            raise(e)

    @property
    def get_sourcecode(self) -> List[int]:
        try:
            data = pd.read_csv(self._get_data_dir)
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