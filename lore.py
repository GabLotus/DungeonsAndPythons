import persistent

class Lore(persistent.Persistent):

    def __init__(self):
        self.entries = {}

    def addLoreEntry(self, entry, content):
        self.entries[entry] = content
        self._p_changed = True

    def removeLoreEntry(self, entry):
        del self.entries[entry]
        self._p_changed = True