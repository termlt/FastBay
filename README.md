# FastBay

FastBay - is a script, that allows it's users to find the best (first) result in PirateBay search and get it's link for a download.

This is a fast way of finding the file you need, not opening your browser. 
You just need to enter the keyword and the script will bring the top result's Information, as well as a Magnet Link, so you are able to download the file.

Sometimes you may notice, that it is not possible to download the torrent as it is loading forever. That's a problem of either PirateBay or the user who uploaded the torrent. In such case try "playing" with keywords, so you will get the result you want.


## Installation

```
pip install FastBay
```


## Usage
**EXAMPLE 1**

```
from fastbay import fb

fb = fb('Search String')

fb.main()
```


**EXAMPLE 2**

```
from fastbay import fb

search = input('Search: ')

fb = fb(search)

fb.main()
```
