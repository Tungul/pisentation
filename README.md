pisentation
===========

A method for 'screen sharing' using non-rooted Android devices and the Raspberry PI.

Quotes are used around screen sharing because it isn't actually screen sharing, it's just showing screenshots easily and automatically onto a TV.

To use:

* Checkout 132fddb3d3.
* Install the kws webserver from the play store.
* Configure webserver path.
* Install qpython from the play store. Alternatively, SL4A should work just fine.
* Configure server.py with the correct paths to the directory where screenshots are saved, and the webservers directory.
* Copy index.html to webserver directory.
* Copy server.py to /sdcard/com.hipipal.qpyplus/scripts/, or your SL4A scripts directory.
* Start webserver.
* Open qpython, tap the big black area with a circle in it > run local script > server.py
* Take a screenshot using your devices gesture, hotkey, key combination, or whatever you use.
* Open a web browser on another device and connect to your device using the webserver configuration.
* ???
* Refresh the page or click the image to refresh the image.