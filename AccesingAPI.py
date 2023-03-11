#                 Application Programming interface
# Interface b/w ends
# JSON Javascript object notation

# Codes and its meaning

##200 - everything okay
##301 - redirect to different end point
##400 - bad request
##401 - not authendicate
##403 - access forbidden
##404 - server not found
##503 - server not ready to handle request

# Example - Login with FB SignIn
# Bus ticket booking from redbus and SETC

#############################################################################

import requests
url="http://api.open-notify.org/astros.json"
a=requests.get(url)
print(a)
b=a.json()
print(b)
import json
c=json.dumps(b,sort_keys=True,indent=4)
print(c)
print(type(c))
