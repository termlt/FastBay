# Official docs for FastBay.

# Installation
To use **FastBay**, first install it using pip:
```
pip install fastbay
```

# Usage
Firstly you need to import FastBay to your project. To do so, use:
```
from fastbay import fbay
```

#
**NOTE** 

Please be careful as sometimes you will need to provide the whole name of a torrent.

*Example:*

**WRONG**: charlie and the choco

**RIGHT**: charlie and the chocolate factory

#
Let's see how to get a torrent title.
```
from fastbay import fbay

fbay = fbay('poirot')
print(fbay.title())
```
As you can see here, we are firstly importing fastbay and after that on line 3, we are providing the name of the torrent.

#
Now let's have a look on how to get the download link for our torrent.
```
from fastbay import fbay

fbay = fbay('poirot')
print(fbay.link())
```

#
Final step is to get some info about the file we are going to download. To get that, we will use:
```
from fastbay import fbay

fbay = fbay('poirot')
print(fbay.info())
```

#
# Now let's get this all by simply using:
```
from fastbay import fbay

fbay = fbay('poirot')
print(fbay.title())
print(fbay.link())
print(fbay.info())
```
