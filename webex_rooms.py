import requests 
import json 

# get token from here: https://developer.webex.com/docs/api/getting-started
access_token = "insert your token here"



# Get the list of room IDs
def get_all_room_ids():
  url_rooms = 'https://api.ciscospark.com/v1/rooms' 
  room_ids = []
  res_space = requests.get(url_rooms,headers=headers)
  print("Total number of rooms: "+str(len(res_space.json()["items"])))
  for room in res_space.json()["items"]:
    room_ids.append(room["id"])
    print("Room ID: "+room["id"]+" added.")
  return room_ids

def get_all_rooms_details():
  url_rooms = 'https://api.ciscospark.com/v1/rooms' 
  rooms = []
  res_space = requests.get(url_rooms,headers=headers)
  for room in res_space.json()["items"]:
    rooms.append(room)
  return rooms



headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
print(get_all_rooms_details())



