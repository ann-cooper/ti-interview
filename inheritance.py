from pathlib import Path

class FileHandler:
    """Base class for handling files.

    Attributes
    ----------
    next_handler: callable
        Which handler to try next.
    
    Methods
    -------
    handle(filepath)
        Passes file to next_handler if needed.
    """
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, filepath):
        return self.next_handler.handle(filepath)

class CSVHandler(FileHandler):
    def __init__(self):
        super().__init__(next_handler=PDFHandler())
    def handle(self, filepath):
        if Path(filepath).suffix == ".csv":
            print(f"Handling {filepath}.")
            return True
        else:
            return super().handle(filepath)

class PDFHandler(FileHandler):
    def handle(self, filepath):
        if Path(filepath).suffix == ".pdf":
            print(f"Handling {filepath}.")
            return True
        else:
            print(f"No handler available for {filepath}")

"""
It's possible to implement the Chain of Responsibility pattern like this, 
but it's a little difficult to reason about and that could make it harder to
maintain.
We can also do the same work in the way shown below, but we lose the 
Chain of Responsibility pattern.
"""
def csv_processor(filepath: str) -> bool:
    print (f"Handling {filepath}.")
    return True


def pdf_processor(filepath: str) -> bool:
    print (f"Handling {filepath}.")
    return True

"""
This example adheres to the zen of python 'composition over inheritance'.
Of course, we could just import and refer to the functions we want to use, we don't have
to make them attributes of the class, but making them attributes of the class
allows for tests that are simpler and easier to read and reason about tests because we don't have to use
mock.patch, we can just supply our own fake functions for testing.
"""

class AnotherFileHandler:

    def __init__(self, filepath):
        self.filepath = filepath
        self.csv_processor = csv_processor
        self.pdf_processor = pdf_processor

    def process(self):
        file_type = Path(self.filepath).suffix
        if file_type == ".csv":
            return self.csv_processor(self.filepath)
        elif file_type == ".pdf":
            return self.pdf_processor(self.filepath)
        else:
            print(f"{self.filepath} suffix not handled")
            return False
