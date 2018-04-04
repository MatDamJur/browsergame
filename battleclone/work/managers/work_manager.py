from ..models import Work
from datetime import datetime, timedelta, timezone
from collections import namedtuple

MONEY_PER_HOUR = 20
EXP_PER_HOUR = 5
Reward = namedtuple('Reward', 'money exp')


class WorkManager:
    def __init__(self, work: Work):
        self.work = work
        self.character = work.character

    def can_work(self):
        character_status = self.character.status
        return True if character_status is 'FREE' else False

    def is_finished(self):
        started, hours = self.work.started, self.work.work_type
        now = datetime.now(timezone.utc)

        if started + timedelta(hours=hours) > now:
            return False

        return True

    def get_reward(self):
        if self.is_finished():
            money = self.work.work_type * self.character.level * MONEY_PER_HOUR
            exp = self.work.work_type * self.character.level * EXP_PER_HOUR
            self.character.update_status('FREE')
            return Reward(money, exp)

        return None


