from setuptools import setup

setup(
    name='dequeue',
    package_dir={'': 'src'},
    py_modules=['dequeue'],
    author='Han and Phillip',
    author_email='hbao2016@hotmail.com',
    description='Data structure graph.',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}

)
