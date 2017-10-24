import persistent
from player import Player

class Party(persistent.Persistent):

    def __init__(self):
        self.players = {}
        self._p_changed = True

    def addPlayer(self, name):
        if name not in self.players:
            self.players[name] = Player(name)
            self._p_changed = True
        # Manage exception

    def removePlayer(self, name):
        if name in self.players:
            del self.players[name]
            self._p_changed = True
