import _specify_dir
import re
from math import log10
from typing import List
from statistics import pstdev
from nltk.util import ngrams
from nltk import RegexpTokenizer
from nltk.tokenize import word_tokenize
from FeatureSet.Extractors.prep_utils import DataPrep


class CodeLinesExtractor(DataPrep):
    """
    Extracts statistics of lines of code
    Examples: mean and standard deviation
    """

    def __init__(self) -> None:
        super().__init__()
        self.IMPORTS = self.PATTERNS["imports"]

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


class CommentsExtractor(DataPrep):
    """Extracts frequency of comments"""

    def __init__(self) -> None:
        super().__init__()
        self.COMMENTS_PATTERN = self.PATTERNS["comments_pattern"]

    @property
    def get_comments_frequency(self) -> List[int]:
        comments_frequency = []
        for file in self.get_sourcecode:
            temp = re.findall(self.COMMENTS_PATTERN, file)
            comments_frequency.append(self.__len__(temp))
        return comments_frequency

    def extract_comments(self) -> List[float]:
        comments_features = []
        for char_freq, cmnt_freq in zip(self.get_character_frequency, self.get_comments_frequency):
            try:
                comments_features.append(log10(char_freq / cmnt_freq))
            except ZeroDivisionError:
                comments_features.append(0.0)
        return comments_features


class KeywordExtractor(DataPrep):
    """Extracts frequency of keywords"""

    def __init__(self) -> None:
        super().__init__()
        self.JAVA_KEYWORDS = self.PATTERNS["java_keywords"]
        self.COMMENTS_PATTERN = self.PATTERNS["comments_pattern"]

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


class MethodsExtractor(DataPrep):
    """Extracts frequency of methods"""

    def __init__(self) -> None:
        super().__init__()
        self.METHODS_PATTERN = self.PATTERNS["methods_pattern"]

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


class WordToken(DataPrep):
    """Extracts word tokens"""

    def __init__(self) -> None:
        super().__init__()
        self.WORD_PATTERN = self.PATTERNS["word_pattern"]

    @property
    def get_word_tokens(self) -> List[int]:
        tokens = []
        for file in self.get_sourcecode:
            tokenizer = RegexpTokenizer(self.WORD_PATTERN)
            word_token = tokenizer.tokenize(file)
            tokens.append(self.__len__(word_token))
        return tokens

    def extract_word_tokens(self) -> List[int]:
        token_features = []
        for char_freq, token_freq in zip(self.get_character_frequency, self.get_word_tokens):
            try:
                token_features.append(log10(char_freq / token_freq))
            except ZeroDivisionError:
                token_features.append(0)
        return token_features
        

class NgramExtractor(DataPrep):
    """Extract ngrams"""

    def __init__(self, n) -> None:
        super().__init__()
        self.NGRAM = n
        self.WORD_PATTERN = self.PATTERNS["word_pattern"]

    def __repr__(self) -> str: return f"Class: {self.__class__.__name__}"

    def extract_ngrams(self) -> List[List[str]]:
        ngrams_ex = []
        for file in self.get_sourcecode:
            n_gram = ngrams(word_tokenize(file), self.NGRAM)
            ngrams_ex.append([''.join(grams) for grams in n_gram])
        return ngrams_ex


class TFIDF(NgramExtractor):
    """Extracts TF-IDF"""

    def __init__(self, n) -> None:
        super().__init__(n)