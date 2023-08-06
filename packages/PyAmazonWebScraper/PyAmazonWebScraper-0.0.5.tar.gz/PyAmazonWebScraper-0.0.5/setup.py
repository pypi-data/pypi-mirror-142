from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='PyAmazonWebScraper',
  version='0.0.5',
  description='Python Web Scraper : Pranav Sai',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Pranav Sai',
  author_email='pranavs31899@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Python Web Scraper', 
  packages=find_packages(),
  install_requires=['bs4','requests','lxml'] 
)