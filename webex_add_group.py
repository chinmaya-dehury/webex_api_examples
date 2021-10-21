import requests 
import json 

# get token from here: https://developer.webex.com/docs/api/getting-started
access_token = "insert your token here"



groups_struc = {
 "groups": [
      { "group": { "group_id": "G1_chinmaya" , "group_name": "GROUP_chinmaya_A" ,    
                   "members": [   
                     {"person_id": "P-1" , "person_name": "first name", "email": "email@id.here"},
                     {"person_id": "P-2" , "person_name": "Chinmaya dehury", "email": "email@id.here"},
                     {"person_id": "P-3" , "person_name": "Chinmaya Dehury", "email": "email@id.here"} 
                   ]
                 }
      }
   ]
}

url = 'https://api.ciscospark.com/v1/rooms'

headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
print(headers)
for rec in groups_struc["groups"]:
    create_group_name = rec["group"]["group_name"]
    print("Creating ... " + create_group_name)
    payload_space={"title": create_group_name}
    res_space = requests.post(url, headers=headers, json=payload_space)
    print(res_space)
    print(res_space.json())
    NEW_SPACE_ID = res_space.json()["id"]
    for mbr in rec["group"]["members"]:
        room_id = NEW_SPACE_ID
        person_email = mbr["email"] 
        url2 = 'https://api.ciscospark.com/v1/memberships'
        payload_member = {'roomId': room_id, 'personEmail': person_email}
        res_member = requests.post(url2, headers=headers, json=payload_member)

