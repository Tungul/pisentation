import threading, socket, os, time

startWebserver = False
shutdown = False
# debug = True
indir = "screenin/"
outdir = "screenout/"

preexisting_files = os.listdir(indir)

def checkFileListUpdate():
	current_files = os.listdir(indir)
	for i in current_files:
		if i not in preexisting_files:
			try:
				os.rename(indir + i, outdir + "i.png")
			except:
				print "what did you even DO to cause an error here?"
				shutdown = True

class Webserver(threading.Thread): # figure out how webservers work in python
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True: # code goes here # http://docs.python.org/2/howto/sockets.html
			if shutdown:
				print "shutting down webserver thread"
				break # can one exit() threads?

class ScreenshotMonitor(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)

	def run(self):
		while True:
			try:
				if shutdown:
					print "shutting down screenshot monitor thread"
					break # can one exit() threads?
				checkFileListUpdate()
				time.sleep(1)
			except: # some error
				continue

if startWebserver:
	webServer = Webserver()
	webServer.start()

screenShotMonitor = ScreenshotMonitor()
screenShotMonitor.start()

while True:
	try:
		pass
	except KeyboardInterrupt:
		shutdown = True
		print "shutting down threads..."

quit()
