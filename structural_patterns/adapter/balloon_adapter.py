from structural_patterns.adapter.balloon import Balloon


class BalloonAdapter:
    def __init__(self, balloon: Balloon) -> None:
        self.balloon = balloon

    def calculate_dp(self,
                     start_temperature: int | float,
                     delta_temperature: int | float) -> float:
        """
        Изменение давления при заданной начальной температуре
        и изменении температуры.
        """
        return (self.balloon.get_pressure(start_temperature) -
                self.balloon.get_pressure(delta_temperature))

    def modify_mass(self, delta_mass: int | float) -> None:
        self.balloon.mass += delta_mass

    def get_data(self) -> str:
        return str(self.balloon)
