          ##API

##API - Application Programming Interface
##it is used for connect front end and back end.


##request ->  API ->   response,
##                     code ,
##                     data(json ,xml)

##json - java script object notation (90% used)


        ##HTTP errors......HyperText Transfer Protocol

##200->Everythink ok...
##404->server not found...
##401->Authentication.....(expire password)
##503->server not able to handle request.....(server is overload)
##301->different endpoint...(multiple URL page will open)
##400->bad request.....(old version,invalid request message)
##403->access forbiddan.....(block for normal user)


##API :
   ##    whether API checking in google for accessing API...
   ##    any website login with fb in example for API...


##import requests
##url="https://www.google.co.in/"
##response=requests.get(url)
##print(response)

##import requests
##url="http://api.open-notify.org/astros.json"
##response=requests.get(url)
##print(response)

##import requests
##url="http://api.open-notify.org/astros.json"
##response=requests.get(url)
##print(response)
##data=response.json()
##print(data)

##import requests
##url="http://api.open-notify.org/astros.json"
##response=requests.get(url)
##print(response)
##data=response.json()
##print(data)
##import json
##format_data=json.dumps(data,sort_keys=True,indent=4)
##print(format_data)
##print(type(format_data))

##import requests
##url="http://api.open-notify.org/iss-pass.json"
##parameters={
##    "lat":40,
##    "lon":30,
##    }
##response=requests.get(url,params=parameters)
##print(response)

##import requests
##url="https://api.tvmaze.com/lookup/shows"
##parameters={"imdb":"tt0944947"}
##response=requests.get(url,params=parameters)
##print(response)
##data=response.json()
##print(data)
##import json
##format_data=json.dumps(data,sort_keys=True,indent=4)
##print(format_data)
