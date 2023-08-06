import json
from textwrap import indent
import uuid
import requests
from temppythonsample.authService import Authentication

class MakanaModel():
  
    def getModelFramworks():
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/modelframeworks"
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())

    def getMakanaModels():
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/models"
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def getMakanaModel(id: uuid):
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/model/" + id
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def registerModel(modeName: str, description: str, modelFrameworkId: int, frameworkName: str, frameworkVersion:float,
                    modelFileName: str, modelFileDirectory: str):
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/models"
        headers = {
            'Authorization': access_token_header
        }
        payload = {
            'id': '',
            'name': modeName,
            'description': description,
            'modelFrameworkId': str(modelFrameworkId),
            'frameworkName': frameworkName,
            'frameworkVersion': str(frameworkVersion),
            'modelFileName': modelFileName,
            'modelFileUri': ''
        }
        files = [
            ('modelFile',(modelFileName,open(modelFileDirectory,'rb'),'application/octet-stream'))
        ]
        
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())


class MakanaService():

    def getMakanaServices():
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/modelservices"
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def getMakanaService(id: uuid):
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/modelservice/" + id
        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())
    
    def registerModelService(serviceName: str, description: str, modelDefinitionId: uuid, scriptFileName:str, dependenciesFileName: str,
                            scriptFileDirectory: str, dependenciesFileDirectory: str):
        
        authentication = Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/modelservices"
        headers = {
            'Authorization': access_token_header
        }
        dependenciesFileDirectory = dependenciesFileDirectory.replace("\r","\\r")
        payload = {
            'id': '',
            'name': serviceName,
            'description': description,
            'modelDefinitionId': modelDefinitionId,
            'containerRunMode': '0',
            'idleTimeUnit': '',
            'idleTimeDuration': '',
            'scriptFileName': scriptFileName,
            'scriptFileUri': '',
            'dependenciesFileName': dependenciesFileName,
            'dependenciesFileUri': ''
        }
        files=[
            ('scriptFile',(scriptFileName,open(scriptFileDirectory,'rb'),'application/octet-stream')),
            ('dependenciesFile',(dependenciesFileName,open(dependenciesFileDirectory,'rb'),'text/plain'))
        ]
        
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
        if response.ok:
            print(json.dumps(response.json(), indent=2))
            return response.json()
        else:
            print("Error" + response.json())

