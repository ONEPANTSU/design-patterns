class Excursion:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return (
            f"\nЭкскурсия: {self.name}\n"
            f"Стоимость билета: {self.price}\n"
        )


class Accommodation:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return (
            f'\nТип размещения: {self.name} \n'
            f'посуточная цена: {self.price}\n'
        )
