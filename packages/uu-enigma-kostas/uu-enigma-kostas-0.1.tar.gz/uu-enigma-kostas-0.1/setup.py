# setup.py
from setuptools import setup
from setuptools import find_packages

setup(name='uu-enigma-kostas',
    version='0.1',
    description='An enigma-like simulator. Encrypts/Decrypts messages, given some enigma settings.',
    url='https://github.com/KPapac/Advanced_python_project',
    author='Konstantinos Papachristos',
    author_email='kostaspapac@gmail.com',
    license='BSD',
    package_dir={"": "src"},
    packages=find_packages(where="src")
)
 
