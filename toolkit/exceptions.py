\"\"\"Custom toolkit exceptions.\"\"\"

class ToolkitException(Exception):
    \"\"\"Base exception for data toolkit.\"\"\"
    pass

class EmptyDatasetException(ToolkitException):
    \"\"\"Raised when dataset is empty.\"\"\"
    pass

class InvalidColumnException(ToolkitException):
    \"\"\"Raised when column is missing.\"\"\"
    pass
