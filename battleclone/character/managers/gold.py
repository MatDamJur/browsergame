from ..models import Character


class GoldManager:
    """ Class handling character level state (level up, information about need exp)"""

    def __init__(self, character: Character):
        self.character = character


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


