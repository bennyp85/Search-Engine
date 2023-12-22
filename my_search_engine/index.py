from collections import defaultdict
from utils import tokenize


class Index:
    def __init__(self):
        self.index = defaultdict(list)

    def add_document(self, document):
        tokens = tokenize(document.text)
        for token in tokens:
            self.index[token].append(document)

    def search(self, query):
        query_tokens = tokenize(query)
        results = []
        for token in query_tokens:
            if token in self.index:
                results.extend(self.index[token])
        return results