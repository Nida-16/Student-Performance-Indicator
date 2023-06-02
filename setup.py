from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns modules from requirements.txt as a list of string to be installed
    "-e ." -> automatically triggers setup.py (last line of requirements.txt)
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements = f.readlines()
        requirements = [line.replace("\n", "") for line in requirements]
        
        if(HYPHEN_E_DOT in requirements):
            requirements.remove(HYPHEN_E_DOT)
        
    return requirements


# Metadata of the project
setup(
    name='Student-Performance-Indicator',
    version='0.0.1',
    author='Nidaaa',
    author_email='nidashaikh16@eng.rizvi.edu.in',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
