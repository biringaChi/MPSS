# Regular expression patterns and java keywords
patterns = {
    "java_keywords": {"abstract", "assert", "boolean", "break", "byte", "case", "catch", "char",
                      "class", "const*", "**", "***", "****", "continue", "default", "do", "double",
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