from structural_patterns.facade.tour_classes import Accommodation, Excursion


class TourFacade:
    def __init__(
            self,
            place: str,
            excursion: Excursion | list[Excursion],
            accommodation: Accommodation | list[Accommodation]
    ):
        self.place = place
        self.excursion = excursion
        self.accommodation = accommodation

    def __str__(self):
        return (
            f"Тур в {self.place}\n"
            f"{self.excursion if isinstance(self.excursion, Excursion) else [ex for ex in self.excursion]}\n"
            f"{self.accommodation if isinstance(self.accommodation, Accommodation) else [ac for ac in self.accommodation]}\n"
        )
