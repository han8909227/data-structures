from setuptools import setup

setup(
    name='graph',
    package_dir={'': 'src'},
    py_modules=['graph'],
    author='Han and Phillip',
    author_email='hbao2016@hotmail.com',
    description='Data structure graph.',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
)


