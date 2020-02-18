# dominion-app
A tool for choosing good games of dominion


### TODO
* Make the application user-interactive (what games, etc) - maybe create a conf file that gets set the first time, but then can be edited
* Make this mobile friendly (don't have a clue how to do that)
* Have images of each character pull up when the final decisions have been made.
* Add the "removed cards" into the game again


## State of the Project
Currently, you may download this project and turn it into a perfectly fine MacOS application. But it seems that Toga/BeeWare does not support "clickable" buttons in iOS. I would love to be proven wrong. Please supply a pull request.

## Steps to use
1. Clone the repo
2. cd dominion-app
3a. If you would like to just run with Python, use the command "python3 RandomChars.py" (you may need to "pip install matplotlib").
3b. cd beeware-app
4. source beeware-venv/bin/activate
5. briefcase run (this should install and build on your system)
