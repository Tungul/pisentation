import threading, sockets, os, time

shutdown = False
debug = True
screendir = "sdcard/Pictures/Screenshots"

preexisting_files = os.listdir(screendir)

def checkFileListUpdate():
	current_files = os.listdir(screendir)
	for i in current_files:
		if i not in preexisting_files:
			# move file to webserver directory

class Webserver(threading.Thread): # figure out how webservers work in python
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True: # code goes here # http://docs.python.org/2/howto/sockets.html
			if shutdown == True:
				break # can one exit() threads?

class ScreenshotMonitor(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:
			try:
				if shutdown == True:
					break # can one exit() threads?
				checkFileListUpdate()
				time.sleep(1)
			except: # some error
				continue

webServer = Webserver()
screenShotMonitor = ScreenshotMonitor()
webServer.start()
screenShotMonitor.start()

while True:
	try:
		pass
	except KeyboardInterrupt:
		shutdown = True

quit()
