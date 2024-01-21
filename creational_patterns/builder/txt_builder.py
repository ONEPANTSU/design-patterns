from creational_patterns.builder.article_builder import ArticleBuilder


class TXTBuilder(ArticleBuilder):
    def set_title(self, title: str) -> "TXTBuilder":
        self.article.title = f"Title: {title}"
        return self

    def set_authors(self, authors: list[str]) -> "TXTBuilder":
        self.article.authors = f"Authors: {'; '.join(authors)}"
        return self

    def set_text(self, text: str) -> "TXTBuilder":
        self.article.text = f"Text: {text}"
        return self

    def set_hash(self, hash_code: str) -> "TXTBuilder":
        self.article.hash = f"Hash code: {hash_code}"
        return self

    def save(self, file_name) -> None:
        with open(f"{file_name}.txt", "w+") as file:
            file.write(str(self.article))
