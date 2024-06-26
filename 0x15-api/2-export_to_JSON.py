#!/usr/bin/python3
"""Python script to export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    employee = user.get("username")
    to_do = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as f:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "employee": employee
            } for t in to_do]}, f)
