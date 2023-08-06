from setuptools import setup

setup(
    name="navdreams",
    description='NavDreams python package, including simulator and tools',
    author='Daniel Dugas',
    version='0.0.2',
    packages=["navdreams",
              ],
    python_requires='>=3.6, <3.7',
    install_requires=[
        'numpy', 'matplotlib',
        'pyrvo2-danieldugas',
        'matplotlib',
        'pyyaml',
        'stable-baselines3',
        'pyglet',
        'navrep',
        'typer',
        'strictfire',
        'jedi==0.17', # jedi because newer versions break ipython (py3.6)
        'gym==0.18.0', #  gym error in (py3.6) https://stackoverflow.com/questions/69520829/openai-gym-attributeerror-module-contextlib-has-no-attribute-nullcontext
    ],
)
