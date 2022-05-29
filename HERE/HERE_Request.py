# Using HERE API to get the information of the chargers in VIC
## information:
# Org ID: org469926402; org96280094


# import libraries:
import requests

# Authen:
accessKeyID = 'svDaoCpcn7teEq61NGB9lQ'
accessKeySecret = 'y4cfzdCKgavMQQKsKdB9q1KN0v4gojHS8w2DGMIlDa-XKWFNc_9EQnb569iaopTI-dy2674I0K0V63TJXTu4-A'

# Get the access token

# get the access token:

def get_access_token(url, client_id, client_secret):
    response = requests.post(
        url,
        data={"grant_type": "client_credentials"},
        auth=(client_id, client_secret),
    )
    return response.json()
get_access_token("https://account.api.here.com/oauth2/token", accessKeyID, accessKeySecret)


#input
key = 'MdsWSRzj3YQdLdrbVnx0nazr_fA8JamYo3zEWSx5shw'
header = {'Authorization': f'Bearer {key}'}

url = f'https://ev-v2.cc.api.here.com/ev/stations.json?prox=52.516667,13.383333,5000&connectortype=31'

res = requests.request("GET", url, headers = header)


print(res.text)

