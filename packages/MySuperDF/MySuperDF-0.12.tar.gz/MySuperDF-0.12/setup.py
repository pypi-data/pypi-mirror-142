import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
     name='MySuperDF',
     version="0.012",
     scripts=['main.py'] ,
     author="Paul Ledesma",
     author_email="paul.ledesma@hotmail.fr",
     description="A package for handling dataframes",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/Pauloledes/MySuperDataFrame",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )