class Saheerout:
	'Common base class for all output'
	activeoutbuffer = []
	def __init__(self, data='', options={}):
		if (data!=''):
			self.addOutput(data, options)

	def displayCount(self):
		print "Total Active Output is %d" % len(Saheerout.activeoutbuffer)

	def addOutput(self, data, options):
		if (options == 1) :
			print data
		else :
			Saheerout.activeoutbuffer.append(["sah_string",data,options])