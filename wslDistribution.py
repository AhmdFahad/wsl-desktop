class Distribution:
    def __init__(self, name, version, state):
        self.name = name
        self.version = version
        self.state = state

    def __repr__(self):
        return f'{self.name} ({self.version}) - {self.state}'
