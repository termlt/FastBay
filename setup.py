from setuptools import setup, find_packages

DESCRIPTION = 'Fast torrent parser from PirateBay.'
LONG_DESCRIPTION = file: docs.md

# Setting up
setup(
    name="fastbay",
    version='90980908989',
    author="termit (Arsen Anoyan)",
    author_email="<anoyan2014@yandex.ru>",
    url="https://github.com/termlt/FastBay",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests'],
    keywords=['python', 'piratebay', 'search', 'parser', 'parsing', 'information'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
