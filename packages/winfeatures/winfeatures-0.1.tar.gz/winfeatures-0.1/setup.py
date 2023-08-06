from distutils.core import setup
setup(
  name = 'winfeatures',
  packages = ['winfeatures'],
  version = '0.1',
  license='MIT',
  description = 'Turn Windows Features On or Off through DISM with Python',
  author = 'Tan (weareblahs)',
  author_email = 'tanyuxuan2005@gmail.com',
  url = 'https://github.com/weareblahs/winfeatures_py',
  download_url = 'https://github.com/weareblahs/winfeatures_py/archive/refs/heads/main.tar.gz',
  keywords = ['windows', 'windows features', 'dism'],
  install_requires=[
          'os',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)