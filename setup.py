from setuptools import setup

setup(
    name='queue',
    package_dir={'': 'src'},
    py_modules=['queue'],
    author='Han and Phillip',
    author_email='fortunato.maycotte@gmail.com',
    description='Emails to donors and organizes contributions',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
    # entry_points={'console_scripts': ['queue = linked_list:__init__']}
)
