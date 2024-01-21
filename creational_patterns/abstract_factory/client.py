from creational_patterns.abstract_factory.abstract_factory import AbstractFactory
from creational_patterns.abstract_factory.movie import Soundtrack, Subtitles, Movie


class Client:
    def __init__(self, factory: type[AbstractFactory]) -> None:
        self.factory = factory

    def get_movie(self, title: str) -> tuple[Movie, Subtitles, Soundtrack]:
        movie = self.factory.create_movie(title=title)
        subtitles = self.factory.create_subtitles(movie=movie)
        soundtrack = self.factory.create_soundtrack(movie=movie)
        print(f"Movie:\t{movie}\n"
              f"Subtitles:\t{subtitles}\n"
              f"Soundtrack:\t{soundtrack}\n")
        return movie, subtitles, soundtrack
