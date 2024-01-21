from abc import ABC, abstractmethod

from creational_patterns.abstract_factory.movie import Movie, Subtitles, Soundtrack


class AbstractFactory(ABC):
    @classmethod
    @abstractmethod
    def create_movie(cls, title: str) -> Movie:
        pass

    @classmethod
    @abstractmethod
    def create_subtitles(cls, movie: Movie) -> Subtitles:
        pass

    @classmethod
    @abstractmethod
    def create_soundtrack(cls, movie: Movie) -> Soundtrack:
        pass
