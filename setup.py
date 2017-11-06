from setuptools import setup

setup(
    name='dll',
    package_dir={'': 'src'},
    py_modules=['dll'],
    author='Han and Phillip',
    author_email='fortunato.maycotte@gmail.com',
    description='Emails to donors and organizes contributions',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
    # entry_points={'console_scripts': ['dll = dll:__init__']}
)
