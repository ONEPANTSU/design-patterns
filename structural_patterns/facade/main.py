from structural_patterns.facade.tour_classes import Excursion, Accommodation
from structural_patterns.facade.tour_facade import TourFacade

excursions = [
    Excursion('Морской курорт', 2500),
    Excursion('Озеро', 5000),
]
accommodations = [
    Accommodation('Квартира', 1000),
]
tour = TourFacade(
    "Париж",
    excursions,
    accommodations
)
print(tour)