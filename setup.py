from setuptools import setup, find_packages

setup(
    name='edsa-packages',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA hackathon recursion and sorting python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/RLSwanepoel/edsa_packages',
    author='Riaan Louis Swanepoel',
    author_email='riaan.swanepoel91@gmail.com'
)
