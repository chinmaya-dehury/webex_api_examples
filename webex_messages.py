import requests 
import json 

# get token from here: https://developer.webex.com/docs/api/getting-started
access_token = "insert your token here"

# here we will get the list of messages


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

# get all messages from ALL rooms
# return type: List
def get_all_msg_from_all_rooms(roomIds):
  all_msgs = []
  for room in roomIds:
    all_msgs.append(get_all_msg_by_roomid(roomId=room))
  return all_msgs

# get all messages from a room
# return type: json
def get_all_msg_by_roomid(roomId):
  url_msg = 'https://api.ciscospark.com/v1/messages'
  msgs = requests.get(url_msg, headers=headers, params = { "roomId":roomId })
  return msgs.json()

def send_msg_to_group(groupId):
  url_msg = 'https://api.ciscospark.com/v1/messages' 
  json_body = {
    "roomId":groupId, 
    "text":"DevNetASC: This is an automated message from Chinmaya Dehury using python and API."
    }
  res_space = requests.post(url_msg, headers=headers,json=json_body)
  print("The response code is : "+str(res_space))


headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }
groupId="Enter the room id or the group id"
send_msg_to_group(groupId=groupId)



def send_one_to_one_msg():
  url_msg = 'https://api.ciscospark.com/v1/messages' 
  json_body = {
    "toPersonEmail":"chinmaya.dehury@ymail.com", 
    "text":"DevNetASC: This is a message from chinmaya dehury using python and API."
    }
  res_space = requests.post(url_msg, headers=headers,json=json_body)
  print("The response is here: "+str(res_space.json()))