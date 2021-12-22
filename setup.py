from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "docs.md").read_text()

setup(
    name="fastbay",
    version='0.1',
    author="termit (Arsen Anoyan)",
    author_email="<anoyan2014@yandex.ru>",
    url="https://github.com/termlt/FastBay",
    description='Fast torrent parser from PirateBay.',
    long_description_content_type="text/markdown",
    long_description=long_description,
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
