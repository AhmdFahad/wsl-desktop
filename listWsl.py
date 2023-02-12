import subprocess
from wslDistribution import Distribution
class Distribution:
    def __init__(self, name, version, state):
        self.name = name
        self.version = version
        self.state = state

    def __repr__(self):
        return f'{self.name} ({self.version}) - {self.state}'

result = subprocess.run(['wsl', '--list', '--verbose'], stdout=subprocess.PIPE)
output = result.stdout.decode('utf-16').replace('*'," ")
distributions = output.strip().split('\n')
distributions.pop(0)

distribution_objects = []
for distribution in distributions:
    name, version, state = distribution.split()
    distribution_objects.append(Distribution(name, version, state))
for distribution in distribution_objects:
    print(distribution)
