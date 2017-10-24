import persistent
class Campaign(persistent.Persistent):
    def __init__(self):
        self.name = ""
        self.test_array = []

