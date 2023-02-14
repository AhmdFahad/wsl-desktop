class Distribution:
    def __init__(self, name, version, status):
        self.name = name
        self.version = version
        self.status = status

    def __repr__(self):
        return f'{self.name} ({self.version}) - {self.status}'


