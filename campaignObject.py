import persistent
from party import Party
class Campaign(persistent.Persistent):
    def __init__(self):
        self.name = ""
        self.test_array = []

    def newParty(self):
        self.party = Party()
        self._p_changed = True

