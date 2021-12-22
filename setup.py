from setuptools import setup, find_packages

DESCRIPTION = 'Fast torrent parser from PirateBay.'
LONG_DESCRIPTION = "FastBay allows it's users to find the top result in PirateBay search and get it's link for a download."

# Setting up
setup(
    name="fastbay",
    version = '1.0'
    author="termit (Arsen Anoyan)",
    author_email="<anoyan2014@yandex.ru>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['bs4', 'requests'],
    keywords=['python', 'piratebay', 'search', 'parser', 'parsing', 'information'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)

