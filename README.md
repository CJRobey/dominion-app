# dominion-app
A tool for choosing good games of dominion


### TODO
* ~Make this mobile friendly (don't have a clue how to do that)~ (kind of done...)
* ~Have images of each character pull up when the final decisions have been made.~
* ~Add the "removed cards" into the game again~


## State of the Project
Currently, you may download this project and turn it into a perfectly fine MacOS application. But it seems that Toga/BeeWare does not support "clickable" buttons in iOS. I would love to be proven wrong. Please supply a pull request.

## Steps to use
1. Clone the repo (this may take a while because of the images needed to download)
2. `cd dominion-app`
3. If you would like to just run with Python, use the command `python3 RandomChars.py` (you may need to `pip install matplotlib`).
4. `cd beeware-app`
5. `source beeware-venv/bin/activate`
6. `briefcase run` (this should install and build on your system)

<br/>Note that I have only tested this with my Macbook Pro.
