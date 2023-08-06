from setuptools import setup, find_packages

VERSION = '0.1.11' 
DESCRIPTION = 'Botnoi speech to text client'
LONG_DESCRIPTION = ''

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="bnasr", 
        version=VERSION,
        author="Peerapon Wechsuwanmanee",
        author_email="peerapon.w@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=[
            'grpcio',
            'protobuf',
            ], 
        
        keywords=['python', 'speech recognition', 'speech to text', 'botnoi'],
        classifiers= [
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)