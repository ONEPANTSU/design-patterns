from enum import Enum


class Language(Enum):
    EN = "EN"
    RU = "RU"


class Movie:
    def __init__(self, title: str) -> None:
        self.title = title

    def __str__(self) -> str:
        return self.title


class Subtitles:
    def __init__(self, movie: Movie, language: Language) -> None:
        self.movie = movie
        self.language = language

    def __str__(self) -> str:
        return f"{self.language.value}"


class Soundtrack:
    def __init__(self, movie: Movie, language: Language) -> None:
        self.movie = movie
        self.language = language

    def __str__(self) -> str:
        return f"{self.language.value}"
