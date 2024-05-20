#!/usr/bin/python3
"""Python script to export data in the JSON format."""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as f:
        json.dump({
            e.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": e.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": e.get("id")}).json()]
            for e in users}, f)
