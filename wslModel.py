import subprocess
from wslDistribution import Distribution
distribution_objects=list()

def list_distribution():
    result = subprocess.run(['wsl', '--list', '--verbose'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-16').replace('*'," ")
    distributions = output.strip().split('\n')
    distributions.pop(0)
    global distribution_objects
    distribution_objects=[]
    for distribution in distributions:
        name, state,version = distribution.split()
        distribution_objects.append(Distribution(name, version, state))
    return distribution_objects