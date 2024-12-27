from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This Function return list of requirements

    """
    requirements_lst=[]
    try:
        with open('requirements.txt','r') as f:
            # Read Lines form file
            lines = f.readlines()
            #process the each line
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement!= '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requirements_lst


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Gnana Chaithanya",
    author_email="m.gnanachaithanya12@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements()
)