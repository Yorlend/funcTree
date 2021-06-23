from setuptools import find_packages, setup

setup(
    name='cfunctree',
    packages=find_packages(include=['cfunctree']),
    version='0.1.0',
    description='Graphical visualization of function calls in c programmes',
    author='Yorlend, Rull Deef',
    license='MIT',
    install_requires=[
        'pycparser==2.20',
        'graphviz==0.16',
        'pcpp==1.22',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==6.2.4'],
    test_suite='tests',
    entry_points={
        "console_scripts": [
            "cfunctree = cfunctree.entrypoint:main"
        ]
    },
)
