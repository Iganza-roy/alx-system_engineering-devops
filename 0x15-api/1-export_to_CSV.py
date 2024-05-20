#!/usr/bin/python3
"""export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    employee = user.get("username")
    to_do = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as f:
        out = csv.writer(f, quoting=csv.QUOTE_ALL)
        [out.writerow(
            [user_id, employee, t.get("completed"), t.get("title")]
         ) for t in to_do]
