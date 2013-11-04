import threading, sockets

shutdown = False

# create an array or list or something of existing files in the screenshots directory, for comparison later.

class Webserver(threading.Thread): # figure out how the hell webservers work in python
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True: # code here # http://docs.python.org/2/howto/sockets.html
			if shutdown == True:
				break

class ScreenshotMonitor(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:
			try:
				if shutdown == True:
					break
				# check if a new file exists, then move it out http://docs.python.org/2/library/filecmp.html
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