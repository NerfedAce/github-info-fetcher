import json
import sys
import requests

if len(sys.argv) <= 1:
    sys.exit(0)

try :
    response = requests.get("https://api.github.com/users/" + sys.argv[1])
    if response.status_code != 200 :
        print("user not found")
        sys.exit(0)
    d = response.json()
    if len(sys.argv) == 2 :
        print("email:      " , d["email"] if "email" in d else "")
        print("name:       " , d["name"] if "name" in d else "")
        print("location:   " , d["location"] if "location" in d else "")
        print("followers:  " , str(d["followers"]) if "followers" in d else "")
        print("following:  " , str(d["following"]) if "following" in d else "")
    elif len(sys.argv) > 2 :
        i = 2
        while i < len(sys.argv) :
            if sys.argv[i] in d:
                print(sys.argv[i] + " = " + str(d[sys.argv[i]]))
            else :
                print("provided field : " + sys.argv[i] + " not found")
            i += 1


except Exception as e :
    print("error occured" ,e)