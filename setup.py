from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_the_reqd(file_path:str)->List[str]:
    ''' this function is useful for you to get the requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
        
setup(
    name='END_TO_END_ML_PROJECT',
    version='0.0.1',
    author='Aniruddhan N',
    author_email='aniruddhan.n2021@vitstudent.ac.in',
    packages=find_packages(),
    install_requires=get_the_reqd('requirements.txt')
    
)


