from setuptools import setup

setup(
    name='project-pycliapp',
    version='0.1',
    py_modules=['main'],
    entry_points={
        'console_scripts': [
            'project-pycliapp=main:main',
        ],
    },
)