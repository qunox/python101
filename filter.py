print '\n'+ 'Assalamualaikum'.title().center(30,'*') + '\n'
#change this sourceFileAdd according to your HiggsExample.txt path
sourceFileAdd = 'C:\\Users\\qunox\\Google Drive\\pythonClass\\HiggsExample.txt'
print 'Opening file: %s' % sourceFileAdd
#ignore the command line try and except for now
try:
    sourceFile = open(sourceFileAdd, 'r')
    print 'Sucess in opening file'
    #read the sourcefile, now rawInput is a string
    rawInput = sourceFile.readlines()
    sourceFile.close()
except IOError:
    print 'Failure to open source file'


parameters = 'label,lepton pT, lepton eta, lepton phi, missing energy magnitude, ' \
            'missing energy phi, jet 1 pt, jet 1 eta, jet 1 phi, jet 1 b-tag, ' \
            'jet 2 pt, jet 2 eta, jet 2 phi, jet 2 b-tag, jet 3 pt, jet 3 eta, ' \
            'jet 3 phi, jet 3 b-tag, jet 4 pt, jet 4 eta, jet 4 phi, jet 4 b-tag, ' \
            'm_jj, m_jjj, m_lv, m_jlv, m_bb, m_wbb, m_wwbb'
parameters = parameters.split(',')
parameters = [item.strip() for item in parameters]

mainSampleDict = {}
id = 0
for event in rawInput:
    #turning the event into a list
    event_l = event.strip().split(',')
    event_l = [float(i) for i in event_l]
    #creating a list of tupple
    # [(label,1.00),(lepton pT, 231.4901) , (lepton eta , 21892,291821)...]
    toBeADict = zip(parameters, event_l)
    #transforming it into a dict
    eventDict = dict(toBeADict)
    #insert into the mainSampleDict and put the id
    mainSampleDict[id] = eventDict
    id += 1

#let says you want event with only 2 jets
def filterJets(x):
    if mainSampleDict[x]['jet 3 pt'] == 0 and mainSampleDict[x]['jet 4 pt']:
        return  True
    else:
        return False

filteredSample = filter(filterJets, mainSampleDict.keys())
print 'Number of event with only two jets:', len(filteredSample)

#import pdb; pdb.set_trace()