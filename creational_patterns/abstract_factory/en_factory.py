from creational_patterns.abstract_factory.abstract_factory import AbstractFactory
from creational_patterns.abstract_factory.movie import Movie, Soundtrack, Subtitles, Language


class ENFactory(AbstractFactory):

    @classmethod
    def create_movie(cls, title: str) -> Movie:
        return Movie(title=title)

    @classmethod
    def create_subtitles(cls, movie: Movie) -> Subtitles:
        return Subtitles(movie=movie, language=Language.EN)

    @classmethod
    def create_soundtrack(cls, movie: Movie) -> Soundtrack:
        return Soundtrack(movie=movie, language=Language.EN)
