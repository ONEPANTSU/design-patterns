class Balloon:
    R = 8.314

    def __init__(self, volume: float, mass: float, molar: float) -> None:
        self.volume = volume
        self.mass = mass
        self.molar = molar

    def get_pressure(self, temperature: int | float) -> float:
        return (self.amount_of_matter() *
                self.volume *
                self.R *
                temperature)

    def amount_of_matter(self) -> float:
        return self.mass / self.molar

    def __str__(self):
        return (f"GasBalloon:\n"
                f"{self.volume=},\n"
                f"{self.mass=},\n"
                f"{self.molar=}")
