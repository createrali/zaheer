welcome_statement="Welcome to zaheer intractive app \nMode of operation\n1. Learning mode\n2. Analysis\n3. Intract\nPlease select the options ! :"
import sys
sys.path.insert(0, './Saheerout')
import Saheerout
zout = Saheerout.Saheerout(welcome_statement,1)

str = raw_input("Enter your input: ");
print "Begining : ",str,"mode" 