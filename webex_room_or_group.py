import requests 
import json 
import getkey

# get token from here: https://developer.webex.com/docs/api/getting-started
access_token = getkey.getkey()
headers = {'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json' }

def add_room():
    # Get the new group information
    groups_struc = json.load(open("new_group.json"))
    url = 'https://api.ciscospark.com/v1/rooms'
    for rec in groups_struc["groups"]:
        create_group_name = rec["group"]["group_name"]
        print("Creating ... " + create_group_name)
        payload_space={"title": create_group_name}
        res_space = requests.post(url, headers=headers, json=payload_space)
        
        NEW_SPACE_ID = res_space.json()["id"]
        for mbr in rec["group"]["members"]:
            room_id = NEW_SPACE_ID
            person_email = mbr["email"] 
            url2 = 'https://api.ciscospark.com/v1/memberships'
            payload_member = {'roomId': room_id, 'personEmail': person_email}
            res_member = requests.post(url2, headers=headers, json=payload_member)

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

# get the room details in json format
# return type: json
def get_single_room_details(roomID):
    url_rooms = 'https://api.ciscospark.com/v1/rooms' 
    url_rooms = url_rooms+"/"+str(roomID)
    details = requests.get(url_rooms,headers=headers)
    return details.json()

# get single room meeting details in json format
# return type: json
def get_room_meeting_details(roomID):
    url_rooms = 'https://api.ciscospark.com/v1/rooms' 
    url_rooms = url_rooms+"/"+str(roomID)+"/meetingInfo"
    meetingDetails = requests.get(url_rooms,headers=headers)
    return meetingDetails.json()

# Get only the meeting link of a room
# input: Room ID
# input type: string
# return : meeting link/url
# return type: String type
def get_meeting_link(roomID):
    meetingDetails = get_room_meeting_details(roomID)
    return meetingDetails["meetingLink"]

# Delete a room
# input: Room ID
# input type: string
# return : status code
# to get the status code description
# https://developer.webex.com/docs/api/v1/rooms/delete-a-room
def delete_single_room(roomID):
    url_rooms = 'https://api.ciscospark.com/v1/rooms'
    url_rooms = url_rooms+"/"+str(roomID)
    status_code = requests.delete(url_rooms, headers=headers, json={})
    return status_code



