import requests
import sys
import json
if len(sys.argv) == 1 :
    sys.exit(0)

try :
    response = requests.get("https://api.github.com/users/" + sys.argv[1]+"/repos")
    if response.status_code != 200 :
        print("user not found")
        sys.exit(0)
    data = response.json()
    if len(sys.argv) == 2 :
        repos = sorted(
            data,
            key=lambda repo: repo["stargazers_count"],
            reverse=True
        )
        for x in range(min(len(repos), 5)):
            print("name:  " ,repos[x]["name"])
            print("stargazers_count:  " ,repos[x]["stargazers_count"])
            print("description:  " ,repos[x]["description"])
            print("")
    else :
        i = 2
        while i < len(sys.argv) :
            found = False
            for x in data :

                if x["name"] == sys.argv[i] :
                    print("Repo : "+x["name"])
                    print("star gazers : " +str(x["stargazers_count"]))
                    print(x["description"] or "no description")
                    print("")
                    found = True
                    break
            if not found :
                print(str(sys.argv[i])+" not found")
            i += 1

except Exception as e:
    print("error : " , e)