import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='func_adl_uproot',
                 version='1.8.2',
                 description=('Functional Analysis Description Language'
                              + ' uproot backend for accessing flat ROOT ntuples'),
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 packages=setuptools.find_packages(exclude=['tests']),
                 python_requires=('>=3.6, <3.11'),
                 install_requires=['awkward>=1.2',
                                   'func-adl>=2.2.1',
                                   'numpy',
                                   'qastle>=0.14.0',
                                   'uproot>=4.1.3',
                                   'vector'],
                 extras_require={'test': ['flake8', 'pytest', 'pytest-cov']},
                 author='Mason Proffitt',
                 author_email='masonlp@uw.edu',
                 url='https://github.com/iris-hep/func_adl_uproot')
