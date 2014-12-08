print '\n'+ 'Assalamualaikum'.title().center(30,'*') + '\n'
#change this sourceFileAdd according to your HiggsExample.txt path
sourceFileAdd = 'C:\\Users\\qunox\\Google Drive\\pythonClass\\HiggsExample.txt'
print 'Opening file: %s' % sourceFileAdd
#ignore the command line try and except for now
try:
    sourceFile = open(sourceFileAdd, 'r')
    print 'Sucess in opening file'
    #read the sourcefile, now rawInput is a string
    rawInput = sourceFile.read()
    sourceFile.close()
except IOError:
    print 'Failure to open source file'

#spliting the different event in the rawInput, automatically transform into a list
rawInput = rawInput.split('\n')
#comand len give the length of somthing
acceptedEvent = 0
rejectedEvent = 0
print 'Total events: %s' % len(rawInput)
for event in rawInput:
    eventElements = event.split(',')
    #element inside the evenElement list is still a string, so have to convert into a float via float()
    #eventElement[0] = higgSignal if == 1 mean it is a higgs, == 0 it is a noise
    if float(eventElements[0]) and float(eventElements[9]): acceptedEvent += 1
    else: rejectedEvent += 1
print 'Accepted events:' , acceptedEvent
print 'Rejected events: %s ' % rejectedEvent