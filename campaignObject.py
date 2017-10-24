import persistent
from party import Party
from lore import Lore
class Campaign(persistent.Persistent):
    def __init__(self):
        self.name = ""
        self.test_array = []
        self.lore = Lore()

    def newParty(self):
        self.party = Party()
        self._p_changed = True


    def addLoreEntry(self, entry, content):
        self.lore.addLoreEntry(entry, content)
        self._p_changed = True
