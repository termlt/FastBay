from setuptools import setup, Extension

with open("description.md", "r") as f:
    long_description = f.read()


setup(
  name = 'FastBay1',
  version = '1.0',
  license= 'MIT',
  description = "FastBay - is a script that allows it's users to find the best (first) result in PirateBay search and get it's link for a download.",
  author = 'termit',
  author_email = 'anoyan2014@yandex.ru',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/termlt/FastBay',
  keywords = ['piratebay', 'search', 'fast', 'fast search', 'FastBay', 'FastBay1'],
  install_requires=[
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3.8',
  ],
)
