from setuptools import setup, find_packages


setup(
   name='pdf_toolbox',
   version='0.1.0',
   author='Samuel López Saura',
   author_email='samuellopezsaura@gmail.com',
   packages=find_packages(),
   license='MIT',
   description='A package to extract and store data from PDFs',
   long_description=open('README.md').read(),
   long_description_content_type="text/markdown",
   install_requires=[
       "textract==1.6.5",
   ],
)
