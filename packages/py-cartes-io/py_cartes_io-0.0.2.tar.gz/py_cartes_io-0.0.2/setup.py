from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Cartes.io official Python API wrapper'
LONG_DESCRIPTION = 'Cartes.io'

# Setting up
setup(
    # the name must match the folder name 'verysimplemodule'
    name="py_cartes_io",
    version=VERSION,
    author="M Media",
    author_email="<contact@mmediagroup.fr>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'requests',
    ],  # add any additional packages that
    # needs to be installed along with your package. Eg: 'caer'

    keywords=['python', 'cartes', 'cartes.io', 'api'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
