import ssl
import os
from websocket import create_connection
import json

class QlikEngine():
    #Initialize websocket
    def __init__(self,host,cert_path,user_directory,user_id):
        self.host = host
        self.cert_path = cert_path
        self.user_directory = user_directory
        self.user_id = user_id

        socketUrl = f"wss://{self.host}:4747/app/"
        cert = {
                "cert_reqs":ssl.CERT_NONE,
                'ca_certs':os.path.join(self.cert_path,'root.pem'),
                'certfile':os.path.join(self.cert_path,'client.pem'),
                'keyfile':os.path.join(self.cert_path,'client_key.pem')
        }

        requestHeader = {
                'X-Qlik-User':f'UserDirectory={self.user_directory};'
                              f'UserId={self.user_id}'
        }

        
        try:
            self.ws = create_connection(socketUrl, sslopt = cert, header = requestHeader)
            self.result = self.ws.recv()
            result = json.loads(self.result)
            self.sessionState = result.get("params").get("qSessionState")
            if  self.sessionState == 'SESSION_CREATED':
                self.sessionCreated = True
            else:
                self.sessionCreated = False    
        except:
            self.result = json.dumps({
                "params": {"qSessionState":"error"}
            })
            self.sessionCreated = False 
            print("error while websocket opening")   

    

    def getDocList(self):
        self.ws.send(json.dumps({
	        "handle": -1,
            "method": "GetDocList",
            "params": [],
            "outKey": -1,
            "id": 1
        }))

        result = self.ws.recv()

        data = json.loads(result)
        documentsList = data["result"]

        documents = []

        for doc in documentsList.get("qDocList"):
            documentMeta = doc.get("qMeta")
            if documentMeta.get("published"):
                stream = documentMeta.get("stream").get("name")
            else:
                stream = None

            document = {
                "docId": doc.get("qDocId"),
                "qvfSize": doc.get("qFileSize"),
                "createdDate":documentMeta.get("createdDate"),
                "modifiedDate":documentMeta.get("modifiedDate"),
                "lastReloadTime":documentMeta.get("qLastReloadTime"),
                "publishTime":documentMeta.get("publishTime"),
                "stream":stream
            }    
            documents.append(document)
        
        return documents



    #Object destroyer       
    def __del__(self):
        if self.sessionCreated:
            self.ws.close()
        
    
