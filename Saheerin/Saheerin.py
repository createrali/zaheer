class Saheerin:
	'Common base class for all input'
	#def __init__(self):
		#print "constructing"

	def fetchInput(self, channels='keyboard',options={'intype':'text','text_label':'Enter your input : ','inforse':'false','interface_option':'raw'}):
		inkey=''
		if (channels=="keyboard") :
			inkey =  self.keyboardInput(options)
		else :
			print "no type recived"
		return inkey

	def keyboardInput(self, options):
		inkey=''
		if (options['interface_option']=="raw") :
			inkey = raw_input(options['text_label'])
		elif (options['interface_option']=="input") :
			inkey = input(options['text_label'])
		return inkey