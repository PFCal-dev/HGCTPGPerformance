from setuptools import setup

setup(
    name = 'hgc_tpg',
    version = '0.1.0',
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
