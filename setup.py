from setuptools import setup

setup(
    name='linked_list',
    package_dir={'': 'src'},
    py_modules=['linked_list'],
    author='Han and Phillip',
    author_email='fortunato.maycotte@gmail.com',
    description='Emails to donors and organizes contributions',
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
    # entry_points={'console_scripts': ['linked_list = linked_list:__init__']}
)
