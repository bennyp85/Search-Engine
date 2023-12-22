class SearchQuery:
    """Search query class.
    Attributes:
        query: A string representing the search query.
    """
    
    def __init__(self, query):
        if not isinstance(query, str) or not query:
            raise ValueError("Query must be a non-empty string")
        self.query = query.lower()  # convert to lower case

    def execute(self, engine):
        results = engine.search(self.query)
        # rank the results based on the number of query terms they contain
        results.sort(key=lambda doc: sum(word in doc.text for word in self.query.split()), reverse=True)
        return results