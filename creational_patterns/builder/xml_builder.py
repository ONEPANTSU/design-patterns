from creational_patterns.builder.article_builder import ArticleBuilder


class XMLBuilder(ArticleBuilder):
    def __init__(self):
        super().__init__()
        self.article.start = "<article>"
        self.article.end = "</article>"

    def set_title(self, title: str) -> "XMLBuilder":
        self.article.title = f"\t<title>{title}</title>"
        return self

    def set_authors(self, authors: list[str]) -> "XMLBuilder":
        authors = "\n".join([f"\t\t<author>{author}</author>" for author in authors])
        self.article.authors = f"\t<authors>\n{authors}\n\t</authors>"
        return self

    def set_text(self, text: str) -> "XMLBuilder":
        self.article.text = f"\t<text>\n\t\t{text}\n\t</text>"
        return self

    def set_hash(self, hash_code: str) -> "XMLBuilder":
        self.article.hash = f"\t<hash>{hash_code}</hash>"
        return self

    def save(self, file_name) -> None:
        with open(f"{file_name}.xml", "w+") as file:
            file.write(str(self.article))
