from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='degreesconv',
    version='2.1.0',
    package_dir={'degreesconv': 'degreesconv',
                 'degreesconv.converter': 'degreesconv/converter',
                 'degreesconv.parser': 'degreesconv/parser'},
    packages=['degreesconv', 'degreesconv.converter', 'degreesconv.parser'],
    author="Alexey Voevoda",
    author_email="AVayavoda@gomel.iba.by",
    description="Temperature converter app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.7",
    entry_points={
        'console_scripts': [
            'degreesconv = degreesconv.start:main'
        ]
    })
