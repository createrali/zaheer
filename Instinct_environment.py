execfile("./master_include.py")

class Instinct_environment:
	#class to listen for the input continusly 
	#or 
	#at regular interval 
	#or as per requirment when it is invoked.

	inhandel = ''
	outhandel = ''
	def __init__(self,listen='no'):
		self.inhandel = Saheerin.Saheerin()
		self.outhandel = Saheerout.Saheerout()
		if (listen=="yes") :
			self.infant_environment_aware()
		return

	def infant_environment_aware(self):
		self.outhandel.addOutput(self.inhandel.fetchInput(), 1)
