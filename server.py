import threading, sockets, os

shutdown = False

# create an array or something of existing files in the screenshots directory, for comparison later.

existing_files = os.listdir("/sdcard/Pictures/Screenshots")

class Webserver(threading.Thread): # figure out how the hell webservers work in python
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True: # code here
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
				# check if a new file exists, then move it out
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