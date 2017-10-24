import persistent

class Condition(persistent.Persistent):

    def __init__(self, name, counter):
        self.name = name
        self.counter = counter