import persistent
from party import Party
from lore import Lore
class Campaign(persistent.Persistent):
    def __init__(self, name = ""):
        self.name = name
        self.lore = Lore()

    def newParty(self):
        self.party = Party()
        self._p_changed = True

    def addLoreEntry(self, entry, content):
        self.lore.addLoreEntry(entry, content)
        self._p_changed = True

    def addPlayer(self, name):
        self.party.addPlayer(name)
        self._p_changed = True

    def setName(self, name):
        self.name = name
        self._p_changed = True
