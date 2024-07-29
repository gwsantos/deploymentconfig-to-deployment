from os import listdir
from os.path import isfile, join
import yaml
import sys
import json

filepath = sys.argv[1]
fileList = [f for f in listdir(filepath) if isfile(join(filepath, f))]
print("File list: " + fileList)
for fileName in fileList:
    fullFilePath=filepath+'/'+fileName
    with open(fullFilePath) as file:    

        deploymentconfig = list(yaml.load_all(file, Loader=yaml.SafeLoader))

    if deploymentconfig[-1] == None:
        del deploymentconfig[-1]

    for manifest in deploymentconfig:
        if manifest != None and manifest['kind'] == 'DeploymentConfig':

            manifest['kind'] = 'Deployment'        
            manifest['apiVersion'] = 'apps/v1'

            try: 
                manifest['spec']['strategy']['type'] = 'RollingUpdate'
            except:
                pass        
            
            try: 
                metadata = json.dumps(manifest['metadata'])
                attributes = json.loads(metadata)
                manifest['metadata'] = attributes
                labelsToKeep = ['name','namespace','labels']
                for label in list(attributes):
                    if label not in labelsToKeep:
                        del manifest['metadata'][label]
            except Exception as error:
                print("An error occurred:", error)
                pass

            try: 
                selector = json.dumps(manifest['spec']['selector'])
                matchLabels = json.loads(selector)
                manifest['spec']['selector']['matchLabels'] = matchLabels
                for label in matchLabels:
                    del manifest['spec']['selector'][label]
            except:
                pass

            try:
                del manifest['spec']['strategy']['rollingParams']['intervalSeconds']
            except:
                pass

            try:
                del manifest['spec']['strategy']['rollingParams']['updatePeriodSeconds']
            except:
                pass

            try:
                rollingParams = json.dumps(manifest['spec']['strategy']['rollingParams'])
                rollingUpdate = json.loads(rollingParams)
                manifest['spec']['strategy']['rollingUpdate'] = rollingUpdate
                del manifest['spec']['strategy']['rollingParams']
            except:
                pass

            try:
                del manifest['spec']['triggers']
            except:
                pass

            try:
                del manifest['spec']['test']
            except:
                pass

            try:
                del manifest['spec']['strategy']['activeDeadlineSeconds']
            except:
                pass

            try:
                del manifest['spec']['strategy']['resources']
            except:
                pass

            try:
                del manifest['status']
            except:
                pass

    with open(fullFilePath, "w") as deployment:
        yaml.dump_all(deploymentconfig, deployment, default_flow_style=False)