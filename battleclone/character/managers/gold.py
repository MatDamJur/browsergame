from typing import Callable


class GoldManager:
    """ Class handling character level state (level up, information about need exp)"""

    def __init__(self, character):
        self.character = character

    def update(self, amount: int):
        return self.add_gold(amount) if amount > 0 else self.remove_gold(amount)

    def add_gold(self, amount: int) -> int:
        self.character.gold += amount
        self.character.save()

        return self.character.gold

    def remove_gold(self, amount: int):
        if amount <= self.character.gold:
            self.character.gold -= amount
            self.character.save()
            return self.character.gold

        return None
