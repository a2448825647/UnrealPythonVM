import sys
import os

def initEnviroment(pluginPath):
    print('initEnviroment')
    sys.path.append(pluginPath + 'Source/ThirdParty/PythonPackages')
    sys.path.append(pluginPath + 'Source/Scripts/yolov3')
    sys.path.append(pluginPath + 'Source/Scripts')
    print(pluginPath + 'Source/ThirdParty/PythonPackages')
    
def initOther():
    print('initOther')

def printEnviromentPath():
    env_dist = os.environ
    for key in env_dist:
        print(key + ' : ' + env_dist[key])