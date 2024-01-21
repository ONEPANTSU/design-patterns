from creational_patterns.builder.article_builder import ArticleBuilder


class ArticleDirector:
    def __init__(self, builder: ArticleBuilder):
        self.builder = builder

    def construct(
        self,
        title: str = "",
        authors: str = "",
        text: str = "",
        hash_code: str = "",
        file_name: str = "text/article",
    ):
        (
            self.builder.set_title(title)
            .set_authors(authors)
            .set_text(text)
            .set_hash(hash_code)
            .save(file_name)
        )
