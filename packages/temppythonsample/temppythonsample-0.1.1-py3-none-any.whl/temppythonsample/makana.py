from turtle import st
import requests
import authService

class MaknaModel():
  
    def getFramwork():
        authentication = authService.Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/modelframeworks"

        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers, verify=False)
        
        return print(response.text)

    def getMakanaModel():
        authentication = authService.Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/models"

        headers = {
            'Authorization': access_token_header,
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers, verify=False)
        if response.ok:
            model = response.json()
            for data in model:
                print("Name: " + data['name'] + " Id : "+ data['id'])
            return print("Data Load SucessFull")
        else:
            return("Error While Load Makana Model")

    def registerModel(modeName: str, description: str, modelFrameworkId: int, frameworkName: str, frameworkVersion:float,
                    modelFileName: str, modelFileDirectory: str):
        
        authentication = authService.Authentication
        access_token_header = authentication.getToken()
        url = "https://localhost:44350/api/makana/models"

        payload={
            'id': '',
            'name': modeName,
            'description': description,
            'modelFrameworkId': str(modelFrameworkId),
            'frameworkName': frameworkName,
            'frameworkVersion': str(frameworkVersion),
            'modelFileName': modelFileName,
            'modelFileUri': ''}
        files=[
        ('modelFile',(modelFileName,open(modelFileDirectory,'rb'),'application/octet-stream'))
        ]
        headers = {
        'Authorization': access_token_header
        }
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)

        # model = response.json()
        # return print("Sucessfull Created Model Name : " + model["name"] + " And Id : "+ model["id"])
        return print(response.text)


class MakanaService():

    def registerModelService(serviceName: str, description: str, modelDefinitionId: str, scriptFileName:str, dependenciesFileName: str,
                            scriptFileDirectory: str, dependenciesFileDirectory: str):
        
        authentication = authService.Authentication
        access_token_header = authentication.getToken()

        url = "https://localhost:44350/api/makana/modelservices"

        dependenciesFileDirectory = dependenciesFileDirectory.replace("\r","\\r")
        payload={
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
            'dependenciesFileUri': ''}

        files=[
            ('scriptFile',(scriptFileName,open(scriptFileDirectory,'rb'),'application/octet-stream')),
            ('dependenciesFile',(dependenciesFileName,open(dependenciesFileDirectory,'rb'),'text/plain'))
        ]
        headers = {
            'Authorization': access_token_header
        }
        response = requests.post(url, headers=headers, data=payload, files=files, verify=False)
        # return print("Sucessfull Created Model Name : " + model["name"] + " And Id : "+ model["id"])

        return print(response.text)

