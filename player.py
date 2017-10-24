import persistent
from condition import Condition

class Player(persistent.Persistent):
    def __init__(self, name):
        self.name = name
        self.max_hp = 0
        self.hp = 0
        self.conditions = []

    def damage(self, amount):
        self.hp -= amount
        self._p_changed = True

    def status(self):
        if hp <= -10:
            return "Dead"
        elif hp <= 0:
            return "Unconcious"
        else:
            return "Alive"

    def addCondition(self, condition, duration):
        self.conditions.append(Condition(condition, duration))

    def decrementConditions(self):
        newConditions = []
        for index, condition in enumerate(self.conditions):
            condition.counter -= 1
            if condition.counter > 0:
                newConditions.append(condition)
                condition._p_changed = True
        self.conditions = newConditions
        self._p_changed = True


