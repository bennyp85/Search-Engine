from document import Document
from index import Index


class SearchEngine:
    """Search engine class.

    Attributes:
        index: An Index object.
    """

    def __init__(self):
        self.index = Index()

    def add_document(self, document):
        """Add a document to the index."""
        if not isinstance(document, Document):
            raise ValueError("Input must be a Document object")
        self.index.add_document(document)

    def search(self, query):
        """Search the index for a query and return the results."""
        if not isinstance(query, str):
            raise ValueError("Query must be a string")
        return self.index.search(query)

    def dump(self):
        """Save the index to a file."""
        # TODO: Implement this method

    def load(self, dump):
        """Load the index from a file."""
        # TODO: Implement this method