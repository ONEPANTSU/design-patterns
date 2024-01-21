from abc import ABC, abstractmethod

from creational_patterns.builder.article import Article


class ArticleBuilder(ABC):
    def __init__(self) -> None:
        self.article = Article()

    @abstractmethod
    def set_title(self, title: str) -> "ArticleBuilder":
        pass

    @abstractmethod
    def set_authors(self, authors: list[str]) -> "ArticleBuilder":
        pass

    @abstractmethod
    def set_text(self, text: str) -> "ArticleBuilder":
        pass

    @abstractmethod
    def set_hash(self, hash_code: str) -> "ArticleBuilder":
        pass

    @abstractmethod
    def save(self, file_name: str) -> None:
        pass
