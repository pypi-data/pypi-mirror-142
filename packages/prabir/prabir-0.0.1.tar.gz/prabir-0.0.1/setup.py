# import os
from setuptools import setup, find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# def read(fname):
#     return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "prabir", # project name
    version = "0.0.1",
    author = "Prabir Debnath",
    author_email = "prabirdeb@gmail.com",
    description = "This is a data science related question asnwering model for the beginners",
    license = "MIT",
    url = "",
    packages=find_packages(),
    install_requires=['numpy','pandas', 're', 'nltk', 'spacy', 'gensim']
    # keywords = ""
    # long_description=read('README.txt'),
    # classifiers=[
    #     "Development Status :: 3 - Alpha",
    #     "Topic :: Utilities",
    #     "License :: OSI Approved :: BSD License",
    # ],
)