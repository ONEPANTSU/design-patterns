class Article:
    def __init__(self):
        self.start = ""
        self.title = ""
        self.authors = ""
        self.text = ""
        self.hash = ""
        self.end = ""

    def __str__(self):
        return (
            self.start + "\n\n" +
            self.title + "\n\n" +
            self.authors + "\n\n" +
            self.text + "\n\n" +
            self.hash + "\n\n" +
            self.end
        )
