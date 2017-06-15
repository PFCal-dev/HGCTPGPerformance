from setuptools import setup

setup(
    name = 'hgc_tpg',
    version = '0.0.1',
    packages = ['hgc_tpg'],
    install_requires = [
        'attrs',
        'scipy',
        'numpy',
        'pandas',
        'root-numpy',
        'rootpy'
        ]
)
