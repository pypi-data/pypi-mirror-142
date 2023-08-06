from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Science/Research',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='CHPCDIANA',
  version='0.0.5',
  description='Implementation of the Divisive Analysis algorithm for clustering.',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Ismail EL Yamani, Salma EL Omari, Widad EL Moutaouakal, Youssef EL Mrabet',
  author_email='ismail.elyamani.2000@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Divisive Analysis', 
  packages=find_packages('DIANA'),
  install_requires=[''] 
)
