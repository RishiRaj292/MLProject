from setuptools import find_packages,setup
from typing import List

hyphen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    '''file path will be in the form of string and list will be returned  in the form of str '''
    '''this function will return a list of requirements'''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()#this readlines reads each line anto this list,as we have learnt in file handling in python
        #next , we write a list comprehension , as each line comes with a new line character
        #ALSO ,JUST FOR CLARIFICATION , WE WOULD USUALLY ITERATE IN THE CASE OF FILE HANDLING , SO THAT IS HOW THESE NEWLINE CHARACTERS WOULD HAVE BEEN HANDLED
        #we use list comprehension for this -
        requirements=[req.replace("\n","")  for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements
setup(#this can be used in the pipeline, this is kind of like metadata 
name='mlproject',
version='0.0.1',
author='Rishi Raj',
author_email='nahsorjar09@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn']
install_requires=get_requirements('requirements.txt')
)