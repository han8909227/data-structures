from setuptools import setup

setup(
    name='data structure',
    package_dir={'': 'src'},
    py_modules=['bst', 'graph_1', 'dll', 'stack', 'deque', 'binheap', 'deque', 'que_', 'priorityq', 'hash_', 'trie', 'bubble_sort', 'insertion_sort'],
    author='Han',
    author_email='hbao2016@hotmail.com',
    description='Data structure graph.',
    install_requires=[],
    extras_require={
        "test": ["pytest", "pytest-cov", "tox"]
    })