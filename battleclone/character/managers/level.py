from ..models import Character


class LevelManager:
    """ Class handling character level state (level up, information about need exp)"""

    def __init__(self, character: Character):
        self.character = character

    def next_level_value(self) -> int:
        """ Return needed next level points"""

        # for low level characters we need more smooth exp grind IMO
        if self.character.level < 10:
            exp_for_level = 4 + self.character.level * self.character.level
            return exp_for_level
        # for higher level characters
        exp_for_level = self.character.level * self.character.level
        return exp_for_level

    def can_level_up(self) -> bool:
        current_exp = self.character.experience_points
        needed_points = self.next_level_value()
        return True if current_exp - needed_points > 0 else False

    def level_up(self) -> bool:
        if self.can_level_up():
            self.character.level += 1
            self.character.save()
            return True
        return False






