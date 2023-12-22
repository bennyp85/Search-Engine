from document import Document
from index import Index
from utils import tokenize
from engine import SearchEngine


def main():
    # Create a search engine
    engine = SearchEngine()

    # Add some documents to the engine
    doc1 = Document(1, "This is the first document.")
    doc2 = Document(2, "This is the second document.")
    engine.add_document(doc1)
    engine.add_document(doc2)

    # Execute a search query
    userQuery = input("Enter your search query: ")
    results = engine.search(userQuery)

    # Print the results
    for doc in results:
        print(doc)

if __name__ == "__main__":
    main()