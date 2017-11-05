from setuptools import setup

setup(
    name='stack',
    package_dir={'': 'src'},
    py_modules=['stack'],
    author='Han and Phillip',
    author_email='hbao2016@hotmail.com',
    description='Data structure stack.',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
)


