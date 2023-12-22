class Document:
  
    def __init__(self, id, text):
        """
        The constructor for Document class.

        Parameters:
            id: A unique identifier for the document.
            text: The text of the document.
        """
        if not isinstance(id, int) or id < 0:
            raise ValueError("ID must be a non-negative integer")
        if not isinstance(text, str) or not text:
            raise ValueError("Text must be a non-empty string")
        self.id = id
        self.text = text.lower()  # convert to lower case

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def __repr__(self):
        return f"Document({self.id}, {self.text})"

    def __eq__(self, other):
        return self.id == other.id and self.text == other.text

    def __hash__(self):
        return hash((self.id, self.text))