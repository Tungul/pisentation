import threading, socket, os, time

try:
	import androidhelper
	droid = androidhelper.Android()
except:
	print "oops, not on android."

startWebserver = False
shutdown = False
indir = "/sdcard/Pictures/Screenshots/" # android paths
outdir = "/sdcard/pisentation/" 

preexisting_files = os.listdir(indir)

def checkFileListUpdate():
	current_files = os.listdir(indir)
	for i in current_files:
		if i not in preexisting_files:
			try:
				os.rename(indir + i, outdir + "i.png")
				try:
					droid.alert("Screen ready.")
				except:
					print "oopsies, no android."
			except:
				print "what did you even DO to cause an error here?"
				shutdown = True

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
				time.sleep(0.25)
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
