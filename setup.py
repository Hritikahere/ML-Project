from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements 
    '''
    requirements=[]
    with open('requirement.txt') as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
name='MLProject',
version='0.0.1',
author='Hritikahere',
author_email='hritika.sharma@mldc.edu.in',
packages=find_packages(),
install_requires=get_requirements('requirement.txt')

)