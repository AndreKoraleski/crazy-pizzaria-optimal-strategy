from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='crazy_pizzaria',
    version='0.1.0',
    description='n optimal strategy and simulation suite for the Crazy Pizzaria board game.',
    author='Andre Koraleski',
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'run-random-pizzaria-game=scripts.test_random_game:main'
        ]
    }
)