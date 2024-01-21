from creational_patterns.abstract_factory.client import Client
from creational_patterns.abstract_factory.en_factory import ENFactory
from creational_patterns.abstract_factory.ru_factory import RUFactory

movie_title = "Barbie"

movie_info_ru = Client(factory=RUFactory).get_movie(title=movie_title)
movie_info_en = Client(factory=ENFactory).get_movie(title=movie_title)
