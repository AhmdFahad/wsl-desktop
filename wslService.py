import subprocess
from wslDistribution import Distribution
from wslModel import distribution_objects



def shutdown_distrobution(name:str):
    subprocess.run(['wsl','-t',name])

def run_distrobution(name:str()):
    subprocess.run(['wsl','-e',name])

