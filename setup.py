from setuptools import setup, find_namespace_packages

setup(
    name='project-pycliapp',
    version='0.1',
    py_modules=['main'],
    packages=find_namespace_packages(where="src"),
    package_dir={"": "src"},
    entry_points={
        'console_scripts': [
            'project-pycliapp=main:main',
        ],
    },
)