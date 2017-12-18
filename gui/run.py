import os
import json
import conditions


cwd = os.getcwd()
mappingFilename = os.path.join(cwd, 'conditionMapping.json')
with open(mappingFilename) as mappingFile:
    conditionMapping = json.load(mappingFile)


##################################################
############# ENTER SUBJECT INFO HERE ############
##################################################

subjectID = 12

##################################################
##################################################
##################################################

conditions.run(conditionMapping[str(subjectID)])
